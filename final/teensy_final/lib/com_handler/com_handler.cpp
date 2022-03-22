#include "com_handler.h"

ComHandler::ComHandler(uint32_t baud_rate) {
    baud = baud_rate;
    Serial.begin(baud_rate);
    Serial.flush();
};

void ComHandler::check_command() {
    if (Serial.available()) {
        String command = Serial.readStringUntil('\n');
        Serial.readString();
        command.trim();
        auto operation = operations[command];
        operation();
    }
};

void ComHandler::send_baud() {
    Serial.print("{\"baud_rate\": ");
    Serial.print(this->baud);
    Serial.println("}");
}

void ComHandler::add_operation(String key, void (*function)()) {
    operations[key] = function;
}