import csv

def convertisseur:
    data = []
    with open('FakeData.csv', mode='r') as csv_file:
        reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)  # change contents to floats
        for row in reader:  # each row is a list
            results.append(row)
