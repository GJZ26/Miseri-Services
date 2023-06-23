import os
import serial
import time

# Configuración de los puertos
puertoProduccion = '/dev/ttyUSB0'
puertoDevelopment = 'COM3'

# Serial Rate
incomingRate = 115200

try:
    incomingConn = serial.Serial(puertoDevelopment, incomingRate)
except:
    print(f'Impossible to reach incoming connection to ESP32 on port {puertoDevelopment} at {incomingRate} rate')

try:
    while True:
        pass
except KeyboardInterrupt:
    pass

incomingConn.close()