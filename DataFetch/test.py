import serial
import io
import time
import struct


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

#ser = serial.Serial('COM3', 57600, bytesize=serial.EIGHTBITS, timeout=30, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)

def test():
    ser.write(b'sys reset\r\n')
    print(ser.readline())
    time.sleep(1)
    ser.write(b'sys get ver\r\n')
    print(ser.readline())

#TALK TO ME LORA
def Lora_setup():
    ser.write(b'radio set freq 914000000\r\n')
    time.sleep(0.1)
    msg = ser.readline()
    print(msg)
    ser.write(b'radio set sf sf11\r\n')
    time.sleep(0.1)
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
    return msg

def COM_fetch():
    time.sleep(0.1)
    ser.write(b'radio rx 0\r\n')
    msg = ser.readline()

    return msg

def communicate():
    ser.write(b'mac pause\r\n')
    msg = ser.readline()
    return msg

def essai_str_to_int():
    str = "0A"
    str = int(str, base=16)
    #str = bytes(str, 'utf-8')

    print(str)

def decoder_gps_data():
    entier = '80'
    fraction = '83023E'

    entier = int(entier, base=16)
    fraction = int(fraction, base=16)

    nombre = -(((entier & 0x80) | (entier & 0x7f)) + (1 - 1 / fraction))

    print(nombre)

    return nombre

"""
    entier_x = int(bin(entier, ), base=2)
    fraction_x = 1 - 1/int(fraction, base=16)

    print(bin(int(entier, base=16)))
"""


data = decoder_gps_data()
print(data)

"""Lora_setup()
data = communicate()
print(data)
"""
#test()