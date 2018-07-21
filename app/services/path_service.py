from model import Path


def get_path(start_id: int, destination_id: int):
    return Path \
        .query \
        .filter(Path.start_id == start_id, Path.destination_id == destination_id) \
        .one()
