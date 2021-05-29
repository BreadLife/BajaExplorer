import csv
import random

#valeurs random
rpm = random.randint(0,10)
speed = random.randint(0,10)
time = random.randint(0,10)

def ecriture():
    # valeurs random
    rpm = random.randint(0, 10)
    speed = random.randint(0, 10)
    time = random.randint(0, 10)

    with open('FakeData.csv', mode='w') as csv_file:
        line = 0
        spamwriter = csv.writer(csv_file, delimiter=',')
        for line in range(1,11):
            if (line==1):
                spamwriter.writerow(["temps"]+["rpm"]+["speed"])
            elif(line>1):
                spamwriter.writerow([time+line]+[rpm+line]+[speed+line])
    return("rpm", "speed", "time")
ecriture()