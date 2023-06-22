import serial
import json
import os

# Configurar la comunicación serial
puerto = '/dev/ttyUSB0'  # Especifica el puerto serial correcto
baudios = 115200

# Iniciar la conexión serial
ser = serial.Serial(puerto, baudios)

try:
    while True:
        if ser.in_waiting > 0:
            # Leer una línea de datos del monitor serial
            linea = ser.readline().decode().strip()
            data = json.loads(linea)
            os.system("clear")
            print(f'Temperatura: {data["temperature"]:.2f}°C')
            print(f'Humedad: {data["humidity"]}%')
            print(f'Concentración de Gases: {data["gas_level"]["percent"]}%')
            print(f'Nivel de luz: {data["light_level"]["percent"]}%')
except KeyboardInterrupt:
    # Cerrar la conexión serial al finalizar
    ser.close()
