# 1. 題目說明:
# 請開啟PYD602.py檔案，依下列題意進行作答，輸出並計算五張牌總和，
# 使輸出值符合題意要求。作答完成請另存新檔為PYA602.py再進行評分。

# 2. 設計說明：
# 請撰寫一程式，讓使用者輸入52張牌中的5張，計算並輸出其總和。

# 提示：J、Q、K以及A分別代表11、12、13以及1。

# 3. 輸入輸出：
# 輸入說明
# 5張牌數

# 輸出說明
# 5張牌的數值總和

# 輸入輸出範例
# 範例輸入
# 5
# 10
# K
# 3
# A
# 範例輸出
# 32

# TODO

list1 = []
ans = 0
for i in range(5):
    n = input()
    if n == 'A':
        list1.append(1)
    elif n == 'J':
        list1.append(11)
    elif n == 'Q':
        list1.append(12)
    elif n == 'K':
        list1.append(13)
    else:
        list1.append(eval(n))
print(list1)
for i in range(len(list1)):
    ans += list1[i]
print(ans)
