#include <ArduinoJson.h>
#include <DHTesp.h>

#define version "2.3.0-dev"

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
  
  // Configuración Salida Serial Rate
  Serial.begin(115200);

  // Configuración libreria DHT
  dhtA.setup(TempHumSensorA, DHTesp::DHT11);
  dhtB.setup(TempHumSensorB, DHTesp::DHT11);

}

void loop() {

  /* CONFIGURACION SERIALIZADOR JSON */
  StaticJsonDocument<300> data;
  String dataParsed;

  /* DETECCION DE GAS */
  int rawGasSensor = analogRead(GasSensor);

  /* AIR QUALITY SENSOR */
  int rawAirQuality = analogRead(AirQualitySensor);

  /* LECTURA FOTORESISTOR */
  int rawPhotoResistorA = analogRead(PhotoResistorA);
  int PhotoResistorPercentA = (rawPhotoResistorA * 100)/4095;

  int rawPhotoResistorB = analogRead(PhotoResistorB);
  int PhotoResistorPercentB = (rawPhotoResistorB * 100)/4095;


  /* TEMPERATURA Y HUMEDAD */
  TempAndHumidity rawTempHumA = dhtA.getTempAndHumidity();
  TempAndHumidity rawTempHumB = dhtB.getTempAndHumidity();

  // Guardando en Json
  data["version"] = version;

  data["air"]["gas_ppm"] = float(rawGasSensor * 1000) / 4025;
  data["air"]["co_ppm"] = float(rawAirQuality * 1000) / 4025;

  data["light_sensor_a"]["raw"] = rawPhotoResistorA;
  data["light_sensor_a"]["percent"] = PhotoResistorPercentA;
  data["light_sensor_b"]["raw"] = rawPhotoResistorB;
  data["light_sensor_b"]["percent"] = PhotoResistorPercentB;

  data["hum_temp_a"]["temperature"] = float(rawTempHumA.temperature);
  data["hum_temp_a"]["humidity"] = int(rawTempHumA.humidity);

  data["hum_temp_b"]["temperature"] = float(rawTempHumB.temperature);
  data["hum_temp_b"]["humidity"] = int(rawTempHumB.humidity);

  // Json -> String
  serializeJson(data,dataParsed);
  Serial.println(dataParsed);

  delay(1000);
}