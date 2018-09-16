#!/usr/bin/env python3
#
# This file is part of pOrtals::reconLIVE:AV which is released
# under version 3 of the GNU General Public License (GPLv3).
# See the LICENSE file in the project root for more information.
#

import eventlet
eventlet.monkey_patch()

from flask import request, redirect, abort
from flask import send_file, render_template
from flask_login import (LoginManager, current_user, login_user, logout_user)
from flask_socketio import emit, join_room, disconnect
from sqlalchemy.orm.exc import NoResultFound

from app import app, bcrypt
from app_socketio import socketio
from model import Actor
from services.session_service import get_active_session
from services.navigation_service import get_adjacent_locations, move_to
from services.path_service import get_path
from services.chat_service import save_log_entry, load_chat_log
from services.asset_metadata_service import asset_metadata
from services.event_service import handle_message, listeners
from event_listeners.socketio import room, namespace, SocketIOEventListener
from event_listeners.supercollider import SuperColliderEventListener
from decorators import public_endpoint, guide_only
from rest import rest_chat_msg

from argparse import ArgumentParser


listeners.append(SocketIOEventListener())
listeners.append(SuperColliderEventListener())
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


def init_assets(asset_dir):
    app.logger.info("Loading assets from {0}".format(asset_dir))
    asset_metadata.load_from_path(asset_dir)


if __name__ == "__main__":
    parser = ArgumentParser("pOrtals::reconLIVE:AV server")
    parser.add_argument('--asset-dir', action='store', dest='asset_dir')
    args = parser.parse_args()
    if args.asset_dir:
        init_assets(args.asset_dir)
    socketio.run(app, host='0.0.0.0', port=8080, debug=True)
