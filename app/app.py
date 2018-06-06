#!/usr/bin/env python3

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

from flask import Flask, request, redirect, abort, jsonify, make_response
from flask import session, send_file, render_template
from flask_login import (LoginManager, UserMixin, current_user,
                        login_user, logout_user, login_required)
from flask_socketio import SocketIO, emit, join_room, leave_room, disconnect
from flask_sqlalchemy import SQLAlchemy as SA

from functools import wraps, update_wrapper
from datetime import datetime
import sys
import os
import logging

ROOM = 'portals'

class User(UserMixin):
    def __init__(self, id):
        self.id = id

app = Flask('portals', static_url_path='')
app.logger.setLevel(logging.DEBUG)
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://portals:portals@localhost:5432/portals'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# See https://github.com/mitsuhiko/flask-sqlalchemy/issues/589#issuecomment-361075700
class SQLAlchemy(SA):
    def apply_pool_defaults(self, app, options):
        SA.apply_pool_defaults(self, app, options)
        options["pool_pre_ping"] = True

db = SQLAlchemy(app)
socketio = SocketIO(app)
login_manager = LoginManager()
login_manager.init_app(app)


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class Chatlog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey(Game.id), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey(Player.id), nullable=False)
    message = db.Column(db.Text, nullable=False)

def nocache(view):
    @wraps(view)
    def no_cache(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers['Last-Modified'] = datetime.now()
        cc = ('no-store, no-cache, must-revalidate, ' +
              'post-check=0, pre-check=0, max-age=0')
        response.headers['Cache-Control'] = cc
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response
    return update_wrapper(no_cache, view)

def public_endpoint(function):
    function.is_public = True
    return function

@app.before_request
def check_valid_login():
    if (not current_user.is_authenticated and
        not getattr(app.view_functions[request.endpoint], 'is_public', False)):
        return redirect('/login')

@login_manager.user_loader
def load_user(userid):
    return User(userid)

@public_endpoint
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == "guide" and password == "foobar":
            user = User(1)
            login_user(user)
            return redirect('/')
        else:
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
    return send_file('static/index.html')

@public_endpoint
@app.route('/style.css')
def style_css():
    return send_file('static/style.css')

@app.route('/chatlog.json')
@nocache
def chatlog():
    results = Chatlog.query.order_by(Chatlog.id.desc()).limit(100).all()
    messages = [{"id": ent.id, "message": ent.message}
                for ent in reversed(results)]
    return jsonify({'messages': messages})

@socketio.on('joined', namespace='/chat')
def joined(message):
    if not current_user.is_authenticated:
        return disconnect()
    join_room(ROOM)
    emit('status', {'msg': 'Someone has entered the room'}, room=ROOM)

@socketio.on('text', namespace='/chat')
def text(message):
    if not current_user.is_authenticated:
        return disconnect()
    text = message['msg']
    logentry = Chatlog(game_id=1, player_id=1, message=text)
    db.session.add(logentry)
    db.session.commit()
    emit('message', {'msg': text}, room=ROOM)

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=8000, debug=True)
