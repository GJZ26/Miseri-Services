import socketio
from enum import Enum
import json

class Mode(Enum):
    LOCAL = "local"
    REMOTE = "remote"

class WsClient:
    URI = {}
    NAMESPACE = '/sensor'
    connection:socketio.client.Client = None
    connectionMode:Mode = None
    isConnected = False
    
    def __init__(self):
        with open('./modules/modules-config.json') as file:
            config = json.load(file)
            self.URI["local"] = config["wsclient"]["local"]
            self.URI["remote"] = config["wsclient"]["remote"]

    def connect(self, mode:Mode):
        
        if mode is not Mode.LOCAL and mode is not Mode.REMOTE:
            print("[WsClient]: Invalid parameter")
            return
        
        if self.connection is not None:
            print("[WsClient]: You already have an active connection")
            return
        
        while not self.isConnected:
            try:
                self.connectionMode = mode.value
                self.connection = socketio.Client()
                self.connection.connect(self.URI[self.connectionMode],namespaces=[self.NAMESPACE])
                print(f"[WsClient]: Your connection to {self.URI[self.connectionMode]} has been successful.")
                self.isConnected = True
            except:
                print(f"[WsClient]: Unable to connect to the server at {self.URI[self.connectionMode]}")
    
    def disconnect(self):
        if self.connection is None:
            print("[WsClient]: You have no active connection")
            return
        self.connection.disconnect()
        self.connection = None
        print("[WsClient]: You have been disconnected from the server")
        
    def toggleConnection(self):
        print(f'[WsClient]: Switching connections 🔄')
        self.disconnect()
        if self.connectionMode == Mode.LOCAL.value:
            self.connect(Mode.REMOTE)
        else:
            self.connect(Mode.LOCAL)
        
    def sendData(self, data):
        print("[WsClient]: New request from ESP32 🤖")
        if self.isConnected:
            try:
                self.connection.emit('data',data,namespace=self.NAMESPACE)
            except:
                print("[WsClient]: The last request could not be fulfilled")
                self.isConnected = False
        else:
            print("[WsClient]: No information can be sent because there is no established connection.")
    