import csv
with open('air.csv','r',encoding="utf8") as airFile:
    see = csv.reader(airFile,delimiter=',')
    for row in see:
        print(row[0]+" "+row[1]+" "+row[2]+" "+row[3])
        