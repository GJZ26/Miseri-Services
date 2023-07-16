import { createServer } from 'http';
import { Server } from 'socket.io';

import settings from './setting.json' assert {type: 'json'}

const HOSTNAME = settings.host
const PORT = settings.port

const httpServer = createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.write('Hello World!');
    res.end();
    console.log("Request made to remote server")
});
const io = new Server(httpServer, {
    cors: {
        origin: "*",
        methods: ["GET", "POST"]
    }
});

/*--------  Sensors namespace  ------*/

io.of("/sensor").on("connect", (cli) => {
    console.log(`✅ A sensor has successfully connected to the server. - IP ${cli.conn.remoteAddress}`)

    io.of("/client").to("monitor").emit("log", "Your device has successfully established connection.")

    cli.on("disconnect", () => {
        io.of("/client").to("monitor").emit("log", "A sensor has lost communication with the server")
        console.log(`❌ A sensor has lost communication with the server - IP ${cli.conn.remoteAddress}`)
    })

    cli.on("data", (data) => {
        io.of("/client").to("monitor").emit('data', data)
        console.log("ℹ️ Information received from a sensor.")
    })
})

/*------- Client Namespace --------*/

io.of("/client").on("connect", (cli) => {
    cli.join("monitor")

    console.log(`📥 A new user connected to the server - IP ${cli.conn.remoteAddress}`)

    io.of("/client").to("monitor").except(cli.id).emit("log", " -> A user has joined the monitoring.", "monitor")
    console.log("A user has joined the monitoring.")

    cli.emit("log", "Welcome to Miseri Sense")

    cli.on("disconnect", () => {
        cli.leave("monitor")
        io.of("/client").to("monitor").emit("log", "A user has left the monitoring  ->")
        console.log(`📤 A user has lost connection to the server - IP ${cli.conn.remoteAddress}`)
    })
})

httpServer.listen(PORT, HOSTNAME, undefined, () => {
    console.log("\n--- Welcome to Miseri WebWSocket Server ---\n")
    console.log(`Access: http://${HOSTNAME}:${PORT}/`)
});