#!/usr/bin/env python3
#
# This file is part of pOrtals::reconLIVE:AV which is released
# under version 3 of the GNU General Public License (GPLv3).
# See the LICENSE file in the project root for more information.
#

import eventlet
eventlet.monkey_patch()

import sys

from flask import request, redirect, abort
from flask import send_file, render_template, jsonify
from flask_login import (LoginManager, current_user, login_user, logout_user)
from flask_socketio import emit, join_room, disconnect
from sqlalchemy.orm.exc import NoResultFound

from app import app, bcrypt, asset_dir
from app_socketio import socketio
from model import Actor
from services.session_service import get_active_session
from services.navigation_service import move_to
from services.location_service import get_adjacent_locations, get_current_location, get_location
from services.path_service import get_path
from services.chat_service import save_log_entry, load_chat_log, get_log_entries
from services.asset_metadata_service import asset_metadata
from services.event_service import handle_message, listeners
from services.nl_util import tokenize
from event_listeners.socketio import room, namespace, SocketIOEventListener
from decorators import public_endpoint, guide_only
from rest import rest_chat_msg, rest_location_msg, rest_asset_metadata_msg

from argparse import ArgumentParser


listeners.append(SocketIOEventListener())
login_manager = LoginManager()
login_manager.init_app(app)


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
    destination_id = data['destinationId']
    move_to(destination_id)
    return '', 204


@guide_only
@app.route('/location_info.json', methods=['POST'])
def update_location_info():
    return '', 204


@public_endpoint
@app.route('/current_location.json', methods=['GET'])
def current_location_info():
    return jsonify(rest_location_msg(get_current_location()))


@public_endpoint
@app.route('/metadata_by_location.json', methods=['GET'])
def get_metadata_by_location():
    location_id = request.args.get('location_id')
    if not location_id:
        return 'Missing parameter: location_id', 400
    location = get_location(location_id)
    if not location:
        return 'Invalid location_id', 400
    metadata = asset_metadata.by_location(location.name)
    rest_metadata = [rest_asset_metadata_msg(m) for m in metadata]
    return jsonify(rest_metadata), 200


@public_endpoint
@app.route('/metadata_by_messages.json', methods=['GET'])
def get_metadata_by_messages():
    message_ids_param = request.args.get('message_ids')
    if not message_ids_param:
        return 'Missing parameter: message_ids', 400
    message_ids = [int(i) for i in message_ids_param.split(',')]
    log_entries = get_log_entries(message_ids)
    tags = [k for ent in log_entries for k in tokenize(ent.message)]
    matches = {}
    scores = {}
    for tag in tags:
        for meta_def in asset_metadata.by_tag(tag):
            if meta_def.filename not in matches:
                matches[meta_def.filename] = rest_asset_metadata_msg(meta_def)
                scores[meta_def.filename] = 0
            scores[meta_def.filename] += 1
    for filename, score in scores.items():
        matches[filename]['score'] = score
    return jsonify({'matches': matches}), 200


@guide_only
@app.route('/chatlog_entry.json', methods=['POST'])
def chatlog_entry():
    data = request.get_json()
    if 'message' not in data:
        return '', 400
    message = data['message']
    active_session = get_active_session()
    if not active_session:
        app.logger.error("No active session")
        return '', 500
    ent = save_log_entry(active_session, current_user, message)
    handle_message(ent)
    return '', 204


@guide_only
@app.route('/guide_controls.html')
def guide_controls():
    active_session = get_active_session()
    if not active_session:
        app.logger.error("No active session")
        return '', 500
    adjacent_locations = get_adjacent_locations(active_session.current_location_id)
    path = get_path(active_session.previous_location_id,
                    active_session.current_location_id)
    return render_template('guide_controls.html',
                           active_session=active_session,
                           adjacent_locations=adjacent_locations,
                           description=path.description)


@public_endpoint
@app.route('/style.css')
def style_css():
    return send_file('static/style.css')


@socketio.on('joined', namespace=namespace)
def joined(_message):
    join_room(room)
    active_session = get_active_session()
    if not active_session:
        app.logger.warn("Message ignored: No active session")
        return
    messages = [rest_chat_msg(ent) for ent in load_chat_log(active_session.id)]
    emit('messages', messages, room=request.sid)


@socketio.on('text', namespace=namespace)
def text(message):
    if not current_user.is_authenticated:
        return disconnect()
    message_text = message['message']
    active_session = get_active_session()
    if not active_session:
        app.logger.warn("Message ignored: No active session")
        return
    ent = save_log_entry(active_session, current_user, message_text)
    handle_message(ent)


def init_assets(directory):
    app.logger.info("Loading assets from {0}".format(directory))
    asset_metadata.load_from_path(directory)


if __name__ == "__main__":
    parser = ArgumentParser("pOrtals::reconLIVE:AV server")
    parser.add_argument('--debug', action='store_true', dest='debug')
    args = parser.parse_args()
    if asset_dir is not None:
        init_assets(asset_dir)
    else:
        sys.exit(1)
    socketio.run(app, host='0.0.0.0', port=8080, debug=args.debug)
