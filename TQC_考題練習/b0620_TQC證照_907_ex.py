# 請撰寫一程式，要求使用者輸入檔名read.txt，顯示該檔案的行數、單字數
# （簡單起見，單字以空白隔開即可，忽略其它標點符號）以及字元數（不含空白）。

# f = 'read_907.txt'
f = input()
line=word=char=0
with open(f,'r')as data:
    for i in data:
        line+=1
        word += len(i.split())
        for i in i.split():
            char+=len(i)
print(line,'line(s)')
print(word,'word(s)')
print(char,'character(s)')