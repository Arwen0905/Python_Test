f = open('test_read.txt','w+')
f.write('你好\n')
f.seek(0,0)
data = f.readlines()
print(data)
f.close()


import pickle
f = open('test_read.dat','wb')
print('pickle 的寫讀方法:')
pickle.dump(123,f)
f.close()

f = open('test_read.dat','rb')
print(pickle.load(f))
f.close()


