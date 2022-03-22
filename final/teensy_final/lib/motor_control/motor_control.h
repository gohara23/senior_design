#include <Arduino.h>
#include <string.h>

#include <iostream>

#ifndef MOTOR_CONTROL_H
#define MOTOR_CONTROL_H

class Motor {
   public:
    Motor(uint16_t axis, uint16_t direction_pin, uint16_t stepper_pin);
    uint16_t ax;
    uint16_t dir_pin;
    uint16_t step_pin;
};

void com_send();


#endif