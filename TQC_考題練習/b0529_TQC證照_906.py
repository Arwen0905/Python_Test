# 1. 題目說明:
# 請開啟PYD906.py檔案，依下列題意進行作答，使輸出值符合題意要求。
# 作答完成請另存新檔為PYA906.py再進行評分。

# 請注意：資料夾或程式碼中所提供的檔案路徑，不可進行變動，
# data.txt檔案需為UTF-8編碼格式。

# 2. 設計說明：
# 請撰寫一程式，要求使用者輸入檔名data.txt、字串s1和字串s2。
# 程式將檔案中的字串s1以s2取代之。

# 3. 輸入輸出：
# 輸入說明
# 輸入data.txt及兩個字串（分別為s1、s2，字串s1被s2取代）

# 輸出說明
# 輸出檔案中的內容
# 輸出取代指定字串後的檔案內容

# 輸入輸出範例
# 範例輸入
# data.txt
# pen
# sneakers
# 範例輸出
# === Before the replacement
# watch shoes skirt
# pen trunks pants
# === After the replacement
# watch shoes skirt
# sneakers trunks pants

#TODO
f_name = input()
str_old = input()
str_new = input()
infile = open(f_name,"r") # 打開檔案
data = infile.read()
print("=== Before the replacement")
print(data)
infile.close()
#TODO

print("=== After the replacement")
new_data = data.replace(str_old,str_new) # 取得新字串
print(new_data)

outfile = open(f_name,"w") # 打開
outfile.write(new_data) # 寫入
outfile.close()         # 關閉
#TODO