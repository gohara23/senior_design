# from smbus2 import SMBus
import time

# if __name__ == "__main__":

#     ADDRESS = 0x8
#     bus = SMBus(1)

#     while True:

#         bus.write_byte(ADDRESS, 0x1)
#         time.sleep(0.1)
#         string = str()
#         data = bus.read_i2c_block_data(ADDRESS, 0, 15)

#         for c in data:
#             string += chr(c)

#         print(string.encode('utf-8'))

#         string = str()

import serial 

if __name__ == "__main__":
    TEENSY_COM = "/dev/ttyACMA0" 
    BAUD_RATE = 9600
    ser = serial.Serial(TEENSY_COM, BAUD_RATE, timeout=0.5)

    while not ser.in_waiting:
        time.sleep(0.0001)
    line = ser.readline().decode("utf-8").rstrip()
    print(line)