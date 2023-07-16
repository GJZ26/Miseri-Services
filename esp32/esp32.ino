#include <ArduinoJson.h>
#include <DHTesp.h>

#define version "3.0.2-dev"
#define deviceId 1

#define GasSensor 2
#define AirQualitySensor 14

#define PhotoResistorA 4
#define PhotoResistorB 26

#define TempHumSensorA 5
#define TempHumSensorB 27

DHTesp dhtA;
DHTesp dhtB;

void setup()
{

  Serial.begin(115200); // Make sure you have the same baud rate in Python:)

  dhtA.setup(TempHumSensorA, DHTesp::DHT11);
  dhtB.setup(TempHumSensorB, DHTesp::DHT11);

}

void loop()
{

  /* JSON SERIALIZER CONFIGURATION */
  StaticJsonDocument<300> data;
  String dataParsed;

  /* GAS & AIR QUALITY SENSOR */
  int rawGasSensor = analogRead(GasSensor);
  int rawAirQuality = analogRead(AirQualitySensor);

  /* PHOTORESISTOR READING AND CONVERSION */
  int rawPhotoResistorA = analogRead(PhotoResistorA);
  int PhotoResistorPercentA = (rawPhotoResistorA * 100) / 4095;

  int rawPhotoResistorB = analogRead(PhotoResistorB);
  int PhotoResistorPercentB = (rawPhotoResistorB * 100) / 4095;

  /* TEMPERATURE AND HUMIDITY */
  TempAndHumidity rawTempHumA = dhtA.getTempAndHumidity();
  TempAndHumidity rawTempHumB = dhtB.getTempAndHumidity();

  // Storing in Json
  data["version"] = version;
  data["deviceId"] = deviceId;

  data["air"]["gas_ppm"] = float(rawGasSensor * 1023.0) / 4025;
  data["air"]["co_ppm"] = float(rawAirQuality * 1023.0) / 4025;

  data["light_sensor_a"]["raw"] = rawPhotoResistorA;
  data["light_sensor_a"]["percent"] = PhotoResistorPercentA;
  data["light_sensor_b"]["raw"] = rawPhotoResistorB;
  data["light_sensor_b"]["percent"] = PhotoResistorPercentB;

  data["hum_temp_a"]["temperature"] = float(rawTempHumA.temperature);
  data["hum_temp_a"]["humidity"] = int(rawTempHumA.humidity);

  data["hum_temp_b"]["temperature"] = float(rawTempHumB.temperature);
  data["hum_temp_b"]["humidity"] = int(rawTempHumB.humidity);

  // Json -> String
  serializeJson(data, dataParsed);
  Serial.println(dataParsed);

  delay(1000);
}