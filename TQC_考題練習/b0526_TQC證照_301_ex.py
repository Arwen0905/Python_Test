# 1. 題目說明:
# 請開啟PYD301.py檔案，依下列題意進行作答，
# 依輸入值計算總和，使輸出值符合題意要求。
# 作答完成請另存新檔為PYA301.py再進行評分。

# 2. 設計說明：
# 請使用迴圈敘述撰寫一程式，
# 讓使用者輸入兩個正整數a、b（a < b），
# 利用迴圈計算從a開始連加到b的總和。
# 例如：輸入a=1、b=100，
# 則輸出結果為5050（1 + 2 + … + 100 = 5050）。

# 3. 輸入輸出：
# 輸入說明
# 兩個正整數（a、b，且a < b）

# 輸出說明
# 計算從a開始連加到b的總和

# 輸入輸出範例
# 範例輸入
# 66
# 666
# 範例輸出
# 219966

# TODO
a = eval(input())
b = eval(input())
ans = 0
if a<b:
    for i in range(a,b+1):
        ans+=i
print(ans)