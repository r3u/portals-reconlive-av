#
# This file is part of pOrtals:reconLIVE:AV which is released
# under version 3 of the GNU General Public License (GPLv3).
# See the LICENSE file in the project root for more information.
#

from flask import Flask
from flask_bcrypt import Bcrypt

import os
import logging
from uuid import uuid4

app = Flask('portals', static_url_path='')
app.logger.setLevel(logging.DEBUG)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
if app.config['SECRET_KEY'] is None:
    app.logger.warning("SECRET_KEY not set. Using random value.")
    app.config['SECRET_KEY'] = str(uuid4())

portals_db = os.environ.get('PORTALS_DB')
if portals_db is None:
    app.logger.warn("PORTALS_DB not set. Using in-memory database.")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{0}'.format(portals_db)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

asset_dir = os.environ.get('ASSET_DIR')
if asset_dir is None:
    app.logger.error("ASSET_DIR not set")

bcrypt = Bcrypt(app)


