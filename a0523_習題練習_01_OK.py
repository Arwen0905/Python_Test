import random
# 以下函式功能為:取隨機10碼，數字不重複並填入list1字串，若遇重複則重新呼叫
# 變數(n)功能為:嘗試取得內部"重新呼叫"的次數
# 發生問題:超出預期般的倒數現象( line:19 變數:n )，不理解倒數現象
n=[0]
def output(x,n):
    for i in range(10):
        num = random.randint(1,20)
        if num not in x:
            x.append(num)
        else:
            x.clear() # 字串清空
            n[0] += 1 # 重新呼叫次數+1
            print('重新呼叫次數:',x,n)
            output(x,n) # 重新呼叫output
            break # 終止重來
        print('填入過程',x)
    # n += 1 # 這邊+=1 也沒辦法阻止倒數的現象
    print('回朔現象',n,'類別確認:',type(n))
    # x.sort() # 排序
    return x,n

list1=[]
n = output(list1,n)[1]
print('\n不重複串列運算:\n%s\n欲取得重新呼叫次數(BUG): %s'%(list1,n))
print('字元長度確認(10):',len(list1))

def maxValue(x):
    maxNum = list1[0]
    for i in list1:
        if i > maxNum:
            maxNum = i
    return maxNum
def minValue(x):
    minNum = list1[0]
    for i in list1:
        if i < minNum:
            minNum = i
    return minNum        
print('最大值',maxValue(list1))
print('最大值',minValue(list1))

list1 = [10,2,11]
def compareSize(list1):
    switch = True
    while switch:
        switch = False
        for i in range(len(list1)-1):
            if list1[i] > list1[i+1]:
                tempMax = list1[i]
                list1[i] = list1[i+1]
                list1[i+1] = tempMax
                switch = True
    return list1
print(compareSize(list1))
