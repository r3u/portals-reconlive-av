#
# This file is part of pOrtals:reconLIVE:AV which is released
# under version 3 of the GNU General Public License (GPLv3).
# See the LICENSE file in the project root for more information.
#

from sqlalchemy.orm.exc import NoResultFound
from model import Session


def get_active_session() -> Session:
    try:
        return Session.query.filter(Session.active == True).one()
    except NoResultFound:
        return None
