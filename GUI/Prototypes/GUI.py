from tkinter import *
import time


def create_tab():
    color = "white"
    gui = Tk()
    gui.title("DATA")
    gui.geometry('100x100')

    rpm = StringVar()
    rpm.set("bruh")

    label = Label(gui, bg=color, font="Times 12", textvariable=rpm)
    label.grid(column=0, row=0)

def update_Data():
    color = "white"
    gui = Tk()
    gui.title("DATA")
    gui.geometry('100x100')

    rpm = StringVar()
    rpm.set("bruh")

    label = Label(gui, bg=color, font="Times 12", textvariable=rpm)
    label.grid(column=0, row=0)
    while (1):
        rpm.set(globals()['return_data'])

        label.grid(column=0, row=0)
        gui.update_idletasks()
        time.sleep(0.1)
        print(globals()['return_data'])
def affichage():
    while(1):
        GUI = Tk()
        GUI.title("DATA")
        GUI.geometry('1000x900')

        Vitesse = Label(GUI, font="Times 12" ,anchor="w" ,justify="left" ,text="Vitesse")
        Vitesse.grid(column=0, row=0)
        RPM = Label(GUI, font="Times 12" ,anchor="w" ,justify="left" ,text="RPM")
        RPM.grid(column=0, row=1)
        Temperature = Label(GUI, font="Times 12" ,anchor="w" ,justify="left" ,text="Temperature")
        Temperature.grid(column=0, row=2)
        Pression= Label(GUI, font="Times 12" ,anchor="w" ,justify="left" ,text="Pression")
        Pression.grid(column=0, row=3)

        GUI.mainloop()

affichage()

"""
def affichage():
    while(1):
        data = pd.read_csv("FakeData.csv")
        df = pd.DataFrame(data)
        df.plot(x='temps', y='rpm', kind='bar')
        plt.show()
        CreateFakeData.ecriture()
affichage()"""