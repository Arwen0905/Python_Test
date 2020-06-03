class Animal():
 def __init__(self, name, age, version):
  self.name = name
  self.age = age
  self.version = version
  
a = Animal("dog",27,'cccccccccccc')  #建立一個名叫dog的Animal實體(物件)
b = Animal("老師",'35','5.0.1')  #建立一個名叫dog的Animal實體(物件)
# b = Animal('boss')
print(a.name)
print(a.age)
print(a.version)

print(b.name)
print(b.age)
print(b.version)
