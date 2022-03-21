#include "header.h"

ComHandler handler = ComHandler(BAUD_RATE);

void setup() {}

void loop() { handler.check_command(); }