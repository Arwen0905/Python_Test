def main():
    # 利用open開啟檔案，若檔案不存在，則建立檔案
    # outfile = open('C:\\Users\\ASUS\\Desktop\\Python_main\\fruits.txt','w')
    outfile = open('C:\\Users\\user\\Desktop\\Python_main\\fruits.txt','w')
    outfile.write('Banana\n')
    outfile.write('Grape\n')
    outfile.write('Orange\n')
    outfile.write('蘋果\n')
    outfile.write('芒果\n')
    outfile.close()
main()

# infile = open('C:\\Users\\ASUS\\Desktop\\Python_main\\fruits.txt','r')
infile = open('C:\\Users\\user\\Desktop\\Python_main\\fruits.txt','r')
print('使用readline() 方法: ')
line1 = infile.readline()
line2 = infile.readline()
line3 = infile.readline()
line4 = infile.readline()

print(repr(line1))
print(repr(line2))
print(repr(line3))
print(repr(line4))

print()
print(line1)
print(line2)
print(line3)
print(line4)
infile.close()


# infile = open('C:\\Users\\ASUS\\Desktop\\Python_main\\fruits.txt','r')
infile = open('C:\\Users\\user\\Desktop\\Python_main\\fruits.txt','r')
line1 = infile.read()
print('使用read() 方法: ')
print(repr(line1))
print(line1)
infile.close()

# infile = open('C:\\Users\\ASUS\\Desktop\\Python_main\\fruits.txt','r')
infile = open('C:\\Users\\user\\Desktop\\Python_main\\fruits.txt','r')
print('\n使用readlines() 方法: ')
line1 = infile.readlines()
print(line1)
infile.close()

def main(): # read()給予指定字元
    # infile = open('C:\\Users\\ASUS\\Desktop\\Python_main\\fruits.txt','r')
    infile = open('C:\\Users\\user\\Desktop\\Python_main\\fruits.txt','r')
    print('使用 read(7) 方法:')
    line1 = infile.read(7)
    print(line1)
    infile.close()
    
    # infile = open('C:\\Users\\ASUS\\Desktop\\Python_main\\fruits.txt','r')
    infile = open('C:\\Users\\user\\Desktop\\Python_main\\fruits.txt','r')
    print('使用 read(8) 方法:')
    line2 = infile.read(8)
    print(line2)
    infile.close()
main()

def main(): # 以迴圈讀取(#1資料, #2檔案)所有內容
    # infile = open('C:\\Users\\ASUS\\Desktop\\Python_main\\fruits.txt','r')
    infile = open('C:\\Users\\user\\Desktop\\Python_main\\fruits.txt','r')
    line1 = infile.readline()
    print('\n利用 for迴圈，依序跑出 readline的資料\n')
    print('>>>',line1)
    for i in line1:
        print(i)
    print('\n利用 while迴圈，依序跑出 readline的資料\n')    
    infile.close()
    
    # infile = open('C:\\Users\\ASUS\\Desktop\\Python_main\\fruits.txt','r')
    infile = open('C:\\Users\\user\\Desktop\\Python_main\\fruits.txt','r')
    line1 = infile.readline()
    while line1 != '':
        print('>>>',line1)
        line1 = infile.readline()
    infile.close()
main()

def main(): # 因應下一則範例，演示 w、r 的正規使用方式
    # outfile = open('C:\\Users\\ASUS\\Desktop\\Python_main\\cities.txt','w')
    outfile = open('C:\\Users\\user\\Desktop\\Python_main\\cities.txt','w')
    outfile.write('Taipei\n')
    outfile.write('London\n')
    outfile.write('Coventry\n')
    outfile.close()
    
    # infile = open('C:\\Users\\ASUS\\Desktop\\Python_main\\cities.txt','r')
    infile = open('C:\\Users\\user\\Desktop\\Python_main\\cities.txt','r')
    data = infile.read()
    print('w: | r: \n',data)
    infile.close()
main()

def main(): # 呼應上則的技巧: open使用'w+'的方式，可省略建立open'r'
    # outfile = open('C:\\Users\\ASUS\\Desktop\\Python_main\\cities.txt','w+')
    outfile = open('C:\\Users\\user\\Desktop\\Python_main\\cities.txt','w+')
    outfile.write('Taipei\n')
    outfile.write('London\n')
    outfile.write('Coventry\n')
    outfile.seek(0, 0) # ※(左邊 0:移動byte數，右邊 0:從哪裡開始位移) ，函式seek為此解決
#       0: 擋頭
# 		1: 目前位置
# 		2: 檔尾
# seek : python只要執行read後，read動作結束後，檔案指標是指向檔尾的 ※檔尾:西瓜|<<檔尾
    data = outfile.read()
    print('w+: \n',data)
main()
# 補充:微軟定義Access 為進階軟體，依據指標指向位置來操作

import pickle
def main():
    # outbinfile = open('C:\\Users\\ASUS\\Desktop\\Python_main\\binaryfile.dat','wb')
    outbinfile = open('C:\\Users\\user\\Desktop\\Python_main\\binaryfile.dat','wb')
    print('pickle 的寫讀方法:')
    pickle.dump(123, outbinfile)
    pickle.dump(77.7, outbinfile)
    pickle.dump('python is good programming', outbinfile)
    pickle.dump([11,22,33], outbinfile)
    # 測試 ------------------------------------------------
    # outbinfile.seek(0 ,0)
    # data = outbinfile.read()
    # print('測試',data)
    # 測試 ------------------------------------------------
    outbinfile.close()  
    # outbinfile = open('C:\\Users\\ASUS\\Desktop\\Python_main\\binaryfile.dat','rb')
    outbinfile = open('C:\\Users\\user\\Desktop\\Python_main\\binaryfile.dat','rb')
    print(pickle.load(outbinfile))
    print(pickle.load(outbinfile))
    print(pickle.load(outbinfile))
    print(pickle.load(outbinfile))
    outbinfile.close()
main()

# def main():
#     outfile = open('C:\\Users\\user\\Desktop\\Python_main\\score.txt','wb')
#     data = eval(input('(第一次)請輸入整數，輸入 0 結束輸入: '))
#     while data != 0:
#         pickle.dump(data, outfile)
#         data = eval(input('(第二次)請輸入整數，輸入 0 結束輸入: '))
#     outfile.close()
    
#     infile = open('C:\\Users\\ASUS\\Desktop\\Python_main\\score.txt','rb')
#     end_of_file = False
#     while not end_of_file:
#         try:
#             print(pickle.load(infile), end=' ')
#         except EOFError:
#                 print('Errrrrrrrrrror')
#                 end_of_file = True
#     infile.close()
#     print('\n所有資料已讀取')
# main()

def main():
    try:
        n1,n2 = eval(input('輸入兩個值，以逗號分隔: '))
        ans = n1 / n2
        print('%d / %d = %d'% (n1, n2, ans))
    except ZeroDivisionError:
        print('除法分母不可為 0！')
    except SyntaxError:
        print('輸入資料必須以逗號分隔！')
    except :
        print('輸入時發生錯誤！')
    else:
         print('沒有異常錯誤！')
    finally:
         print('finally 子句被執行！')
main()


