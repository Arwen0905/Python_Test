# 1. 題目說明:
# 請開啟PYD203.py檔案，依下列題意進行作答，判斷輸入值是否為閏年，
# 使輸出值符合題意要求。作答完成請另存新檔為PYA203.py再進行評分。

# 2. 設計說明：
# 請使用選擇敘述撰寫一程式，讓使用者輸入一個西元年份，
# 然後判斷它是否為閏年（leap year）或平年。
# 其判斷規則為：每四年一閏，每百年不閏，但每四百年也一閏。

# 3. 輸入輸出：
# 輸入說明
# 一個正整數

# 輸出說明
# 判斷是否為閏年或平年

# 輸入輸出範例
# 範例輸入1
# 1992
# 範例輸出1
# 1992 is a leap year.
# 範例輸入2
# 2010
# 範例輸出2
# 2010 is not a leap year.

# TODO
year = eval(input())
# year = 2010
if year%400==0 or (year%4==0 and year%100!=0):  
    print('%4d is a leap year.' % year)
else:
    print('%4d is not a leap year.' % year)
    
"""
_ is a leap year.
_ is not a leap year.
"""