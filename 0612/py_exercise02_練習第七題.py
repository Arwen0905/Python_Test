# (7):請設計一程式，讓使用者輸入姓名與電話，，當要結束輸入通訊資料時，
# 可以輸入「finish」結束。接著可以查詢通訊錄姓名，程式會回應其通訊電話
# ，若沒有會回復「不在通訊中」。
# userlst=[]
# phonelst=[]
# def f():
#     while True:
#         name = str(input('請輸入姓名: '))
#         if name == 'finish':
#             break
#         userlst.append(name)
#         phone = str(input('請輸入電話: '))
#         if phone == 'finish':
#             break
#         phonelst.append(phone)
#     print(userlst,phonelst)
#     s()
# def s():
#     search = str(input('輸入欲查詢名字: '))
#     if search in userlst:
#         print(phonelst[userlst.index(search)])
#     else:
#         print('不在通訊裡')
# f()

# (5):請設計一程式，計算級數1+2+4+7+11...+106的過程和結果。
# n = 0
# ans = 1
# for i in range(1,16):
#     print('%3d + %3d = '%(n,ans),end='')
#     n+=ans
#     print('%3d'%n)
#     ans+=i

# count = 1
# i = 0
# ans = 0
# while count<=106:
#     print(ans,'+',count,'=',end='')
#     ans += count
#     print(ans)
#     i += 1
#     count+=i


