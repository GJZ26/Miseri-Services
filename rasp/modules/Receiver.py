import serial
import json
import time

class Receiver:
    # This class is in charge of connecting and reading the serial outputs from the USB input.
    # Miseri Sense - 2023 
    # By: GJZ26
    
    rate:int = 115200
    port:str = '/dev/ttyUSB0'
    serialConnection:serial = None
    autoReconnect:bool = True
    isConnected:bool = False
    reconn_delay:int = 0
    max_reconn_attempts: int = 0
    
    def __init__(self, rate:int=None, port:int=None):
        self.port = port if port is not None else self.port
        self.rate = rate if rate is not None else self.rate
        self.setup()
    
    def setup(self):
        with open('./config.json') as file:
            config = json.load(file)
            self.max_reconn_attempts = config["reconnexion"]["attempts_limit"]
            self.reconn_delay = config["reconnexion"]["delay"]
            
    
    def connect(self, autorecconect=True):
        try:
            print("Connecting...")
            self.serialConnection = serial.Serial(self.port,self.rate, timeout=0.01)
            print("Conected!")
            self.isConnected = True
            with open('./config.json') as file:
                config = json.load(file)
                self.max_reconn_attempts = config["reconnexion"]["attempts_limit"]
            return 0
        except:
            self.max_reconn_attempts -= 1
            print(f'Unable to connect to Serial by port {self.port} and rate {self.rate}')
            print(f'Retrying in {self.reconn_delay} seconds - Missing Attempts {self.max_reconn_attempts}')
            self.isConnected = False
            time.sleep(1)
            if self.max_reconn_attempts > 0:
                print("Retrying to connect...")
                self.connect()
                return
            print("Unable to recover connection, please check your hardware connection.")
            quit()
            
    def readSerial(self):
        if self.serialConnection is None:
            print('No connection to the serial port has been established.')
            return None
        
        try:
            if self.serialConnection.in_waiting > 0:
                return json.loads(
                    self.serialConnection.readline()
                    .decode()
                    .strip()
                )
        except serial.SerialException:
            if(self.autoReconnect and self.max_reconn_attempts > 0):
                print(f'Connection to port {self.port} lost or interrupted.')
                print("Retrying to connect...")
                self.connect()
            return None
    
    def disconnect(self):
        self.serialConnection.close()