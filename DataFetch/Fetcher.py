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
ser = serial.Serial('COM15', 57600, bytesize=serial.EIGHTBITS, timeout=30, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser), newline='\r\n')


#Fetch buffer
def COM15_fetch():
    msg = sio.readall()
    return msg
    sio.flush()

#TALK TO ME LORA
def Lora_setup():
    ser.write("radio set freq 914000000")
    time.sleep(0.05)
    ser.write("radio set sf sf11")
    time.sleep(0.05)
    ser.write("radio set bw 500")
    time.sleep(0.05)
    ser.write("radio set sync bf")
    time.sleep(0.05)
    ser.write("mac pause")

#It's action time babiiiii
"""
Lora_setup()

while(1):
    raw_data = COM15_fetch()
    print(raw_data)
"""