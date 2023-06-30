import socketio
import eventlet
import os
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

sio = socketio.Server(cors_allowed_origins='*')


# Client connection

@sio.on('connect', namespace='/client')
def connect(sid, environ):
    sio.enter_room(sid,'monitor','/client')
    sio.emit('log','A new user has just connected to your device.', room='monitor',namespace='/client', skip_sid=sid)
    sio.emit('log', 'Your connection to the server has been successful.',to=sid, namespace='/client')
    print("User connected")


@sio.on('disconnect', namespace='/client')
def disconnect(sid):
    sio.leave_room(sid,'monitor','/client')
    sio.emit('log','A user has disconnected from your device.', room='monitor',namespace='/client', skip_sid=sid)
    print("User disconnected")

# Sensors namespace

@sio.on('connect', namespace='/sensor')
def connect(sid, environ, algomas):
    print("Your sensor has been successfully connected")
    sio.emit('log','Your sensor has been successfully connected',room='monitor',namespace='/client')
    
@sio.on('disconnect', namespace='/sensor')
def disconnect(sid):
    print("We have lost communication with your sensor.")
    sio.emit('log','We have lost communication with your sensor.',room='monitor',namespace='/client')
    
@sio.on('data', namespace='/sensor')
def data(sid, data):
    print(data)
    sio.emit('data',data,room='monitor',namespace='/client')

# Running App
app = socketio.WSGIApp(sio, app)
if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)),
                         app, log=open(os.devnull, 'w'))
