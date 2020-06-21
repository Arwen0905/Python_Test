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
f_name = 'read_908.txt'
n = 3
# f_name = input() # 輸入檔名
# n = int(input()) # 輸入次數
with open(f_name,"r") as file:
    data = sorted(file.read().split()) # 讀取內容，分割後 排序
    # print(data.count(3)) #串列可以直接挖到"該值數量"
    # print(sorted(set(data))) #不重複且排序的方式進迴圈"挖掘單字"，注意不是實際比對值，比對值是在判斷區!
    for i in sorted(set(data)):
        # print(i)
        # print(data.count('a')) # 3次，count方法可以搜尋該(字元)於資料出現次數
        # print(data,'<< 注意哦，實際資料是沒變的，因為要取count(值)做比對')
        if data.count(i)==n:
            print(i)
