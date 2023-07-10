import { createServer } from 'http';
import { Server } from 'socket.io';

const httpServer = createServer();
const io = new Server(httpServer, {
    cors: {
        origin: "*",
        methods: ["GET", "POST"]
    }
});

/*--------  Sensors namespace  ------*/

io.of("/sensor").on("connect", (cli) => {
    console.log(cli.conn.remoteAddress)
    console.log("Nuevo sensor conectado:)!")

    cli.on("disconnect",()=>{
        io.of("/client").to("monitor").emit("log","Tu sensor ha perdido conexion con nuuestro servidor...")
        console.log("Sensor ha perdido conexion con el cliente")
    })

    cli.on("data",(data)=>{
        io.of("/client").to("monitor").emit('data',data)
    })
})

/*------- Client Namespace --------*/

io.of("/client").on("connect", (cli) => {
    cli.join("monitor")
    io.of("/client").to("monitor").except(cli.id).emit("log", "Nuevo cliente conectado!", "monitor")
    cli.emit("log", "Conexion exitosa")
    console.log(`Nuevo cliente conectado, a través de la IP: ${cli.conn.remoteAddress}`)
    cli.on("disconnect", () => {
        cli.leave("monitor")
        io.of("/client").to("monitor").emit("log", "Un usuario ha perdido conexion con el servidor")
        console.log(`El cliente ${cli.conn.remoteAddress} ha perdido conexion con el servidor`)
    })
})

httpServer.listen(5555, "192.168.1.66", undefined, () => {
    console.log("Miseri WebSocket Server - Running on: ....")
});