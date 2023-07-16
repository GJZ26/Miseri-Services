import socketio
import eventlet
import os
import PyE
import Database
from flask import Flask, request, render_template
from flask_cors import CORS

app = Flask(__name__, static_folder="public", static_url_path="/static", template_folder="view")

CORS(app)

god = PyE.PyE()
saver = Database.Storer()

saver.setConnection()

sio = socketio.Server(cors_allowed_origins='*')


# Client connection

@sio.on('connect', namespace='/client')
def connect(sid, environ):
    sio.enter_room(sid,'monitor','/client')
    sio.emit('log','A new user has just connected to your device.', room='monitor',namespace='/client', skip_sid=sid)
    sio.emit('log', 'Your connection to the server has been successful.',to=sid, namespace='/client')
    print("User connected")


@sio.on('disconnect', namespace='/client')
def disconnect(sid):
    sio.leave_room(sid,'monitor','/client')
    sio.emit('log','A user has disconnected from your device.', room='monitor',namespace='/client', skip_sid=sid)
    print("User disconnected")

# Sensors namespace

@sio.on('connect', namespace='/sensor')
def connect(sid, environ, algomas):
    print("Your sensor has been successfully connected")
    sio.emit('log','Your sensor has been successfully connected',room='monitor',namespace='/client')
    
@sio.on('disconnect', namespace='/sensor')
def disconnect(sid):
    print("We have lost communication with your sensor.")
    sio.emit('log','We have lost communication with your sensor.',room='monitor',namespace='/client')
    
@sio.on('data', namespace='/sensor')
def data(sid, data):
    print("Data received from user...")
    sio.emit('data',data,room='monitor',namespace='/client')
    
@app.route('/data', methods=["GET","POST"])
def data():
    global god
    global saver
    
    rawData = request.get_json()
    InformationDecomposed = god.decomposeAndGroup(rawData)
    stats = god.calculateData(InformationDecomposed)
    sio.emit("stats",stats, room='monitor', namespace='/client')
    
    saver.saveRecord(rawData,"data")
    saver.saveRecord(stats,"stats")
    print("Request Done!")
    
    return "Done"

@app.route('/', methods=["GET"])
def page():
    return render_template('index.html')

@app.route('/oiiaoiia', methods=["GET"])
def cat():
    return render_template('hehe.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# Running App
app = socketio.WSGIApp(sio, app)
if __name__ == '__main__':
    try:
        print("\n--- Miseri Sense - HTTP / WS Local Server ---\n")
        print("Server up on port 5000")
        eventlet.wsgi.server(eventlet.listen(('', 5000)),
                            app, log=open(os.devnull, 'w'))
    except KeyboardInterrupt:
        print("Closing server...")
        pass