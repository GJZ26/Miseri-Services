import socketio
from enum import Enum

class Mode(Enum):
    LOCAL = "local"
    REMOTE = "remote"

class WsClient:
    URI = {'local':'http://localhost:5000', 'remote':'http://localhost:5000'}
    NAMESPACE = '/sensor'
    connection:socketio.client.Client = None
    connectionMode:Mode = None
    isConnected = False
    
    def __init__(self):
        pass

    def connect(self, mode:Mode):
        
        if mode is not Mode.LOCAL and mode is not Mode.REMOTE:
            print("Parámetro no válido")
            return
        
        if self.connection is not None:
            print("Ya tienes una conexion activa")
            return
        
        try:
            self.connectionMode = mode.value
            self.connection = socketio.Client()
            self.connection.connect(self.URI[self.connectionMode],namespaces=[self.NAMESPACE])
            print("Conexion exitosa!")
        except:
            print("Conexion fallida!")
    
    def disconnect(self):
        if self.connection is None:
            print("No tienes ninguna conexion activa")
            return
        self.connection.disconnect()
        self.connection = None
        print("Te has desconectado del servidor")
        
    def toggleConnection(self):
        self.disconnect()
        if self.connectionMode == Mode.LOCAL.value:
            self.connect(Mode.REMOTE)
        else:
            self.connect(Mode.LOCAL)
        
    def sendData(self, data):
        if self.isConnected:
            self.connection.emit('data',data,namespace=self.NAMESPACE)
        else:
            print("No se puede enviar informacion porque no hay una conexion establecida")
    