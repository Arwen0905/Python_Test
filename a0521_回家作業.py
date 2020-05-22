# 宣告一整數串列(大小為5)
# 傳遞給 output(aList)函式
# 函式由輸入初始化後
# 回傳給主程式並且輸出該串列
# 再由主程式將該串列傳給max(aList)及min(aList)函式
# 輸出aList之最大值及最小值
# (不可以使用內建函式)

import random
s = eval(input('輸入串列數量: '))
def output(s=6):
    alist = []
    count = 0
    while count < s:
        alist.append(random.randint(1, 100))    
        if len(alist) <= 1:
            maxNum = alist[0]
            minNum = alist[0]
        else:
            if alist[-1] > maxNum:
                maxNum = alist[-1]
            elif alist[-1]< minNum:
                minNum = alist[-1]
        count+=1
    print('\n字串列為:%s\n最大值為: %d \n最小值為: %d' % (alist,maxNum,minNum))
output(s)
