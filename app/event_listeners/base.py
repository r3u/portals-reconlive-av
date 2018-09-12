from model import ChatlogEntry


class BaseEventListener:
    def on_message(self, msg: ChatlogEntry):
        pass

    def on_navigation(self, start_id: int, destination_id: int, session_id: int):
        pass


