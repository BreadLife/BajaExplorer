from functools import partial

from PyQt5 import QtCore, QtWidgets, QtSvg
from PyQt5.QtSvg import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from gui_assets import *
#from gui_functions import *
from gui_secondaryWindows import liveClockingProcede_dialog
from serial_communication import *


## Not sure what these are for
EVT_status_tab = None
EVT_clocking_tab = None
EVT_tuning_tab = None
EVT_debugging_tab = None
settings_tab = None


class LORAApp_tab(QtWidgets.QWidget):
    def __init__(self, parent, name):
        super(LORAApp_tab, self).__init__()
        parent.addTab(self, name)
        self.parent = parent


class LORAStatusTab(LORAApp_tab):

    def __init__(self, root):
        super(LORAStatusTab, self).__init__(root.MainTabs, name=" LORA Status ")
        self.setObjectName("LORA_status_tab")

        self.root = root

        # displays
        self.tabMainLayout = QtWidgets.QVBoxLayout(self)
        self.tabMainLayout.setObjectName("tabMainLayout")
        self.tabMainLayout.setContentsMargins(15, 10, 15, 15)

        # display - Connections status
        self.connectionStatusDisplayArea = QtWidgets.QWidget(self)
        self.connectionStatusDisplayArea.setObjectName("loraConnectionStatusArea")
        self.connectionStatusDisplayArea.setFixedWidth(300)
        self.connectionStatusDisplayArea.setFixedHeight(100)
        self.connectionStatusDisplayArea.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))

        self.connectionStatusDisplayLayout = QtWidgets.QVBoxLayout(self.connectionStatusDisplayArea)
        self.connectionStatusDisplayLayout.setObjectName("connectionStatusDisplayLayout")
        self.connectionStatusDisplayLayout.setAlignment(Qt.AlignLeft)

        self.connectionStatusDisplayTitle = loraApp_label(self,
                                                          layout=self.connectionStatusDisplayLayout,
                                                          fontSize=TEXT_FONT_SIZE_TITLE,
                                                          text="Connections Status",
                                                          alignment=Qt.AlignLeft)
        self.connectionStatusDisplayValue = loraApp_label(self,
                                                          layout=self.connectionStatusDisplayLayout,
                                                          fontSize=TEXT_FONT_SIZE_TITLE,
                                                          text="N/A",
                                                          alignment=Qt.AlignLeft)


        #loraApp_HLine(self, self.tabMainLayout)

        # display - Console
        self.consoleDisplayArea = QtWidgets.QWidget(self)
        self.consoleDisplayArea.setObjectName("consoleDisplayArea")
        self.consoleDisplayArea.setFixedWidth(300)
        self.consoleDisplayArea.setFixedHeight(100)

        #self.consoleDisplayArea.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))

        self.consoleDisplay = loraConsole(self,
                                     layout=self.consoleDisplayArea)

        self.tabMainLayout.insertWidget(0, self.connectionStatusDisplayArea, Qt.AlignHCenter)
        self.tabMainLayout.insertWidget(1, self.consoleDisplayArea, Qt.AlignHCenter)





#        self.consoleDisplayTitle = evtApp_label(self,
#                                                layout=self.consoleDisplayLayout,
#                                                fontSize=TEXT_FONT_SIZE_TITLE,
#                                                text="Sheave Clamping",
#                                                alignment=Qt.AlignHCenter)
#        self.consoleDisplayValue = evtApp_label(self,
#                                                layout=self.consoleDisplayLayout,
#                                                fontSize=TEXT_FONT_SIZE_TITLE * 2,
#                                                text="N/A",
#                                                alignment=Qt.AlignHCenter)

        # information section ----------------------------------------------------------------------------------------
#        self.informationLayout = QtWidgets.QHBoxLayout(self)
#        self.informationLayout.setObjectName("informationLayout")
#        self.tabMainLayout.addLayout(self.informationLayout)
#
#        # Sensor Status Section
#        self.SensorStatusTopLayout = QtWidgets.QVBoxLayout(self)
#        self.SensorStatusTopLayout.setObjectName("SensorStatusTitleLayout")
#        self.informationLayout.addLayout(self.SensorStatusTopLayout)
#
#        # Vertical Line
#        loraApp_VLine(self, self.informationLayout)
#
#        # General Information Section
#        self.generalInformationLayout = QtWidgets.QVBoxLayout(self)
#        self.generalInformationLayout.setObjectName("generalInformationLayout")
#        self.informationLayout.addLayout(self.generalInformationLayout)
#
#        # Sensor Status
#        self.SensorStatusTitle = loraApp_label(self,
#                                               layout=self.SensorStatusTopLayout,
#                                               fontSize=TEXT_FONT_SIZE_TITLE,
#                                               text="Sensor Status Information",
#                                               alignment=Qt.AlignLeft)
#
#        self.SensorStatusLayout = QtWidgets.QHBoxLayout(self)
#        self.SensorStatusLayout.setObjectName("SensorStatusLayout")
#        self.SensorStatusTopLayout.addLayout(self.SensorStatusLayout)
#
#        self.SensorStatusTitleLayout = QtWidgets.QVBoxLayout(self)
#        self.SensorStatusTitleLayout.setObjectName("SensorStatusTitleLayout")
#        self.SensorStatusLayout.addLayout(self.SensorStatusTitleLayout)
#
#        loraApp_VLine(self, self.SensorStatusLayout)
#
#        self.SensorStatusValueLayout = QtWidgets.QVBoxLayout(self)
#        self.SensorStatusValueLayout.setObjectName("SensorStatusValueLayout")
#        self.SensorStatusLayout.addLayout(self.SensorStatusValueLayout)
#
#        # TPM Sensor status
#        self.TPMSensorStatusTitle = loraApp_label(self,
#                                                  layout=self.SensorStatusTitleLayout,
#                                                  fontSize=TEXT_FONT_SIZE_NORMAL,
#                                                  text="TPM",
#                                                  alignment=Qt.AlignRight)
#        self.TPMSensorStatusValue = loraApp_label(self,
#                                                  layout=self.SensorStatusValueLayout,
#                                                  fontSize=TEXT_FONT_SIZE_NORMAL,
#                                                  text="EVT Not Connected",
#                                                  alignment=Qt.AlignLeft)
#
#        # RPM Sensor status
#        self.RPMSensorStatusTitle = loraApp_label(self,
#                                                  layout=self.SensorStatusTitleLayout,
#                                                  fontSize=TEXT_FONT_SIZE_NORMAL,
#                                                  text="RPM",
#                                                  alignment=Qt.AlignRight)
#        self.RPMSensorStatusValue = loraApp_label(self,
#                                                  layout=self.SensorStatusValueLayout,
#                                                  fontSize=TEXT_FONT_SIZE_NORMAL,
#                                                  text="EVT Not Connected",
#                                                  alignment=Qt.AlignLeft)
#
#        # ADC Sensor status
#        self.ADCSensorStatusTitle = loraApp_label(self,
#                                                  layout=self.SensorStatusTitleLayout,
#                                                  fontSize=TEXT_FONT_SIZE_NORMAL,
#                                                  text="ADC",
#                                                  alignment=Qt.AlignRight)
#        self.ADCSensorStatusValue = loraApp_label(self,
#                                                  layout=self.SensorStatusValueLayout,
#                                                  fontSize=TEXT_FONT_SIZE_NORMAL,
#                                                  text="EVT Not Connected",
#                                                  alignment=Qt.AlignLeft)
#
#        # General Info Status
#        self.generalInformationTitle = loraApp_label(self,
#                                                     layout=self.generalInformationLayout,
#                                                     fontSize=TEXT_FONT_SIZE_TITLE,
#                                                     text="General Information",
#                                                     alignment=Qt.AlignLeft)
#
#        self.codeVersionLabel = loraApp_label(self,
#                                              layout=self.generalInformationLayout,
#                                              fontSize=TEXT_FONT_SIZE_NORMAL,
#                                              text="      Code Version:",
#                                              alignment=Qt.AlignLeft)
#
#        self.debuggingLevelLabel = loraApp_label(self,
#                                                 layout=self.generalInformationLayout,
#                                                 fontSize=TEXT_FONT_SIZE_NORMAL,
#                                                 text="      Debugging Level:",
#                                                 alignment=Qt.AlignLeft)
#
#        self.ControlsTitle = loraApp_label(self,
#                                           layout=self.generalInformationLayout,
#                                           fontSize=TEXT_FONT_SIZE_TITLE,
#                                           text="Controls",
#                                           alignment=Qt.AlignLeft)
#
#        self.controlsSectionLayout = QtWidgets.QHBoxLayout(self)
#        self.controlsSectionLayout.setObjectName("controlsSectionLayout")
#        self.generalInformationLayout.addLayout(self.controlsSectionLayout)
#
#        self.liveStatus_checkBox = evtApp_checkBox(self,
#                                                   layout=self.controlsSectionLayout,
#                                                   text="Live status?",
#                                                   connect=(lambda: self.setLiveStatus()))
#
#        self.liveStatusPeriod_label = loraApp_label(self,
#                                                    layout=self.controlsSectionLayout,
#                                                    text="Période des mises à jour: ")
#        self.liveStatusPeriod_spinBox = evtApp_spinBox(self,
#                                                       layout=self.controlsSectionLayout,
#                                                       maxVal=10000)
#
        # End filler
        #loraApp_HLine(self, self.tabMainLayout)

    def setLiveStatus(self):
        if self.liveStatus_checkBox.checkState() == Qt.Checked:
            self.root.statusPeriodicUpdateActive = True
        else:
            self.root.statusPeriodicUpdateActive = False

    def updateDebuggingLevel(self, level):
        if level == 0:
            self.debuggingLevelLabel.changeText("      Debugging Level: " + "Rien")
        elif level == 1:
            self.debuggingLevelLabel.changeText("      Debugging Level: " + "Base")
        elif level == 2:
            self.debuggingLevelLabel.changeText("      Debugging Level: " + "Tout")
        else:
            self.debuggingLevelLabel.changeText("      Debugging Level: " + "Inconnu")

    def updateSheavePosition(self, value):
        self.connectionStatusDisplayValue.changeText(str(value))
        self.ADCSensorStatusValue.changeText(" OK")

    def updateMotorRPM(self, value):
        self.rpmMoteurDisplayValue.changeText(str(value))
        self.RPMSensorStatusValue.changeText(" OK")

    def updateTPM(self, value):
        self.throttlePositionDisplayValue.changeText(str(value))
        self.TPMSensorStatusValue.changeText(" OK")

