f_name = input()
str_old = input()
str_new = input()
with open(f_name,'r',encoding='utf-8') as f:
    data = f.read() #小出包
    print("=== Before the replacement")
    print(data)
    data = data.replace(str_old,str_new) #設定給變數才能使用replace()的方法
    print("=== After the replacement")
    print(data)
