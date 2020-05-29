# 1. 題目說明:
# 請開啟PYD802.py檔案，依下列題意進行作答，
# 顯示字串每個字元對應的ASCII碼及其總和，使輸出值符合題意要求。
# 作答完成請另存新檔為PYA802.py再進行評分。

# 2. 設計說明：
# 請撰寫一程式，要求使用者輸入一字串，
# 顯示該字串每個字元的對應ASCII碼及其總和。

# 3. 輸入輸出：
# 輸入說明
# 一個字串

# 輸出說明
# 依序輸出字串中每個字元對應的ASCII碼
# 每個字元ASCII碼的總和

# 輸入輸出範例
# 範例輸入
# Kingdom
# 範例輸出
# ASCII code for 'K' is 75
# ASCII code for 'i' is 105
# ASCII code for 'n' is 110
# ASCII code for 'g' is 103
# ASCII code for 'd' is 100
# ASCII code for 'o' is 111
# ASCII code for 'm' is 109
# 713

# TODO
total = 0
# string = input('ASCII code: ')
string = input()
for i in range(len(string)):
    num = ord(string[i])
    print(num,'<< ord函式將字碼轉成ASCII')
    print("ASCII code for '%s' is %d"%(string[i],num))
    total+=num
print(total)
####### ASCII:"拆開單字元方式"，再以ord函式取得ASCII碼 ########
"""
ASCII code for '_' is _
"""
