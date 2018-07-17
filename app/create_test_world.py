from db import db
from model import World, Location, Path, PathDescription, Session


def add(obj):
    db.session.add(obj)
    return obj


world = add(World(name='Test World'))

plaza = add(Location(name='Plaza', world=world))
hotel = add(Location(name='Old Grand Hotel', world=world))
basement = add(Location(name='Hotel Basement', world=world))

plaza_to_hotel = add(Path(start=plaza, destination=hotel))
hotel_to_plaza = add(Path(start=hotel, destination=plaza))

hotel_to_basement = add(Path(start=hotel, destination=basement))
basement_to_hotel = add(Path(start=basement, destination=hotel))

plaza_to_hotel_desc = add(PathDescription(
    path=plaza_to_hotel,
    description="YOU ARE IN THE HOTEL. THERE'S A DOOR TO THE BASEMENT IN FRONT OF YOU."
))

hotel_to_plaza_desc = add(PathDescription(
    path=hotel_to_plaza,
    description="YOU ARE IN THE PLAZA, FACING THE HOTEL."
))

test_session = add(Session(code='TestSession1', active=True, current_location=hotel))

db.session.commit()
