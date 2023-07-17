import modules.Receiver as Receiver
import modules.WsClient as wsclient
from modules.WsClient import Mode
import modules.Backuper as GoodMan
import modules.LCD as screen
import modules.physicalManager as phy
import modules.ServersManager as sm

scrn = screen.LCD()
physic = phy.PhysicalManager()
scrn.say("Conectando a los servidores...")
ser = sm.ServerManager()

ws = wsclient.WsClient()
backup = GoodMan.Backup(3,10,"remote")

# Configurar la comunicación serial
puerto = None #'COM3'  # Especifica el puerto serial correcto
baudios = 115200

def setup():
    global reader, ws, scrn
    ws.connect(Mode.REMOTE)
    reader = Receiver.Receiver(baudios,puerto)
    reader.connect()
    print("\n--- Miseri Sense | Raspberry Services ---\n")
    scrn.welcomeScreen()
    
def loop():
    global backup, reader, physic,ser
    linea = reader.readSerial()
    if linea is not None:
        ws.sendData(linea)
        backup.saveRecord(linea)
    backup.verifyBackup()
    if physic.readPins():
        scrn.clear()
        scrn.say("Cambiando       protocolos")
        ser.toggleServer()
        print("[Main]: Toggling servers")
        ws.toggleConnection()
        backup.toggleConnection()
        scrn.clear()
        scrn.say(f"Actualizado a:  {ws.connectionMode}")
    pass

try:
    setup()
    while True:
        loop()
except KeyboardInterrupt:
    pass