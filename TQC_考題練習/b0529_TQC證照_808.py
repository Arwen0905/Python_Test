# 1. 題目說明:
# 請開啟PYD808.py檔案，依下列題意進行作答，進行社會安全碼格式檢查，
# 使輸出值符合題意要求。作答完成請另存新檔為PYA808.py再進行評分。

# 2. 設計說明：
# 請撰寫一程式，提示使用者輸入一個社會安全碼SSN，格式為ddd-dd-dddd，
# d表示數字。若格式完全符合（正確的SSN）則顯示【Valid SSN】，
# 否則顯示【Invalid SSN】。

# 3. 輸入輸出：
# 輸入說明
# 一個字串（格式為ddd-dd-dddd，d表示數字）

# 輸出說明
# 判斷是否符合SSN格式

# 輸入輸出範例
# 範例輸入1
# 329-48-4977
# 範例輸出1
# Valid SSN
# 範例輸入2
# 837-a3-3000
# 範例輸出2
# Invalid SSN

# TODO
s = input() #輸入
isSSN = (len(s) == 11) # 取布林值，判斷長度是否符合
# 如果長度就不符合了，則反應最下方的else
if isSSN: # 長度符合才能進入以下判斷
    for i in range(len(s)): # 進迴圈，以字串長度做[索引值]設定
        if i==3 or i ==6: # 當迴圈進行到預估為'-'符號的的位置時再進入檢測
            if s[i] != '-': # 檢查第3及第6的字碼位置是否為'-'
                isSSN = False # 如果該位置不是'-'就給false
                break # 跳出
        elif not s[i].isdigit(): # 這看起來像是比對數字型態的方法?
            isSSN = False
            break
if isSSN: # 印出的方式為布林值判斷
    print('Valid SSN')
else:
    print('Invalid SSN')   

