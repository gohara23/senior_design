import serial
from globals import *


class ComHandler:
    def __init__(self, com_port, baud_rate=9600):
        ser = serial.Serial(com_port, baud_rate, timeout=1)
        ser.flush()


if __name__ == "__main__":

    COM_PORT = "COM13"
    handler = ComHandler(COM_PORT)
