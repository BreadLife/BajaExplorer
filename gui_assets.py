from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from gui_stylesheet import *
from constants import *
from math import *

import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

ASSET_DEFAULT_LEFT_SPACING = 5
ASSET_DEFAULT_RIGHT_SPACING = 5
ASSET_DEFAULT_TOP_SPACING = 5
ASSET_DEFAULT_BOTTOM_SPACING = 3

DEFAULT_PUSHBUTTON_WIDTH = 200
DEFAULT_PUSHBUTTON_HEIGHT = 30
DEFAULT_SPINBOX_HEIGHT = 25
DEFAULT_SPINBOX_WIDTH = 150
DEFAULT_TEXTBOX_HEIGHT = 30
DEFAULT_TEXTBOX_WIDTH = 100

DEFAULT_SLIDER_HEIGHT = 20
DEFAULT_SLIDER_WIDTH  = 200



class evtApp_pushButton(QPushButton):

    def __init__(self, parent, pos_x=0, pos_y=0,
                 text="", fontSize=10,
                 height=None, width=None,
                 connect=None, layout=None):
        super().__init__(parent)

        self.setFont(QFont('Arial', fontSize))
        self.setText(text)
        self.setStyleSheet(pushButtonStyleSheetString)

        self.pos_x = pos_x
        self.pos_y = pos_y

        if ((pos_x != 0) or (pos_y != 0)):
            self.move(self.pos_x, self.pos_y)

        if layout is not None:
            layout.addWidget(self)

        if height is None:
            if layout is not None:
                self.height = None
            else:
                self.height = DEFAULT_PUSHBUTTON_HEIGHT
                self.setFixedHeight(self.height)
        else:
            self.height = height
            self.setFixedHeight(self.height)

        if width is None:
            if layout is not None:
                self.width = None
            else:
                self.width = DEFAULT_PUSHBUTTON_WIDTH
                self.setFixedWidth(self.width)
        else:
            self.width = width
            self.setFixedWidth(self.width)

        if connect is not None:
            self.clicked.connect(connect)


class loraApp_label(QLabel):

    def __init__(self, parent, layout=None,
                 pos_x=0, pos_y=0,
                 text="", fontSize=TEXT_FONT_SIZE_NORMAL,
                 alignment=None):
        super().__init__(parent)

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.fontSize = fontSize

        self.setFont(QFont('Arial', self.fontSize))
        self.height = self.fontSize * 2
        self.setText(text)
        self.adjustSize()

        if ((pos_x != 0) or (pos_y != 0)):
            self.move(self.pos_x, self.pos_y)

        if alignment is not None:
            self.setAlignment(alignment)

        if layout is not None:
            layout.addWidget(self)

    def changeText(self, text):
        self.setText(text)
        self.adjustSize()

    def getHeight(self):
        return self.height


class evtApp_textBox(QLineEdit):

    def __init__(self, parent, pos_x=0, pos_y=0,
                 height=None, width=None,
                 text="", layout=None, fontSize=10):
        super(evtApp_textBox, self).__init__(parent)

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height

        self.setStyleSheet("color: rgba(255,255,255,255); \
                                                  ")

        if height is None:
            if layout is not None:
                self.height = None
            else:
                self.height = DEFAULT_TEXTBOX_HEIGHT
                self.setFixedHeight(self.height)
        else:
            self.height = height
            self.setFixedHeight(self.height)

        if width is None:
            if layout is not None:
                self.width = None
            else:
                self.width = DEFAULT_TEXTBOX_WIDTH
                self.setFixedWidth(self.width)
        else:
            self.width = width
            self.setFixedWidth(self.width)

        if ((pos_x != 0) or (pos_y != 0)):
            self.move(self.pos_x, self.pos_y)

        if layout is not None:
            layout.addWidget(self)

