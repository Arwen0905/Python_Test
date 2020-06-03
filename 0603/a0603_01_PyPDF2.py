from PyPDF2 import PdfFileReader, PdfFileWriter
# 此範例可定義為: 文件檔的分割

readFile = r'C:\Users\ASUS\Documents\GitHub\Python_Test\0603\health.pdf'
#設定!檔案來源為 readFile 變數
PdfFileReader = PdfFileReader(readFile,strict=False)
#讀取!檔案並設定給 pdfFileReader 變數

documentInfo = PdfFileReader.getDocumentInfo()
#取得!檔案資訊並設定給 documentInfo 變數

outFile = r'C:\Users\ASUS\Documents\GitHub\Python_Test\0603\health_cut.pdf'
#設定輸出檔案名稱為 outFile 變數

PdfFileWriter = PdfFileWriter()
#將檔案寫入方法設定給 pdfFileWriter 變數

numPages = PdfFileReader.getNumPages()
#讀取檔案頁數並設定給 numPages 變數

if numPages>3: #若是頁數大於 3 
    for index in range(3,numPages):
        #則將頁數帶入迴圈，從3開始到最後的頁數
        pageObj = PdfFileReader.getPage(index)
        #以迴圈每一圈的index值取得該頁並設定給pageObj變數
        PdfFileWriter.addPage(pageObj)
        #將取得的頁面加入
    PdfFileWriter.write(open(outFile,'wb'))
    #將所有加入的頁面寫入輸出檔案
