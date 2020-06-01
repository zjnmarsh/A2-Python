import csv


"""
with open('trains.csv','r') as file:
    data = csv.reader(file)
    for row in data:
        #print(f"{row}, name: {row[0]}, weight: {row[1]}")
        print(f"{row}")
"""

"""
with open('trains.csv','r') as file:
    data = csv.DictReader(file)
    for row in data:
        print(row['Engine_name'])
"""

with open('trains.csv','r') as file:
    writer = csv.writer(file, dialect='excel', delimiter='')
    writer.writerow(['Engine_name','weight','colour'])
    for e in getEngineList():
        writer.writerow([e.name, e.weight, e.colour])
