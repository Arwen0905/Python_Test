class Animal():
 def __init__(self, name, age, version):
  self.name = name
  self.age = age
  self.version = '寫了就變固定資料'
  
a = Animal("dog",27,'無法設定了')  #建立一個名叫dog的Animal實體(物件)
b = Animal("老師",'35','5.0.1')

print(a.name)
print(a.age)
print(a.version)

print(b.name)
print(b.age)
print(b.version)
