from datetime import datetime
import pytz

class PyE:
    def __init__(self) -> None:
        pass

    def decomposeAndGroup(self, data):
        result = {
            "meta": {"total_data": 0, "date": None, "session":None, "deviceId":None},
            "gas_ppm": [],
            "co_ppm": [],
            "light": [],
            "tem": [],
            "hum": []
        }
        for i in data:
            result["gas_ppm"].append(i["air"]["gas_ppm"])
            result["co_ppm"].append(i["air"]["co_ppm"])
            result["hum"].append(
                (i["hum_temp_a"]["humidity"] + i["hum_temp_b"]["humidity"])/2)
            result["tem"].append(
                (i["hum_temp_a"]["temperature"] + i["hum_temp_b"]["temperature"])/2)
            result["light"].append(
                (i["light_sensor_a"]["percent"] + i["light_sensor_b"]["percent"])/2)
            result["meta"]["total_data"] += 1
        now = datetime.now(pytz.timezone('America/Mexico_City'))
        result["meta"]["date"] = f'{now.day}/{now.month}/{now.year} - {now.hour}:{now.minute}:{now.second} - {now.tzinfo}'
        result["meta"]["session"] = data[0]["session"]
        result["meta"]["deviceId"] = data[0]["deviceId"]
        return result

    def calculateData(self, list):
        result = {
            "meta": {"total_data": 0, "date": None},
            "gas_ppm": {"media": None, "range": None, "highest": None, "lowest": None, "varUnit": None},
            "co_ppm": {"media": None, "range": None, "highest": None, "lowest": None, "varUnit": None},
            "light": {"media": None, "range": None, "highest": None, "lowest": None, "varUnit": None},
            "tem": {"media": None, "range": None, "highest": None, "lowest": None, "varUnit": None},
            "hum": {"media": None, "range": None, "highest": None, "lowest": None, "varUnit": None}
        }

        result["meta"]["total_data"] = list["meta"]["total_data"]
        result["meta"]["date"] = list["meta"]["date"]
        result["meta"]["session"] = list["meta"]["session"]
        result["meta"]["deviceId"] = list["meta"]["deviceId"]

        result["gas_ppm"]["media"] = sum(
            list["gas_ppm"]) / len(list["gas_ppm"])
        result["co_ppm"]["media"] = sum(list["co_ppm"]) / len(list["co_ppm"])
        result["light"]["media"] = sum(list["light"]) / len(list["light"])
        result["tem"]["media"] = sum(list["tem"]) / len(list["tem"])
        result["hum"]["media"] = sum(list["hum"]) / len(list["hum"])

        result["gas_ppm"]["highest"] = max(list["gas_ppm"])
        result["co_ppm"]["highest"] = max(list["co_ppm"])
        result["light"]["highest"] = max(list["light"])
        result["tem"]["highest"] = max(list["tem"])
        result["hum"]["highest"] = max(list["hum"])

        result["gas_ppm"]["lowest"] = min(list["gas_ppm"])
        result["co_ppm"]["lowest"] = min(list["co_ppm"])
        result["light"]["lowest"] = min(list["light"])
        result["tem"]["lowest"] = min(list["tem"])
        result["hum"]["lowest"] = min(list["hum"])

        result["gas_ppm"]["range"] = result["gas_ppm"]["highest"] - \
            result["gas_ppm"]["lowest"]
        result["co_ppm"]["range"] = result["co_ppm"]["highest"] - \
            result["co_ppm"]["lowest"]
        result["light"]["range"] = result["light"]["highest"] - \
            result["light"]["lowest"]
        result["tem"]["range"] = result["tem"]["highest"] - \
            result["tem"]["lowest"]
        result["hum"]["range"] = result["hum"]["highest"] - \
            result["hum"]["lowest"]
            
        result["gas_ppm"]["varUnit"] = self.variationUnit(list["gas_ppm"])
        result["co_ppm"]["varUnit"] = self.variationUnit(list["co_ppm"])
        result["light"]["varUnit"] = self.variationUnit(list["light"])
        result["tem"]["varUnit"] = self.variationUnit(list["tem"])
        result["hum"]["varUnit"] = self.variationUnit(list["hum"])

        return result

    def variationUnit(self,data: list):
        maxDecimalNumber = 0
        for i in data:
            if "." in str(i):
                maxDecimalNumber = (
                    len(str(i).split(".")[1])
                    if len(str(i).split(".")[1]) > maxDecimalNumber
                    else maxDecimalNumber
                )

        return "0." + ("0" * (maxDecimalNumber - 2)) + "1"
