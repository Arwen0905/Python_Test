# 給定一個整數數組nums 和一個目標值target，
# 請你在該數組中找出和為目標值的那兩個整數，
# 並返回他們的數組下標。

# 你可以假設每種輸入只會對應一個答案。但是，
# 你不能重複利用這個數組中同樣的元素。

# 範例
# 給定nums = [2, 7, 11, 15], target = 9
# 因為nums[0] + nums[1] = 2 + 7 = 9
# 所以返回[0, 1]

# 解題思路
# 用字典保存遍歷過的數字和下標
# 尋找target-nums[i]是否在字典中出現過，是則返回兩數的下標
# 否則存入nums[i]及其下標

nums = [2,7,11,15]
target = 9
# nums = eval(input())
# target = eval(input())
for i in range(len(nums)): #0,4
    for j in range(i+1,len(nums)): #0+1,4
        if nums[i]+nums[j]==target:
            print(i,j)
