import math #載入數學模組
with open('data5.txt','r') as fin:
    #以讀取模式開啟data5.txt設定給變數fin
    with open('data5_w.txt','w') as fout:
        #以寫入模式開啟，因不存在所以建立"data5_w.txt"，並設定給 fout變數
        for line in fin: #以 fin變數執行迴圈，挖取其內容
            data = math.ceil(20/(float(line)*0.001425))
            # math.ceil(數值) ※老師補充: 比該數值小的整數，比ceil小的為 math.floor()
            print('每股價格%5.2f，每日需購股數:%5.0f'%(float(line),data))
            fout.write(str(data)+'\n')
            #將data以字串型態寫入 fout檔案