import modules.Receiver as Receiver
import modules.WsClient as wsclient
from modules.WsClient import Mode
import modules.Backuper as GoodMan
import modules.LCD as screen

scrn = screen.LCD()

scrn.say("Conectando a los servidores...")

ws = wsclient.WsClient()
backup = GoodMan.Backup()

# Configurar la comunicación serial
puerto = 'COM3'  # Especifica el puerto serial correcto
baudios = 115200

def setup():
    global reader, ws, scrn
    ws.connect(Mode.LOCAL)
    reader = Receiver.Receiver(baudios,puerto)
    reader.connect()
    print("\n--- Miseri Sense | Raspberry Services ---\n")
    scrn.welcomeScreen()
    
def loop():
    global backup, reader
    linea = reader.readSerial()
    if linea is not None:
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