#
# This file is part of pOrtals::reconLIVE:AV which is released
# under version 3 of the GNU General Public License (GPLv3).
# See the LICENSE file in the project root for more information.
#

from app import app
from flask_sqlalchemy import SQLAlchemy as SQLAlchemyBase


# See https://github.com/mitsuhiko/flask-sqlalchemy/issues/589#issuecomment-361075700
class SQLAlchemy(SQLAlchemyBase):
    def apply_pool_defaults(self, flask_app, options):
        SQLAlchemyBase.apply_pool_defaults(self, flask_app, options)
        # options["echo"] = True  # Uncomment for SQL debugging
        options["pool_pre_ping"] = True


db = SQLAlchemy(app)

