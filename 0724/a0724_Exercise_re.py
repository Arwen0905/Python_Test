import re

str1 ="ABCDEFGHIJK"

# 輸出: CD
pattern1 = re.compile('[CD]{2}')
ans1 = pattern1.findall(str1)
print(ans1[0])

# 輸出: ABC BCD
pattern2 = re.compile('^\w{3}')
pattern3 = re.compile('BCD')
ans2 = pattern2.findall(str1)
ans3 = pattern3.findall(str1)
print(f"{ans2[0]} {ans3[0]}")

# 輸出: DEF BCD CDE DEF
pattern4 = re.compile('[^A-C]{3}')
pattern5 = re.compile('[^AB]{3}')
ans4 = pattern4.findall(str1)
ans5 = pattern5.findall(str1)
print(f"{ans4[0]} {ans3[0]} {ans5[0]} {ans4[0]}")
