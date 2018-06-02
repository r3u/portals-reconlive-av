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

from flask import Flask
from flask import send_file
from flask import session
from flask_socketio import SocketIO, emit, join_room, leave_room

import logging
from logger import logger

ROOM = 'portals'

app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return send_file('static/index.html')

@socketio.on('joined', namespace='/chat')
def joined(message):
    join_room(ROOM)
    emit('status', {'msg': 'Someone has entered the room'}, room=ROOM)

@socketio.on('text', namespace='/chat')
def text(message):
    emit('message', {'msg': message['msg']}, room=ROOM)

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=8000, debug=True)
