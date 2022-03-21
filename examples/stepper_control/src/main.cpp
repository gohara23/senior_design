#include <Arduino.h>

#define step_pin 12
#define dir_pin 11

void setup() {
  pinMode(step_pin, OUTPUT);
  pinMode(dir_pin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(dir_pin, HIGH);
  Serial.println("forward");
  for (uint16_t x = 0; x < 200; x++){
    digitalWrite(step_pin, HIGH);
    delayMicroseconds(1000);
    digitalWrite(step_pin, LOW);
    delayMicroseconds(1000);
  }
  delay(1000);
  digitalWrite(dir_pin, LOW);
  Serial.println("backward");
  for (uint16_t x = 0; x < 200; x++){
    digitalWrite(step_pin, HIGH);
    delayMicroseconds(1000);
    digitalWrite(step_pin, LOW);
    delayMicroseconds(1000);
  }
  delay(1000);
}

