#
# This file is part of pOrtals:reconLIVE:AV which is released
# under version 3 of the GNU General Public License (GPLv3).
# See the LICENSE file in the project root for more information.
#

from model import Path


def get_path(start_id: int, destination_id: int):
    return Path \
        .query \
        .filter(Path.start_id == start_id, Path.destination_id == destination_id) \
        .one()
