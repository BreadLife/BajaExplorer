data = [0,0]
bytearray(data)

def cake(cok):
    global dik
    dik = int.from_bytes(data, byteorder='big', signed='False')
    print(dik)

cake(data)

