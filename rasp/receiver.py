import serial
import json
import time

class Receiver:
    rate:int = 115200
    port:str = '/dev/ttyUSB0'
    serialConnection:serial = None
    autoReconnect:bool = True
    isConnected:bool = False
    
    def __init__(self, rate:int=None, port:int=None):
        self.port = port if port is not None else self.port
        self.rate = rate if rate is not None else self.rate
    
    def connect(self, autorecconect=True):
        try:
            self.serialConnection = serial.Serial(self.port,self.rate)
            self.isConnected = True
            return 0
        except:
            print(f'Unable to connect to Serial by port {self.port} and rate {self.rate}')
            self.isConnected = False
            print("Restoring connection......")
            time.sleep(1)
            self.connect()
            return 1
            
    def readSerial(self):
        if self.serialConnection is None:
            print('No connection to the serial port has been established.')
            return 1
        
        try:
            if self.serialConnection.in_waiting > 0:
                return json.loads(
                    self.serialConnection.readline()
                    .decode()
                    .strip()
                )
        except serial.SerialException:
            print(f'Connection to port {self.port} lost or interrupted.')
            if(self.autoReconnect):
                print("Restoring connection......")
                self.connect()
            return 1
    
    def disconnect(self):
        self.serialConnection.close()