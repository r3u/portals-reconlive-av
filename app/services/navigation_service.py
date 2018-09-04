#
# This file is part of pOrtals:reconLIVE:AV which is released
# under version 3 of the GNU General Public License (GPLv3).
# See the LICENSE file in the project root for more information.
#

from model import Path
from services.session_service import get_active_session
from services.event_service import post_event
from rest import rest_navigation_msg
from db import db


def get_adjacent_locations(current_location_id: int):
    return [p.destination for p in
            Path.query.filter(Path.start_id == current_location_id).all()]


def move_to(destination_id: int):
    active_session = get_active_session()
    start_id = active_session.current_location_id
    active_session.previous_location_id = start_id
    active_session.current_location_id = destination_id
    db.session.add(active_session)
    db.session.commit()

    post_event(rest_navigation_msg(start_id, destination_id, active_session.id))
