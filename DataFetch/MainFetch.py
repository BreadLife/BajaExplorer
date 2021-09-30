import sys
import os
import time

sys.path.append(os.path.abspath("/Baja-ETS/BajaExplorer/DataFetch"))
from DataFetch import Interpreter
from DataFetch import Fetcher as Ft

Ft.Lora_setup()

while(1):
    raw_data = Ft.COM_fetch()
    Data = Interpreter.interpreter(raw_data)

