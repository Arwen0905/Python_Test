# 【lambda 模擬switch比對】
# score = int(input('請輸入分數：'))
# level = score // 10
# {
#     10 : lambda: print('Perfect'),
#     9  : lambda: print('A'),
#     8  : lambda: print('B'),
#     7  : lambda: print('C'),
#     6  : lambda: print('D')
# }.get(level, lambda: print('E'))()

# ===lambda小測試===
# {'小叮噹':lambda:print('童年回憶'),
#  '金鋼狼':lambda:print('X戰警')
#  }.get('金鋼狼',lambda:print('不符合'))()

# ===lambda小測試===
{1:lambda:print('電視'),
 2:lambda:print('遊戲')}.get(1,lambda:print('啥'))()
print('============================')
# 補充:如果函式的閒置變數與當時語彙環境綁定，該函式才稱為閉包。
# 【鞣制（Curry）的概念】
def add(n1):
    def add2(n2):
        return n1+n2
    return add2
print(add(1)(2))


print('============================')
def outer():
    x=10
    def inner():
        print(x)
    inner() #! 綁定了區域變數
    x=20
    return inner 

# f = outer()
# f()
outer()()