class LORADataTab(LORAApp_tab):

    def __init__(self, root):
        super(LORADataTab, self).__init__(root.MainTabs, name=" Data ")
        self.setObjectName("LORA_data_tab")

        self.root = root

        self.liveClocking = False

        self.tabLineLayout = QtWidgets.QVBoxLayout(self)
        self.tabLineLayout.setObjectName("tabLineLayout")
        self.tabLineLayout.setContentsMargins(15, 10, 15, 15)

        loraApp_HLine(self, self.tabLineLayout)

        self.tabMainLayout = QtWidgets.QHBoxLayout(self)
        self.tabMainLayout.setObjectName("tuningSettingsLayout")
        self.tabLineLayout.addLayout(self.tabMainLayout)

        self.evt_graphic = evt_clocking_graphic(self)
        self.tabMainLayout.addWidget(self.evt_graphic)

        # Control Layout
        self.controlsLayoutWidget = QtWidgets.QWidget(self)
        self.controlsLayoutWidget.setMaximumWidth(400)
        self.controlsLayoutWidget.setObjectName("controlsLayoutWidget")

        self.controlsLayout = QtWidgets.QVBoxLayout(self.controlsLayoutWidget)
        self.controlsLayout.setContentsMargins(10, 10, 10, 10)
        self.controlsLayout.setAlignment(Qt.AlignTop)
        self.controlsLayout.setObjectName("controlsLayout")
        self.tabMainLayout.addWidget(self.controlsLayoutWidget)

        # Clocking
        self.clockingTitle = loraApp_label(self.controlsLayoutWidget,
                                           fontSize=TEXT_FONT_SIZE_TITLE,
                                           text="Clocking",
                                           layout=self.controlsLayout)

        self.clockingCurrentValue_Label = loraApp_label(self.controlsLayoutWidget,
                                                        text="Clocking current value: N/A",
                                                        layout=self.controlsLayout)

        self.clockingValueLayout = QtWidgets.QHBoxLayout()
        self.clockingValueLayout.setObjectName("clockingValueLayout")
        self.controlsLayout.addLayout(self.clockingValueLayout)

        self.clockingValueField_spinBox = evtApp_spinBox(self.controlsLayoutWidget,
                                                         width=DEFAULT_SPINBOX_WIDTH,
                                                         height=DEFAULT_SPINBOX_HEIGHT,
                                                         maxVal=ADC_MAX_VAL,
                                                         layout=self.clockingValueLayout)
        self.clockingValueSend_PushButton = evtApp_pushButton(self.controlsLayoutWidget,
                                                              layout=self.clockingValueLayout,
                                                              text=" Send ",
                                                              height=30,
                                                              connect=(lambda: self.setSheaveOpenPosEEPROM(
                                                                  self.clockingValueField_spinBox.value())))

        # Clocking buttons
        self.clockingButtonsLayout = QtWidgets.QHBoxLayout()
        self.clockingButtonsLayout.setObjectName("clockingButtonsLayout")
        self.controlsLayout.addLayout(self.clockingButtonsLayout)

        self.trompetteRotateCWFast_PushButton = evtApp_pushButton(self.controlsLayoutWidget,
                                                                  height=30,
                                                                  layout=self.clockingButtonsLayout,
                                                                  text=" -100 ",
                                                                  connect=(lambda: self.incrementSheavePosition(-100)))

        self.trompetteRotateCWSlow_PushButton = evtApp_pushButton(self.controlsLayoutWidget,
                                                                  height=30,
                                                                  layout=self.clockingButtonsLayout,
                                                                  text=" -10 ",
                                                                  connect=(lambda: self.incrementSheavePosition(-10)))

        self.trompetteRotateCCWSlow_PushButton = evtApp_pushButton(self.controlsLayoutWidget,
                                                                   height=30,
                                                                   layout=self.clockingButtonsLayout,
                                                                   text=" +10 ",
                                                                   connect=(lambda: self.incrementSheavePosition(10)))

        self.trompetteRotateCCWFast_PushButton = evtApp_pushButton(self.controlsLayoutWidget,
                                                                   height=30,
                                                                   layout=self.clockingButtonsLayout,
                                                                   text=" +100 ",
                                                                   connect=(lambda: self.incrementSheavePosition(100)))

        # Clocking Slider
        self.clockingSlider = evtApp_horizontalSlider(self, layout=self.controlsLayout,
                                                      connect=(lambda: self.setSheaveOpenPosEEPROM(
                                                          self.clockingSlider.value())))

        # Live Clocking Checkbox
        self.liveClocking_CheckBox = evtApp_checkBox(self, layout=self.controlsLayout,
                                                     text=" Live Clocking",
                                                     connect=(lambda: self.setLiveClockingValue(
                                                         self.liveClocking_CheckBox.checkState())))

        # Spacing and line
        evtApp_HSpacer(self.controlsLayout)
        loraApp_HLine(self, self.controlsLayout)

        # Travel
        self.travelTitle = loraApp_label(self.controlsLayoutWidget,
                                         fontSize=TEXT_FONT_SIZE_TITLE,
                                         text="Travel",
                                         layout=self.controlsLayout)
        self.travelCurrentValue_Label = loraApp_label(self.controlsLayoutWidget,
                                                      text="Travel current value: N/A",
                                                      layout=self.controlsLayout)

        self.travelValueLayout = QtWidgets.QHBoxLayout()
        self.travelValueLayout.setObjectName("travelValueLayout")
        self.controlsLayout.addLayout(self.travelValueLayout)

        self.travelValueField_spinBox = evtApp_spinBox(self.controlsLayoutWidget,
                                                       layout=self.travelValueLayout,
                                                       width=DEFAULT_SPINBOX_WIDTH,
                                                       maxVal=ADC_MAX_VAL,
                                                       height=DEFAULT_SPINBOX_HEIGHT)
        self.travelValueSend_PushButton = evtApp_pushButton(self.controlsLayoutWidget,
                                                            layout=self.travelValueLayout,
                                                            text=" Send ",
                                                            height=30,
                                                            connect=(lambda: self.setSheaveTravelEEPROM(
                                                                self.travelValueField_spinBox.value())))

        # Spacing and line
        evtApp_HSpacer(self.controlsLayout)
        loraApp_HLine(self, self.controlsLayout)

        # ThrottlePosition (TPM)
        self.tpmTitle = loraApp_label(self.controlsLayoutWidget,
                                      fontSize=TEXT_FONT_SIZE_TITLE,
                                      text="Throttle Position Calibration",
                                      layout=self.controlsLayout)
        self.tpmCurrentValue_Label = loraApp_label(self.controlsLayoutWidget,
                                                   layout=self.controlsLayout,
                                                   text="Throttle current position: N/A")
        self.tpmMaxTitle_Label = loraApp_label(self.controlsLayoutWidget,
                                               layout=self.controlsLayout,
                                               fontSize=TEXT_FONT_SIZE_TITLE - 5,
                                               text="Full throttle")
        self.tpmMaxValue_Label = loraApp_label(self.controlsLayoutWidget,
                                               layout=self.controlsLayout,
                                               text="Full throttle current value: N/A")
        self.tpmMaxValueSetWithCurrent_PushButton = evtApp_pushButton(self.controlsLayoutWidget,
                                                                      layout=self.controlsLayout,
                                                                      text=" Set with current value ",
                                                                      height=30,
                                                                      connect=None)

        self.tpmMaxValueLayout = QtWidgets.QHBoxLayout()
        self.tpmMaxValueLayout.setObjectName("tpmMaxValueLayout")
        self.controlsLayout.addLayout(self.tpmMaxValueLayout)

        self.tpmMaxValueField_spinBox = evtApp_spinBox(self.controlsLayoutWidget,
                                                       layout=self.tpmMaxValueLayout,
                                                       maxVal=ADC_MAX_VAL,
                                                       width=DEFAULT_SPINBOX_WIDTH,
                                                       height=DEFAULT_SPINBOX_HEIGHT)
        self.tpmMaxValueSend_PushButton = evtApp_pushButton(self.controlsLayoutWidget,
                                                            layout=self.tpmMaxValueLayout,
                                                            text=" Send ",
                                                            height=30,
                                                            connect=(lambda: self.setTPMFullThrottleEEPROM(
                                                                self.tpmMaxValueField_spinBox.value())))

        self.tpmMinTitle_Label = loraApp_label(self.controlsLayoutWidget,
                                               layout=self.controlsLayout,
                                               fontSize=TEXT_FONT_SIZE_TITLE - 5,
                                               text="No throttle")
        self.tpmMinValue_Label = loraApp_label(self.controlsLayoutWidget,
                                               layout=self.controlsLayout,
                                               text="No throttle current value: N/A")

        self.tpmMinValueSetWithCurrent_PushButton = evtApp_pushButton(self.controlsLayoutWidget,
                                                                      layout=self.controlsLayout,
                                                                      text=" Set with current value ",
                                                                      height=30,
                                                                      connect=None)

        self.tpmMinValueLayout = QtWidgets.QHBoxLayout()
        self.tpmMinValueLayout.setObjectName("tpmMinValueLayout")
        self.controlsLayout.addLayout(self.tpmMinValueLayout)

        self.tpmMinValueField_spinBox = evtApp_spinBox(self.controlsLayoutWidget,
                                                       layout=self.tpmMinValueLayout,
                                                       maxVal=ADC_MAX_VAL,
                                                       width=DEFAULT_SPINBOX_WIDTH,
                                                       height=DEFAULT_SPINBOX_HEIGHT)
        self.tpmMinValueSend_PushButton = evtApp_pushButton(self.controlsLayoutWidget,
                                                            layout=self.tpmMinValueLayout,
                                                            text=" Send ",
                                                            height=30,
                                                            connect=(lambda: self.setTPMNoThrottleEEPROM(
                                                                self.tpmMinValueField_spinBox.value())))

        # End Spacer
        evtApp_HSpacer(self.controlsLayout)

        # Refresh
        self.refreshClockingTab_PushButton = evtApp_pushButton(self, pos_x=20, pos_y=20,
                                                               text=" Refresh ",
                                                               connect=(lambda: self.refresh_clocking_tab_values()))

    @pyqtSlot()
    def setLiveClockingValue(self, value):
        if value == Qt.Checked:
            if liveClockingProcede_dialog() == QMessageBox.Ok:
                self.liveClocking = True
                self.root.print_status("Live clocking activated!")
                self.root.COMPort.EVT_read_EEPROM(const.SHEAVE_OPEN_POS_EEPROM_ADDR)
            else:
                self.liveClocking_CheckBox.setCheckState(Qt.Unchecked)
        else:
            self.liveClocking = False

    @pyqtSlot()
    def incrementSheavePosition(self, increment):

        if (self.root.evt_eeprom.sheave_open_pos is not None) and \
                (self.root.evt_eeprom.sheave_travel is not None):

            if checklimits(int(self.root.evt_eeprom.sheave_open_pos
                               + self.root.evt_eeprom.sheave_open_pos
                               + increment), maxVal=ADC_MAX_VAL) != "error":
                self.root.evt_eeprom.sheave_open_pos += increment
                self.setSheaveOpenPosEEPROM(self.root.evt_eeprom.sheave_open_pos)
        else:
            print("Please refresh first.")

    @pyqtSlot()
    def setSheaveOpenPosEEPROM(self, set_value=None):
        if set_value is None:
            return None
        else:
            send_value = int(set_value)

        if(self.root.evt_eeprom.sheave_open_pos is None) or (self.root.evt_eeprom.sheave_travel is None):
            self.root.print_status("EVT is not connected or local variable not refreshed.")
            return None

        if checklimits((send_value + self.root.evt_eeprom.sheave_travel), maxVal=ADC_MAX_VAL) != "error":
            self.root.evt_eeprom.sheave_open_pos = int(send_value)

            self.updateSheaveOpenPos(self.root.evt_eeprom.sheave_open_pos)
            self.root.print_status("Sheave clocking position set to: " + str(self.root.evt_eeprom.sheave_open_pos))

            if self.liveClocking and self.root.COMConnected:
                self.root.COMPort.EVT_write_to_EEPROM(const.SHEAVE_OPEN_POS_EEPROM_ADDR,
                                                      int(self.root.evt_eeprom.sheave_open_pos))
            else:
                self.root.print_status("Live Clocking mode is not enabled or EVT is not connected.")

        else:
            self.root.print_status("Value entered out of limits.")

    @pyqtSlot()
    def setSheaveTravelEEPROM(self, set_value=None):
        if set_value is None:
            return None
        else:
            send_value = int(set_value)

        if(self.root.evt_eeprom.sheave_travel is None):
            self.root.print_status("EVT is not connected or local variable not refreshed.")
            return None

        if checklimits(send_value + self.root.evt_eeprom.sheave_open_pos, maxVal=ADC_MAX_VAL) != "error":
            self.root.evt_eeprom.sheave_travel = int(send_value)

            self.updateSheaveTravel(self.root.evt_eeprom.sheave_travel)
            self.root.print_status("Sheave travel set to: " + str(self.root.evt_eeprom.sheave_travel))

            if self.root.COMConnected:
                self.root.COMPort.EVT_write_to_EEPROM(const.SHEAVE_TRAVEL_EEPROM_ADDR,
                                                      int(self.root.evt_eeprom.sheave_travel))
            else:
                self.root.print_status("EVT is not connected.")
        else:
            self.root.print_status("Value entered out of limits.")

    @pyqtSlot()
    def setTPMFullThrottleEEPROM(self, set_value=None):
        if set_value is None:
            return None
        else:
            send_value = int(set_value)

        if(self.root.evt_eeprom.tpm_full_throttle is None):
            self.root.print_status("EVT is not connected or local variable not refreshed.")
            return None

        if checklimits(send_value, maxVal=ADC_MAX_VAL) != "error":
            self.root.evt_eeprom.tpm_full_throttle = int(send_value)

            self.updateTPMFullThrottle(self.root.evt_eeprom.tpm_full_throttle)
            self.root.print_status("Full throttle value set to: " + str(self.root.evt_eeprom.tpm_full_throttle))

            if self.root.COMConnected:
                self.root.COMPort.EVT_write_to_EEPROM(const.TPM_FULL_TROTTLE_EEPROM_ADDR,
                                                      int(self.root.evt_eeprom.tpm_full_throttle))
            else:
                self.root.print_status("EVT is not connected.")
        else:
            self.root.print_status("Value entered out of limits.")

    @pyqtSlot()
    def setTPMNoThrottleEEPROM(self, set_value=None):
        if set_value is None:
            return None
        else:
            send_value = int(set_value)

        if(self.root.evt_eeprom.tpm_no_throttle is None):
            self.root.print_status("EVT is not connected or local variable not refreshed.")
            return None

        if checklimits(send_value, maxVal=ADC_MAX_VAL) != "error":
            self.root.evt_eeprom.tpm_no_throttle = int(send_value)

            self.updateTPMNoThrottle(self.root.evt_eeprom.tpm_no_throttle)
            self.root.print_status("No throttle value set to: " + str(self.root.evt_eeprom.tpm_no_throttle))

            if self.root.COMConnected:
                self.root.COMPort.EVT_write_to_EEPROM(const.TPM_NO_TROTTLE_EEPROM_ADDR,
                                                      int(self.root.evt_eeprom.tpm_no_throttle))
            else:
                self.root.print_status("EVT is not connected.")
        else:
            self.root.print_status("Value entered out of limits.")

    @pyqtSlot()
    def refresh_clocking_tab_values(self):
        if self.root.COMConnected:
            self.root.COMPort.EVT_read_EEPROM(const.SHEAVE_OPEN_POS_EEPROM_ADDR)
            self.root.COMPort.EVT_read_EEPROM(const.SHEAVE_TRAVEL_EEPROM_ADDR)
            self.root.COMPort.EVT_read_EEPROM(const.TPM_NO_TROTTLE_EEPROM_ADDR)
            self.root.COMPort.EVT_read_EEPROM(const.TPM_FULL_TROTTLE_EEPROM_ADDR)
            self.root.print_status("Values refreshed")
        else:
            self.root.print_status("EVT is not connected.")

    # Reception of new values
    def updateSheaveOpenPos(self, value):
        self.clockingCurrentValue_Label.changeText("Clocking current value: " + str(value))
        self.evt_graphic.rotate_trumpet(int(value))
        self.clockingValueField_spinBox.setValue(int(value))

        self.clockingSlider.blockSignals(True)
        self.clockingSlider.setSliderPosition(int(value))
        self.clockingSlider.blockSignals(False)

    def updateSheaveTravel(self, value):
        self.travelCurrentValue_Label.changeText("Travel current value: " + str(value))
        self.travelValueField_spinBox.setValue(value)

        self.clockingSlider.setMaximum(ADC_MAX_VAL - value)

    def updateTPMFullThrottle(self, value):
        self.tpmMaxValue_Label.changeText("Full throttle current value: " + str(value))
        self.tpmMaxValueField_spinBox.setValue(value)

    def updateTPMNoThrottle(self, value):
        self.tpmMinValue_Label.changeText("No throttle current value: " + str(value))
        self.tpmMinValueField_spinBox.setValue(value)

