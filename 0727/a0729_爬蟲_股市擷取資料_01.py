import requests
import json,csv
import pandas as pd
import os

pd.options.mode.chained_assignment = None

filepath = "stockmonth01.csv"

if not os.path.isfile(filepath):
    url_twse = "http://www.twse.com.tw/exchangeReport/\
        STOCK_DAY?response=json&date=20190101&stockNo=2633&_=1595925201119"
    
    res = requests.get(url_twse)
    jdata = json.loads(res.text)
    
    outputfile = open(filepath, 'w',newline='',encoding='utf-8')
    outputwriter = csv.writer(outputfile)
    outputwriter.writerow(jdata['fields'])
    for dataline in (jdata['data']):
        outputwriter.writerow(dataline)
    outputfile.close()
    
def convertDate(data):
    str1 = str(data)
    yearst = str1[:3] #取出民國年
    ryear = str(int(yearst)+1911) #轉為西元年
    findata = ryear + str1[4:6] + str1[7:9]
    return findata
pdstock = pd.read_csv(filepath, encoding='utf-8')
for i in range(len(pdstock['日期'])):
    pdstock['日期'][i] = convertDate(pdstock['日期'][i])
pdstock['日期'] = pd.to_datetime(pdstock['日期'])
pdstock.plot(kind='line', figsize=(12,6), x='日期', y=['收盤價','最低價','最高價'])
