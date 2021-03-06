# 1. 題目說明:
# 請開啟PYD904.py檔案，依下列題意進行作答，使輸出值符合題意要求。
# 作答完成請另存新檔為PYA904.py再進行評分。

# 請注意：資料夾或程式碼中所提供的檔案路徑，不可進行變動，
# read.txt檔案需為UTF-8編碼格式。

# 2. 設計說明：
# 請撰寫一程式，讀取read.txt
# （每一列的格式為名字和身高、體重，以空白分隔）
# 並顯示檔案內容、所有人的平均身高、平均體重以及最高者、最重者。

# 提示：輸出浮點數到小數點後第二位。

# 3. 輸入輸出：
# 輸入說明
# 讀取read.txt（每一行的格式為名字和身高、體重，以空白分隔）

# 輸出說明
# 輸出檔案中的內容
# 平均身高
# 平均體重
# 最高者
# 最重者

# 輸入輸出範例
# 範例輸入
# 無

# 範例輸出
# Ben 175 65

# Cathy 155 55

# Tony 172 75
# Average height: 167.33
# Average weight: 65.00
# The tallest is Ben with 175.00cm
# The heaviest is Tony with 75.00kg

# TODO
data = []
with open("read_904.txt","r") as file: # 檔案開啟
    for i_line in file: # 設定迴圈
        print(i_line)

        tmp = i_line.strip('\n').split(' ') # 拆解結構，移除無用符號與空白
        tmp = [tmp[0],eval(tmp[1]),eval(tmp[2])] # 填入data串列
        data.append(tmp)

name = [data[x][0] for x in range(len(data))]
height = [data[x][1] for x in range(len(data))]
weight = [data[x][2] for x in range(len(data))]

print("Average height: %.2f"% (sum(height)/len(height))) # 總數除以個數=平均身高
print("Average weight: %.2f"% (sum(weight)/len(weight))) # 總數除以個數=平均體重

max_h = max(height)
max_w = max(weight)
print("The tallest is %s with %.2fcm"% (name[height.index(max_h)],max_h))
print("The heaviest is %s with %.2fkg"% (name[weight.index(max_w)],max_w))


