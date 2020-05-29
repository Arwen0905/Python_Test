# TODO
n = int(input())
if n == 0:
    print(n)
while n != 0:
    print(n%10,end='')
    n//=10