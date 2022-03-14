#include <Arduino.h>

#include "header.h"

void setup() { Serial.begin(9600); }

void loop() {
    print_message("Hello from lib");
    delay(USER_DEFINED_GLOBAL_VAR);
}