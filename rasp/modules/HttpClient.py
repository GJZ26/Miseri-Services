from enum import Enum
import requests


class Mode(Enum):
    REMOTE = "remote"
    LOCAL = "local"


class HttpClient:

    URI = {"local": "http://localhost:5000/data",
           "remote": "http://localhost:5000/data"}

    connectionMode: Mode = None

    def __init__(self) -> None:
        pass

    def connect(self, mode: Mode):

        if mode is not Mode.LOCAL and mode is not Mode.REMOTE:
            print("Parámetro no válido")
            return

        self.connectionMode = mode.value
        print(
            f'Conexion establecida como {mode.value} hacia {self.URI[mode.value]}')

    def toggleConnection(self):
        if self.connectionMode == Mode.LOCAL.value:
            self.connect(Mode.REMOTE)
        else:
            self.connect(Mode.LOCAL)

    def sendData(self, data):
        try:
            response = requests.post(self.URI[self.connectionMode], json=data)
            if response.status_code == 200:
                print("Consulta con éxito")
        except:
            print("No se pudo realizar la conexion con el servidor HTTP")
