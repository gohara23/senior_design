#include <Arduino.h>

class ComHandler {
   public:
    ComHandler(uint32_t baud_rate);
    uint32_t baud;
    void check_command();
    void send_baud();
};