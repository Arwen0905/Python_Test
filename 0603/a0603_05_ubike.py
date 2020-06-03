import csv #載入內建套件
with open('ubike_1.csv','r',encoding="utf8") as csvFile:
    #以 with讀取模式開啟並設定給 csvFile變數 ※老師補充: encoding需要設定比較保險
    plots = csv.reader(csvFile,delimiter=',')
    #以reader(方法)讀取CSV檔案，每一列資料以delimiter設定資料的分隔字元，藉以取出每一個資料
    for row in plots: #以讀取的plots資料做為迴圈依據
        print(row[0]+" "+row[1]+" "+row[3]+" "+row[5]+" "+row[12])
        #每一個欄位(row)以索引取出該欄位資料
        