from typing import List
from event_listeners.base import BaseEventListener
from event_listeners.socketio import SocketIOEventListener
from event_listeners.supercollider import SuperColliderEventListener
from model import ChatlogEntry


listeners: List[BaseEventListener] = [SocketIOEventListener(), SuperColliderEventListener()]


def handle_message(msg: ChatlogEntry):
    for listener in listeners:
        listener.on_message(msg)


def handle_navigation(start_id: int, destination_id: int, session_id: int):
    for listener in listeners:
        listener.on_navigation(start_id, destination_id, session_id)
