#
# This file is part of pOrtals:reconLIVE:AV which is released
# under version 3 of the GNU General Public License (GPLv3).
# See the LICENSE file in the project root for more information.
#

from model import Path, Location
from services.session_service import get_active_session
from typing import List


def get_adjacent_locations(current_location_id: int) -> List[Location]:
    return [p.destination for p in
            Path.query.filter(Path.start_id == current_location_id).all()]


def get_location(location_id: int) -> Location:
    return Location.query.get(location_id)


def get_current_location() -> Location:
    active_session = get_active_session()
    return get_location(active_session.current_location_id)
