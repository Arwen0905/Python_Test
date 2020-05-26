infile = open('C:\\Users\\ASUS\\Desktop\\Python_main\\students.dat','r')
info = infile.readline()
while info != '':
    list1 = info.split(' ')
    calculus = eval(list1[1])
    accounting = eval(list1[2])
    average = calculus *0.6 + accounting*0.6
    print('|%10s:%.2f|' % (list1[0],average))
    info = infile.readline()
infile.close()