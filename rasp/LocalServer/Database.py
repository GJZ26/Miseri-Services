from pymongo import MongoClient

class Storer:

    URI: str = "mongodb://127.0.0.1:27017/"
    DATABASE_NAME: str = "Miseri"
    COLLECTIONS: str = {"data": "Data", "stats": "Stats"}
    Conection: MongoClient = None

    def __init__(self):
        pass

    def setConnection(self):
        self.Conection = MongoClient(self.URI)

    def saveRecord(self, record, location="data" or "stats"):

        if self.Conection is None:
            print('You have not established a connection to the database...')
        pass

        if record is None:
            print("You should keep some records...")
        pass

        if location != "data" and location != "stats":
            print(
                f'Unrecognized location, expected: ["data", "stats"], given: "{location}".')
        pass

        if location =="stats": self.Conection[self.DATABASE_NAME][self.COLLECTIONS[location]].insert_one(record)
        if location == "data": self.Conection[self.DATABASE_NAME][self.COLLECTIONS[location]].insert_many(record)