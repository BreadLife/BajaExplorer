#libs
import random
import time
from tkinter import *
import tkinter.ttk as ttk
import CréationVariablesOrdonnées as Cr

#Max
MAX_RPM_AVG = 1000
MAX_RPM_AVD = 1000
MAX_RPM_ARR = 1000
MAX_TEMP_CVT = 100
MAX_RPM_MOT = 3700
MAX_THROT_POS = 100
MAX_SHV_POS = 100

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

#rpm_av_d = StringVar()
#rpm_av_g = StringVar()
rpm_arr = StringVar()
temp_cvt = StringVar()
rpm_mot = StringVar()
throt_pos = StringVar()
shv_pos = StringVar()

#rpm_av_d.set("0")
#rpm_av_g.set("0")
rpm_arr.set("0")
temp_cvt.set("12.7")
rpm_mot.set("0")
throt_pos.set("0")
shv_pos.set("0")

#Variables
#RPM_AVG = Label(gui, bg=color, font="Times 12", textvariable=rpm_av_g, pady=2)
#RPM_AVD = Label(gui, bg=color, font="Times 12", textvariable=rpm_av_d, pady=2)
RPM_ARR = Label(gui, bg=color, font="Times 12", textvariable=rpm_arr, pady=2)
TEMP_CVT = Label(gui, bg=color, font="Times 12", textvariable=temp_cvt, pady=2)
RPM_MOT = Label(gui, bg=color, font="Times 12", textvariable=rpm_mot, pady=2)
THROT_POS = Label(gui, bg=color, font="Times 12", textvariable=throt_pos, pady=2)
SHV_POS = Label(gui, bg=color, font="Times 12", textvariable=shv_pos, pady=2)

#RPM_AVG.grid(column=1, row=0)
#RPM_AVD.grid(column=1, row=1)
RPM_ARR.grid(column=1, row=2)
TEMP_CVT.grid(column=1, row=3)
RPM_MOT.grid(column=1, row=4)
THROT_POS.grid(column=1, row=5)
SHV_POS.grid(column=1, row=6)

#Noms
#rpm_av_d_nom = Label(gui, text="Rpm_AVD: ")
#rpm_av_g_nom = Label(gui, text="Rpm_AVG: ")
rpm_arr_nom = Label(gui, text="Rpm_ARR: ")
temp_cvt_nom = Label(gui, text="Bat_Volt: ")
rpm_mot_nom = Label(gui, text="Rpm_MOT: ")
throt_pos_nom = Label(gui, text="Throt_POS: ")
shv_pos_nom = Label(gui, text="Shv_POS: ")

#rpm_av_d_nom.grid(column=0, row=0, sticky="W")
#rpm_av_g_nom.grid(column=0, row=1, sticky="W")
rpm_arr_nom.grid(column=0, row=2, sticky="W")
temp_cvt_nom.grid(column=0, row=3, sticky="W")
rpm_mot_nom.grid(column=0, row=4, sticky="W")
throt_pos_nom.grid(column=0, row=5, sticky="W")
shv_pos_nom.grid(column=0, row=6, sticky="W")

#Barres
#rpm_av_d_barre = ttk.Progressbar(gui, orient=HORIZONTAL, length=100, mode='determinate')
#rpm_av_g_barre = ttk.Progressbar(gui, orient=HORIZONTAL, length=100, mode='determinate')
rpm_arr_barre = ttk.Progressbar(gui, orient=HORIZONTAL, length=100, mode='determinate')
temp_cvt_barre = ttk.Progressbar(gui, orient=HORIZONTAL, length=100, mode='determinate')
rpm_mot_barre = ttk.Progressbar(gui, orient=HORIZONTAL, length=100, mode='determinate')
throt_pos_barre = ttk.Progressbar(gui, orient=HORIZONTAL, length=100, mode='determinate')
shv_pos_barre = ttk.Progressbar(gui, orient=HORIZONTAL, length=100, mode='determinate')

#rpm_av_d_barre.grid(column=2, row=0, padx=10)
#rpm_av_g_barre.grid(column=2, row=1, padx=10)
rpm_arr_barre.grid(column=2, row=2, padx=10)
temp_cvt_barre.grid(column=2, row=3, padx=10)
rpm_mot_barre.grid(column=2, row=4, padx=10)
throt_pos_barre.grid(column=2, row=5, padx=10)
shv_pos_barre.grid(column=2, row=6, padx=10)

while (1):
    rpm_arr_temp, temp_cvt_temp, rpm_mot_temp, throt_pos_temp, shv_pos_temp = 460, 12.7, 2500, 80, 80
    #Cr.Creation_Variables()

    #rpm_av_d.set(f'{rpm_av_d_temp:04}')
    #rpm_av_g.set(f'{rpm_av_g_temp:04}')
    rpm_arr.set(f'{rpm_arr_temp:04}')
    temp_cvt.set(f'{temp_cvt_temp:04}')
    rpm_mot.set(f'{rpm_mot_temp:04}')
    throt_pos.set(f'{throt_pos_temp:04}')
    shv_pos.set(f'{shv_pos_temp:04}')

    #rpm_av_d_barre['value'] = int(rpm_av_d_temp/MAX_RPM_AVD*100)
    #rpm_av_g_barre['value'] = int(rpm_av_g_temp/MAX_RPM_AVG*100)
    rpm_arr_barre['value'] = int(rpm_arr_temp/MAX_RPM_ARR*100)
    #temp_cvt_barre['value'] = int(temp_cvt_temp/MAX_TEMP_CVT*100)
    rpm_mot_barre['value'] = int(rpm_mot_temp/MAX_RPM_MOT*100)
    throt_pos_barre['value'] = int(throt_pos_temp/MAX_THROT_POS*100)
    shv_pos_barre['value'] = int(shv_pos_temp/MAX_SHV_POS*100)

    #RPM_AVG.grid(column=1, row=0, padx=5, sticky=W)
    #RPM_AVD.grid(column=1, row=1, padx=5, sticky=W)
    RPM_ARR.grid(column=1, row=2, padx=5, sticky=W)
    TEMP_CVT.grid(column=1, row=3, padx=5, sticky=W)
    RPM_MOT.grid(column=1, row=4, padx=5, sticky=W)
    THROT_POS.grid(column=1, row=5, padx=5, sticky=W)
    SHV_POS.grid(column=1, row=6, padx=5, sticky=W)

    gui.update_idletasks()
    time.sleep(0.5)