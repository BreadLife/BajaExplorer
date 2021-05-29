import kivy
from kivy.app import App
from kivy.uix.progressbar import ProgressBar
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGrid(Widget):
   pass

class GUI(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    GUI().run()