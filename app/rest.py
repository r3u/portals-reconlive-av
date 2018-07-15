from model import ChatlogEntry


def rest_chat_msg(ent: ChatlogEntry):
    return {
        "session_id": ent.session_id,
        "id": ent.id,
        "message": ent.message,
        "actor": ent.actor.name
    }