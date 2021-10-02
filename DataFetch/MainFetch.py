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

def data():
    global frameCounterByte
    global runTime
    global speed
    global tpm
    global rpm
    global oilTemp
    global boardTemp
    global actPos
    global actCmd
    global actDc
    global actRot
    global rpmCmd
    global volt

    raw_data = Ft.COM_fetch()
    Data = Interpreter.interpreter(raw_data)
    if len(Data) > 20:
        frameCounterByte, runTime, speed, tpm, rpm, oilTemp, boardTemp, actPos, actCmd, actDc, actRot, rpmCmd, volt = Interpreter.assignation(Data)

    return frameCounterByte, runTime, speed, tpm, rpm, oilTemp, boardTemp, actPos, actCmd, actDc, actRot, rpmCmd, volt
