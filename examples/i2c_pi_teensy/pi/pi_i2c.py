from smbus2 import SMBus
import time

if __name__ == "__main__":

    ADDRESS = 0x8
    bus = SMBus(1)

    while True:

        bus.write_byte(ADDRESS, 0x1)
        time.sleep(0.1)
        string = str()
        data = bus.read_i2c_block_data(ADDRESS, 0, 15)

        for c in data:
            string += chr(c)

        print(string.encode('utf-8'))

        string = str()

