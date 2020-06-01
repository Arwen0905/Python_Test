dic = {'第一個':1,'第二個':2,'第三個':3,'第五個':3,'第六個':2}
n = 3
# dic = set(dic)
# for i in sorted(set(dic)):
#     if dic.count(i) == n:
#         print(i)
# ===========================================================

dic_test = list(dic.items())
# print(dic_test,type(dic_test))
for i in sorted(dic_test):
    print(i)
print('===========================================')
dic_list = dic.items()
for i in sorted(dic_list):
    print(i)
# print(dic_list,type(dic_list))
# dicQTY = [x for (x,y) in dci_list if y == n]
# print(dicQTY)
# ===========================================================
# for i in dic:
#     if n == dic[i]:
#         print(i)
# wordQTY = [x for (x,y) in word_list if y == n]
# print(wordQTY)
# ===========================================================

# data = sorted(file.read().split()) # 讀取內容，分割後 排序
#     for i in sorted(set(data)):
#         # print(i)
#         if data.count(i)==n:
#             print(i)

# a1 = [5,4,6,95,25]
# print(a1)
# print(sorted(a1))
# print(a1)
# a1.sort(reverse=True)
# print(a1)

# member = [['Simon','A',95],
#           ['Amy','B',80],
#           ['Ruby','C',78],
#           ['kelly','B',82],
#           ]
# print(member)
# m_sort1 = sorted(member)
# print(m_sort1)
# member.sort()
# print(member)
# m_sort2 = sorted(member,key=lambda Q1:Q1[2])
# print(m_sort2)

# s = [20,30,10,40,90]
# sort_s = sorted((range(len(s))),key=lambda a:s[a])
# print(sort_s)