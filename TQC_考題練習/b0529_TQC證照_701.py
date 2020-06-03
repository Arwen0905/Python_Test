# 2. 設計說明：
# 請撰寫一程式，輸入數個整數並儲存至串列中，
# 以輸入-9999為結束點（串列中不包含-9999），
# 再將此串列轉換成數組，最後顯示該數組以及其長度（Length）、
# 最大值（Max）、最小值（Min）、總和（Sum）。

# 3. 輸入輸出：
# 輸入說明
# n個整數，直至-9999結束輸入

# 輸出說明
# 數組
# 數組的長度
# 數組中的最大值
# 數組中的最小值
# 數組內的整數總和

# 輸入輸出範例
# 範例輸入
# -4
# 0
# 37
# 19
# 26
# -43
# 9
# -9999
# 範例輸出
# (-4, 0, 37, 19, 26, -43, 9)
# Length: 7
# Max: 37
# Min: -43
# Sum: 44

# TODO
lst = []
while True:
    t = eval(input())
    if t == -9999:
        break
    lst.append(t)
tup = tuple(lst)
print(tup)
print('Length:',len(tup))
print('Max:',max(tup))
print('Min:',min(tup))
print('Sum:',sum(tup))

"""
Length: _
Max: _
Min: _
Sum: _
"""