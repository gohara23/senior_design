#include <Arduino.h>
#include <functional>
#include <map>
#include <cstdio>
#include <unordered_map>

typedef std::map<String, void(*)()> MapType;

class ComHandler {
   public:
    ComHandler(uint32_t baud_rate);
    uint32_t baud;
    MapType operations;
    void check_command();
    void send_baud();
    void add_operation(String key, void(*function)());

};