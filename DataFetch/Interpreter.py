#check if bytes are signed or not



def interpreter(Data):
    #Reception = float(len(Data)*100/57)

    print("Raw Data :" + str(Data))

    Data = str(Data)
    Data = Data.split(" ")

    if Data[0] == "b'radio_rx":
        Data.pop(0)
        Data = ''.join(map(str, Data))
        Data = Data.replace("\\r\\n'", "")
        Data = ''.join(map(str, Data))

        for i in range(len(Data)*2-58):
            if i%3==0:
                Data = Data[:i] + '.' + Data[i:]

        Data = Data.split('.')
        Data.pop(0)

    return Data

def assignation(Data):

    global frameCounterByte
    global runTime
    global speed
    global tpm
    global rpm
    global oilTemp
    global boardTemp
    global actPos
    global actCmd
    global actDc
    global actRot
    global rpmCmd
    global volt

    frameCounterByte =  int(Data[0], base=16)
    runTime =           int(Data[1], base=16)
    speed =             int(Data[2], base=16)
    tpm =               int(Data[3] + Data[4], base=16)
    rpm =               int(Data[5] + Data[6], base=16)
    oilTemp =           int(Data[7] + Data[8], base=16)
    boardTemp =         int(Data[9] + Data[10], base=16)
    actPos =            int(Data[11] + Data[12], base=16)
    actCmd =            int(Data[13] + Data[14], base=16)
    actDc =             int(Data[15] + Data[16], base=16)
    actRot =            int(Data[17] + Data[18], base=16)
    rpmCmd =            int(Data[19] + Data[20], base=16)
    volt =              int(Data[21] + Data[22], base=16)

    return frameCounterByte, runTime, speed, tpm, rpm, oilTemp, boardTemp, actPos, actCmd, actDc, actRot, rpmCmd, volt

