#include "header.h"

ComHandler handler = ComHandler(BAUD_RATE);

void setup() {
    handler.add_operation("motor", com_send);
}

void loop() { handler.check_command(); }