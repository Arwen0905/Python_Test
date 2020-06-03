import PyPDF2
pdfFiles = ['out1.pdf',
            'out2.pdf',
            'out3.pdf']
#設定要讀取的複數pdf文件
pdfWriter = PyPDF2.PdfFileWriter()
#將 PyPDF2的寫入方法設定給 pdfWriter變數
pdfoutput = open('comb.pdf','wb')
#以寫入模式開啟該檔案，若不存在則建立資料，設定給 pdfoutput變數(欲輸出檔案)

for fileName in pdfFiles: #以複數文件資料的 pdfFiles變數進行迴圈處理
    #以"檔案名稱"做為迴圈的執行參數fileName，所以必須要用挖元素的方式做迴圈
    pdfReader = PyPDF2.PdfFileReader(open(fileName,'rb'))
    #以讀取模式開啟每一筆文件，並設定給 pdfReader變數
    for pageNum in range(pdfReader.numPages):
        #將第一圈取得的檔案名稱的"頁數"做巢狀迴圈執行的次數
        print(pdfReader.getPage(pageNum))
        #輸出讀取到的資料
        pdfWriter.addPage(pdfReader.getPage(pageNum))
        # 取得的每筆資料(頁數)加入，儲存至 pdfWriter變數
pdfWriter.write(pdfoutput)
#將儲存至變數的全部資料一次寫入至 pdfWriter變數
pdfoutput.close()
#關閉寫入後的檔案