#include "motor_control.h"

Motor::Motor(uint16_t axis, uint16_t direction_pin, uint16_t stepper_pin) {
    ax = axis;
    dir_pin = direction_pin;
    step_pin = stepper_pin;
}
