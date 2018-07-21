#!/usr/bin/env python3
#
# pOrtals::reconLIVE:AV
#
# Copyright (C) 2018  Rachael Melanson
# Copyright (C) 2018  Henry Rodrick
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

from flask import request, redirect, abort, flash
from flask import send_file, render_template
from flask_login import (LoginManager, current_user, login_user, logout_user)
from sqlalchemy.orm.exc import NoResultFound

from app import app, bcrypt
from model import Actor, MediaAsset
from services.session_service import get_active_session
from services.navigation_service import get_adjacent_locations
from services.asset_service import save_asset
from services.path_service import get_path
from services.chat_service import save_log_entry
from decorators import public_endpoint, guide_only
from rest import rest_navigation_msg, rest_chat_msg
from db import db

import pathlib
import uuid
import os
import io
import requests

login_manager = LoginManager()
login_manager.init_app(app)

EVENT_ENDPOINT = 'http://127.0.0.1:8080/event.json'


@app.before_request
def check_valid_login():
    if request.endpoint is None:
        return
    if (not current_user.is_authenticated and
            not getattr(app.view_functions[request.endpoint], 'is_public', False)):
        return redirect('/login')
    if (getattr(current_user, 'role', None) != 'guide' and
            getattr(app.view_functions[request.endpoint], 'guide_only', False)):
        return abort(401)


@login_manager.user_loader
def load_user(user_id):
    return Actor.query.get(int(user_id))


@public_endpoint
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        query = Actor.query.filter(Actor.name == username)
        try:
            actor = query.one()
            if password is not None and bcrypt.check_password_hash(actor.password, password):
                login_user(actor)
                return redirect('/')
        except NoResultFound:
            pass
        error = "Invalid username or password"
        return render_template('login.html', error=error)
    else:
        return render_template('login.html')


@app.route("/logout")
def logout():
    logout_user()
    return render_template('logout.html')


def render_guide_view():
    return render_template('guide_view.html',
                           active_session=get_active_session())


def render_scout_view():
    return render_template('scout_view.html',
                           active_session=get_active_session())


@app.route('/')
def index():
    if current_user.role == 'guide':
        return render_guide_view()
    else:
        return render_scout_view()


@guide_only
@app.route('/move.json', methods=['POST'])
def move():
    data = request.get_json()
    active_session = get_active_session()

    start_id = active_session.current_location_id
    destination_id = data['destinationId']

    active_session.previous_location_id = start_id
    active_session.current_location_id = destination_id
    db.session.add(active_session)
    db.session.commit()

    post_event(rest_navigation_msg(start_id, destination_id, active_session.id))
    return '', 204


@guide_only
@app.route('/location_info.json', methods=['POST'])
def location_info():
    return '', 204


@guide_only
@app.route('/chatlog_entry.json', methods=['POST'])
def chatlog_entry():
    data = request.get_json()
    if 'message' not in data:
        return '', 400
    message = data['message']
    active_session = get_active_session()
    ent = save_log_entry(active_session, current_user, message)
    post_event(rest_chat_msg(ent))
    return '', 204


def post_event(json):
    res = requests.post(EVENT_ENDPOINT, json=json)
    if not res.ok:
        app.logger.error("Failed to post event, status code: {0}".format(res.status_code))


@guide_only
@app.route('/guide_controls.html')
def guide_controls():
    active_session = get_active_session()
    adjacent_locations = get_adjacent_locations(active_session.current_location_id)
    path = get_path(active_session.previous_location_id,
                    active_session.current_location_id)
    return render_template('guide_controls.html',
                           active_session=active_session,
                           adjacent_locations=adjacent_locations,
                           description=path.description)


@guide_only
@app.route('/asset_manager.html', methods=['GET', 'POST'])
def asset_manager():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if not file or file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        suffix = pathlib.Path(file.filename).suffix
        temp_filename = str(uuid.uuid4()) + suffix
        temp_filepath = os.path.join(app.config['UPLOAD_FOLDER'], temp_filename)
        file.save(temp_filepath)
        try:
            with open(temp_filepath, 'rb') as fp:
                data = fp.read()
            save_asset(file.filename, data)
            return redirect(request.url)
        finally:
            os.remove(temp_filepath)
    return render_template('asset_manager.html')


@public_endpoint
@app.route('/media_asset/<int:asset_id>')
def download_media_asset(asset_id):
    asset = MediaAsset.query.get(int(asset_id))
    if not asset:
        return abort(404)
    return send_file(
        io.BytesIO(asset.content),
        mimetype=asset.mime_type,
        as_attachment=True,
        attachment_filename=asset.filename)


@public_endpoint
@app.route('/style.css')
def style_css():
    return send_file('static/style.css')


if __name__ == "__main__":
    app.run(debug=True)
