# Tickets = True
# while Tickets:
#     outfile = open('C:\\Users\\ASUS\\Desktop\\Python_main\\students.dat','w+')
#     name = input('請輸入學生姓名: (若沒有學生請輸入:沒了 )')
#     score = input('請輸入微積分: ')
#     acc = input('請輸入會計成績: ')
#     if name == '沒了':
#         Tickets = False
#         break
#     else:
#         outfile.write(name)
#         outfile.write(' ')
#         outfile.write(score)
#         outfile.write(' ')
#         outfile.write(acc)
# outfile.close()      

# 寫入
# outfile = open('C:\\Users\\ASUS\\Desktop\\Python_main\\students.dat','w')
# while True:
#     name = input('請輸入學生姓名: ')
#     calculus = input('請輸入微積分成績: ')
#     accounting = input('請輸入會計成績: ')
#     if name == 'none':
#         break
#     else:
#         outfile.write(name)
#         outfile.write(' ')
#         outfile.write(calculus)
#         outfile.write(' ')
#         outfile.write(accounting)
#         outfile.write(' ')
#         outfile.write('\n')
# outfile.close()
# -----------------------------------------------------------------------
# outfile.seek(0)
# data = outfile.read()
# print(data)
# outfile.close()

# 讀取
# infile = open('C:\\Users\\ASUS\\Desktop\\Python_main\\students.dat','r')
# see = infile.readline()
# while see != '':
#     print(see)
#     see = infile.readline()
# infile.close()

# 讀取後，計算平均成績，微積分比重為60%、會計比重為40%，印出來
# infile = open('C:\\Users\\ASUS\\Desktop\\Python_main\\students.dat','r')
# info = infile.readline()
# while info != '':
#     list1 = info.split(' ')
#     calculus = eval(list1[1])
#     accounting = eval(list1[2])
#     average = calculus *0.6 + accounting*0.6
#     print('|%10s:%.2f|' % (list1[0],average))
#     info = infile.readline()
# infile.close()
# ------------------------------------------------------------------------
# 讀取後，計算出成績最高
# infile = open('C:\\Users\\ASUS\\Desktop\\Python_main\\students.dat','r')
# info = infile.readline()
# list2 = []
# bigName = []
# while info != '':
#     list1 = info.split(' ')
#     calculus = eval(list1[1])
#     accounting = eval(list1[2])
#     average = calculus *0.6 + accounting*0.6
#     print('|%10s:%.2f|' % (list1[0],average))
#     list2.append(list1[0]) #名字
#     list2.append(average)    #平均分數
#     # list2.sort()
#     info = infile.readline()
# infile.close()
# print(list2)
# print('成績最高分數:',max(list2))
# print('成績最高同學:',list1)
# ------------------------------------------------------------------------
infile = open('C:\\Users\\ASUS\\Desktop\\Python_main\\students.dat','r')
max = -1
info = infile.readline()
while info != '':
    list1 = info.split(' ')
    print(list1)
    calculus = eval(list1[1])
    if calculus > max:
        max = calculus
        name = list1[0]
    info = infile.readline()
print('微積分分數最高者為: \n %10s: %3d。'% (name , max))
infile.close()

# ------------------------------------------------------------------------
infile = open('C:\\Users\\ASUS\\Desktop\\Python_main\\students.dat','r')
min = 101
info = infile.readline()
while info != '':
    list1 = info.split(' ')
    print(list1)
    accounting = eval(list1[2])
    if accounting < min:
        min = accounting
        name = list1[0]
    info = infile.readline()
print('會計分數最低者為: \n %10s: %3d。'% (name , min))
infile.close()

# ------------------------------------------------------------------------
# 輸入B開頭的才能寫入 #
# outfile = open('C:\\Users\\ASUS\\Desktop\\Python_main\\Bname.dat','w+')
# Bname = []
# while True:
#     name = input('請輸入以 B開頭的姓名: ')
#     if name == 'end':
#         break
#     elif name[0] == 'B':
#         Bname.append(name)
#         outfile.write(name)
#         outfile.write(' ')
#         outfile.write('\n')
#     else:
#         continue
# outfile.seek(0)
# data = outfile.read()
# print(data)
# outfile.close()
# print(Bname)
# ------------------------------------------------------------------------
# 輸入欲找的字串比對有沒有找到，並將該字串替換為'Bright'，若無找到則顯示沒找到 #
# str1 = 'I have an appointment with Amy'
# # findStr = 'Amy'
# findStr = input('請輸入欲尋找的字串: ')
# if findStr in str1:
#     str2 = str1.replace(findStr,'Bright')
#     print(str2)
# else:
#     print('is not found !')
# ------------------------------------------------------------------------
str2 = 'I have an appointment with Amy'
findStr = input('請輸入欲尋找的字串: ')
if str2.find(findStr) != -1:
    str3 = str2.replace(findStr,'Bright')
    print(str3)
else:
    print('is not found !')

# ------------------------------------------------------------------------
