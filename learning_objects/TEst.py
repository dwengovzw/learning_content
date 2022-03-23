#include <Wire.h>
#include <Dwenguino.h>
#include <LiquidCrystal.h>
#define SOUND_SENSOR_PIN_12 12
void setup()
{
  initDwenguino();
  pinMode(SOUND_SENSOR_PIN_12, INPUT);
}

void loop()
{
    dwenguinoLCD.clear();
    dwenguinoLCD.setCursor(0,0);
    dwenguinoLCD.print((digitalRead(SOUND_SENSOR_PIN_12)) + String("db"));
    delay(100);
}