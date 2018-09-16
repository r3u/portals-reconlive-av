from model import ChatlogEntry, Location
from services.event_service import BaseEventListener
from services.asset_metadata_service import asset_metadata, AssetMetadataDef
from services.navigation_service import get_location
from pythonosc import udp_client
import random

host = "127.0.0.1"
port = 57120


class SuperColliderEventListener(BaseEventListener):
    def __init__(self):
        super().__init__()
        self.__client = udp_client.SimpleUDPClient(host, port)

    def on_message(self, msg: ChatlogEntry):
        pass

    def on_navigation(self, start_id: int, destination_id: int, session_id: int):
        destination: Location = get_location(destination_id)
        print(destination.name)
        metadata = [m for m in asset_metadata.by_location(destination.name)
                    if m.type == 'supercollider']

        if len(metadata) > 0:
            m: AssetMetadataDef = random.choice(metadata)
            print(m.asset_filename)
            self.__client.send_message('/load_macro', m.asset_filename)
