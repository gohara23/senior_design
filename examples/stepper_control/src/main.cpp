#include <Arduino.h>

#define step_pin 32
#define dir_pin 31

#define step_pin2 3
#define dir_pin2 2

#define step_pin3 5
#define dir_pin3 4

void setup() {
  pinMode(step_pin, OUTPUT);
  pinMode(dir_pin, OUTPUT);
  pinMode(step_pin2, OUTPUT);
  pinMode(dir_pin2, OUTPUT);

  pinMode(step_pin3, OUTPUT);
  pinMode(dir_pin3, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(dir_pin, HIGH);
  digitalWrite(dir_pin2, HIGH);

  Serial.println("forward");
  for (uint16_t x = 0; x < 200; x++){
    digitalWrite(step_pin, HIGH);
    digitalWrite(step_pin2, HIGH);

    delayMicroseconds(1000);
    digitalWrite(step_pin, LOW);
    digitalWrite(step_pin2, LOW);

    delayMicroseconds(1000);
  }
  delay(1000);
  digitalWrite(dir_pin, LOW);
  digitalWrite(dir_pin2, LOW);

  Serial.println("backward");
  for (uint16_t x = 0; x < 200; x++){
    digitalWrite(step_pin, HIGH);
    digitalWrite(step_pin2, HIGH);

    delayMicroseconds(1000);
    digitalWrite(step_pin, LOW);
    digitalWrite(step_pin2, LOW);

    delayMicroseconds(1000);
  }

  digitalWrite(dir_pin3, HIGH);

  for (uint16_t x = 0; x < 200; x++){
    digitalWrite(step_pin3, HIGH);

    delayMicroseconds(1000);
    digitalWrite(step_pin3, LOW);

    delayMicroseconds(1000);
  }

  digitalWrite(dir_pin3, LOW);

  for (uint16_t x = 0; x < 200; x++){
    digitalWrite(step_pin3, HIGH);

    delayMicroseconds(1000);
    digitalWrite(step_pin3, LOW);

    delayMicroseconds(1000);
  }
  

  delay(1000);
}

