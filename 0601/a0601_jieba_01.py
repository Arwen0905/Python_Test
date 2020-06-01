import jieba
import jieba.analyse
import pdfkit

# f = open('article.txt','r',encoding='utf8')
# f = open('water.pdf','r',encoding='utf8')
# article = f.read()
# tags = jieba.analyse.extract_tags(article,10)
# print('最重要的字詞',tags)

# pdfkit 範例==============================================================================
# config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
# pdfkit.from_url('https://www.csf.org.tw/main/index.asp','out1.pdf',configuration=config)
# pdfkit.from_string('helloWorld','out2.pdf',configuration=config)
# pdfkit.from_file('CSF.html','out3.pdf',configuration=config)
# pdfkit.from_file('test.html','out4.pdf',configuration=config)
# ==================================================================================


# PyPDF2 範例=============================================================================
# from PyPDF2 import PdfFileReader, PdfFileWriter
# readFile = 'water.pdf'
# PdfFileReader = PdfFileReader(readFile)

# documentInfo = PdfFileReader.getDocumentInfo()
# print('documentInfo = %s'%documentInfo)

# pageLayout = PdfFileReader.getPageLayout()
# print('pageLayout = %s'%pageLayout)

# pageMode = PdfFileReader.getPageMode()
# print('pageModew = %s'%pageMode)

# xmpMetadata = PdfFileReader.getXmpMetadata()
# print('xmpMetadata = %s'%xmpMetadata)

# pageCount = PdfFileReader.getNumPages()
# print('pageCount = %s'%pageCount)
# ==================================================================================

from PyPDF2 import PdfFileReader, PdfFileWriter #函式庫使用
readFile = 'health.pdf' #將處理檔案賦予變數
PdfFileReader = PdfFileReader(readFile,strict=False) #即為health.pdf

documentInfo = PdfFileReader.getDocumentInfo() 
outFile = 'health_output.pdf' #輸出的pdf檔名設定
PdfFileWriter = PdfFileWriter() #將寫入的方法()，賦予一個變數
numPages = PdfFileReader.getNumPages() #將讀取到的檔案，取得總頁數
for index in range(0, numPages): #進迴圈 range(0筆,總頁數)
    pageObj = PdfFileReader.getPage(index) #帶入index，取得每一頁
    # pageObj 即是 撈出來的每一頁
    PdfFileWriter.addPage(pageObj) #增加頁數；加入每一頁
    PdfFileWriter.write(open(outFile, 'wb')) #將每頁寫入至outDile
                                    #使用'wb'用二進位寫入較快
PdfFileWriter.addBlankPage() #以上寫完後，再加入一張空白頁
PdfFileWriter.write(open(outFile, 'wb')) #遵循上面，將空白頁實際寫入

