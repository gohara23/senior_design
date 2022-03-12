#include <Arduino.h>
#include <string.h>

/*/
  Example of two functions running
  which would otherwise use a delay
/*/

/*/
  Note -- Could use Teensy clock cycles
  One clock cycle = 1.67 ns

  600 MHz clock speed
  6e8 cycles per sec
  1 cyle = 1 / (6e8) seconds
/*/

// Buit-in LED
#define LED 13

unsigned long current_millis;
bool led_state;
unsigned long led_change_time;

unsigned long on_ms = 5000;
unsigned long off_ms = 500;

unsigned long last_message_time;

void led_control(unsigned long on_time_ms, unsigned long off_time_ms) {
    if ((led_state == LOW) &&
        (current_millis - led_change_time) > off_time_ms) {
        led_state = HIGH;
        digitalWrite(LED, led_state);
        led_change_time = current_millis;
    } else if ((led_state == HIGH) &&
               (current_millis - led_change_time) > on_time_ms) {
        led_state = LOW;
        digitalWrite(LED, led_state);
        led_change_time = current_millis;
    }
}

void serial_control(String message, unsigned long delay_ms){
  if ((current_millis - last_message_time) > delay_ms){
    Serial.println(message);
    last_message_time = current_millis;
  }
}

void setup() {
    current_millis = millis();
    pinMode(LED, OUTPUT);
    Serial.begin(9600);
}

void loop() {
    current_millis = millis();
    led_control(on_ms, off_ms);
    serial_control("Hello, 10 seconds has elapsed", 10000);
}