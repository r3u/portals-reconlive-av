#
# This file is part of pOrtals:reconLIVE:AV which is released
# under version 3 of the GNU General Public License (GPLv3).
# See the LICENSE file in the project root for more information.
#

from flask_socketio import SocketIO

from app import app


socketio = SocketIO(app, engineio_logger=False)
