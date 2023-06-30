import socketio
import eventlet
import os
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

sio = socketio.Server(cors_allowed_origins='*')


@sio.on('connect', namespace='/client')
def connect(sid, eviron):
    print("New User Connect on Client:)")


app = socketio.WSGIApp(sio, app)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)),
                         app, log=open(os.devnull, 'w'))
