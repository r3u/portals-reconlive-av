from model import ChatlogEntry
from pythonosc import udp_client

host = "127.0.0.1"
port = 57120


class SuperColliderEventListener:
    def __init__(self):
        super().__init__()
        self.__client = udp_client.SimpleUDPClient(host, port)

    def on_message(self, msg: ChatlogEntry):
        pass

    def on_navigation(self, start_id: int, destination_id: int, session_id: int):
        self.__client.send_message('/load_macro', 'test-macro-1')
