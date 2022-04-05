from smbus import SMbus
import RPi.GPIO as GPIO
import time

def readNumberFromArduino():
    
    data_received_from_Arduino = i2c.read_i2c_block_data(slaveAddress, 0,15)
    for i in range(len(data_received_from_Arduino)):
        smsNumber += chr(data_received_from_Arduino[i])

    print(smsNumber.encode('utf-8'))
    data_received_from_Arduino = ""
    smsNumber = ""

if __name__ == "__main__":

    ADDRESS = 0x8
    bus = SMbus(1)

    while True:

        bus.write_byte(ADDRESS, 0x1)
        time.sleep(0.1)
        string = str()
        data = bus.read_i2c_block_data(ADDRESS, 0, 15)

        for c in data:
            string += chr(c)

        print(string.encode('utf-8'))

        string = str()

