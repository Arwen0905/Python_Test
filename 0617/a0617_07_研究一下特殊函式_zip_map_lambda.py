# a = zip(*map(str,[i for i in range(1,11)]))
# ('1', '2', '3', '4', '5', '6', '7', '8', '9', '1')
a = map(str,[i for i in range(1,11)])
# 1 2 3 4 5 6 7 8 9 10
# print(*a) #一樣會有bug 解過壓縮 就無法在下面運行"輸出"

# z = ''
# for i in a:
#     z += str(i)
# print(z)
# qq = ''.join(str(x) for x in a) #專門對付串列資料形式
qq = ''.join(a)
print(qq)


data = ['ACME', 50, 91.1]
q = ''.join(str(x) for x in data) #專門對付串列資料形式
print(q)