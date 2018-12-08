#
# This file is part of pOrtals:reconLIVE:AV which is released
# under version 3 of the GNU General Public License (GPLv3).
# See the LICENSE file in the project root for more information.
#

from model import Path, Location
from typing import List


def get_path(start_id: int, destination_id: int):
    return Path \
        .query \
        .filter(Path.start_id == start_id, Path.destination_id == destination_id) \
        .one()


def get_paths_and_locations():
    locations: List[Location] = Location.query.all()
    paths: List[Path] = Path.query.all()
    return {
        "locations": [{"id": l.id, "name": l.name} for l in locations],
        "paths": [{"id": p.id, "start_id": p.start_id, "destination_id": p.destination_id} for p in paths]
    }