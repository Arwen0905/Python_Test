# 1. 題目說明:
# 請開啟PYD310.py檔案，依下列題意進行作答，依公式計算總和，使輸出值符合題意要求。
# 作答完成請另存新檔為PYA310.py再進行評分。

# 2. 設計說明：
# 請使用迴圈敘述撰寫一程式，讓使用者輸入正整數n (1 < n)，
# 計算以下公式的總和並顯示結果：
#   1  +   1   +   1   +    1
# 1+√2 | √2+√3 | √3+√4 | √n−1+√n
 
# 提示：輸出結果至小數點後四位。

# 3. 輸入輸出：
# 輸入說明
# 一個正整數

# 輸出說明
# 代入公式計算結果

# 輸入輸出範例
# 範例輸入
# 8
# 範例輸出
# 1.8284

# TODO
n = eval(input())
sum = 0
for i in range(2,n+1):
    sum+=1/((i-1)**0.5+i**0.5)
print('%.4f'%sum)
