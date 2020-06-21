# f = open('write.txt','w+')
# f.write('Banana\n')
# f.write('Grape\n')
# f.write('Orange\n')
# f.write('蘋果\n')
# f.write('芒果\n')
# f.close()

# f2 = open('write2.txt','w+')
# for i in range(3):
#     s = input()
#     f2.write(s+'\n')
# f2.close()

f = open('write2.txt','r')
r = f.read()
# print(repr(r)) #加入\很像 路徑\路徑\路徑
f.close()
print(r)