# 1. 題目說明:
# 請開啟PYD810.py檔案，依下列題意進行作答，
# 找出串列數字中最大值和最小值之間的差，使輸出值符合題意要求。
# 作答完成請另存新檔為PYA810.py再進行評分。

# 2. 設計說明：
# 請撰寫一程式，首先要求使用者輸入正整數k（1 <= k <= 100），
# 代表有k筆測試資料。每一筆測試資料是一串數字，
# 每個數字之間以一空白區隔，請找出此串列數字中最大值和最小值之間的差。

# 提示：差值輸出到小數點後第二位。

# 3. 輸入輸出：
# 輸入說明
# 先輸入測試資料的筆數，再輸入每一筆測試資料
# （一串數字，每個數字之間以空白區隔）

# 輸出說明
# 每個串列數字中，最大值和最小值之間的差

# 輸入輸出範例
# 輸入與輸出會交雜如下，輸出的部份以粗體字表示
# 4
# 94 52.9 3.14 77 46
# 90.86
# -2 0 1000.34 -14.4 89 50
# 1014.74
# 87.78 33333 29.3
# 33303.70
# 9998 9996 9999
# 3.00   

# TODO
total = eval(input())
for i in range(total):
    t = input()
    t = t.split(' ')
    t = [eval(x) for x in t] # 神奇的運算
    ans = (max(t)-min(t))
    print('%.2f'%ans)

