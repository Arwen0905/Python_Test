import pandas as pd

char = ["女","男","男","女","女","男"]
newLis = []

for i in char:
    # ans = i.replace("男","1").replace("女","0") # 連續判斷是否為男或女，並替換元素
    # newLis.append(int(ans)) # 裝進新串列前，要宣告為int數值，以便後續分析
    
    if i == "男":
        newLis.append(1)
    elif i == "女":
        newLis.append(0)
        
print(char)
print(newLis)


