import jwt
import eventlet
import socketio
import os
import json
from flask import Flask
from flask_cors import CORS

with open('config.json', 'r') as file:
    dataApp = json.loads(file.read())
    
SECRET_SEED = "MiseriDevSeed"

# Crear una instancia de Flask
app = Flask(__name__)
CORS(app)

# Crear una instancia de Socket.IO
sio = socketio.Server(cors_allowed_origins='*')

# Definir el evento de conexión
@sio.on('connect')
def connect(sid, environ, token):
    
    try:
        jwt.decode(token["token"], SECRET_SEED, algorithms=["HS256"])
    except:
        sio.emit('log', "Invalid token, your connection is about to be closed.", to=sid)
        sio.disconnect(sid, None,True)
        return
    
    sio.emit('servversion', dataApp["version"], to=sid)

# Definir el evento de desconexión
@sio.on('disconnect')
def disconnect(sid):
    print('Cliente desconectado:', sid)

# Definir un evento personalizado
@sio.on('my_event')
def my_event(sid, data):
    print('Evento personalizado recibido:', data)
    sio.emit('my_response', {'response': 'Respuesta del servidor'}, room=sid)


# Adjuntar la aplicación Flask al servidor Socket.IO
app = socketio.WSGIApp(sio, app)

if __name__ == '__main__':
    # Iniciar el servidor Socket.IO
    eventlet.wsgi.server(eventlet.listen(('', 5000)),
                         app, log=open(os.devnull, "w"))
