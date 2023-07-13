#include <ArduinoJson.h>
#include <DHTesp.h>
#include <LiquidCrystal_I2C.h>

#define version "3.0.1-dev"
#define deviceId 1

#define GasSensor 2
#define AirQualitySensor 14

#define PhotoResistorA 4
#define PhotoResistorB 26

#define TempHumSensorA 5
#define TempHumSensorB 27

#define SCLPin 22
#define SDAPin 21

DHTesp dhtA;
DHTesp dhtB;

LiquidCrystal_I2C lcd(0x27, 16, 2); // Idk why i did that twice, but it works :)

byte Alien[8] = {
    0b00000, // [ ][ ][ ][ ][ ]
    0b11111, // [#][#][#][#][#]
    0b10101, // [#][ ][#][ ][#]
    0b11111, // [#][#][#][#][#]
    0b11111, // [#][#][#][#][#]
    0b01110, // [ ][#][#][#][ ]
    0b01010, // [ ][#][ ][#][ ]
    0b11011  // [#][#][ ][#][#]
};

byte Grade[8] =
    {
        0b00000, // [ ][ ][ ][ ][ ]
        0b00110, // [ ][ ][#][#][ ]
        0b00110, // [ ][ ][#][#][ ]
        0b00000, // [ ][ ][ ][ ][ ]
        0b00000, // [ ][ ][ ][ ][ ]
        0b00000, // [ ][ ][ ][ ][ ]
        0b00000, // [ ][ ][ ][ ][ ]
        0b00000  // [ ][ ][ ][ ][ ]
};

void setup()
{

  Serial.begin(115200); // Make sure you have the same baud rate in Python:)

  dhtA.setup(TempHumSensorA, DHTesp::DHT11);
  dhtB.setup(TempHumSensorB, DHTesp::DHT11);

  Wire.begin(SDAPin, SCLPin); // Setting SDA and SCL pins to control LCDs

  lcd = LiquidCrystal_I2C(0x27, 16, 2);

  lcd.init();
  lcd.createChar(0, Alien);
  lcd.createChar(1, Grade);
  lcd.clear();
  lcd.backlight();
  welcomeScreen();
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

  readSerial();

  delay(1000);
}

void readSerial()
{
  char byteCharacter;
  int byteValue = 0;
  int queueLength = 0;
  bool isLCDScreenCleared = false;
  while (Serial.available() > 0)
  {
    if (!isLCDScreenCleared)
    {
      lcd.clear();
      isLCDScreenCleared = true;
    }
    byteValue = Serial.read();
    byteCharacter = byteValue;

    char a[2];
    a[0] = byteCharacter;
    a[1] = '\0';

    if (byteValue != 13 && byteValue != 10)
    {
      if(byteValue == 126){
        welcomeScreen();
        while (Serial.available() > 0){Serial.read();}
        return;
      }
      if (queueLength == 16)
      {
        lcd.setCursor(0, 1);
      }
      if (byteValue == 94)
      {
        lcd.write(1);
        continue;
      }
      lcd.print(a);
      queueLength++;
    }
  }
}

void welcomeScreen()
{
  lcd.clear();
  lcd.setCursor(2, 0);
  lcd.print("Miseri Sense");
  lcd.setCursor(5, 1);
  lcd.write(0);
  lcd.setCursor(7, 1);
  lcd.write(0);
  lcd.setCursor(9, 1);
  lcd.write(0);
}