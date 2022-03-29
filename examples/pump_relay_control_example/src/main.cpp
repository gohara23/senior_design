#include <Arduino.h>

#define PUMP_ONE 33
#define PUMP_TWO 34
#define PUMP_THREE 35



void setup() {
  pinMode(PUMP_ONE, OUTPUT);
  pinMode(PUMP_TWO, OUTPUT);
  pinMode(PUMP_THREE, OUTPUT);

}

void loop() {
  digitalWrite(PUMP_ONE, HIGH);
  delay(500);
  digitalWrite(PUMP_ONE, LOW);
  digitalWrite(PUMP_TWO, HIGH);
  delay(1000);
  digitalWrite(PUMP_TWO, LOW);
  delay(200);
  digitalWrite(PUMP_THREE, HIGH);
  delay(100);
  digitalWrite(PUMP_THREE, LOW);
}