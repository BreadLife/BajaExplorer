#libs
import os
import sys
import time
from tkinter import *
import tkinter.ttk as ttk
from GUI import CréationVariablesOrdonnées as Cr

sys.path.append(os.path.abspath("/Baja-ETS/BajaExplorer/DataFetch"))
from DataFetch import MainFetch as MF

global Hour
global Minute
global Second
global Latitude_int
global Latitude_frac
global longitude_int
global longitude_frac

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
gui.geometry('400x400')

Hour = StringVar()
Minute = StringVar()
Second = StringVar()
Latitude_int = StringVar()
Latitude_frac = StringVar()
longitude_int = StringVar()
longitude_frac = StringVar()

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

Hour.set("0")
Minute.set("0")
Second.set("0")
Latitude_int.set("0")
Latitude_frac.set("0")
longitude_int.set("0")
longitude_frac.set("0")

#Variables

HOUR = Label(gui, bg=color, font="Times 12", textvariable=Hour, pady=2)
MINUTE = Label(gui, bg=color, font="Times 12", textvariable=Minute, pady=2)
SECOND = Label(gui, bg=color, font="Times 12", textvariable=Second, pady=2)
LATITUDE_INT = Label(gui, bg=color, font="Times 12", textvariable=Latitude_int, pady=2)
LATITUDE_FRAC = Label(gui, bg=color, font="Times 12", textvariable=Latitude_frac, pady=2)
LONGITUDE_INT = Label(gui, bg=color, font="Times 12", textvariable=longitude_int, pady=2)
LONGITUDE_FRAC = Label(gui, bg=color, font="Times 12", textvariable=longitude_frac, pady=2)

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

HOUR.grid(column=1, row=0)
MINUTE.grid(column=1, row=1)
SECOND.grid(column=1, row=2)
LATITUDE_INT.grid(column=1, row=3)
LATITUDE_FRAC.grid(column=1, row=4)
LONGITUDE_INT.grid(column=1, row=5)
LONGITUDE_FRAC.grid(column=1, row=6)

FRAMECOUNTERBYTE.grid(column=1, row=7)
RUNTIME.grid(column=1, row=8)
SPEED.grid(column=1, row=9)
TPM.grid(column=1, row=10)
RPM.grid(column=1, row=11)
OILTEMP.grid(column=1, row=12)
BOARDTEMP.grid(column=1, row=13)
ACTPOS.grid(column=1, row=14)
ACTCMD.grid(column=1, row=15)
ACTDC.grid(column=1, row=16)
ACTROT.grid(column=1, row=17)
RPMCMD.grid(column=1, row=18)
VOLT.grid(column=1, row=19)


#Noms

Hour_nom = Label(gui, text="Hour: ")
Minute_nom = Label(gui, text="Minute: ")
Second_nom = Label(gui, text="Second: ")
Latitude_int_nom = Label(gui, text="Latitude_int: ")
Latitude_frac_nom = Label(gui, text="Latitude_frac: ")
longitude_int_nom = Label(gui, text="longitude_int: ")
longitude_frac_nom = Label(gui, text="longitude_frac: ")

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

Hour_nom.grid(column=0, row=0, sticky="W")
Minute_nom.grid(column=0, row=1, sticky="W")
Second_nom.grid(column=0, row=2, sticky="W")
Latitude_int_nom.grid(column=0, row=3, sticky="W")
Latitude_frac_nom.grid(column=0, row=4, sticky="W")
longitude_int_nom.grid(column=0, row=5, sticky="W")
longitude_frac_nom.grid(column=0, row=6, sticky="W")

