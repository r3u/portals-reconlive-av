from db import db
from model import World, Location, Path, Session


def add(obj):
    db.session.add(obj)
    return obj


world = add(World(name='Test World'))

portal = add(Location(name='Portal', world=world))

plaza = add(Location(name='Plaza', world=world))
hotel = add(Location(name='Old Grand Hotel', world=world))
basement = add(Location(name='Hotel Basement', world=world))

portal_to_hotel = add(Path(
    start=portal, destination=hotel,
    description="YOU ARE IN THE HOTEL. THERE'S A DOOR TO THE BASEMENT IN FRONT OF YOU."
))

plaza_to_hotel = add(Path(
    start=plaza, destination=hotel,
    description="YOU ARE IN THE HOTEL. THERE'S A DOOR TO THE BASEMENT IN FRONT OF YOU."
))

hotel_to_plaza = add(Path(
    start=hotel, destination=plaza,
    description="YOU ARE IN THE PLAZA, FACING THE HOTEL."
))

hotel_to_basement = add(Path(
    start=hotel, destination=basement,
    description="YOU ARE IN THE BASEMENT. THERE ARE STAIRS UP TO THE HOTEL LOBBY BEHIND YOU."

))
basement_to_hotel = add(Path(
    start=basement, destination=hotel,
    description="YOU ARE IN THE HOTEL LOBBY. THERE'S AN EXIT TO THE PLAZA IN FRONT OF YOU."
))

test_session = add(Session(
    code='TestSession1', active=True,
    current_location=hotel, previous_location=portal))

db.session.commit()
