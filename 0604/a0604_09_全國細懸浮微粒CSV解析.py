import csv
with open('全國細懸浮微粒手動監測資料.csv','r',encoding="utf8") as fin:
    see = csv.reader(fin,delimiter=',')
    for row in see:
        print('測站:(%s)--縣市 (%s)--PM2.5 = %s'%(row[0],row[2],row[3]))