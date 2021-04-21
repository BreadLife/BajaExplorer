from tkinter import *
import csv
import time
import serial


def ecriture(val):
    # valeurs random
    rpm = val

    with open('FakeData.csv', mode='w', newline='') as csv_file:
        spamwriter = csv.writer(csv_file, delimiter=',')
        spamwriter.writerow(["\n"]+[rpm]+[rpm])

def affichage():
    with serial.Serial('COM15', 9600, timeout=1) as ser:
        color = "white"
        gui = Tk()
        gui.title("DATA")
        gui.geometry('100x100')

        rpm = StringVar()
        rpm.set("0")

        label = Label(gui, bg=color, font="Times 12", textvariable=rpm)
        label.grid(column=0, row=0)

        while (1):
            x = ser.read(1)  # read one byte
            ecriture(x)
            rpm.set(x)

            label.grid(column=0, row=0)
            gui.update_idletasks()
            #time.sleep(0.1)
            print(x)

affichage()