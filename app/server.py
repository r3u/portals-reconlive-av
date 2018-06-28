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

from flask import request, redirect, jsonify
from flask import send_file, render_template
from flask_login import (LoginManager, current_user, login_user, logout_user)
from flask_socketio import emit, join_room, disconnect
from sqlalchemy.orm.exc import NoResultFound

from app import app, socketio, bcrypt
from db import db, Actor, ChatlogEntry
from decorators import public_endpoint, nocache

ROOM = 'portals'

login_manager = LoginManager()
login_manager.init_app(app)


@app.before_request
def check_valid_login():
    if (not current_user.is_authenticated and
            not getattr(app.view_functions[request.endpoint], 'is_public', False)):
        return redirect('/login')


@login_manager.user_loader
def load_user(userid):
    return Actor.query.get(int(userid))


@public_endpoint
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        query = Actor.query.filter(Actor.name == username)
        try:
            actor = query.one()
            if (password is not None and
                bcrypt.check_password_hash(actor.password, password)):
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


@app.route('/')
def index():
    if current_user.role == 'guide':
        return render_template('guide_view.html')
    else:
        return render_template('scout_view.html')


@public_endpoint
@app.route('/style.css')
def style_css():
    return send_file('static/style.css')


@app.route('/chatlog.json')
@nocache
def chatlog_json():
    return jsonify(chatlog())


def chatlog():
    results = ChatlogEntry.query.order_by(ChatlogEntry.id.desc()).limit(100).all()
    messages = [{"id": ent.id, "message": ent.message, "actor": ent.actor.name }
                for ent in reversed(results)]
    return {'messages': messages}


@socketio.on('joined', namespace='/chat')
def joined(_message):
    if not current_user.is_authenticated:
        return disconnect()
    join_room(ROOM)
    emit('messages', chatlog()['messages'], room=request.sid)


@socketio.on('text', namespace='/chat')
def text(message):
    if not current_user.is_authenticated:
        return disconnect()
    message_text = message['message']
    log_entry = ChatlogEntry(session_id=1,
                             actor_id=current_user.get_id(),
                             message=message_text)
    db.session.add(log_entry)
    db.session.commit()
    emit('messages', [{'message': message_text, 'actor': current_user.name}], room=ROOM)


if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=80, debug=True)
