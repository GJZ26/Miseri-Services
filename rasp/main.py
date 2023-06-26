import receiver
import socketio

# sio = socketio.Client()

def setup():
    global espReader#, sio
    # sio.connect("http://localhost:5000")
    espReader = receiver.Receiver(74880,"COM3")
    espReader.setup()
    espReader.connect()

def loop():
    global espReader
    lectura = espReader.readSerial()
    if lectura is not None:
        print(lectura)
    pass

try:
    setup()
    while True:
        loop()
        pass
except KeyboardInterrupt:
    pass