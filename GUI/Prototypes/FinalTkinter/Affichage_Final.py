#libs
import os
import sys
import time
from tkinter import *
import tkinter.ttk as ttk
from GUI import CréationVariablesOrdonnées as Cr

sys.path.append(os.path.abspath("/Baja-ETS/BajaExplorer/DataFetch"))
from DataFetch import MainFetch as MF

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

#Max
MAX_RPM_AVG = 1000
MAX_RPM_AVD = 1000
MAX_RPM_ARR = 1000
MAX_TEMP_CVT = 100
MAX_RPM_MOT = 5000
MAX_THROT_POS = 100
MAX_SHV_POS = 360

#valeurs random
"""
rpm_av_d = random.randint(0,MAX_RPM_AVD)
rpm_av_g = random.randint(0,MAX_RPM_AVG)
rpm_arr = random.randint(0,MAX_RPM_ARR)
temp = random.randint(0,MAX_TEMP_CVT)
rpm_mot = random.randint(0,MAX_RPM_MOT)
throt_pos = random.randint(0,MAX_TROT_POS)
shv_pos = random.randint(0,MAX_SHV_POS)
"""

color = "white"
gui = Tk()
gui.title("DATA")
gui.geometry('300x300')

frameCounterByte = StringVar()
runTime = StringVar()
speed = StringVar()
tpm = StringVar()
rpm = StringVar()
oilTemp = StringVar()
boardTemp = StringVar()
actPos = StringVar()
actCmd = StringVar()
actDc = StringVar()
actRot = StringVar()
rpmCmd = StringVar()
volt = StringVar()


frameCounterByte.set("0")
runTime.set("0")
speed.set("0")
tpm.set("0")
rpm.set("0")
oilTemp.set("0")
boardTemp.set("0")
actPos.set("0")
actCmd.set("0")
actDc.set("0")
actRot.set("0")
rpmCmd.set("0")
volt.set("0")

#Variables
FRAMECOUNTERBYTE = Label(gui, bg=color, font="Times 12", textvariable=frameCounterByte, pady=2)
RUNTIME = Label(gui, bg=color, font="Times 12", textvariable=runTime, pady=2)
SPEED = Label(gui, bg=color, font="Times 12", textvariable=speed, pady=2)
TPM = Label(gui, bg=color, font="Times 12", textvariable=tpm, pady=2)
RPM = Label(gui, bg=color, font="Times 12", textvariable=rpm, pady=2)
OILTEMP = Label(gui, bg=color, font="Times 12", textvariable=oilTemp, pady=2)
BOARDTEMP = Label(gui, bg=color, font="Times 12", textvariable=boardTemp, pady=2)
ACTPOS = Label(gui, bg=color, font="Times 12", textvariable=actPos, pady=2)
ACTCMD = Label(gui, bg=color, font="Times 12", textvariable=actCmd, pady=2)
ACTDC = Label(gui, bg=color, font="Times 12", textvariable=actDc, pady=2)
ACTROT = Label(gui, bg=color, font="Times 12", textvariable=actRot, pady=2)
RPMCMD = Label(gui, bg=color, font="Times 12", textvariable=rpmCmd, pady=2)
VOLT = Label(gui, bg=color, font="Times 12", textvariable=volt, pady=2)

FRAMECOUNTERBYTE.grid(column=1, row=0)
RUNTIME.grid(column=1, row=1)
SPEED.grid(column=1, row=2)
TPM.grid(column=1, row=3)
RPM.grid(column=1, row=4)
OILTEMP.grid(column=1, row=5)
BOARDTEMP.grid(column=1, row=6)
ACTPOS.grid(column=1, row=7)
ACTCMD.grid(column=1, row=8)
ACTDC.grid(column=1, row=9)
ACTROT.grid(column=1, row=10)
RPMCMD.grid(column=1, row=11)
VOLT.grid(column=1, row=12)

#Noms

frameCounterByte_nom = Label(gui, text="frameCounterByte: ")
runTime_nom = Label(gui, text="runTime: ")
speed_nom = Label(gui, text="speed: ")
tpm_nom = Label(gui, text="tpm: ")
rpm_nom = Label(gui, text="rpm: ")
oilTemp_nom = Label(gui, text="oilTemp: ")
boardTemp_nom = Label(gui, text="boardTemp: ")
actPos_nom = Label(gui, text="actPos: ")
actCmd_nom = Label(gui, text="actCmd: ")
actDc_nom = Label(gui, text="actDc: ")
actRot_nom = Label(gui, text="actRot: ")
rpmCmd_nom = Label(gui, text="rpmCmd: ")
volt_nom = Label(gui, text="volt: ")

