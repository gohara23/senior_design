#include <Arduino.h>

#define LED 13

// Basic Blink Code for Teensy 4.1

void setup() { pinMode(LED, OUTPUT); }

void loop() {
    digitalWrite(LED, HIGH);
    delay(300);
    digitalWrite(LED, LOW);
    delay(300);
}