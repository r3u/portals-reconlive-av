import os

from db import db
from services import navigation_service
from services import session_service

from create_portals_world import create_portals_world


def test_basic_nav():
    schema_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', 'schema', 'portals.sql')
    with open(schema_path) as fp:
        schema = fp.read()
    db.engine.raw_connection().executescript(schema)

    create_portals_world()

    cur_loc_id = session_service.get_active_session().current_location_id
    cur_loc = navigation_service.get_location(cur_loc_id)
    assert 'Tower Top' == cur_loc.name
