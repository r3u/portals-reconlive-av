from flask_socketio import SocketIO

from app import app


socketio = SocketIO(app)
