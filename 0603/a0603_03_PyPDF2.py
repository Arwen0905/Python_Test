# txt 文字檔的讀取範例
f = open('score.txt') #開啟檔案，後續不加入"指定符號"的話，即為唯獨檔案
# ※老師補充: 以唯獨的方式開啟，主要是安全考量及不希望更改到原始檔案的內容
a = f.read() #將檔案的讀取功能，指定 a變數
L = a.split( ) #將讀取的資料設定分割，以( )空格做設定","分割成為一個【串列】
# ※老師補充: 串列中的資料為整數"字串"
for i in range(0,len(L)): #以串列資料長度作為迴圈執行次數
    L[i] = int(L[i]) #以索引帶入串列L中取得每1個元素，並轉成整數後設定回自己
#分類統計各級別人數的列表 c
c = [0]*6 # 實用的[0]*數
for x in L: #以串列L中元素作迴圈執行依據 ※可以挖出串列 L內的各元素以 x做表示
    if x >=90: #比對
        c[0]+=1
    elif x >= 80:
        c[1]+=1
    elif x >= 70:
        c[2]+=1
    elif x >= 60:
        c[3]+=1
    elif x >= 40:
        c[4]+=1
    else:
        c[5]+=1
#輸出各級別統計結果
print('90 分以上 %d 人'%c[0]) #輸出
print('89-80 分  %d 人'%c[1])
print('79-70 分  %d 人'%c[2])
print('69-60 分  %d 人'%c[3])
print('59-40 分  %d 人'%c[4])
print('39 分以下 %d 人'%c[5])
