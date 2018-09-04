from flask_socketio import emit


room = 'portals'
namespace = '/chat'


def post_event(json):
    emit('messages', [json], room=room, namespace=namespace)


