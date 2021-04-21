import serial


def Serial_get():
    with serial.Serial('COM15', 9600, timeout=1) as ser:
        while (1):
            x = ser.read(1)  # read one byte
            print(x)

Serial_get()