import jwt
import eventlet
import socketio
import os
import json
from flask import Flask
from flask_cors import CORS

users = []

with open('config.json', 'r') as file:
    dataApp = json.loads(file.read())
    
SECRET_SEED = "MiseriDevSeed" # Secreto de prueba, eliminar en produccion

# Crear una instancia de Flask
app = Flask(__name__)
CORS(app)

# Crear una instancia de Socket.IO
sio = socketio.Server(cors_allowed_origins='*')

# Definir el evento de conexión
@sio.on('connect')
def connect(sid, environ, token):
    global users
    # try:
    #     jwt.decode(token["token"], SECRET_SEED, algorithms=["HS256"])
    # except:
    #     sio.emit('forbidden', {"message":"Invalid token, your connection is about to be closed."})
    #     sio.disconnect(sid)
        
    print('A new user logged in:', environ['REMOTE_ADDR'])
    sio.emit('servversion', dataApp["version"], to=sid)
    users.append(sid)

# Definir el evento de desconexión
@sio.on('disconnect')
def disconnect(sid):
    print('A user has disconnected')

@sio.on('data')
def data(ssid, data):
    global users
    print(data)
    for i in users:
        sio.emit('log',data,to=i)
    

# Adjuntar la aplicación Flask al servidor Socket.IO
app = socketio.WSGIApp(sio, app)

if __name__ == '__main__':
    # Iniciar el servidor Socket.IO
    eventlet.wsgi.server(eventlet.listen(('', 5000)),
                         app, log=open(os.devnull, "w"))
