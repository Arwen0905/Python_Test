# 1. 題目說明:
# 請開啟PYD504.py檔案，依下列題意進行作答，
# 依使用者輸入的整數作為參數傳遞進行公式計算，使輸出值符合題意要求。
# 作答完成請另存新檔為PYA504.py再進行評分。

# 2. 設計說明：
# 請撰寫一程式，讓使用者輸入兩個整數，接著呼叫函式compute()，
# 此函式接收兩個參數a、b，並回傳 a次方b的值。

# 範例輸入
# 14
# 3
# 範例輸出
# 2744

# TODO
a = eval(input())
b = eval(input())
def compute(a,b):
    ans = a**b
    return ans
print(compute(a,b))