frameCounterByte_nom.grid(column=0, row=7, sticky="W")
runTime_nom.grid(column=0, row=8, sticky="W")
speed_nom.grid(column=0, row=9, sticky="W")
tpm_nom.grid(column=0, row=10, sticky="W")
rpm_nom.grid(column=0, row=11, sticky="W")
oilTemp_nom.grid(column=0, row=12, sticky="W")
boardTemp_nom.grid(column=0, row=13, sticky="W")
actPos_nom.grid(column=0, row=14, sticky="W")
actCmd_nom.grid(column=0, row=15, sticky="W")
actDc_nom.grid(column=0, row=16, sticky="W")
actRot_nom.grid(column=0, row=17, sticky="W")
rpmCmd_nom.grid(column=0, row=18, sticky="W")
volt_nom.grid(column=0, row=19, sticky="W")


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
    Hour_i, Minute_i, Second_i, Latitude_int_i, Latitude_frac_i, longitude_int_i, longitude_frac_i = MF.data()

    Hour.set(f'{Hour_i:04}')
    Minute.set(f'{Minute_i:04}')
    Second.set(f'{Second_i:04}')
    Latitude_int.set(f'{Latitude_int_i:04}')
    Latitude_frac.set(f'{Latitude_frac_i:04}')
    longitude_int.set(f'{longitude_int_i:04}')
    longitude_frac.set(f'{longitude_frac_i:04}')

    #frameCounterByte.set(f'{frameCounterByte_i:04}')
    #runTime.set(f'{runTime_i:04}')
    #speed.set(f'{speed_i:04}')
    #tpm.set(f'{tpm_i:04}')
    #rpm.set(f'{rpm_i:04}')
    #oilTemp.set(f'{oilTemp_i:04}')
    #boardTemp.set(f'{boardTemp_i:04}')
    #actPos.set(f'{actPos_i:04}')
    #actCmd.set(f'{actCmd_i:04}')
    #actDc.set(f'{actDc_i:04}')
    #actRot.set(f'{actRot_i:04}')
    #rpmCmd.set(f'{rpmCmd_i:04}')
    #volt.set(f'{volt_i:04}')

    #rpm_av_d_barre['value'] = int(rpm_av_d_temp/MAX_RPM_AVD*100)
    #rpm_av_g_barre['value'] = int(rpm_av_g_temp/MAX_RPM_AVG*100)
    #rpm_arr_barre['value'] = int(rpm_arr_temp/MAX_RPM_ARR*100)
    #temp_cvt_barre['value'] = int(temp_cvt_temp/MAX_TEMP_CVT*100)
    #rpm_mot_barre['value'] = int(rpm_mot_temp/MAX_RPM_MOT*100)
    #throt_pos_barre['value'] = int(throt_pos_temp/MAX_THROT_POS*100)
    #shv_pos_barre['value'] = int(shv_pos_temp/MAX_SHV_POS*100)

    HOUR.grid(column=1, row=0, padx=5, columnspan=2, sticky=W)
    MINUTE.grid(column=1, row=1, padx=5, columnspan=2, sticky=W)
    SECOND.grid(column=1, row=2, padx=5, columnspan=2, sticky=W)
    LATITUDE_INT.grid(column=1, row=3, padx=5, columnspan=2, sticky=W)
    LATITUDE_FRAC.grid(column=1, row=4, padx=5, columnspan=2, sticky=W)
    LONGITUDE_INT.grid(column=1, row=5, padx=5, columnspan=2, sticky=W)
    LONGITUDE_FRAC.grid(column=1, row=6, padx=5, columnspan=2, sticky=W)

    FRAMECOUNTERBYTE.grid(column=1, row=7, padx=5, columnspan=2, sticky=W)
    RUNTIME.grid(column=1, row=8, padx=5, columnspan=2, sticky=W)
    SPEED.grid(column=1, row=9, padx=5, columnspan=2, sticky=W)
    TPM.grid(column=1, row=10, padx=5, columnspan=2, sticky=W)
    RPM.grid(column=1, row=11, padx=5, columnspan=2, sticky=W)
    OILTEMP.grid(column=1, row=12, padx=5, columnspan=2, sticky=W)
    BOARDTEMP.grid(column=1, row=13, padx=5, columnspan=2, sticky=W)
    ACTPOS.grid(column=1, row=14, padx=5, columnspan=2, sticky=W)
    ACTCMD.grid(column=1, row=15, padx=5, columnspan=2, sticky=W)
    ACTDC.grid(column=1, row=16, padx=5, columnspan=2, sticky=W)
    ACTROT.grid(column=1, row=17, padx=5, columnspan=2, sticky=W)
    RPMCMD.grid(column=1, row=18, padx=5, columnspan=2, sticky=W)
    VOLT.grid(column=1, row=19, padx=5, columnspan=2, sticky=W)

    gui.update_idletasks()
    time.sleep(0.5)