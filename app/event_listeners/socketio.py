from event_listeners.base import BaseEventListener
from flask_socketio import emit
from rest import rest_chat_msg, rest_navigation_msg
from model import ChatlogEntry

room = 'portals'
namespace = '/chat'


class SocketIOEventListener(BaseEventListener):
    def on_message(self, msg: ChatlogEntry):
        emit('messages', [rest_chat_msg(msg)], room=room, namespace=namespace)

    def on_navigation(self, start_id: int, destination_id: int, session_id: int):
        emit('messages', [rest_navigation_msg(start_id, destination_id, session_id)], room=room, namespace=namespace)


