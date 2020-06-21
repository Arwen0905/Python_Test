# 2. 設計說明：
# 請撰寫一程式，提示使用者輸入一個社會安全碼SSN，格式為ddd-dd-dddd，
# d表示數字。若格式完全符合（正確的SSN）則顯示【Valid SSN】，否則顯示【Invalid SSN】。

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

import re # 引入"正規表示法" 函式庫
s = [str(input())] #接受一個str字串，再用 [] 中括號框起來，直接轉串列型態，此步驟目的是取得[索引]功能
# 以下為引用 re "正規表示法" ，他的功能是利用"各符號去限制該字元必須是什麼型態"，以下冒號後解釋效果
# ^:代表開頭必須為 \d:只能接受數值 {3}:只接受數量為3個 [-]:只能接受中括號裡面的字元，以此類推的限制條件。
# 因為input時 s 已轉成串列型態，所以能用索引[0]取得純字元，接著用 re.findall('正規表示法',s[0]) 做比對
res = re.findall('\d{3}[-]\d{2}[-]\d{4}$',s[0]) # 很像火星文，但符號效果理解，即能讀懂正規表示法的限制條件
if s == res: # 如果上述比對符合，res會回傳跟 s 一樣字元，否則就回傳空串列[]，如此就能拿來做判斷結果。
    print('Valid SSN')
else:
    print('Invalid SSN')

