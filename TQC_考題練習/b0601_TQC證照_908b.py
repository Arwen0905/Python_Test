# 1. 題目說明:
# 請開啟PYD908.py檔案，依下列題意進行作答，使輸出值符合題意要求。
# 作答完成請另存新檔為PYA908.py再進行評分。

# 請注意：資料夾或程式碼中所提供的檔案路徑，不可進行變動，
# read.txt檔案需為UTF-8編碼格式。

# 2. 設計說明：
# 請撰寫一程式，要求使用者輸入檔名read.txt，以及檔案中某單字出現的次數。
# 輸出符合次數的單字，並依單字的第一個字母大小排序。
# （單字的判斷以空白隔開即可）

# 3. 輸入輸出：
# 輸入說明
# 讀取read.txt的內容，以及檔案中某單字出現的次數

# 輸出說明
# 輸出符合次數的單字，並依單字的第一個字母大小排序

# 輸入輸出範例
# 範例輸入
# read.txt
# 3
# 範例輸出
# a
# is
# programming

# TODO
f_name = 'read.txt'
n = 3
# f_name = input() # 輸入檔名
# n = int(input()) # 輸入次數
with open(f_name,"r") as file:
    data = sorted(file.read().split()) # 讀取內容，分割後 排序
    for i in sorted(set(data)):
        print(i)
        if data.count(i)==n:
            print(i)
