import json #載入JSON套件
with open('ubike_1.json',encoding='utf8') as fin:
    #開啟JSON檔並設定給變數file
    f = json.load(fin) #透過load方法，執行解碼
    #執行load()方法將JSON檔案解碼為Python物件，並設定給data變數
    for item in f: #以data作為迴圈執行的依據，即解碼後的資料設為item
        print(item['sno'],item['sna'],item['tot'])
        # print(item)
        #以索引列印item各欄位資料

# JSON：JavaScritp Object Notation
# JavaScript 開放資料交換格式
# JSON 為JavaScript程式的一個子集合

# JSON型態轉換到Python型態的對照：
            # object → dict
            # array  → list
            # string → unicode
            # true   → True
            # false  → False
            # null   → None
            # number(int)  → int,long
            # number(real) → float
