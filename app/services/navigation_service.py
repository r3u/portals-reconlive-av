#
# This file is part of pOrtals:reconLIVE:AV which is released
# under version 3 of the GNU General Public License (GPLv3).
# See the LICENSE file in the project root for more information.
#

from model import Path
from services.session_service import get_active_session
from db import db


def get_adjacent_locations(current_location_id):
    return [p.destination for p in
            Path.query.filter(Path.start_id == current_location_id).all()]


def update_location(new_location_id):
    active_session = get_active_session()
    active_session.current_location_id = new_location_id
    db.session.add(active_session)
    db.session.commit()
