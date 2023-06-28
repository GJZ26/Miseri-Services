import receiver
import json
import socketio

sio = socketio.Client()
sio.connect("http://localhost:5000")

# Configurar la comunicación serial
puerto = 'COM3'  # Especifica el puerto serial correcto
baudios = 115200

def setup():
    global reader
    reader = receiver.Receiver(baudios,puerto)
    reader.connect()
    
def loop():
    global sio
    linea = reader.readSerial()
    if linea is not None:
        print(str(linea) + ",")
        sio.emit("data",linea)
    pass

try:
    setup()
    while True:
        loop()
except KeyboardInterrupt:
    pass