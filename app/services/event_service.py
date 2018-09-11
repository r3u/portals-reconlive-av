from flask_socketio import emit
from typing import List
from model import ChatlogEntry
from rest import rest_chat_msg, rest_navigation_msg

room = 'portals'
namespace = '/chat'


class BaseEventListener:
    def on_message(self, msg: ChatlogEntry):
        pass

    def on_navigation(self, start_id: int, destination_id: int, session_id: int):
        pass


class SocketIOEventListener(BaseEventListener):
    def on_message(self, msg: ChatlogEntry):
        emit('messages', [rest_chat_msg(msg)], room=room, namespace=namespace)

    def on_navigation(self, start_id: int, destination_id: int, session_id: int):
        emit('messages', [rest_navigation_msg(start_id, destination_id, session_id)], room=room, namespace=namespace)


listeners: List[BaseEventListener] = [SocketIOEventListener()]


def handle_message(msg: ChatlogEntry):
    for listener in listeners:
        listener.on_message(msg)


def handle_navigation(start_id: int, destination_id: int, session_id: int):
    for listener in listeners:
        listener.on_navigation(start_id, destination_id, session_id)
