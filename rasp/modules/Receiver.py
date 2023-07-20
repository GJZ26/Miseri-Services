import serial
import json
import time


class Receiver:

    # This class is in charge of connecting and reading the serial outputs from the USB input.
    # Miseri Sense - 2023
    # By: GJZ26

    rate: int = 115200
    port: str = '/dev/ttyUSB0'
    serialConnection: serial = None
    autoReconnect: bool = True
    isConnected: bool = False
    reconn_delay: int = 0
    max_reconn_attempts: int = 0

    def __init__(self, rate: int = None, port: int = None):
        self.port = port if port is not None else self.port
        self.rate = rate if rate is not None else self.rate
        self.setup()

    def setup(self):
        with open('./modules/modules-config.json') as file:
            config = json.load(file)
            self.max_reconn_attempts = config["receiver"]["attempts_limit"]
            self.reconn_delay = config["receiver"]["delay"]

    def connect(self, autorecconect=True):
        try:
            print(
                f'[Receiver]: Trying to establish connection with serial port {self.port} and baudios {self.rate}')
            self.serialConnection = serial.Serial(
                self.port, self.rate, timeout=0.01)
            print("[Receiver]: Connected ✅")
            self.isConnected = True
            with open('./modules/modules-config.json') as file:
                config = json.load(file)
                self.max_reconn_attempts = config["receiver"]["attempts_limit"]
            return 0
        except:
            self.max_reconn_attempts -= 1
            print(
                f'[Receiver]: Unable to connect to Serial by port {self.port} and rate {self.rate} ❌')
            print(
                f'[Receiver]: Retrying in {self.reconn_delay} seconds - Missing Attempts {self.max_reconn_attempts}')
            self.isConnected = False
            time.sleep(1)
            if self.max_reconn_attempts > 0:
                print("Retrying to connect...")
                self.connect()
                return
            print(
                "[Receiver]: Unable to recover connection, please check your hardware connection.")
            quit()

    def readSerial(self):
        if self.serialConnection is None:
            print('[Receiver]: No connection to the serial port has been established.')
            return None

        try:
            if self.serialConnection.in_waiting > 0:
                linea = None
                raw = None
                try:
                    raw = self.serialConnection.readline().decode().strip()
                    linea = json.loads(raw)
                    return linea
                except:
                    print("Could not parse json")
                    print(raw)
                    return None
        except serial.SerialException:
            if (self.autoReconnect and self.max_reconn_attempts > 0):
                print(
                    f'[Receiver]: Connection to port {self.port} lost or interrupted.')
                print("[Receiver]: Retrying to connect...")
                self.connect()
            return None

    def disconnect(self):
        self.serialConnection.close()
