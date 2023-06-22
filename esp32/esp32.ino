#include <ArduinoJson.h>
#include <DHTesp.h>

#define GasSensor 2
#define PhotoResistor 4
#define TempHumSensor 5

DHTesp dht;

void setup() 
{
  // Configuración Salida Serial Rate
  Serial.begin(115200);

  // Configuración libreria DHT
  dht.setup(TempHumSensor, DHTesp::DHT11);

}

void loop() {

  /* CONFIGURACION SERIALIZADOR JSON */
  StaticJsonDocument<200> data;
  String dataParsed;

  /* LECTURA FOTORESISTOR */
  int rawPhotoResistor = analogRead(PhotoResistor);
  int PhotoResistorPercent = (rawPhotoResistor * 100)/4095;

  /* DETECCION DE GAS */
  int rawGasSensor = analogRead(GasSensor);

  /* TEMPERATURA Y HUMEDAD */
  TempAndHumidity rawTempHum = dht.getTempAndHumidity();

  // Guardando en Json
  data["temperature"] = float(rawTempHum.temperature);
  data["humidity"] = int(rawTempHum.humidity);
  data["light_level"]["raw"] = rawPhotoResistor;
  data["light_level"]["percent"] = PhotoResistorPercent;
  data["gas_level"]["raw"] = rawGasSensor;
  data["gas_level"]["percent"] = (rawGasSensor* 100)/4095;

  // Json -> String
  serializeJson(data,dataParsed);
  Serial.println(dataParsed);

  delay(1000);
}