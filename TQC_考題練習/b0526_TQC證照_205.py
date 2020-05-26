# 1. 題目說明:
# 請開啟PYD205.py檔案，依下列題意進行作答，
# 判斷輸入值的字元，使輸出值符合題意要求。
# 作答完成請另存新檔為PYA205.py再進行評分。

# 2. 設計說明：
# 請使用選擇敘述撰寫一程式，讓使用者輸入一個字元，
# 判斷它是包括大、小寫的英文字母（alphabet）、
# 數字（number）、或者其它字元（symbol）。
# 例如：a為英文字母、9為數字、$為其它字元。

# 3. 輸入輸出：
# 輸入說明
# 一個字元

# 輸出說明
# 判斷是英文字母（包括大、小寫）、數字、或者其它字元

# 輸入輸出範例
# 範例輸入1
# P
# 範例輸出1
# P is an alphabet.
# 範例輸入2
# @
# 範例輸出2
# @ is a symbol.
# 範例輸入3
# 7
# 範例輸出3
# 7 is a number.

# TODO
c = input()
if ('a'<= c <='z') or ('A'<= c <='Z'):
    print(c,'is an alphabet.')
elif ('0'<= c <='9'):
    print(c,'is a number.')
else:
    print(c,'is a symbol.')

"""
_ is an alphabet.
_ is a number.
_ is a symbol.
"""