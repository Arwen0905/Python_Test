# 2. 設計說明：
# 請撰寫一程式，要求使用者輸入檔名read.txt，以及檔案中某單字出現的次數。
# 輸出符合次數的單字，並依單字的第一個字母大小排序。（單字的判斷以空白隔開即可）

# 3. 輸入輸出：
# 輸入說明
# 讀取read.txt的內容，以及檔案中某單字出現的次數

# 輸出說明
# 輸出符合次數的單字，並依單字的第一個字母大小排序

# 輸入輸出範例
# 範例輸入
# read.txt
# 3
# 範例輸出
# a
# is
# programming

# f_name = 'read_908.txt'
# n = int(3)
f_name = input()
n = int(input())
with open(f_name,'r') as f:
    fr = sorted(f.read().split())
    # f.seek() #雄飛教的，表示讀取後的指標，參數可控制位置
    # print(fr) ['C','It','Java','Python',...] 因為沒有間隔的原文件資料，當切割後，即會產生完整的一包串列
    for i in set(fr): # 集合化，排除重複值，但須注意只針對迴圈取i，為了避免底下的重複if判斷
        # print(i,'<< i') # 挖串列就會會跑出 ['a','b','c','d','e']
        # print(i.split(),'<< 切割') # 對象為乾淨的字串，則會轉成單一串列，例如:['hava']\n['best']
        if fr.count(i) == n:
            print(i)
            