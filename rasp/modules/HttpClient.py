from enum import Enum
import requests
import json


class Mode(Enum):
    REMOTE = "remote"
    LOCAL = "local"


class HttpClient:

    URI = {}

    connectionMode: Mode = None

    def __init__(self):
        with open('./modules/modules-config.json') as file:
            config = json.load(file)
            self.URI["local"] = config["httpclient"]["local"]
            self.URI["remote"] = config["httpclient"]["remote"]

    def connect(self, mode: Mode):

        if mode is not Mode.LOCAL and mode is not Mode.REMOTE:
            print("[HttClient]: Invalid parameter ❌")
            return

        self.connectionMode = mode.value
        print(
            f'[HttClient]: Requests for endorsement will be made as {mode.value} to {self.URI[mode.value]}.')

    def toggleConnection(self):
        print(f'[HttClient]: Switching connections 🔄')
        if self.connectionMode == Mode.LOCAL.value:
            self.connect(Mode.REMOTE)
        else:
            self.connect(Mode.LOCAL)

    def sendData(self, data):
        try:
            response = requests.post(self.URI[self.connectionMode], json=data)
            if response.status_code == 200:
                print("[HttClient]: Successful database backup ☁️")
        except:
            print("[HttClient]: Unable to complete server backup request ❌")
