#
# This file is part of pOrtals::reconLIVE:AV which is released
# under version 3 of the GNU General Public License (GPLv3).
# See the LICENSE file in the project root for more information.
#

from flask_login import UserMixin
from sqlalchemy.orm import relationship

from db import db


class Actor(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(length=255), nullable=False)
    role = db.Column(db.VARCHAR(length=255), nullable=False)
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

