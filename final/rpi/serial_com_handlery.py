import serial
import json
import time
from globals import *


class ComHandler:
    def __init__(self, com_port, baud_rate=9600):
        self.ser = serial.Serial(com_port, baud_rate, timeout=0.5)
        self.ser.flush()

    def send_command(self, command):
        self.ser.write(f"{command}\n")

    def get_data(self, command):
        self.ser.write(str.encode(f"{command}\n"))
        while not self.ser.in_waiting:
            time.sleep(0.0001)
        line = self.ser.readline().decode("utf-8").rstrip()
        return line


if __name__ == "__main__":

    COM_PORT = "COM15"
    COM_PORT = "ttyS0"
    # handler = ComHandler(COM_PORT)
    # cmd = "temps"
    # while True:
    #     line = handler.get_data(f"{cmd}\n")
    #     print(line)
    #     # dictionary = json.loads(line)
    #     # print(dictionary["motor"])
    #     time.sleep(0.1)

    ser = serial.Serial(COM_PORT, BAUD_RATE)
    while True: 
        while not ser.in_waiting:
            time.sleep(0.001)
            line = ser.readline().decode("utf-8").rstrip()
            print(line)
        