class evtApp_spinBox(QSpinBox):
    def __init__(self, parent,pos_x=0, pos_y=0,
                 height=None, width=None, maxVal=32768,
                 text="", layout=None, fontSize=10):
        super(evtApp_spinBox, self).__init__(parent)

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height

        self.setStyleSheet("color: rgba(255,255,255,255); \
                                                  ")

        if height is None:
            if layout is not None:
                self.height = None
            else:
                self.height = DEFAULT_SPINBOX_HEIGHT
                self.setFixedHeight(self.height)
        else:
            self.height = height
            self.setFixedHeight(self.height)

        if width is None:
            if layout is not None:
                self.width = None
            else:
                self.width = DEFAULT_SPINBOX_WIDTH
                self.setFixedWidth(self.width)
        else:
            self.width = width
            self.setFixedWidth(self.width)

        self.setWrapping(True)
        self.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.setMaximum(maxVal)

        if ((pos_x != 0) or (pos_y != 0)):
            self.move(self.pos_x, self.pos_y)

        if layout is not None:
            layout.addWidget(self)

class evtApp_spinBox_double(QDoubleSpinBox):
    def __init__(self, parent,pos_x=0, pos_y=0,
                 height=None, width=None, maxVal=32768,
                 text="", layout=None, fontSize=10, decimals=6):
        super(evtApp_spinBox_double, self).__init__(parent)

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height

        self.setStyleSheet("color: rgba(255,255,255,255); \
                                                  ")
        self.setDecimals(decimals)

        if height is None:
            if layout is not None:
                self.height = None
            else:
                self.height = DEFAULT_SPINBOX_HEIGHT
                self.setFixedHeight(self.height)
        else:
            self.height = height
            self.setFixedHeight(self.height)

        if width is None:
            if layout is not None:
                self.width = None
            else:
                self.width = DEFAULT_SPINBOX_WIDTH
                self.setFixedWidth(self.width)
        else:
            self.width = width
            self.setFixedWidth(self.width)

        self.setWrapping(True)
        self.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.setMaximum(maxVal)

        if ((pos_x != 0) or (pos_y != 0)):
            self.move(self.pos_x, self.pos_y)

        if layout is not None:
            layout.addWidget(self)

class evtApp_horizontalSlider(QSlider):
    def __init__(self, parent,pos_x=0, pos_y=0,
                 height=None, width=None,
                 layout=None, maxValue=4096,
                 connect=None):
        super(evtApp_horizontalSlider, self).__init__(parent)

        self.setOrientation(Qt.Horizontal)

        self.setMaximum(maxValue)
        self.setSliderPosition(0)

        if height is None:
            if layout is not None:
                self.height = None
            else:
                self.height = DEFAULT_SLIDER_HEIGHT
                self.setFixedHeight(self.height)
        else:
            self.height = height
            self.setFixedHeight(self.height)

        if width is None:
            if layout is not None:
                self.width = None
            else:
                self.width = DEFAULT_SLIDER_WIDTH
                self.setFixedWidth(self.width)
        else:
            self.width = width
            self.setFixedWidth(self.width)

        if ((pos_x != 0) or (pos_y != 0)):
            self.move(self.pos_x, self.pos_y)

        if layout is not None:
            layout.addWidget(self)

        if connect is not None:
            self.valueChanged.connect(connect)

class evtApp_checkBox(QCheckBox):
    def __init__(self, parent, layout=None,
                 pos_x=0, pos_y=0,
                 text="", fontSize=TEXT_FONT_SIZE_NORMAL,
                 connect=None):
        super(evtApp_checkBox, self).__init__(parent)

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.fontSize = fontSize

        self.setFont(QFont('Arial', self.fontSize))
        self.height = self.fontSize * 2
        self.setText(text)
        self.adjustSize()

        if ((pos_x != 0) or (pos_y != 0)):
            self.move(self.pos_x, self.pos_y)

        if layout is not None:
            layout.addWidget(self)

        if connect is not None:
            self.stateChanged.connect(connect)

