import serial
import time

ser = serial.Serial('COM15', 9600, bytesize=serial.EIGHTBITS, timeout=40, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)

def COM15_fetch():
    byt = ser.in_waiting
    if (byt > 1):
        number = ser.read(byt)
        return int(number)

while(1):
    bruh = COM15_fetch()
    print(bruh)

"""
    byt = ser.in_waiting
    number = ser.read(byt)
    if (byt > 1):
        print(byt)
        print(number)"""