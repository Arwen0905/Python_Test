while True:
    s = str(input())
    if len(s) == 6:
        break
    print('|%-10s|'%s)
    print('|%10s|'%s.center())
    print('|%10s|'%s)