class evt_clocking_graphic(QLabel):

    def __init__(self, parent, pos_x=None, pos_y=None):
        super(evt_clocking_graphic, self).__init__(parent)

        self.pos_x = pos_x
        self.pox_y = pos_y
        self.evt_scale = 0.65
        self.trumpet_scale = 0.15
        self.trumpet_rotation = 0

        self.setAlignment(Qt.AlignCenter)
        self.setAttribute(Qt.WA_TranslucentBackground)

        if ((pos_x is not None) and (pos_y is not None)):
            self.move(pos_x, pos_y)

        self.evt_pixmap = QPixmap(resource_path("EVT_schematic.png"))
        self.evt_trumpet_pixmap = QPixmap(resource_path("Trompette_schematic.png"))

        self.evt_trumpet_image_width = self.evt_trumpet_pixmap.width()
        self.evt_trumpet_image_height = self.evt_trumpet_pixmap.height()

        self.draw_graphic()


    def draw_graphic(self):

        evt_pixmap_transform = QTransform()
        evt_pixmap_transform.scale(self.evt_scale, self.evt_scale)

        evt_trumpet_pixmap_transform = QTransform()
        evt_trumpet_pixmap_transform.rotate(self.trumpet_rotation)
        evt_trumpet_pixmap_transform.scale(self.trumpet_scale, self.trumpet_scale)


        evt_rectF = QRectF(0, 0,
                           int(self.evt_pixmap.width() * self.evt_scale),
                           int(self.evt_pixmap.height() * self.evt_scale))

        evt_trumpet_rotated_image_width = self.evt_trumpet_image_width * self.trumpet_scale\
                                          * (1+0.41421*(abs(sin(radians(self.trumpet_rotation*2)))))
        evt_trumpet_rotated_image_height = self.evt_trumpet_image_height * self.trumpet_scale\
                                           * (1+0.41421*(abs(sin(radians(self.trumpet_rotation*2)))))

        trompette_rectF = QRectF(int((643 * self.evt_scale) - (evt_trumpet_rotated_image_width / 2)),
                                 int((487 * self.evt_scale) - (evt_trumpet_rotated_image_height / 2)),
                                 int(self.evt_trumpet_image_width),
                                 int(self.evt_trumpet_image_height))

        newPixmap = QPixmap(int(evt_rectF.getRect()[2]), int(evt_rectF.getRect()[3]))
        newPixmap.fill(Qt.transparent)

        finalPixmap = QPainter(newPixmap)
        finalPixmap.drawPixmap(evt_rectF, self.evt_pixmap.transformed(evt_pixmap_transform,
                                                                           Qt.SmoothTransformation),
                                    QRectF(self.evt_pixmap.transformed(evt_pixmap_transform,
                                                                       Qt.SmoothTransformation).rect()))

        finalPixmap.drawPixmap(trompette_rectF,
                               self.evt_trumpet_pixmap.transformed(evt_trumpet_pixmap_transform,
                                                                        Qt.SmoothTransformation),
                              QRectF(self.evt_trumpet_pixmap.rect()))
        finalPixmap.end()

        self.setPixmap(newPixmap)



    @pyqtSlot()
    def rotate_CCW(self, rotation=1):
        self.trumpet_rotation -= rotation

        self.draw_graphic()

    @pyqtSlot()
    def rotate_CW(self, rotation=1):
        self.trumpet_rotation += rotation

        self.draw_graphic()

    @pyqtSlot()
    def rotate_trumpet(self, rotation_value):
        self.trumpet_rotation = int((int(rotation_value)/4096)*360);
        self.draw_graphic();


class loraApp_HLine(QFrame):

    def __init__(self, parent, layout):
        super(loraApp_HLine, self).__init__(parent)

        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)
        self.setObjectName("line")
        layout.addWidget(self)

class loraApp_VLine(QFrame):

    def __init__(self, parent, layout):
        super(loraApp_VLine, self).__init__(parent)

        self.setFrameShape(QFrame.VLine)
        self.setFrameShadow(QFrame.Sunken)
        self.setObjectName("line")
        layout.addWidget(self)

class evtApp_HSpacer(QSpacerItem):
    def __init__(self, layout):
        super(evtApp_HSpacer, self).__init__(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(self)

class evtApp_VSpacer(QSpacerItem):
    def __init__(self, layout):
        super(evtApp_VSpacer, self).__init__(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        layout.addItem(self)

class loraConsole(QTextEdit):
    def __init__(self, parent,pos_x=0, pos_y=0,
                 height=200, width=600,
                 text="", layout=None, fontSize=10):
        super(loraConsole, self).__init__(parent)

        self.moveCursor(QTextCursor.Start)
        self.ensureCursorVisible()
        self.setFixedHeight(height)
        self.setFixedWidth(width)
        self.setFontPointSize(12)



        #self.lineWrapColumnOrWidth()
        #self.setLineWrapMode(QTextEdit.WidgetWidth)