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

max_message_log_size = 10
message_log = []


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
            message_log.append(message)
            if len(message_log) > max_message_log_size:
                del message_log[-1]
        elif message['event_type'] == 'navigation':
            on_location_change(message['destination_id'])


@sio.on('disconnect', namespace='/chat')
async def on_disconnect():
    print('Disconnected')


def get_location_metadata(location_id):
    url = '{0}/metadata_by_location.json?location_id={1}'.format(web_server, location_id)
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


def get_metadata_by_message_ids(message_ids):
    id_list = ','.join([str(i) for i in message_ids])
    print("Getting metadata for message ids: {0}".format(id_list))
    url = '{0}/metadata_by_messages.json?message_ids={1}'.format(web_server, id_list)
    res = requests.get(url)
    if res.status_code != 200:
        raise BridgeError("Failed to get metadata by message ids, status code={0}".format(res.status_code))
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
    iterations = 0
    while True:
        print("Background task iterations={0}".format(iterations))
        if iterations == 0:  # Skip messages from first iteration
            await sio.sleep(10)
            message_log.clear()
        else:
            if len(message_log) > 0:
                ids = [m['id'] for m in message_log]
                try:
                    matches = get_metadata_by_message_ids(ids)['matches']
                    matches = {k: v for k, v in matches.items() if v['type'] == 'supercollider'}
                    if len(matches) > 0:
                        sorted_matches = list(sorted(matches.items(), key=lambda i: i[1]['score'], reverse=True))
                        max_score = sorted_matches[0][1]['score']
                        best_matches = []
                        for item in sorted_matches:
                            if item[1]['score'] == max_score:
                                best_matches.append(item)
                            else:
                                break
                        asset = random.choice(best_matches)[1]['asset']
                        print("Metadata based asset choice: {0} (score={1})".format(asset, max_score))
                        osc_client.send_message('/load_simple', asset)
                except Exception as e:
                    print("Error in background task: {0}".format(e))
            message_log.clear()
            await sio.sleep(3)
        iterations += 1


async def start():
    on_location_change(get_current_location()['id'])

    sio.start_background_task(background_task)
    await sio.connect(web_server, namespaces=['/chat'])
    await sio.wait()


if __name__ == '__main__':
    loop.run_until_complete(start())
