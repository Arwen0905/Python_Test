import csv #載入csv套件
with open('stock.csv','r') as fin:
    #以讀取模式開啟檔案stock.csv並設定為變數fin
    with open('stock_out.csv','w') as fout:
        #以寫入模式開啟檔案stock_out.csv，若檔案不存在則建立，並設定為變數out
        csvReader = csv.reader(fin, delimiter=',') #將讀取方法設定給 csvReader變數
        #以csv套件的reader方法將檔案fin讀入並設定給變數csvReader(為一個讀取物件)
        csvWrite = csv.writer(fout, delimiter=',') #將寫入方法設定給 csvWrite變數
        #以csv套件的writer方法將寫入檔案fout並設定給變數csvWriter(為一個寫入物件)
        header = next(csvReader) #取得"標頭" ※讀取資料的表頭設定給變數header
        print(header) #輸出表頭，檢視看看

        csvWrite.writerow(header)
        #將表頭寫入檔案
        for row in csvReader: #以迴圈逐行讀取資料
            row[6]=row[6].replace('/', '-') #將每一行日期字串中的 / 改為 -
            print(','.join(row)) #使用join()方法將字串合併並印出
            csvWrite.writerow(row) #以寫入物件利用 writerow()方法將每列資料寫入
