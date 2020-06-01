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
f_name = input() # 輸入檔名
n = int(input()) # 輸入次數
word_dict = dict()
with open(f_name,"r") as file: #簡短讀寫語句
    for line in file: #以迴圈逐一讀取 file內容
        word = line.strip('\n').split(' ') # 去除換行(\n)並以空格分割word
        # ※下面開始 進行word轉成字典(鍵值對)了
        for x in word:
        # 取出字典中所有key及 value值，
        # 設定給 word_list.items():傳回字典中所有key、value
            if x in word_dict:
                word_dict[x] += 1
            else:
                word_dict[x] = 1
print('===================================')
print(word_dict,'<<< word_dict')
print('===================================')
word_list = word_dict.items()

print(word_list,'<<< word_list')

wordQTY = [x for (x,y) in word_list if y == n]
# 利用迴圈以輸入值作為終止值並取出list中的字詞 wordQTY
# 以 x 帶入迴圈中，若符合存在於 word 則將 word_dict[x] 加1
sortedword = sorted(wordQTY)
for x in sortedword:
    print(x)
# 最後將 wordQTY(即取出符合出現次數) 排序( sorted ) 並印出
