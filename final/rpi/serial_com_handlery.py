import serial
import json
import time
from globals import *


class ComHandler:
    def __init__(self, com_port, baud_rate=9600):
        self.ser = serial.Serial(com_port, baud_rate, timeout=1)
        self.ser.flush()

    def send_command(self, command):
        self.ser.write(f"{command}\n")

    def get_data(self, command):
        self.ser.write(str.encode(f"{command}\n"))
        while not self.ser.in_waiting:
            time.sleep(0.01)
        line = self.ser.readline().decode("utf-8").rstrip()
        return line
        




if __name__ == "__main__":

    COM_PORT = "COM13"
    handler = ComHandler(COM_PORT)

    cmd = "baud"
    while True:
        line = handler.get_data(f"{cmd}\n")
        print(line)
        dictionary = json.loads(line)
        print(dictionary["baud_rate"])
        time.sleep(5)
