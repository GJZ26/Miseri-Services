# Version 2.0.0 - dev

import os
import serial
import time
import json

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
        if incomingConn.in_waiting > 0:
            # Leer una línea de datos del monitor serial
            linea = incomingConn.readline().decode().strip()
            data = json.loads(linea)
            os.system("cls")
            print("Miseri Sense Version:",data["version"])
            print("")
            print(data)
            print("")
            print("Temperature Sensor A: ",data["hum_temp_a"]["temperature"], "°C")
            print("Temperature Sensor B: ",data["hum_temp_b"]["temperature"], "°C")
            print("")
            print("Humidity Sensor A: ",data["hum_temp_a"]["humidity"], "%")
            print("Humidity Sensor B: ",data["hum_temp_b"]["humidity"], "%")
            print("")
            print("Light Level Sensor A:", data["light_sensor_a"]["percent"],"%")
            print("Light Level Sensor B:", data["light_sensor_b"]["percent"],"%")
            print("")
            print("Raw Gas Data:", data["air"]["gas_raw"])
            print("Raw Air Quality Data:", data["air"]["quality_raw"])
            
except KeyboardInterrupt:
    # Cerrar la conexión serial al finalizar
    incomingConn.close()

incomingConn.close()