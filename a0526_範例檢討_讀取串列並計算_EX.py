# infile = open('C:\\Users\\ASUS\\Desktop\\Python_main\\students.dat','r')
infile = open('C:\\Users\\user\\Desktop\\Python_main\\students.dat','r')
info = infile.readline() # 變數 為open後讀取的方法(r)
while info != '':
    list1 = info.split(' ') # 空格給予 "，" 
    calculus = eval(list1[1]) # 取微積分成績
    accounting = eval(list1[2]) # 取會計成績
    average = calculus *0.6 + accounting*0.6
    print('|%10s:%.2f|' % (list1[0],average))
    info = infile.readline()
infile.close()

# 先指定變數 為指定位置的文件檔案
# 設定變數為讀取方法
# 進不定數迴圈倒出資料
# 一直挖一直挖，挖到空字串就停止
