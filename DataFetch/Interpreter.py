
#check if bytes are signed or not

def interpreter(Data):
    Reception = float(len(Data)*100/57)

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

    return Reception