import serial
import io
import time
"""
Settings for Lora

Bd rate = 5600
DataBits = 8
Parity = None
StopBits = One
PortName = 
WriteTimeout = 30
Newline = "\r\n"
"""

#I could make a program to look for the port.... but am I gonna?
ser = serial.Serial('COM16', 57600, bytesize=serial.EIGHTBITS, timeout=30, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)

#Fetch buffer
def COM_fetch():
    msg = ser.read(size=57)
    return msg

#TALK TO ME LORA
def Lora_setup():
    ser.write(b'radio set freq 914000000\r\n')
    time.sleep(0.1)
    msg = ser.readline()
    print(msg)
    ser.write(b'radio set sf sf11\r\n')
    msg = ser.readline()
    print(msg)
    time.sleep(0.1)
    ser.write(b'radio set bw 500\r\n')
    msg = ser.readline()
    print(msg)
    time.sleep(0.1)
    ser.write(b'radio set sync bf\r\n')
    msg = ser.readline()
    print(msg)
    time.sleep(0.1)
    ser.write(b'mac pause\r\n')
    msg = ser.readline()
    print(msg)
    time.sleep(0.1)

def test():
    ser.write(b'sys reset\r\n')
    print(ser.readline())
    time.sleep(1)
    ser.write(b'sys get ver\r\n')
    print(ser.readline())

#It's action time babiiiii
Lora_setup()

#test()

while(True):
    ser.write(b'radio rx 100\r\n')
    raw_data = COM_fetch()
    print(raw_data)
