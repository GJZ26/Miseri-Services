import random
import datetime
import modules.HttpClient as HttpClient
from modules.HttpClient import Mode
import threading


class Backup:

    dataCached = []
    dataCachedRemote = []
    session: str = None
    sampleTime: int = 0
    backTime: int = 0

    lastSample = 0
    lastBackup = 0

    requester = HttpClient.HttpClient()

    def __init__(self, sampling_time: int = 3, backup_time: int = 10, connectionMode: str = None):
        self.session = self.createSession()
        self.setup(sampling_time, backup_time)
        if connectionMode == "remote":
            self.requester.connect(Mode.REMOTE)
        else:
            self.requester.connect(Mode.LOCAL)

    def createSession(self):
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890"
        session = f'{letters[random.randrange(0,len(letters),1)]}{letters[random.randrange(0,len(letters),1)]}{letters[random.randrange(0,len(letters),1)]}_{letters[random.randrange(0,len(letters),1)]}{letters[random.randrange(0,len(letters),1)]}{letters[random.randrange(0,len(letters),1)]}'
        return session

    def toggleConnection(self):
        self.requester.toggleConnection()

    def setup(self, sampling_time: int = 3, backup_time: int = 10):
        self.sampleTime = sampling_time
        self.backTime = backup_time

    def verifyBackup(self):
        if self.lastBackup == 0 or datetime.datetime.now() - self.lastBackup >= datetime.timedelta(seconds=self.backTime):
            if len(self.dataCached) <= 0:
                print("[Backuper]: Backup time reached, but no cache data to backup")
                self.lastBackup = datetime.datetime.now()
                return
            print("[Backuper]: Contacting the server for backup ☁️")
            dataToSend = None
            if self.requester.connectionMode == "local":
                dataToSend = self.dataCached
            else:
                dataToSend = self.dataCachedRemote
                
            threading.Thread(target=self.requester.sendData,
                             args=(dataToSend,)).start()
            print("[Backuper]: Removing cache data 🗑️")
            self.dataCached = []
            self.dataCachedRemote = []
            self.lastBackup = datetime.datetime.now()
        pass

    def saveRecord(self, record):

        if self.lastSample == 0 or datetime.datetime.now() - self.lastSample >= datetime.timedelta(seconds=self.sampleTime):
            if record is None:
                print(
                    "[Backuper]: Your last record isn't valid, we're not save that on cache")
                self.lastSample = datetime.datetime.now()
                return
            for recor in record:
                select = {
                    "air": {
                        "gasPpm": None,
                        "coPpm": None
                    },
                    "light": {
                        "raw": None,
                        "percent": None
                    },
                    "humTemp": {
                        "temperature": None,
                        "humidity": None
                    },
                    "date": None,
                    "deviceId": None,
                    "session": None
                }
                select["air"]["gasPpm"] = recor["air"]["gas_ppm"]
                select["air"]["coPpm"] = recor["air"]["co_ppm"]
                select["light"]["raw"] = (
                    recor["light_sensor_a"]["raw"] + recor["light_sensor_b"]["raw"])/2
                select["light"]["percent"] = (
                    recor["light_sensor_a"]["percent"] + recor["light_sensor_b"]["percent"])/2
                select["humTemp"]["raw"] = (
                    recor["hum_temp_a"]["raw"] + recor["hum_temp_b"]["raw"])/2
                select["humTemp"]["percent"] = (
                    recor["hum_temp_a"]["percent"] + recor["hum_temp_b"]["percent"])/2
                select["date"] = datetime.datetime.now().strftime("%d-%m-%Y")
                select["session"] = self.session
                select["deviceId"] = recor["deviceId"]
                self.dataCachedRemote.append(select)

            record.pop("version")
            record["session"] = self.session
            self.dataCached.append(record)
            self.lastSample = datetime.datetime.now()
            print("[Backuper]: Data saved to caché 💾")
