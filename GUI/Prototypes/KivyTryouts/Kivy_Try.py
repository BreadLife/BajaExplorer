import kivy
import os
import sys

kivy.require('2.0.0')

import datetime

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.app import Builder


sys.path.append(os.path.abspath("/Baja-ETS/BajaExplorer/DataFetch"))
from DataFetch import MainFetch as MF

kv = """
<LAYOUT>:
    GridLayout:
        cols : 2
        Label:
            text: 'frameCounterByte'
        Label:
            id : 'frameCounterByte'

        Label:
            text: 'runTime'
        Label:
            id : 'runTime'

        Label:
            text: 'speed'
        Label:
            id : 'speed'

        Label:
            text: 'tpm'
        Label:
            id : 'tpm'

        Label:
            text: 'rpm'
        Label:
            id : 'rpm'

        Label:
            text: 'oilTemp'
        Label:
            id : 'oilTemp'

        Label:
            text: 'boardTemp'
        Label:
            id : 'boardTemp'

        Label:
            text: 'actPos'
        Label:
            id : 'actPos'

        Label:
            text: 'actCmd'
        Label:
            id : 'actCmd'

        Label:
            text: 'actDc'
        Label:
            id : 'actDc'

        Label:
            text: 'actRot'
        Label:
            id : 'actRot'

        Label:
            text: 'rpmCmd'
        Label:
            id : 'rpmCmd'

        Label:
            text: 'volt'
        Label:
            id : 'volt'
"""


class Layout(GridLayout):

    def __init__(self,*args, **kwargs):
        super(Layout, self).__init__(**kwargs)

        self.cols = 2

        self.add_widget(Label(text='frameCounterByte'))
        self.add_widget(Label(text='label', id='frameCounterByte'))

        self.add_widget(Label(text='runTime'))
        self.add_widget(Label(text='label', id='runTime'))

        self.add_widget(Label(text='speed'))
        self.add_widget(Label(text='label', id='speed'))

        self.add_widget(Label(text='tpm'))
        self.add_widget(Label(text='label', id='tpm'))

        self.add_widget(Label(text='rpm'))
        self.add_widget(Label(text='label', id='rpm'))

        self.add_widget(Label(text='oilTemp'))
        self.add_widget(Label(text='label', id='oilTemp'))

        self.add_widget(Label(text='boardTemp'))
        self.add_widget(Label(text='label', id='boardTemp'))

        self.add_widget(Label(text='actPos'))
        self.add_widget(Label(text='label', id='actPos'))

        self.add_widget(Label(text='actCmd'))
        self.add_widget(Label(text='label', id='actCmd'))

        self.add_widget(Label(text='actDc'))
        self.add_widget(Label(text='label', id='actDc'))

        self.add_widget(Label(text='actRot'))
        self.add_widget(Label(text='label', id='actRot'))

        self.add_widget(Label(text='rpmCmd'))
        self.add_widget(Label(text='label', id='rpmCmd'))

        self.add_widget(Label(text='volt'))
        self.add_widget(Label(text='label', id='volt'))

class MyApp(App):
    frameCounterByte = 0
    tpm = 0
    speed = 0
    runTime = 0
    rpm = 0
    oilTemp = 0
    boardTemp = 0
    actPos = 0
    actCmd = 0
    actDc = 0
    actRot = 0
    rpmCmd = 0
    volt = 0

    def build(self):
        #return Layout()
        return Builder.load_string(kv)

    def update_values(self):
        #frameCounterByte, runTime, speed, tpm, rpm, oilTemp, boardTemp, actPos, actCmd, actDc, actRot, rpmCmd, volt = MF.data()

        self.root.ids.frameCounterByte.text= str(5)
        self.root.ids.runTime.text= str(self.runTime)
        self.root.ids.speed.text= str(self.speed)
        self.root.ids.tpm.text= str(self.tpm)
        self.root.ids.rpm.text= str(self.rpm)
        self.root.ids.oilTemp.text= str(self.oilTemp)
        self.root.ids.boardTemp.text= str(self.boardTemp)
        self.root.ids.actPos.text= str(self.actPos)
        self.root.ids.actRot.text= str(self.actCmd)
        self.root.ids.actDc.text= str(self.actDc)
        self.root.ids.actRot.text= str(self.actRot)
        self.root.ids.rpmCmd.text= str(self.rpmCmd)
        self.root.ids.volt.text= str(self.volt)


if __name__ == '__main__':
    MyApp().run()