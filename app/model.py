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

from flask_login import UserMixin
from sqlalchemy.orm import relationship, deferred
from sqlalchemy.dialects.postgresql import ENUM, BYTEA

from db import db


actor_role = ENUM('guide', 'scout', name='actor_role')


class Actor(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(length=255), nullable=False)
    role = db.Column(actor_role, nullable=False)
    password = db.Column(db.VARCHAR(length=255), nullable=False)


class World(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(length=255), nullable=False)


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(length=255), nullable=False)
    world_id = db.Column(db.Integer, db.ForeignKey(World.id), nullable=False)
    world = relationship("World")


class Path(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_id = db.Column(db.Integer, db.ForeignKey(Location.id))
    destination_id = db.Column(db.Integer, db.ForeignKey(Location.id))
    description = db.Column(db.TEXT)
    start = relationship("Location", foreign_keys=[start_id])
    destination = relationship("Location", foreign_keys=[destination_id])


class LocationInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.Integer, db.ForeignKey(Location.id))
    description = db.Column(db.TEXT)
    location = relationship("Location")


class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.VARCHAR(length=255), nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    current_location_id = db.Column(db.Integer, db.ForeignKey(Location.id), nullable=False)
    previous_location_id = db.Column(db.Integer, db.ForeignKey(Location.id), nullable=False)
    current_location = relationship("Location", foreign_keys=[current_location_id])
    previous_location = relationship("Location", foreign_keys=[previous_location_id])


class ChatlogEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.Integer, db.ForeignKey(Session.id), nullable=False)
    actor_id = db.Column(db.Integer, db.ForeignKey(Actor.id), nullable=False)
    message = db.Column(db.Text, nullable=False)
    session = relationship("Session")
    actor = relationship("Actor")


class MediaAsset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.Text, nullable=False)
    hash_sha256 = db.Column(db.VARCHAR(length=64), nullable=False)
    content = deferred(db.Column(BYTEA, nullable=False))
    mime_type = db.Column(db.Text, nullable=False)
