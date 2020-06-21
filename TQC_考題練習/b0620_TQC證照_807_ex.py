# 1. 題目說明:
# 請開啟PYD807.py檔案，依下列題意進行作答，計算數字加總並計算平均，
# 使輸出值符合題意要求。作答完成請另存新檔為PYA807.py再進行評分。

# 2. 設計說明：
# 請撰寫一程式，要求使用者輸入一字串，該字串為五個數字，以空白隔開。
# 請將此五個數字加總（Total）並計算平均（Average）。

# 3. 輸入輸出：
# 輸入說明
# 一個字串（五個數字，以空白隔開）

# 輸出說明
# 總合
# 平均 (輸出浮點數到小數點後第一位)

# 輸入輸出範例
# 範例輸入
# -2 34 18 29 -56
# 範例輸出
# Total = 23
# Average = 4.6

s = str(input()).split()
s = [int(s) for s in s]
print('Total = %d'%sum(s))
print('Average = %.1f'%(sum(s)/len(s)))


# s = str(input()).split()
# total = [int(s) for s in s]
# print('Total = %d'%sum(total))
# print('Average = %.1f'%(sum(total)/len(s)))
