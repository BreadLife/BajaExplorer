from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtSerialPort import QSerialPort
import queue as Queue
import serial, time
from constants import *
from struct import *

SER_TIMEOUT = 0.1                   # Timeout for serial Rx
CONNECTED_TO_EVT = True

COMMAND_START_BYTE = 0xAF

txq = Queue.Queue()
rxq = Queue.Queue()

# Convert bytes to string (if Python 3)
def bytes_str(d):
    return d if type(d) is str else "".join([chr(b) for b in d])


class SerialThread(QtCore.QThread):
    RX_Update = QtCore.pyqtSignal()
    TX_Update = QtCore.pyqtSignal()

    def __init__(self, portname, baudrate):  # Initialise with serial port details
        QtCore.QThread.__init__(self)
        self.portname = portname #'COM4'
        self.baudrate = baudrate #57600

        self.running = True

    def ser_out(self, s):  # Write outgoing data to serial port if open
        txq.put(s)  # ..using a queue to sync with reader thread

    def ser_in(self, s):  # Write incoming serial data to screen
        rxq.put(s)
        self.RX_Update.emit()

    def get_message(self):
        return self.rxq.get()

    def run(self):  # Run serial reader thread
        print("Opening %s at %u baud" % (self.portname, self.baudrate))

        try:
            self.ser = serial.Serial(self.portname, self.baudrate, timeout=SER_TIMEOUT,
                                     bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE,
                                     stopbits=serial.STOPBITS_ONE)
            time.sleep(SER_TIMEOUT * 1.2)
            self.ser.flushInput()
        except:
            self.ser = None

        if not self.ser:
            print("Can't open port")
            self.running = False
        while self.running:
            s = self.ser.read(5)
            if s:  # Get data from serial port
                self.ser_in(s)  # ..and convert to string
            if not txq.empty():
                message = txq.get()
                #print(message)
                self.ser.write(message) # If Tx data in queue, write to serial port
        if self.ser:  # Close serial port when thread finished
            self.ser.close()
            self.ser = None

class evt_com_port(SerialThread, QObject):

    def __init__(self):
        super().__init__('COM5', 57600)

    @pyqtSlot()
    def EVT_connect(self, portname):

        self.portname = portname

        self.start()
        time.sleep(0.5)
        if self.running:
            return self.portname
        else:
            return None

    # @pyqtSlot()
    # def EVT_read(self, COMPort, Address):
    #     inputAddress = int(Address)
    #     opcode = 2
    #
    #     message = opcode.to_bytes(1, 'big', signed=False) \
    #               + inputAddress.to_bytes(1, 'big', signed=False)
    #
    #     COMPort.write(message)
    #     returned_value = COMPort.read()
    #
    #     TreatValue(Address, returned_value)

    @pyqtSlot()
    def EVT_write(self, OpCode, Address, Value):
        commandStart = COMMAND_START_BYTE
        inputOpCode = int(OpCode)
        inputAddress = int(Address)
        inputValue = int(Value)

        message = commandStart.to_bytes(1, 'big', signed=False) \
                  + inputOpCode.to_bytes(1, 'big', signed=False) \
                  + inputAddress.to_bytes(1, 'big', signed=False) \
                  + inputValue.to_bytes(2, 'big', signed=False)

        #print(message)

        if CONNECTED_TO_EVT:
            txq.put(message)

    @pyqtSlot()
    def EVT_write_to_EEPROM(self, Address, Value):
        commandStart = int(COMMAND_START_BYTE)
        inputOpCode = int(OPCODE_WRITE_EEPROM)
        inputAddress = int(Address)
        inputValue = int(Value)

        message = commandStart.to_bytes(1, 'big', signed=False) \
                  + inputOpCode.to_bytes(1, 'big', signed=False) \
                  + inputAddress.to_bytes(1, 'big', signed=False) \
                  + inputValue.to_bytes(2, 'big', signed=False)

        #message = pack('BBBH', commandStart, inputOpCode, inputAddress, inputValue)

        print(message)

        if CONNECTED_TO_EVT:
            self.ser_out(message)

    @pyqtSlot()
    def EVT_read_EEPROM(self, Address):
        commandStart = COMMAND_START_BYTE
        inputOpCode = int(OPCODE_READ_EEPROM)
        inputAddress = int(Address)
        inputValue = int(0)

        message = commandStart.to_bytes(1, 'big', signed=False) \
                  + inputOpCode.to_bytes(1, 'big', signed=False) \
                  + inputAddress.to_bytes(1, 'big', signed=False) \
                  + inputValue.to_bytes(2, 'big', signed=False)

        print(message)

        if CONNECTED_TO_EVT:
            self.ser_out(message)

#Archive
class SerPort:

    def __init__(self, port):
        self.port = serial.Serial(port, 57600, bytesize=serial.EIGHTBITS, timeout=5, parity=serial.PARITY_NONE,
                                  stopbits=serial.STOPBITS_ONE)

    def read(self):
        msg = self.port.readline(2)
        value = int.from_bytes(msg, byteorder='big', signed=False)
        return value

    def write(self, input):
        self.port.write(input)

