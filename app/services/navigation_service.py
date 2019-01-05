#
# This file is part of pOrtals:reconLIVE:AV which is released
# under version 3 of the GNU General Public License (GPLv3).
# See the LICENSE file in the project root for more information.
#

from services.session_service import get_active_session
from services.event_service import handle_navigation
from db import db


def move_to(destination_id: int) -> None:
    active_session = get_active_session()
    start_id = active_session.current_location_id
    active_session.previous_location_id = start_id
    active_session.current_location_id = destination_id
    db.session.add(active_session)
    db.session.commit()
    handle_navigation(start_id, destination_id, active_session.id)
