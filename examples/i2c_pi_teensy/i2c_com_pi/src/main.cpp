#include <Arduino.h>
#include <Wire.h>

void onReceive(int howMany);

void setup() {
  Wire2.begin(0x8);
  Wire2.onReceive(onReceive);
}

void onReceive(int howMany){
  while (Wire2.available()){
    Wire2.read();
  }
  Wire2.write("{one: 1, two: 2}");
}

void loop() {
  delay(50);
}