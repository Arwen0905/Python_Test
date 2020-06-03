# TODO
lst = []
for i in range(10):
    n = eval(input())
    lst.append(n)
lst.sort()
ans = 0
for i in lst[1:-1]:
    ans += i
average = ans/8
print(ans)
print('%.2f'%average)
