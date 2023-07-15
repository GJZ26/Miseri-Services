# Events Map - WS Server

Lista de eventos y payload para conexiones con clientes

# Conexion
Para establecer la conexion con el servidor web socket, puedes hacerlo mediante la IP pública de nuestro servidor, y bajo el namespace de `/client`, como se muestra en el ejemplo anterior con Node + Socket io:

```javascript
import { io } from "socket.io-client"; // Importamos socket.io client

const URI = "http://10.0.0.1:5505/client" // Reemplazar la IP por la IP pública del server

const token = "eyJhb ... w5c" // token de autenticacion de registro

const socket = io(URI, {
    auth:{
        token: token
    }
})
```

De esta forma estaremos estableciendo conexion con nuestro servidor WebSocket :)

## On "data"
El evento `data`, retorna los valores de los multiples sensores del ESP32, este evento se usa principalmente en la actualizacion de los monitores de la página principal.

Ejemplo:

```javascript
// ... Conexion ..//

socket.on('data', (data) => {

    console.log(`Data recibida del servidor: ${data}`)

    //... Uso del objeto data para DOM ...//
})

```

### Payload
Este es el valor que contiene data:

```json
{
    "version": "2.3.0-dev",
    "session": "UAD_AS",
    "deviceId": 1,
    "air": {
      "gas_ppm": 485.173767,
      "co_ppm": 465.3416138
    },
    "light_sensor_a": {
      "raw": 2906,
      "percent": 70
    },
    "light_sensor_b": {
      "raw": 2814,
      "percent": 68
    },
    "hum_temp_a": {
      "temperature": 28,
      "humidity": 74
    },
    "hum_temp_b": {
      "temperature": 28,
      "humidity": 74
    }
  }
```

## On "log"
El evento `log` provee información de parte del servidor sobre acontecimientos importantes sobre la conexion del servidor, por ejemplo, una nueva conexión, el fallo de algún servidor o conexion fisica, entre otro. El uso de este evento es **opcional**, pero aquí está un ejemplo de uso:

```javascript
// ... Conexion .. //
socket.on("log",(message)=>{
    console.log(message); // Imprime el mensaje del servidor en consola del navegador
})
```

### payload
El payload es un `string`, por lo que no hace falta hacer conversiones o validaciones, estos son algunos de los posibles mensajes:
```text
"Tu sensor ha perdido conexion con nuuestro servidor..."
"Conexion exitosa"
"Nuevo cliente conectado!"
"Un usuario ha perdido conexion con el servidor"
```

## On "updateData"
Falta definicion

### payload
```json
{
    "id":21,
    "air": {"gasPmm": 234.45, "coPmm":245.34},
    "light": { "raw": 2906, "percent": 70},
    "humTemp": { "temperature": 28, "humidity": 74},
    "date":"26-06-2023",
    "session": "asd_asd",
    "deviceId":3
}
```

# On "updateListData"
Falta definicion x2

### payload
```json
[
    {
        "id":21,
        "air": {"gasPmm": 234.45, "coPmm":245.34},
        "light": { "raw": 2906, "percent": 70},
        "humTemp": { "temperature": 28, "humidity": 74},
        "date":"26-06-2023",
        "session": "asd_asd",
        "deviceId":3
    },
    {...},
    {...},
    {...}
]
```