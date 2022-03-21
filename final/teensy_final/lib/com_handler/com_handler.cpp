#include "com_handler.h"

ComHandler::ComHandler(uint32_t baud_rate) {
    baud = baud_rate;
    Serial.begin(baud_rate);
};

void ComHandler::check_command() {
    if (Serial.available()) {
        String command = Serial.readStringUntil('\n');
        command.trim();
        if (command == "baud") {
            ComHandler::send_baud();
        }
    }
};

void ComHandler::send_baud() {
    Serial.print("{\"baud_rate\": ");
    Serial.print(ComHandler::baud);
    Serial.println("}");
}