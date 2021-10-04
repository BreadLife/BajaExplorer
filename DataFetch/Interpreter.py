#check if bytes are signed or not
Hour = 0
Minute = 0
Second = 0
Latitude_int = 0
Latitude_frac = 0
longitude_int = 0
longitude_frac = 0


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

def decoder_gps_data(entier, fraction):
    entier = int(entier, base=16)
    fraction = int(fraction, base=16)

    nombre = -(((entier & 0x80) | (entier & 0x7f)) + (1 - 1 / fraction))

    print(nombre)

    return nombre

def assignation(Data):


    global canData1
    global canData2
    global canData3
    global canData4
    global canData5
    global canData6

    global Hour
    global Minute
    global Second
    global Latitude_int
    global Latitude_frac
    global longitude_int
    global longitude_frac

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

    Hour = int(Data[2], base=16)
    Minute = int(Data[3], base=16)
    Second = int(Data[4], base=16)
    Latitude_int = int(Data[5], base=16)
    Latitude_frac = int(Data[9] + Data[8] + Data[7] + Data[6], base=16)
    longitude_int = int(Data[10], base=16)
    Latitude_frac = int(Data[14] + Data[13] + Data[12] + Data[11], base=16)

    speed = int(Data[16] + Data[15], base=16)

    canData1 = int(Data[20], base=16)
    canData2 = int(Data[21], base=16)
    canData3 = int(Data[22], base=16)
    canData4 = int(Data[23], base=16)
    canData5 = int(Data[24], base=16)
    canData6 = int(Data[25], base=16)


    #frameCounterByte =  int(Data[0], base=16)
    #runTime =           int(Data[1], base=16)
    #speed =             int(Data[2], base=16)
    #tpm =               int(Data[3] + Data[4], base=16)
    #rpm =               int(Data[5] + Data[6], base=16)
    #oilTemp =           int(Data[7] + Data[8], base=16)
    #boardTemp =         int(Data[9] + Data[10], base=16)
    #actPos =            int(Data[11] + Data[12], base=16)
    #actCmd =            int(Data[13] + Data[14], base=16)
    #actDc =             int(Data[15] + Data[16], base=16)
    #actRot =            int(Data[17] + Data[18], base=16)
    #rpmCmd =            int(Data[19] + Data[20], base=16)
    #volt =              int(Data[21] + Data[22], base=16)

    return Hour, Minute, Second, Latitude_int, Latitude_frac, longitude_int, longitude_frac, canData1, canData2, canData3, canData4, canData5, canData6
