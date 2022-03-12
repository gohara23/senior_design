#include <Adafruit_MLX90614.h>
#include <Arduino.h>
#include <SPI.h>
#include <Wire.h>

/*/ 
  Example for reading temperature with the 
  MLX90614 via I2C
/*/

Adafruit_MLX90614 mlx = Adafruit_MLX90614();

void setup() {
    Serial.begin(9600);
    while (!Serial)
        ;

    Serial.println("IR Temp Sensor Test");

    if (!mlx.begin()) {
        Serial.println("Error Connecting to Sensor");
        delay(5000);
    }
}

void loop() {
    Serial.print("Ambient: ");
    Serial.print(mlx.readAmbientTempF());
    Serial.println("F");

    Serial.print("Target: ");
    Serial.print(mlx.readObjectTempF());
    Serial.println(" F");

    Serial.println();
    delay(1000);
}