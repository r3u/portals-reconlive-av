from model import ChatlogEntry, Path


def rest_chat_msg(ent: ChatlogEntry):
    return {
        "event_type": "message",
        "session_id": ent.session_id,
        "id": ent.id,
        "message": ent.message,
        "actor": ent.actor.name
    }


def rest_navigation_msg(start_id: int, destination_id: int, session_id: int):
    return {
        "event_type": "navigation",
        "session_id": session_id,
        "start_id": start_id,
        "destination_id": destination_id
    }