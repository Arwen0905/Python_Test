f_name = "read_910.dat"
# f_name = "read.dat"
with open(f_name,'r',encoding="utf8") as f:
    m = fm = 0
    for i in f:
        print(i)
        r = i.strip('\n').split()
        if r[2] == '0':
            fm +=1
        elif r[2] == '1':
            m += 1
print('Number of males: %d'%m)
print('Number of females: %d'%fm)
