# TODO
total = 10
lst = []
count = [0]*10
for i in range(total):
    n = eval(input())
    lst.append(n)
    count[lst.index(n)] += 1 
maxPos = max(count) #lst[索引內的索引] maxPos <<需要先抓出來該數值
print(lst[count.index(maxPos)])
print(max(count))
