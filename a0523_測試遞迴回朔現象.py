def age(n):
    if n < 1:
        return 18
    print('測試遞迴: ',n)
    return age(n-1)+2
print(age(5))


def fk():
    print('單獨執行');    
if __name__ == '__main__':
    fk()

# 例2：字串反轉（ 不準用s[::-1]哈哈哈）

def f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return f(n - 2) + f(n - 2)

for i in range(1, 10):
    print(f(i))
