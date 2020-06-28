def compute():
    lst=[]
    for i in range(1):
        d = input()
        lst.append(d)
        s = input()
        lst.append(s)
        n = input()
        lst.append(n)
    print('Department: %s'%lst[0])
    print('Student ID: %s'%lst[1])
    print('Name: %s'%lst[2])
        
compute()