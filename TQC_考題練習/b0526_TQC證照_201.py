# 1. 題目說明:
# 請開啟PYD201.py檔案，依下列題意進行作答，判斷輸入值是否為偶數，
# 使輸出值符合題意要求。作答完成請另存新檔為PYA201.py再進行評分。

# 2. 設計說明：
# 請使用選擇敘述撰寫一程式，讓使用者輸入一個正整數，
# 然後判斷它是否為偶數（even）。

# 3. 輸入輸出：
# 輸入說明
# 一個正整數

# 輸出說明
# 判斷是否為偶數

# 輸入輸出範例
# 範例輸入1
# 56
# 範例輸出1
# 56 is an even number.
# 範例輸入2
# 21
# 範例輸出2
# 21 is not an even number.

# TODO
num = eval(input())
# num = 1
if num % 2 == 0:
    print('%d is an even number.'% num)
else:
    print('%d is not an even number.'% num)

"""
_ is an even number.
_ is not an even number.
"""