#
# This file is part of pOrtals::reconLIVE:AV which is released
# under version 3 of the GNU General Public License (GPLv3).
# See the LICENSE file in the project root for more information.
#

from flask import make_response
from functools import wraps, update_wrapper
from datetime import datetime


def nocache(view):
    @wraps(view)
    def no_cache(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers['Last-Modified'] = datetime.now()
        cc = ('no-store, no-cache, must-revalidate, ' +
              'post-check=0, pre-check=0, max-age=0')
        response.headers['Cache-Control'] = cc
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response
    return update_wrapper(no_cache, view)


def public_endpoint(fn):
    fn.is_public = True
    return fn


def guide_only(fn):
    fn.guide_only = True
    return fn
