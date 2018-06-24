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

from app import app
from flask_sqlalchemy import SQLAlchemy as SA
from flask_login import UserMixin
from sqlalchemy.orm import relationship

# See https://github.com/mitsuhiko/flask-sqlalchemy/issues/589#issuecomment-361075700
class SQLAlchemy(SA):
    def apply_pool_defaults(self, app, options):
        SA.apply_pool_defaults(self, app, options)
        options["pool_pre_ping"] = True

db = SQLAlchemy(app)

class Actor(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(length=255))
    password = db.Column(db.VARCHAR(length=255))

class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class ChatlogEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.Integer, db.ForeignKey(Session.id), nullable=False)
    actor_id = db.Column(db.Integer, db.ForeignKey(Actor.id), nullable=False)
    message = db.Column(db.Text, nullable=False)
    session = actor = relationship("Session")
    actor = relationship("Actor")
