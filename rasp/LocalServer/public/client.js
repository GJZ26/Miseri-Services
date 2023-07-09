import dataApp from "./manifest.json" assert {type: 'json'}

const confButton = document.getElementById("config")
const saveButton = document.getElementById("save")
const jsonCheck = document.getElementById("format-json")
const timeStamp = document.getElementById("showDateTime")
const dialogBox = document.getElementById("preferences")
const autoScroll = document.getElementById("autoScroll")

const gasmedia = document.getElementById("gasMedia")
const comedia = document.getElementById("coMedia")
const gasRange = document.getElementById("gasRange")
const coRange = document.getElementById("coRange")
const gasAmplitude = document.getElementById("gasAmplitude")
const coAmplitude = document.getElementById("coAmplitude")

const token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiZGV2In0.93fVYOMMwzMUI4druQmCtNLQtjgJUufNHTJqsJXtSkU" // Token de autenticación de prueba
const gasLog = []
const coLog = []

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
    if (typeof(data)==="object"){
        gasLog.push(data["air"]["gas_ppm"])
        coLog.push(data["air"]["co_ppm"])
        // console.log(gasLog)
        // console.log(coLog)

        gasmedia.textContent = Math.round(gasLog.reduce((a,b)=> a+b,0) / gasLog.length) + "ppm"
        comedia.textContent = Math.round(coLog.reduce((a,b)=> a+b,0) / coLog.length) + "ppm"

        gasRange.textContent = Math.round(Math.max(...gasLog) - Math.min(...gasLog)) + "ppm"
        coRange.textContent = Math.round(Math.max(...coLog) - Math.min(...coLog)) + "ppm"

        data = JSON.stringify(data,null,4)
        if(jsonCheck.checked) data = data.replace(/\n/g, "<br>").replace(/\t/g, "&nbsp;").replace(/ /g, "&nbsp;")
    }
    print(data)
})

socket.emit("data","Hola mundo")

// MIS COSAS, NI LO LEAS xd

function print(text) {
    const chat = document.getElementById("output")
    if(timeStamp.checked){
        let date = new Date()
        chat.innerHTML += `[${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}]: ` 
    }
    chat.innerHTML += `${text}<br>`

    if(autoScroll.checked) chat.scrollTo(0,chat.scrollHeight)
}

confButton.onclick = () => {
    dialogBox.showModal()
    dialogBox.style.display = "block"
}

saveButton.onclick = () => {
    dialogBox.close()
    dialogBox.style.display = "none"
}

document.getElementById("clientversion").textContent = `Client: ${dataApp["version"]}`
document.getElementById("clear").onclick = () => {document.getElementById("output").innerHTML=""}