print('Input to set1:')
set1 = set()
count = 0
while count!=5:
  set1.add(eval(input()))
  count+=1
print('Input to set2:')
set2 = set()
count = 0
while count!=3:
  set2.add(eval(input()))
  count+=1
print('Input to set3:')
set3 = set()
count = 0
while count!=9:
  set3.add(eval(input()))

  count+=1
print('set2 is subset of set1:',set2.issubset(set1))
print('set3 is superset of set1:',set3.issuperset(set1))
