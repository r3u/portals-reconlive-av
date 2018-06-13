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
from flask_socketio import SocketIO
from flask_bcrypt import Bcrypt

import os
import logging

app = Flask('portals', static_url_path='')
app.logger.setLevel(logging.DEBUG)
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql+psycopg2://portals:portals@localhost:5432/portals'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

socketio = SocketIO(app)
bcrypt = Bcrypt(app)


