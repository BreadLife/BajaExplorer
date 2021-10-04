import time

lat = 45.493431
long = -73.563312

def GPS_Rando():
    global lat
    global long

    lat = lat + 0.000001
    long = long

    time.sleep(0.1)

    return lat, long