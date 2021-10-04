import sys
import os
import time

sys.path.append(os.path.abspath("/Baja-ETS/BajaExplorer/DataFetch"))
from DataFetch import Interpreter
from DataFetch import Fetcher as Ft

Ft.Lora_setup()

frameCounterByte = 0
runTime = 0
speed = 0
tpm = 0
rpm = 0
oilTemp = 0
boardTemp = 0
actPos = 0
actCmd = 0
actDc = 0
actRot = 0
rpmCmd = 0
volt = 0

Hour = 0
Minute = 0
Second = 0
Latitude_int = 0
Latitude_frac = 0
longitude_int = 0
longitude_frac = 0
canData1 = 0
canData2 = 0
canData3 = 0
canData4 = 0
canData5 = 0
canData6 = 0

def data():
    global Hour
    global Minute
    global Second
    global Latitude_int
    global Latitude_frac
    global longitude_int
    global longitude_frac
    global canData1
    global canData2
    global canData3
    global canData4
    global canData5
    global canData6


    raw_data = Ft.COM_fetch()
    Data = Interpreter.interpreter(raw_data)
    if len(Data) > 20:
        Hour, Minute, Second, Latitude_int, Latitude_frac, longitude_int, longitude_frac, canData1, canData2, canData3, canData4, canData5, canData6 = Interpreter.assignation(Data)

    return Hour, Minute, Second, Latitude_int, Latitude_frac, longitude_int, longitude_frac, canData1, canData2, canData3, canData4, canData5, canData6