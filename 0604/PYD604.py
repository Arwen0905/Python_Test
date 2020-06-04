# TODO
lst = []
count = [0]*10
for i in range(10):
    n = eval(input())
    lst.append(n)
    count[lst.index(n)] += 1
print(lst[count.index(max(count))])
print(max(count))
