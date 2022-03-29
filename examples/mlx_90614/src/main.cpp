#include <Adafruit_MLX90614.h>
#include <Arduino.h>
#include <SPI.h>
#include <Wire.h>

/*/ 
  Example for reading temperature with the 
  MLX90614 via I2C
/*/

Adafruit_MLX90614 mlx = Adafruit_MLX90614();
Adafruit_MLX90614 mlx2 = Adafruit_MLX90614();

void setup() {
    Serial.begin(9600);
    while (!Serial)
        ;

    Serial.println("IR Temp Sensor Test");

    if (!mlx.begin(0x5B)) {
        Serial.println("Error Connecting to Sensor");
        delay(5000);
    }
    if (!mlx2.begin(0x5A)){
        Serial.println("Can't Connect to 0x5a");
    }
}

void loop() {
    Serial.print("Ambient: ");
    Serial.print(mlx.readAmbientTempF());
    Serial.println("F");

    Serial.print("Target: ");
    Serial.print(mlx.readObjectTempF());
    Serial.println(" F");

    Serial.println(mlx2.readObjectTempF());

    Serial.println();
    delay(1000);
}