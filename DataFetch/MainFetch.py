import sys
import os
import time

sys.path.append(os.path.abspath("/Baja-ETS/BajaExplorer/DataFetch"))
from DataFetch import Interpreter
from DataFetch import Fetcher as Ft

#Ft.Lora_setup()

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

def data():

    raw_data = Ft.COM_fetch()
    Data = Interpreter.interpreter(raw_data)
    if len(Data) > 20:
        Hour, Minute, Second, Latitude_int, Latitude_frac, longitude_int, longitude_frac = Interpreter.assignation(Data)

    return Hour, Minute, Second, Latitude_int, Latitude_frac, longitude_int, longitude_frac