frameCounterByte_nom.grid(column=0, row=0, sticky="W")
runTime_nom.grid(column=0, row=1, sticky="W")
speed_nom.grid(column=0, row=2, sticky="W")
tpm_nom.grid(column=0, row=3, sticky="W")
rpm_nom.grid(column=0, row=4, sticky="W")
oilTemp_nom.grid(column=0, row=5, sticky="W")
boardTemp_nom.grid(column=0, row=6, sticky="W")
actPos_nom.grid(column=0, row=7, sticky="W")
actCmd_nom.grid(column=0, row=8, sticky="W")
actDc_nom.grid(column=0, row=9, sticky="W")
actRot_nom.grid(column=0, row=10, sticky="W")
rpmCmd_nom.grid(column=0, row=11, sticky="W")
volt_nom.grid(column=0, row=12, sticky="W")


#Barres
"""
rpm_av_d_barre = ttk.Progressbar(gui, orient=HORIZONTAL, length=100, mode='determinate')
rpm_av_g_barre = ttk.Progressbar(gui, orient=HORIZONTAL, length=100, mode='determinate')
rpm_arr_barre = ttk.Progressbar(gui, orient=HORIZONTAL, length=100, mode='determinate')
temp_cvt_barre = ttk.Progressbar(gui, orient=HORIZONTAL, length=100, mode='determinate')
rpm_mot_barre = ttk.Progressbar(gui, orient=HORIZONTAL, length=100, mode='determinate')
throt_pos_barre = ttk.Progressbar(gui, orient=HORIZONTAL, length=100, mode='determinate')
shv_pos_barre = ttk.Progressbar(gui, orient=HORIZONTAL, length=100, mode='determinate')

rpm_av_d_barre.grid(column=3, row=0, padx=10)
rpm_av_g_barre.grid(column=3, row=1, padx=10)
rpm_arr_barre.grid(column=3, row=2, padx=10)
temp_cvt_barre.grid(column=3, row=3, padx=10)
rpm_mot_barre.grid(column=3, row=4, padx=10)
throt_pos_barre.grid(column=3, row=5, padx=10)
shv_pos_barre.grid(column=3, row=6, padx=10)
"""

while (1):
    frameCounterByte_i, runTime_i, speed_i, tpm_i, rpm_i, oilTemp_i, boardTemp_i, actPos_i, actCmd_i, actDc_i, actRot_i, rpmCmd_i, volt_i = MF.data()

    frameCounterByte.set(f'{frameCounterByte_i:04}')
    runTime.set(f'{runTime_i:04}')
    speed.set(f'{speed_i:04}')
    tpm.set(f'{tpm_i:04}')
    rpm.set(f'{rpm_i:04}')
    oilTemp.set(f'{oilTemp_i:04}')
    boardTemp.set(f'{boardTemp_i:04}')
    actPos.set(f'{actPos_i:04}')
    actCmd.set(f'{actCmd_i:04}')
    actDc.set(f'{actDc_i:04}')
    actRot.set(f'{actRot_i:04}')
    rpmCmd.set(f'{rpmCmd_i:04}')
    volt.set(f'{volt_i:04}')

    #rpm_av_d_barre['value'] = int(rpm_av_d_temp/MAX_RPM_AVD*100)
    #rpm_av_g_barre['value'] = int(rpm_av_g_temp/MAX_RPM_AVG*100)
    #rpm_arr_barre['value'] = int(rpm_arr_temp/MAX_RPM_ARR*100)
    #temp_cvt_barre['value'] = int(temp_cvt_temp/MAX_TEMP_CVT*100)
    #rpm_mot_barre['value'] = int(rpm_mot_temp/MAX_RPM_MOT*100)
    #throt_pos_barre['value'] = int(throt_pos_temp/MAX_THROT_POS*100)
    #shv_pos_barre['value'] = int(shv_pos_temp/MAX_SHV_POS*100)

    FRAMECOUNTERBYTE.grid(column=1, row=0, padx=5, columnspan=2, sticky=W)
    RUNTIME.grid(column=1, row=1, padx=5, columnspan=2, sticky=W)
    SPEED.grid(column=1, row=2, padx=5, columnspan=2, sticky=W)
    TPM.grid(column=1, row=3, padx=5, columnspan=2, sticky=W)
    RPM.grid(column=1, row=4, padx=5, columnspan=2, sticky=W)
    OILTEMP.grid(column=1, row=5, padx=5, columnspan=2, sticky=W)
    BOARDTEMP.grid(column=1, row=6, padx=5, columnspan=2, sticky=W)
    ACTPOS.grid(column=1, row=7, padx=5, columnspan=2, sticky=W)
    ACTCMD.grid(column=1, row=8, padx=5, columnspan=2, sticky=W)
    ACTDC.grid(column=1, row=9, padx=5, columnspan=2, sticky=W)
    ACTROT.grid(column=1, row=10, padx=5, columnspan=2, sticky=W)
    RPMCMD.grid(column=1, row=11, padx=5, columnspan=2, sticky=W)
    VOLT.grid(column=1, row=12, padx=5, columnspan=2, sticky=W)

    gui.update_idletasks()
    time.sleep(0.5)