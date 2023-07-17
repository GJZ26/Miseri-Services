import subprocess

class ServerManager:
    runnig = False
    thread = None
    
    def __init__(self) -> None:
        pass
    
    def up(self):
        print("Levantando servidor")
        if self.runnig:
            print ("[SerMan]: You already have a server running...")
            return
        print("[SerMan]: Server running...")
        self.thread = subprocess.Popen(["python", "localServer/WebSocketServer.py"])
        self.runnig = True
        
    def shutdown(self):
        print("Apagando servidor")
        if self.runnig:    
            print("[SerMan]: Shutting down server...")
            self.thread.terminate()
            print("[SerMan]: Server shutdown success!")
            self.runnig = False
        

    def isRunnig(self):
        return self.runnig
    
    def toggleServer(self):
        print("[SerMan]: Toggling server state 😏")
        if(not self.runnig):
            self.up()
        else:
            self.shutdown()