#
# This file is part of pOrtals::reconLIVE:AV which is released
# under version 3 of the GNU General Public License (GPLv3).
# See the LICENSE file in the project root for more information.
#

from db import db
from model import World, Location, Path, Session


def add(obj):
    db.session.add(obj)
    return obj


def create_test_world():
    world = add(World(name='Test World'))

    portal = add(Location(name='Portal', world=world))

    plaza = add(Location(name='Plaza', world=world))
    hotel = add(Location(name='Old Grand Hotel', world=world))
    basement = add(Location(name='Hotel Basement', world=world))

    add(Path(
        start=portal, destination=hotel,
        description="YOU ARE IN THE HOTEL. THERE'S A DOOR TO THE BASEMENT IN FRONT OF YOU."
    ))

    add(Path(
        start=plaza, destination=hotel,
        description="YOU ARE IN THE HOTEL. THERE'S A DOOR TO THE BASEMENT IN FRONT OF YOU."
    ))

    add(Path(
        start=hotel, destination=plaza,
        description="YOU ARE IN THE PLAZA, FACING THE HOTEL."
    ))

    add(Path(
        start=hotel, destination=basement,
        description="YOU ARE IN THE BASEMENT. THERE ARE STAIRS UP TO THE HOTEL LOBBY BEHIND YOU."

    ))

    add(Path(
        start=basement, destination=hotel,
        description="YOU ARE IN THE HOTEL LOBBY. THERE'S AN EXIT TO THE PLAZA IN FRONT OF YOU."
    ))

    add(Session(
        code='TestSession1', active=True,
        current_location=hotel, previous_location=portal))

    db.session.commit()


if __name__ == '__main__':
    create_test_world()
