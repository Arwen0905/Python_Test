import csv
with open('../0604/全國細懸浮微粒手動監測資料.csv',encoding="utf8") as fin:
    f = csv.reader(fin, delimiter=",")
    for i in f:
        print(i)
        
import xml.etree.ElementTree as ET
tree = ET.ElementTree()
root = tree.getroot()
for i in root.find_all('fata'):
    print(i)

    