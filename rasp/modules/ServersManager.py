import subprocess

class ServerManager:
    runnig = False
    thread = None
    
    def __init__(self) -> None:
        pass
    
    def up(self):
        if self.runnig:
            print ("[SerMan]: You already have a server running...")
            return
        print("Server running...")
        self.thread = subprocess.Popen(["python", "localServer/WebSocketServer.py"])
        self.runnig = True
        
    def shutdown(self):
        if self.runnig:    
            print("[SerMan]: Shutting down server...")
            self.thread.terminate()
            print("[SerMan]: Server shutdown success!")
            self.runnig = False
        

    def isRunnig(self):
        return self.isRunnig