"""
class LORATuningTab(LORAApp_tab):

    def __init__(self, root):
        super(LORATuningTab, self).__init__(root.MainTabs, name=" EVT Tuning ")
        self.setObjectName("EVT_tuning_tab")

        self.root = root

        sendButtonWidth = 90
        sendButtonHeight = 30

        row_space = 15

        self.tabMainLayout = QtWidgets.QVBoxLayout(self)
        self.tabMainLayout.setObjectName("tabMainLayout")
        self.tabMainLayout.setContentsMargins(15, 10, 15, 15)

        evtApp_HLine(self, self.tabMainLayout)

        # Refresh --------------------------------------------------------------------#
        self.refreshLayout = QtWidgets.QHBoxLayout(self)
        self.refreshLayout.setObjectName("refreshLayout")
        self.tabMainLayout.addLayout(self.refreshLayout)

        self.refreshTuningTab_PushButton = evtApp_pushButton(self,
                                                             layout=self.refreshLayout,
                                                             width=300,
                                                             height=40,
                                                             text=" Refresh ",
                                                             connect=(lambda: self.refresh_tuning_tab_values()))

        # Tuning Section Layout -----------------------------------------------------#
        self.tuningSettingsLayout = QtWidgets.QHBoxLayout(self)
        self.tuningSettingsLayout.setObjectName("tuningSettingsLayout")
        self.tabMainLayout.addLayout(self.tuningSettingsLayout)

        # Sheave movement PID Layout
        self.PIDLayout = QtWidgets.QVBoxLayout(self)
        self.PIDLayout.setContentsMargins(10, 10, 10, 10)
        self.PIDLayout.setObjectName("PIDLayout")
        self.tuningSettingsLayout.addLayout(self.PIDLayout)

        # RPM Control Layout
        self.rpmCTRLLayout = QtWidgets.QVBoxLayout(self)
        self.rpmCTRLLayout.setContentsMargins(10, 10, 10, 10)
        self.rpmCTRLLayout.setObjectName("rpmCTRLLayout")
        self.tuningSettingsLayout.addLayout(self.rpmCTRLLayout)

        # Fields
        self.sheavePIDTitle = evtApp_label(self,
                                           fontSize=TEXT_FONT_SIZE_TITLE,
                                           text="Sheave PID",
                                           layout=self.PIDLayout)

        spacer = QSpacerItem(0, row_space, QSizePolicy.Minimum, QSizePolicy.Preferred)
        self.PIDLayout.addItem(spacer)

        self.sheavePIDPValue_Label = evtApp_label(self,
                                                  layout=self.PIDLayout,
                                                  text="P current value: N/A")

        self.sheavePIDPValueLayout = QtWidgets.QHBoxLayout(self)
        self.sheavePIDPValueLayout.setObjectName("sheavePIDPValueLayout")
        self.PIDLayout.addLayout(self.sheavePIDPValueLayout)

        self.sheavePIDPField_spinBox = evtApp_spinBox_double(self,
                                                             layout=self.sheavePIDPValueLayout,
                                                             width=150)
        self.sheavePIDPSend_PushButton = evtApp_pushButton(self,
                                                           layout=self.sheavePIDPValueLayout,
                                                           width=sendButtonWidth, height=sendButtonHeight,
                                                           text=" Send ",
                                                           connect=(lambda: self.setSheaveCTRLP_EEPROM(
                                                               self.sheavePIDPField_spinBox.value())))

        spacer = QSpacerItem(0, row_space, QSizePolicy.Minimum, QSizePolicy.Preferred)
        self.PIDLayout.addItem(spacer)

        self.sheavePIDIValue_Label = evtApp_label(self,
                                                  layout=self.PIDLayout,
                                                  text="I current value: N/A")

        self.sheavePIDIValueLayout = QtWidgets.QHBoxLayout(self)
        self.sheavePIDIValueLayout.setObjectName("sheavePIDIValueLayout")
        self.PIDLayout.addLayout(self.sheavePIDIValueLayout)

        self.sheavePIDIField_spinBox = evtApp_spinBox_double(self,
                                                             layout=self.sheavePIDIValueLayout,
                                                             width=150)
        self.sheavePIDISend_PushButton = evtApp_pushButton(self,
                                                           layout=self.sheavePIDIValueLayout,
                                                           width=sendButtonWidth, height=sendButtonHeight,
                                                           text=" Send ",
                                                           connect=(lambda: self.setSheaveCTRLI_EEPROM(
                                                               self.sheavePIDIField_spinBox.value())))

        spacer = QSpacerItem(0, row_space, QSizePolicy.Minimum, QSizePolicy.Preferred)
        self.PIDLayout.addItem(spacer)

        self.sheavePIDDValue_Label = evtApp_label(self,
                                                  layout=self.PIDLayout,
                                                  text="D current value: N/A")

        self.sheavePIDValueLayout = QtWidgets.QHBoxLayout(self)
        self.sheavePIDValueLayout.setObjectName("sheavePIDValueLayout")
        self.PIDLayout.addLayout(self.sheavePIDValueLayout)

        self.sheavePIDDField_spinBox = evtApp_spinBox_double(self,
                                                             layout=self.sheavePIDValueLayout,
                                                             width=150)
        self.sheavePIDDSend_PushButton = evtApp_pushButton(self,
                                                           layout=self.sheavePIDValueLayout,
                                                           width=sendButtonWidth, height=sendButtonHeight,
                                                           text=" Send ",
                                                           connect=(lambda: self.setSheaveCTRLD_EEPROM(
                                                               self.sheavePIDDField_spinBox.value())))

        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.PIDLayout.addItem(spacerItem)

        # RPM CTRL PID
        self.rpmCTRLTitle = evtApp_label(self,
                                         fontSize=TEXT_FONT_SIZE_TITLE,
                                         text="RPM Control",
                                         layout=self.rpmCTRLLayout)

        spacer = QSpacerItem(0, row_space, QSizePolicy.Minimum, QSizePolicy.Preferred)
        self.rpmCTRLLayout.addItem(spacer)

        self.rpmCTRLPValue_Label = evtApp_label(self,
                                                layout=self.rpmCTRLLayout,
                                                text="P current value: N/A")

        self.rpmCTRLPValueLayout = QtWidgets.QHBoxLayout(self)
        self.rpmCTRLPValueLayout.setObjectName("rpmCTRLPValueLayout")
        self.rpmCTRLLayout.addLayout(self.rpmCTRLPValueLayout)

        self.rpmCTRLPField_spinBox = evtApp_spinBox_double(self,
                                                           layout=self.rpmCTRLPValueLayout,
                                                           width=150)
        self.rpmCTRLPSend_PushButton = evtApp_pushButton(self,
                                                         layout=self.rpmCTRLPValueLayout,
                                                         width=sendButtonWidth, height=sendButtonHeight,
                                                         text=" Send ",
                                                         connect=(lambda: self.setRPMCTRLP_EEPROM(
                                                             self.rpmCTRLPField_spinBox.value())))

        spacer = QSpacerItem(0, row_space, QSizePolicy.Minimum, QSizePolicy.Preferred)
        self.rpmCTRLLayout.addItem(spacer)

        self.rpmCTRLDValue_Label = evtApp_label(self,
                                                layout=self.rpmCTRLLayout,
                                                text="D current value: N/A")

        self.rpmCTRLDValueLayout = QtWidgets.QHBoxLayout(self)
        self.rpmCTRLDValueLayout.setObjectName("rpmCTRLDValueLayout")
        self.rpmCTRLLayout.addLayout(self.rpmCTRLDValueLayout)

        self.rpmCTRLDField_spinBox = evtApp_spinBox_double(self,
                                                           layout=self.rpmCTRLDValueLayout,
                                                           width=150)
        self.rpmCTRLDSend_PushButton = evtApp_pushButton(self,
                                                         layout=self.rpmCTRLDValueLayout,
                                                         width=sendButtonWidth, height=sendButtonHeight,
                                                         text=" Send ",
                                                         connect=(lambda: self.setRPMCTRLD_EEPROM(
                                                             self.rpmCTRLDField_spinBox.value())))

        spacer = QSpacerItem(0, row_space, QSizePolicy.Minimum, QSizePolicy.Preferred)
        self.rpmCTRLLayout.addItem(spacer)

        self.rpmCTRLFFValue_Label = evtApp_label(self,
                                                 layout=self.rpmCTRLLayout,
                                                 text="FF current value: N/A")

        self.rpmCTRLFFValueLayout = QtWidgets.QHBoxLayout(self)
        self.rpmCTRLFFValueLayout.setObjectName("rpmCTRLFFValueLayout")
        self.rpmCTRLLayout.addLayout(self.rpmCTRLFFValueLayout)

        self.rpmCTRLFFField_spinBox = evtApp_spinBox_double(self,
                                                            layout=self.rpmCTRLFFValueLayout,
                                                            width=150)
        self.rpmCTRLFFSend_PushButton = evtApp_pushButton(self,
                                                          layout=self.rpmCTRLFFValueLayout,
                                                          width=sendButtonWidth, height=sendButtonHeight,
                                                          text=" Send ",
                                                          connect=(lambda: self.setRPMCTRLFF_EEPROM(
                                                              self.rpmCTRLFFField_spinBox.value())))

        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.rpmCTRLLayout.addItem(spacerItem)

        # Other Parameters ----------------------------------------------------------------#
        evtApp_HLine(self, self.tabMainLayout)

        # Other settings layout
        self.otherSettingsLayout = QtWidgets.QHBoxLayout(self)
        self.otherSettingsLayout.setObjectName("otherSettingsLayout")
        self.tabMainLayout.addLayout(self.otherSettingsLayout)

        # Clamping
        self.clampingLayout = QtWidgets.QVBoxLayout(self)
        self.clampingLayout.setObjectName("clampingLayout")
        self.otherSettingsLayout.addLayout(self.clampingLayout)

        self.clampingTitle = evtApp_label(self,
                                            fontSize=TEXT_FONT_SIZE_TITLE,
                                            alignment=Qt.AlignHCenter,
                                            text="Clamping Settings",
                                            layout=self.clampingLayout)

        spacer = QSpacerItem(0, row_space, QSizePolicy.Minimum, QSizePolicy.Preferred)
        self.clampingLayout.addItem(spacer)

        self.clampingIncrementsTitle_Label = evtApp_label(self,
                                                layout=self.clampingLayout,
                                                alignment=Qt.AlignCenter,
                                                fontSize=14,
                                                text="Clamping speed Increments")
        self.clampingIncrementsValue_Label = evtApp_label(self,
                                                  layout=self.clampingLayout,
                                                  alignment=Qt.AlignHCenter,
                                                  text="Clamping speed increments current value: N/A")

        self.clampingIncrementsValueLayout = QtWidgets.QHBoxLayout(self)
        self.clampingIncrementsValueLayout.setObjectName("clampingValueLayout")
        self.clampingLayout.addLayout(self.clampingIncrementsValueLayout)

        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.clampingIncrementsValueLayout.addItem(spacerItem)

        self.clampingIncrementsValue_spinBox = evtApp_spinBox_double(self,
                                                             layout=self.clampingIncrementsValueLayout,
                                                             decimals=2,
                                                             maxVal=100,
                                                             width=150)
        self.clampingIncrementsValueSend_PushButton = evtApp_pushButton(self,
                                                           layout=self.clampingIncrementsValueLayout,
                                                           width=sendButtonWidth, height=sendButtonHeight,
                                                           text=" Send ",
                                                           connect=(lambda: self.setClampingSpeedIncrement_EEPROM(
                                                               self.clampingIncrementsValue_spinBox.value())))

        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.clampingIncrementsValueLayout.addItem(spacerItem)

        spacer = QSpacerItem(0, row_space, QSizePolicy.Minimum, QSizePolicy.Preferred)
        self.clampingLayout.addItem(spacer)

        self.clampingSpeedMaximunTitle_Label = evtApp_label(self,
                                                          layout=self.clampingLayout,
                                                          alignment=Qt.AlignCenter,
                                                          fontSize=14,
                                                          text="Clamping Speed Maximum")
        self.clampingSpeedMaximunValue_Label = evtApp_label(self,
                                                          layout=self.clampingLayout,
                                                          alignment=Qt.AlignHCenter,
                                                          text="Clamping speed maximum current value: N/A")

        self.clampingSpeedMaximunValueLayout = QtWidgets.QHBoxLayout(self)
        self.clampingSpeedMaximunValueLayout.setObjectName("clampingSpeedMaximunValueLayout")
        self.clampingLayout.addLayout(self.clampingSpeedMaximunValueLayout)

        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.clampingSpeedMaximunValueLayout.addItem(spacerItem)

        self.clampingSpeedMaximunField_spinBox = evtApp_spinBox_double(self,
                                                           layout=self.clampingSpeedMaximunValueLayout,
                                                           decimals=2,
                                                                       maxVal=100,
                                                           width=150)
        self.clampingSpeedMaximunSend_PushButton = evtApp_pushButton(self,
                                                         layout=self.clampingSpeedMaximunValueLayout,
                                                         width=sendButtonWidth, height=sendButtonHeight,
                                                         text=" Send ",
                                                         connect=(lambda: self.setClampingSpeedMaximum_EEPROM(
                                                             self.clampingSpeedMaximunField_spinBox.value())))

        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.clampingSpeedMaximunValueLayout.addItem(spacerItem)

        # Declamping
        self.declampingLayout = QtWidgets.QVBoxLayout(self)
        self.declampingLayout.setObjectName("declampingLayout")
        self.otherSettingsLayout.addLayout(self.declampingLayout)

        self.declampingTitle = evtApp_label(self,
                                          fontSize=TEXT_FONT_SIZE_TITLE,
                                          alignment=Qt.AlignHCenter,
                                          text="Declamping Settings",
                                          layout=self.declampingLayout)

        spacer = QSpacerItem(0, row_space, QSizePolicy.Minimum, QSizePolicy.Preferred)
        self.declampingLayout.addItem(spacer)

        self.declampingIncrementsTitle_Label = evtApp_label(self,
                                                          layout=self.declampingLayout,
                                                          alignment=Qt.AlignCenter,
                                                          fontSize=14,
                                                          text="Declamping speed Increments")
        self.declampingIncrementsValue_Label = evtApp_label(self,
                                                          layout=self.declampingLayout,
                                                          alignment=Qt.AlignHCenter,
                                                          text="Declamping speed increments current value: N/A")

        self.declampingIncrementsValueLayout = QtWidgets.QHBoxLayout(self)
        self.declampingIncrementsValueLayout.setObjectName("declampingValueLayout")
        self.declampingLayout.addLayout(self.declampingIncrementsValueLayout)

        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.declampingIncrementsValueLayout.addItem(spacerItem)

        self.declampingIncrementsValue_spinBox = evtApp_spinBox_double(self,
                                                                     layout=self.declampingIncrementsValueLayout,
                                                                     decimals=2,
                                                                       maxVal=100,
                                                                     width=150)
        self.declampingIncrementsValueSend_PushButton = evtApp_pushButton(self,
                                                                        layout=self.declampingIncrementsValueLayout,
                                                                        width=sendButtonWidth, height=sendButtonHeight,
                                                                        text=" Send ",
                                                                        connect=(lambda: self.setDeclampingSpeedIncrement_EEPROM(
                                                                            self.declampingIncrementsValue_spinBox.value())))

        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.declampingIncrementsValueLayout.addItem(spacerItem)

        spacer = QSpacerItem(0, row_space, QSizePolicy.Minimum, QSizePolicy.Preferred)
        self.declampingLayout.addItem(spacer)

        self.declampingSpeedMaximunTitle_Label = evtApp_label(self,
                                                            layout=self.declampingLayout,
                                                            alignment=Qt.AlignCenter,
                                                            fontSize=14,
                                                            text="Delamping Speed Maximum")
        self.declampingSpeedMaximunValue_Label = evtApp_label(self,
                                                            layout=self.declampingLayout,
                                                            alignment=Qt.AlignHCenter,
                                                            text="Delamping speed maximum current value: N/A")

        self.declampingSpeedMaximunValueLayout = QtWidgets.QHBoxLayout(self)
        self.declampingSpeedMaximunValueLayout.setObjectName("declampingSpeedMaximunValueLayout")
        self.declampingLayout.addLayout(self.declampingSpeedMaximunValueLayout)

        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.declampingSpeedMaximunValueLayout.addItem(spacerItem)

        self.declampingSpeedMaximunField_spinBox = evtApp_spinBox_double(self,
                                                                       layout=self.declampingSpeedMaximunValueLayout,
                                                                       decimals=2,
                                                                         maxVal=100,
                                                                       width=150)
        self.declampingSpeedMaximunSend_PushButton = evtApp_pushButton(self,
                                                                     layout=self.declampingSpeedMaximunValueLayout,
                                                                     width=sendButtonWidth, height=sendButtonHeight,
                                                                     text=" Send ",
                                                                     connect=(lambda: self.setDeclampingSpeedMaximum_EEPROM(
                                                                         self.declampingSpeedMaximunField_spinBox.value())))

        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.declampingSpeedMaximunValueLayout.addItem(spacerItem)

        # End Spacer ----------------------------------------------------------------#
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.tabMainLayout.addItem(spacerItem)

    @pyqtSlot()
    def refresh_tuning_tab_values(self):
        if self.root.COMConnected:
            self.root.COMPort.EVT_read_EEPROM(const.SHEAVE_CTRL_P_C1_EEPROM_ADDR)
            self.root.COMPort.EVT_read_EEPROM(const.SHEAVE_CTRL_I_C1_EEPROM_ADDR)
            self.root.COMPort.EVT_read_EEPROM(const.SHEAVE_CTRL_D_C1_EEPROM_ADDR)
            self.root.COMPort.EVT_read_EEPROM(const.RPM_CTRL_P_C1_EEPROM_ADDR)
            self.root.COMPort.EVT_read_EEPROM(const.RPM_CTRL_D_C1_EEPROM_ADDR)
            self.root.COMPort.EVT_read_EEPROM(const.RPM_CTRL_FF_C1_EEPROM_ADDR)
            self.root.COMPort.EVT_read_EEPROM(const.DECLAMPING_SPEED_MAXIMUM_C1_EEPROM_ADDR)
            self.root.COMPort.EVT_read_EEPROM(const.DECLAMPING_SPEED_INCREMENT_C1_EEPROM_ADDR)
            self.root.COMPort.EVT_read_EEPROM(const.CLAMPING_SPEED_MAXIMUM_C1_EEPROM_ADDR)
            self.root.COMPort.EVT_read_EEPROM(const.CLAMPING_SPEED_INCREMENT_C1_EEPROM_ADDR)
            self.root.print_status("Values refreshed")
        else:
            self.root.print_status("EVT is not connected.")


    def updateSheaveCTRLP(self, value):
        self.sheavePIDPValue_Label.changeText("P current value: " + str(value / SHEAVE_CTRL_P_MUL))
        self.sheavePIDPField_spinBox.setValue(value / SHEAVE_CTRL_P_MUL)

    def updateSheaveCTRLI(self, value):
        self.sheavePIDIValue_Label.changeText("I current value: " + str(value / SHEAVE_CTRL_I_MUL))
        self.sheavePIDIField_spinBox.setValue(value / SHEAVE_CTRL_I_MUL)

    def updateSheaveCTRLD(self, value):
        self.sheavePIDDValue_Label.changeText("D current value: " + str(value / SHEAVE_CTRL_D_MUL))
        self.sheavePIDDField_spinBox.setValue(value / SHEAVE_CTRL_D_MUL)

    def updateRPMCTRLP(self, value):
        self.rpmCTRLPValue_Label.changeText("P current value: " + str(value / RPM_CTRL_P_MUL))
        self.rpmCTRLPField_spinBox.setValue(value / RPM_CTRL_P_MUL)

    def updateRPMCTRLD(self, value):
        self.rpmCTRLDValue_Label.changeText("D current value: " + str(value / RPM_CTRL_D_MUL))
        self.rpmCTRLDField_spinBox.setValue(value / RPM_CTRL_D_MUL)

    def updateRPMCTRLFF(self, value):
        self.rpmCTRLFFValue_Label.changeText("FF current value: " + str(value / RPM_CTRL_FF_MUL))
        self.rpmCTRLFFField_spinBox.setValue(value / RPM_CTRL_FF_MUL)

    def updateDeclampingSpeedIncrement(self, value):
        self.declampingIncrementsValue_Label.changeText("Declamping speed increments current value: " + str(value / DECLAMPING_INCREMENT_MUL))
        self.declampingIncrementsValue_spinBox.setValue(value / DECLAMPING_INCREMENT_MUL)

    def updateDeclampingSpeedMaximum(self, value):
        self.declampingSpeedMaximunValue_Label.changeText("Delamping speed maximum current value: " + str(value))
        self.declampingSpeedMaximunField_spinBox.setValue(value)

    def updateClampingSpeedIncrement(self, value):
        self.clampingIncrementsValue_Label.changeText("Clamping speed increments current value: " + str(value / CLAMPING_INCREMENT_MUL))
        self.clampingIncrementsValue_spinBox.setValue(value / CLAMPING_INCREMENT_MUL)

    def updateClampingSpeedMaximum(self, value):
        self.clampingSpeedMaximunValue_Label.changeText("Clamping speed maximum current value: " + str(value))
        self.clampingSpeedMaximunField_spinBox.setValue(value)

    @pyqtSlot()
    def setSheaveCTRLP_EEPROM(self, set_value=None):
        if set_value is None:
            return None
        else:
            send_value = int(set_value * SHEAVE_CTRL_P_MUL)

        if(self.root.evt_eeprom.sheave_ctrl_P_C1 is None):
            self.root.print_status("EVT is not connected or local variable not refreshed.")
            return None

        if checklimits(send_value) != "error":
            self.root.evt_eeprom.sheave_ctrl_P_C1 = int(send_value)

            self.updateSheaveCTRLP(send_value)
            self.root.print_status("Sheave CTRL P value set to: " + str(set_value))

            if self.root.COMConnected:
                self.root.COMPort.EVT_write_to_EEPROM(const.SHEAVE_CTRL_P_C1_EEPROM_ADDR,
                                                      int(self.root.evt_eeprom.sheave_ctrl_P_C1))
            else:
                self.root.print_status("EVT is not connected.")
        else:
            self.root.print_status("Value entered out of limits.")

    @pyqtSlot()
    def setSheaveCTRLI_EEPROM(self, set_value=None):
        if set_value is None:
            return None
        else:
            send_value = int(set_value * SHEAVE_CTRL_I_MUL)

        if(self.root.evt_eeprom.sheave_ctrl_I_C1 is None):
            self.root.print_status("EVT is not connected or local variable not refreshed.")
            return None

        if checklimits(send_value) != "error":
            self.root.evt_eeprom.sheave_ctrl_I_C1 = int(send_value)

            self.updateSheaveCTRLI(send_value)
            self.root.print_status("Sheave CTRL I value set to: " + str(set_value))

            if self.root.COMConnected:
                self.root.COMPort.EVT_write_to_EEPROM(const.SHEAVE_CTRL_I_C1_EEPROM_ADDR,
                                                      int(self.root.evt_eeprom.sheave_ctrl_I_C1))
            else:
                self.root.print_status("EVT is not connected.")
        else:
            self.root.print_status("Value entered out of limits.")

    @pyqtSlot()
    def setSheaveCTRLD_EEPROM(self, set_value=None):
        if set_value is None:
            return None
        else:
            send_value = int(set_value * SHEAVE_CTRL_D_MUL)

        if(self.root.evt_eeprom.sheave_ctrl_D_C1 is None):
            self.root.print_status("EVT is not connected or local variable not refreshed.")
            return None

        if checklimits(send_value) != "error":
            self.root.evt_eeprom.sheave_ctrl_D_C1 = int(send_value)

            self.updateSheaveCTRLD(send_value)
            self.root.print_status("Sheave CTRL D value set to: " + str(set_value))

            if self.root.COMConnected:
                self.root.COMPort.EVT_write_to_EEPROM(const.SHEAVE_CTRL_D_C1_EEPROM_ADDR,
                                                      int(self.root.evt_eeprom.sheave_ctrl_D_C1))
            else:
                self.root.print_status("EVT is not connected.")
        else:
            self.root.print_status("Value entered out of limits.")

    @pyqtSlot()
    def setRPMCTRLP_EEPROM(self, set_value=None):
        if set_value is None:
            return None
        else:
            send_value = int(set_value * RPM_CTRL_P_MUL)

        if(self.root.evt_eeprom.rpm_ctrl_P_C1 is None):
            self.root.print_status("EVT is not connected or local variable not refreshed.")
            return None

        if checklimits(send_value) != "error":
            self.root.evt_eeprom.rpm_ctrl_P_C1 = int(send_value)

            self.updateRPMCTRLP(send_value)
            self.root.print_status("RPM CTRL P value set to: " + str(set_value))

            if self.root.COMConnected:
                self.root.COMPort.EVT_write_to_EEPROM(const.RPM_CTRL_P_C1_EEPROM_ADDR,
                                                      int(self.root.evt_eeprom.rpm_ctrl_P_C1))
            else:
                self.root.print_status("EVT is not connected.")
        else:
            self.root.print_status("Value entered out of limits.")

    @pyqtSlot()
    def setRPMCTRLD_EEPROM(self, set_value=None):
        if set_value is None:
            return None
        else:
            send_value = int(set_value * RPM_CTRL_D_MUL)

        if (self.root.evt_eeprom.rpm_ctrl_D_C1 is None):
            self.root.print_status("EVT is not connected or local variable not refreshed.")
            return None

        if checklimits(send_value) != "error":
            self.root.evt_eeprom.rpm_ctrl_D_C1 = int(send_value)

            self.updateRPMCTRLD(send_value)
            self.root.print_status("RPM CTRL P value set to: " + str(set_value))

            if self.root.COMConnected:
                self.root.COMPort.EVT_write_to_EEPROM(const.RPM_CTRL_D_C1_EEPROM_ADDR,
                                                      int(self.root.evt_eeprom.rpm_ctrl_D_C1))
            else:
                self.root.print_status("EVT is not connected.")
        else:
            self.root.print_status("Value entered out of limits.")

    @pyqtSlot()
    def setRPMCTRLFF_EEPROM(self, set_value=None):
        if set_value is None:
            return None
        else:
            send_value = int(set_value * RPM_CTRL_FF_MUL)

        if (self.root.evt_eeprom.rpm_ctrl_FF_C1 is None):
            self.root.print_status("EVT is not connected or local variable not refreshed.")
            return None

        if checklimits(send_value) != "error":
            self.root.evt_eeprom.rpm_ctrl_FF_C1 = int(send_value)

            self.updateRPMCTRLFF(send_value)
            self.root.print_status("RPM CTRL FF value set to: " + str(set_value))

            if self.root.COMConnected:
                self.root.COMPort.EVT_write_to_EEPROM(const.RPM_CTRL_FF_C1_EEPROM_ADDR,
                                                      int(self.root.evt_eeprom.rpm_ctrl_FF_C1))
            else:
                self.root.print_status("EVT is not connected.")
        else:
            self.root.print_status("Value entered out of limits.")

    @pyqtSlot()
    def setDeclampingSpeedIncrement_EEPROM(self, set_value=None):
        if set_value is None:
            return None
        else:
            send_value = int(set_value * DECLAMPING_INCREMENT_MUL)

        if (self.root.evt_eeprom.declamping_speed_increment_C1 is None):
            self.root.print_status("EVT is not connected or local variable not refreshed.")
            return None

        if checklimits(send_value) != "error":
            self.root.evt_eeprom.declamping_speed_increment_C1 = int(send_value)

            self.updateDeclampingSpeedIncrement(send_value)
            self.root.print_status("Declamping speed increment value set to: " + str(set_value))

            if self.root.COMConnected:
                self.root.COMPort.EVT_write_to_EEPROM(const.DECLAMPING_SPEED_INCREMENT_C1_EEPROM_ADDR,
                                                      int(self.root.evt_eeprom.declamping_speed_increment_C1))
            else:
                self.root.print_status("EVT is not connected.")
        else:
            self.root.print_status("Value entered out of limits.")

    @pyqtSlot()
    def setDeclampingSpeedMaximum_EEPROM(self, set_value=None):
        if set_value is None:
            return None
        else:
            send_value = int(set_value * DECLAMPING_MAX_MUL)

        if (self.root.evt_eeprom.declamping_speed_maximum_C1 is None):
            self.root.print_status("EVT is not connected or local variable not refreshed.")
            return None

        if checklimits(send_value) != "error":
            self.root.evt_eeprom.declamping_speed_maximum_C1 = int(send_value)

            self.updateDeclampingSpeedMaximum(send_value)
            self.root.print_status("Declamping speed maximum value set to: " + str(set_value))

            if self.root.COMConnected:
                self.root.COMPort.EVT_write_to_EEPROM(const.DECLAMPING_SPEED_MAXIMUM_C1_EEPROM_ADDR,
                                                      int(self.root.evt_eeprom.declamping_speed_maximum_C1))
            else:
                self.root.print_status("EVT is not connected.")
        else:
            self.root.print_status("Value entered out of limits.")

    @pyqtSlot()
    def setClampingSpeedIncrement_EEPROM(self, set_value=None):
        if set_value is None:
            return None
        else:
            send_value = int(set_value * CLAMPING_INCREMENT_MUL)

        if (self.root.evt_eeprom.clamping_speed_increment_C1 is None):
            self.root.print_status("EVT is not connected or local variable not refreshed.")
            return None

        if checklimits(send_value) != "error":
            self.root.evt_eeprom.clamping_speed_increment_C1 = int(send_value)

            self.updateClampingSpeedIncrement(send_value)
            self.root.print_status("Clamping speed increment value set to: " + str(set_value))

            if self.root.COMConnected:
                self.root.COMPort.EVT_write_to_EEPROM(const.CLAMPING_SPEED_INCREMENT_C1_EEPROM_ADDR,
                                                      int(self.root.evt_eeprom.clamping_speed_increment_C1))
            else:
                self.root.print_status("EVT is not connected.")
        else:
            self.root.print_status("Value entered out of limits.")

    @pyqtSlot()
    def setClampingSpeedMaximum_EEPROM(self, set_value=None):
        if set_value is None:
            return None
        else:
            send_value = int(set_value * CLAMPING_MAX_MUL)

        if (self.root.evt_eeprom.clamping_speed_maximum_C1 is None):
            self.root.print_status("EVT is not connected or local variable not refreshed.")
            return None

        if checklimits(send_value) != "error":
            self.root.evt_eeprom.clamping_speed_maximum_C1 = int(send_value)

            self.updateClampingSpeedMaximum(send_value)
            self.root.print_status("Clamping speed maximum value set to: " + str(set_value))

            if self.root.COMConnected:
                self.root.COMPort.EVT_write_to_EEPROM(const.CLAMPING_SPEED_MAXIMUM_C1_EEPROM_ADDR,
                                                      int(self.root.evt_eeprom.clamping_speed_maximum_C1))
            else:
                self.root.print_status("EVT is not connected.")
        else:
            self.root.print_status("Value entered out of limits.")

class LORADebuggingTab(LORAApp_tab):

    def __init__(self, root):
        super(LORADebuggingTab, self).__init__(root.MainTabs, name=" Debug ")
        self.setObjectName("EVT_debugging_tab")
        self.root = root

        self.tabMainLayout = QtWidgets.QVBoxLayout(self)
        self.tabMainLayout.setObjectName("tabMainLayout")
        self.tabMainLayout.setContentsMargins(15, 10, 15, 15)

        evtApp_HLine(self, self.tabMainLayout)

        self.debuggingLevelLayout = QtWidgets.QHBoxLayout(self)
        self.debuggingLevelLayout.setObjectName("debuggingLevelLayout")
        self.debuggingLevelLayout.setAlignment(Qt.AlignLeft)
        self.tabMainLayout.addLayout(self.debuggingLevelLayout)

        self.debuggingLevel_Label = evtApp_label(self,
                                                 fontSize=15,
                                                 text="Debugging Level: ",
                                                 layout=self.debuggingLevelLayout)
        self.debuggingLevel0_PushButton = evtApp_pushButton(self,
                                                            fontSize=12,
                                                            width=100, height=30,
                                                            text=" Rien ",
                                                            connect=(lambda: self.setDebuggingLevel(0)),
                                                            layout=self.debuggingLevelLayout)
        self.debuggingLevel1_PushButton = evtApp_pushButton(self,
                                                            fontSize=12,
                                                            width=100, height=30,
                                                            text=" Base ",
                                                            connect=(lambda: self.setDebuggingLevel(1)),
                                                            layout=self.debuggingLevelLayout)
        self.debuggingLevel2_PushButton = evtApp_pushButton(self,
                                                            fontSize=12,
                                                            width=100, height=30,
                                                            text=" Tout ",
                                                            connect=(lambda: self.setDebuggingLevel(2)),
                                                            layout=self.debuggingLevelLayout)

        spacerItem = QtWidgets.QSpacerItem(0, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.tabMainLayout.addItem(spacerItem)
        evtApp_HLine(self, self.tabMainLayout)

        self.directCOMLayout = QtWidgets.QGridLayout(self)
        self.directCOMLayout.setObjectName("directCOMLayout")
        self.directCOMLayout.setContentsMargins(0, 0, 0, 0)
        self.tabMainLayout.addLayout(self.directCOMLayout)

        self.directCOM_Label = evtApp_label(self,
                                            fontSize=15,
                                            text="Direct Communication with EVT: ")
        self.directCOMLayout.addWidget(self.directCOM_Label, 0, 0, Qt.AlignRight)

        # Write Section
        self.writeAddress_spinBox = evtApp_spinBox(self)
        self.directCOMLayout.addWidget(self.writeAddress_spinBox, 0, 1, Qt.AlignHCenter)
        self.writeValue_spinBox = evtApp_spinBox(self)
        self.directCOMLayout.addWidget(self.writeValue_spinBox, 0, 2, Qt.AlignHCenter)
        self.write_PushButton = evtApp_pushButton(self,
                                                  fontSize=12,
                                                  width=100, height=30,
                                                  text=" Write ",
                                                  connect=(lambda: self.writeEEPROM()))
        self.directCOMLayout.addWidget(self.write_PushButton, 0, 3, Qt.AlignHCenter)

        # Read Section
        self.readAddress_spinBox = evtApp_spinBox(self)
        self.directCOMLayout.addWidget(self.readAddress_spinBox, 1, 1, Qt.AlignHCenter)
        self.readValue_Label = evtApp_label(self,
                                            text="Value: ",
                                            fontSize=10)
        self.directCOMLayout.addWidget(self.readValue_Label, 1, 2, Qt.AlignCenter)
        self.read_PushButton = evtApp_pushButton(self,
                                                 fontSize=12,
                                                 width=100, height=30,
                                                 text=" Read ",
                                                 connect=(lambda: self.readEEPROM()))
        self.directCOMLayout.addWidget(self.read_PushButton, 1, 3, Qt.AlignHCenter)

        spacerItem = QtWidgets.QSpacerItem(0, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.tabMainLayout.addItem(spacerItem)

        evtApp_HLine(self, self.tabMainLayout)

        # End filler
        evtApp_HSpacer(self.tabMainLayout)

    @pyqtSlot()
    def writeEEPROM(self):
        self.root.COMPort.EVT_write_to_EEPROM(self.writeAddress_spinBox.text(),
                                              self.writeValue_spinBox.text())

    @pyqtSlot()
    def readEEPROM(self):
        temp = self.readAddress_spinBox.text()
        self.root.COMPort.EVT_read_EEPROM(temp)

    @pyqtSlot()
    def setDebuggingLevel(self, set_value):
        send_value = int(set_value)

        if checklimits(send_value) != "error":
            if self.root.COMConnected:
                self.root.evt_eeprom.debugging_lvl = send_value
                self.updateDebuggingLevel(send_value)
                self.root.EVTStatusTab.updateDebuggingLevel(send_value)
                self.root.COMPort.EVT_write_to_EEPROM(const.DEBUGGING_LVL_EEPROM_ADDR,
                                                      int(self.root.evt_eeprom.debugging_lvl))
            else:
                self.root.print_status("EVT is not connected.")

        else:
            self.root.print_status("Value entered out of limits.")

    def updateDebuggingLevel(self, level):
        if level == 0:
            self.debuggingLevel0_PushButton.setStyleSheet(pushButtonSelectedStyleSheetString)
            self.debuggingLevel1_PushButton.setStyleSheet(pushButtonStyleSheetString)
            self.debuggingLevel2_PushButton.setStyleSheet(pushButtonStyleSheetString)
        elif level == 1:
            self.debuggingLevel0_PushButton.setStyleSheet(pushButtonStyleSheetString)
            self.debuggingLevel1_PushButton.setStyleSheet(pushButtonSelectedStyleSheetString)
            self.debuggingLevel2_PushButton.setStyleSheet(pushButtonStyleSheetString)
        elif level == 2:
            self.debuggingLevel0_PushButton.setStyleSheet(pushButtonStyleSheetString)
            self.debuggingLevel1_PushButton.setStyleSheet(pushButtonStyleSheetString)
            self.debuggingLevel2_PushButton.setStyleSheet(pushButtonSelectedStyleSheetString)
        else:
            self.debuggingLevel0_PushButton.setStyleSheet(pushButtonStyleSheetString)
            self.debuggingLevel1_PushButton.setStyleSheet(pushButtonStyleSheetString)
            self.debuggingLevel2_PushButton.setStyleSheet(pushButtonStyleSheetString)


class SettingsTab(LORAApp_tab):

    def __init__(self, parent):
        super(SettingsTab, self).__init__(parent, name=" Settings ")
        self.setObjectName("EVT_settings_tab")
        self.parent = parent

        # add rotation increment setting for trumpet
"""