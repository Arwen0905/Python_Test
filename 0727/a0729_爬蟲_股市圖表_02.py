import requests
import json,csv
import pandas as pd
import os
import time

def twodigit(n):
    if(n<10):
        retstr = '0' +str(n)
    else:
        retstr = str(n)
    return retstr

def convertDate(date):
    str1 = str(date)
    yearst = str1[:3] #取出民國年
    realyear = str(int(yearst)+1911) #轉為西元年
    realdate = realyear + str1[4:6] + str1[7:9]
    return realdate

pd.options.mode.chained_assignment = None

filepath = "stockmonth01.csv"

urlbase = "http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20180"
urltail = "01&stockNo=2633&_=1595925201119" 
filepath = "storkyear2017.csv"

if not os.path.isfile(filepath):
    for i in range(1,13):
        url_twse = urlbase + twodigit(i) + urltail
        res = requests.get(url_twse)
        jdata = json.loads(res.text)
        
        outputfile = open(filepath, 'a',newline='',encoding='utf-8')
        outputwriter = csv.writer(outputfile)
        if i == 1:
            outputwriter.writerow(jdata['fields'])        
        for dataline in (jdata['data']):
            outputwriter.writerow(dataline)
        time.sleep(0.5)
    outputfile.close()

pdstock = pd.read_csv(filepath, encoding='utf-8')
for i in range(len(pdstock['日期'])):
    pdstock['日期'][i] = convertDate(pdstock['日期'][i])
pdstock['日期'] = pd.to_datetime(pdstock['日期'])
pdstock.plot(kind='line', figsize=(12,6), x='日期', y=['收盤價','最低價','最高價'])
