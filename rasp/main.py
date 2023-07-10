import modules.Receiver as Receiver
import modules.WsClient as wsclient
from modules.WsClient import Mode
import modules.Backuper as GoodMan

ws = wsclient.WsClient()
backup = GoodMan.Backup()

# Configurar la comunicación serial
puerto = 'COM3'  # Especifica el puerto serial correcto
baudios = 115200

ws.connect(Mode.REMOTE)

def setup():
    global reader
    reader = Receiver.Receiver(baudios,puerto)
    reader.connect()
    
def loop():
    global backup, reader
    linea = reader.readSerial()
    if linea is not None:
        #print(str(linea) + ",")
        print("-- Data from ESP32")
        ws.sendData(linea)
        backup.saveRecord(linea)
    backup.verifyBackup()
    pass

try:
    setup()
    while True:
        loop()
except KeyboardInterrupt:
    pass