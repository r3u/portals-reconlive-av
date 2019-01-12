import asyncio
import socketio
import requests
import random

import state

from pythonosc import udp_client


web_server = "http://127.0.0.1:8080"
osc_host = "127.0.0.1"
osc_port = 57120

debug = False

loop = asyncio.get_event_loop()
sio = socketio.AsyncClient()
osc_client = udp_client.SimpleUDPClient(osc_host, osc_port)


class BridgeError(Exception):
    pass


@sio.on('connect', namespace='/chat')
async def on_connect():
    print('Connected')
    await sio.emit('joined', {}, namespace='/chat')


@sio.on('messages', namespace='/chat')
async def on_message(messages):
    for message in messages:
        if message['event_type'] == 'message':
            if debug:
                print("Received message: {0}".format(message['message']))
        elif message['event_type'] == 'navigation':
            on_location_change(message['destination_id'])


@sio.on('disconnect', namespace='/chat')
async def on_disconnect():
    print('Disconnected')


def get_location_metadata(location_id):
    url = '{0}/metadata.json?location_id={1}'.format(web_server, location_id)
    res = requests.get(url)
    if res.status_code != 200:
        raise BridgeError("Failed to get location metadata, status code={0}".format(res.status_code))
    return res.json()


def get_current_location():
    url = '{0}/current_location.json'.format(web_server)
    res = requests.get(url)
    if res.status_code != 200:
        raise BridgeError("Failed to get current location, status code={0}".format(res.status_code))
    return res.json()


def on_location_change(new_current_location_id):
    print("Location changed. New location_id={0}".format(new_current_location_id))
    metadata = get_location_metadata(new_current_location_id)
    state.current_location = {
        'id': new_current_location_id,
        'metadata': metadata
    }

    if len(metadata) > 0:
        random_meta = random.choice(metadata)
        asset = random_meta['asset']
        print('Sending message /load_macro "{0}"'.format(asset))
        osc_client.send_message('/load_macro', asset)


async def background_task():
    while True:
        print("Hello from background thread! Current location = {0}".format(state.current_location))
        await sio.sleep(10)


async def start():
    on_location_change(get_current_location()['id'])

    sio.start_background_task(background_task)
    await sio.connect(web_server, namespaces=['/chat'])
    await sio.wait()


if __name__ == '__main__':
    loop.run_until_complete(start())
