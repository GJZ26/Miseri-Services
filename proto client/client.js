import dataApp from "./manifest.json" assert {type: 'json'}

const token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiZGV2In0.93fVYOMMwzMUI4druQmCtNLQtjgJUufNHTJqsJXtSkU" // Token de autenticación, solo test


// Crear una instancia del cliente Socket.IO
const socket = io(`${dataApp["protocol"]}://${dataApp["host"]}:${dataApp["port"]}`,
    {
        auth: {
            token: token
        }
    }); // Reemplaza la URL con la dirección del servidor Socket.IO

// Evento de conexión
socket.on('connect', (data) => {
    print("Connection established")
});

socket.on('servversion', (data) => {
    document.getElementById("servversion").textContent = `Server: ${data}`
})

// Evento de desconexión
socket.on('disconnect', () => {
    print("Connection lost")
});

socket.on('log',(data)=>{
    print(data)
})

function print(text) {
    const chat = document.getElementById("output")
    chat.innerHTML += `${text}<br>`
    console.log(chat.scrollTo(0,chat.scrollHeight))
}



document.getElementById("clientversion").textContent = `Client: ${dataApp["version"]}`
document.getElementById("clear").onclick = () => {document.getElementById("output").innerHTML=""}