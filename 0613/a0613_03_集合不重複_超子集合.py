set1 = set([i for i in range(10,20)])
print(set1)
tup = tuple([i for i in range(8)])
print(tup,type(tup))
set2 = set((5,5,10,10,6,9,8))
print(set2,'集合不重複')
print('=================')
print(set2,type(set2))



print('=== 集合大典 ===')
setA = {1, 6, 8, 10, 20}
setB = {1, 3, 8, 10}
print('A',setA)
print('B',setB)
print()
# 以下兩個都是 聯集 的寫法
print('| 聯集 ， | 全秀出來，但不重複，話說集合本就不該重複')
# print(setA.union(setB))
print(setA | setB)
print()
# 以下兩個都是 交集 的寫法
print('& 交集 ， & 只取重複的')
# print(setA.intersection(setB))
print(setA & setB)
print()
# 以下兩個都是 對稱差集 的寫法
print('^ 反差集 , ^ 只取不重複的')
# print(setA.symmetric_difference(setB))
print(setA ^ setB)
print()
# 以下兩個都是 差集 的寫法
print('- 差集 , - 減掉後者')
# print(setA.difference(setB))
print(setA - setB)
