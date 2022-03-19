from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
import ctypes
from gui_tabs import *
import gui_stylesheet as gss
from gui_assets import *
#from gui.gui_functions import *
#from functools import partial
from serial_communication import *
#from EVT.evt_info import *

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QTextEdit, QWidget, QApplication, QVBoxLayout

class Ui_MainWindow(QObject):

    def __init__(self):
        super().__init__()

        user32 = ctypes.windll.user32
        screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

        # Structure
        self.MainWindow = QtWidgets.QMainWindow()

        #Serial Communication
        #self.COMPort = evt_com_port()
        #self.COMPort.RX_Update.connect(partial(parse_message, self))
        #self.COMConnected = False

        self.statusPeriodicUpdateActive = False

        #Window Size and position
        self.width = 1000
        self.height = 600
        self.left = (screensize[0] / 2) - (self.width / 2)
        self.top = (screensize[1] / 2) - (self.height / 2)

        #EVT_Variables
        #self.evt_eeprom = EVT_EEPROM_Values()
        self.setupUI()
        #self.setupTimer()


    def setupUI(self):
        # General
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.setWindowTitle('BAJA EVT Application')
        self.MainWindow.setGeometry(int(self.left), int(self.top), int(self.width), int(self.height))
        self.MainWindow.setStyleSheet(windowStyleSheetString)
        self.MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

        #self.createMenuBar()
        self.createStatusBar()
        self.createCentralWidget()
        self.createMainLayout()

        #self.create_ConnectionStatus()

    def createCentralWidget(self):
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        #sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        #sizePolicy.setHorizontalStretch(0)
        #sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        #self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.MainWindow.setCentralWidget(self.centralwidget)

    def createMainLayout(self):

        #main Layout
        self.mainLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.mainLayout.setObjectName("mainLayout")

        #self.spintest = evtApp_spinBox(self.centralwidget, pos_x=20, pos_y=40)

        #HeaderLayout
        self.headerArea = QtWidgets.QWidget(self.centralwidget)
        self.headerArea.setObjectName("headerAreaWidget")
        self.headerArea.setFixedHeight(100)
        self.headerArea.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))
        self.mainLayout.addWidget(self.headerArea)

        self.headerLayout = QtWidgets.QHBoxLayout(self.headerArea)
        self.headerLayout.setObjectName("headerLayout")

        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.headerLayout.addItem(spacerItem)

        #Connection Layout
        self.connectionLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.connectionLayout.setObjectName("connectionLayout")
        self.headerLayout.addLayout(self.connectionLayout)

        self.connectButton = evtApp_pushButton(self.centralwidget,
                                               layout=self.connectionLayout,
                                               width=300,
                                               height=30,
                                               text="Connect",
                                               connect=lambda :self.connect_to_evt()
                                               )

        self.COMPortName_textbox = evtApp_textBox(self.centralwidget,
                                                  layout=self.connectionLayout,
                                                  text="COM4",
                                                  width=300
                                                  )

        self.statusLabel = loraApp_label(self.centralwidget,
                                         layout=self.connectionLayout,
                                         text="Status: ")
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.connectionLayout.addItem(spacerItem)

        #Main Tabs
        self.MainTabs = QtWidgets.QTabWidget(self.centralwidget)
        self.MainTabs.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.MainTabs.setAutoFillBackground(False)
        self.MainTabs.setStyleSheet(gss.tabStyleSheetString)
        self.MainTabs.setTabPosition(QtWidgets.QTabWidget.North)
        self.MainTabs.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.MainTabs.setObjectName("MainTabs")

        self.mainLayout.addWidget(self.MainTabs)

        self.EVTStatusTab = LORAStatusTab(self)
        self.EVTClockingTab = LORADataTab(self)
        #self.EVTTuningTab = LORATuningTab(self)
        #self.EVTDebuggingTab = LORADebuggingTab(self)
        #self.SettingsTab = SettingsTab(self.MainTabs)


    def createMenuBar(self):
        self.menubar = QMenuBar(self.MainWindow)
        self.MainWindow.setMenuBar(self.menubar)

        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")

        # Creating menus using a title
        fileMenu = self.menubar.addMenu("&File")
        editMenu = self.menubar.addMenu("&Edit")
        helpMenu = self.menubar.addMenu("&Help")


    def createStatusBar(self):
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)

    def create_ConnectionStatus(self):
        self.statusLabel = loraApp_label(self.centralwidget, pos_x=self.width - 225, pos_y=40, text="Status: ")
        self.connectButton = evtApp_pushButton(self.centralwidget, pos_x=self.width - 225, pos_y=5, text="Connect")

        #self.connectButton.clicked.connect(partial(EVT_connect, self.COMPort, 'COM5', self.statusLabel))
        #self.connectButton.clicked.connect(partial(self.COMPort.EVT_connect, self.statusLabel))

    def closeEvent(self, event):
        self.serth.running = False
        self.serth.wait()

    def print_status(self, string):
        print(string)
        self.statusbar.showMessage(string, 4000)

    @pyqtSlot()
    def connect_to_evt(self):
        port = str(self.COMPortName_textbox.text())

        if not port:
            self.statusLabel.changeText("Please specify port name.")
            self.print_status("Unspecified port")
            return None

        if self.COMPort.EVT_connect(port) == None:
            self.statusLabel.changeText("Status: Can't connect to port " + self.COMPort.portname)
            self.print_status("Can't connect to port " + self.COMPort.portname)
        else:
            self.statusLabel.changeText("Status: Connected")
            self.print_status("Connected to port" + self.COMPort.portname + "!")
            self.COMConnected = True

            self.COMPort.EVT_read_EEPROM(CODE_VER_EEPROM_ADDR)
            self.COMPort.EVT_read_EEPROM(DEBUGGING_LVL_EEPROM_ADDR)

    def setupTimer(self):
        self.statusUpdatePeriod = 1000 #in msec

        self.periodicStatusTimer = QTimer()
        self.periodicStatusTimer.timeout.connect(self.statusTimerTimeout)
        self.periodicStatusTimer.start(self.statusUpdatePeriod)

    def statusTimerTimeout(self):
        self.periodicStatusTimer.start(self.statusUpdatePeriod)

        if (self.statusPeriodicUpdateActive is True) and (self.COMConnected is True):
            self.COMPort.EVT_write(OPCODE_EVT_STATUS_REQUEST, 0, 0)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    # global MainWindow
    # MainWindow = QtWidgets.QMainWindow()
    # MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    ui = Ui_MainWindow()
    # ui.setupUI(MainWindow)
    ui.MainWindow.show()

    # layout = QVBoxLayout(MainWindow)
    # button = QPushButton('Exit')
    # button.clicked.connect(app.quit)
    # layout.addWidget(button)

    print("EVT Application Started")

    sys.exit(app.exec_())
