import random
import datetime
import time # test only
import modules.HttpClient as HttpClient
from modules.HttpClient import Mode

class Backup:

    dataCached = []
    session: str = None
    sampleTime: int = 0
    backTime: int = 0

    lastSample = 0
    lastBackup = 0
    
    requester = HttpClient.HttpClient()

    def __init__(self, sampling_time: int = 3, backup_time: int = 10):
        self.session = self.createSession()
        self.setup(sampling_time, backup_time)
        self.requester.connect(Mode.LOCAL)

    def createSession(self):
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890"
        session = f'{letters[random.randrange(0,len(letters),1)]}{letters[random.randrange(0,len(letters),1)]}{letters[random.randrange(0,len(letters),1)]}_{letters[random.randrange(0,len(letters),1)]}{letters[random.randrange(0,len(letters),1)]}{letters[random.randrange(0,len(letters),1)]}'
        return session

    def setup(self, sampling_time: int = 3, backup_time: int = 10):
        self.sampleTime = sampling_time
        self.backTime = backup_time
        
    def verifyBackup(self):
        if self.lastBackup == 0 or datetime.datetime.now() - self.lastBackup >= datetime.timedelta(seconds=self.backTime):
            if len(self.dataCached) <= 0:
                print("Time to backup!, but there's not info cached")
                self.lastBackup = datetime.datetime.now()
                return
            print("Data Backed up ->")
            self.requester.sendData(self.dataCached)
            self.dataCached = []
            self.lastBackup = datetime.datetime.now()
        pass
    
    def saveRecord(self, record):
        if self.lastSample == 0 or datetime.datetime.now() - self.lastSample >= datetime.timedelta(seconds=self.sampleTime):
            if record is None:
                print("Your last record isn't valid, we're not save that on cache")
                self.lastSample = datetime.datetime.now()
                return
            
            record.pop("version")
            record["session"] = self.session
            self.dataCached.append(record)
            self.lastSample = datetime.datetime.now()
            print("Data saved to caché <-")