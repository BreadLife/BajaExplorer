#check if bytes are signed or not

def interpreter(Data):
    Reception = float(len(Data)*100/57)

    print("Raw Data :" + str(Data))

    Data = str(Data)
    Data = Data.split(" ")
    bData = 0

    if Data[0] == "b'radio_rx":
        Data.pop(0)
        Data = ''.join(map(str, Data))
        Data = Data.replace("\\r\\n'", "")
        Data = ''.join(map(str, Data))
        bData = bytearray(Data, 'utf-8')

        for i in range(len(Data)*2-58):
            if i%3==0:
                Data = Data[:i] + '.' + Data[i:]
                print(Data)

        Data = Data.split('.')

    print("Data :" + str(Data))
    print("Data_b :" + str(bData))

    return Data
"""

    print("lenght: " + str(len(Data)))
    print("0: " + str(Data[0]))
    print("1: " + str(Data[1]))
    print("2: " + str(Data[2]))
    print("3: " + str(Data[3]))
    
    global frameCounterByte
    global tpm
    global speed
    global runTime
    global rpm
    global oilTemp
    global boardTemp
    global actPos
    global actCmd
    global actDc
    global actRot
    global rpmCmd
    global volt

    frameCounterByte =  int.from_bytes(Data[0:1]  , byteorder='big')
    runTime =           int.from_bytes(Data[2:4]  , byteorder='big')
    speed =             int.from_bytes(Data[5:6]  , byteorder='big')
    tpm =               int.from_bytes(Data[8:11] , byteorder='big')
    rpm =               int.from_bytes(Data[13:16], byteorder='big')
    oilTemp =           int.from_bytes(Data[18:21], byteorder='big')
    boardTemp =         int.from_bytes(Data[23:26], byteorder='big')
    actPos =            int.from_bytes(Data[28:31], byteorder='big')
    actCmd =            int.from_bytes(Data[33:36], byteorder='big')
    actDc =             int.from_bytes(Data[38:41], byteorder='big')
    actRot =            int.from_bytes(Data[43:46], byteorder='big')
    rpmCmd =            int.from_bytes(Data[48:51], byteorder='big')
    volt =              int.from_bytes(Data[53:56], byteorder='big')

    print("frame: " + str(frameCounterByte))
    print("speed: " + str(speed))
    print("volt: " + str(volt))
"""

