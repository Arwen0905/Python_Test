# 1. 題目說明:
# 請開啟PYD105.py檔案，依下列題意進行作答，計算矩形之面積和周長，
# 使輸出值符合題意要求。作答完成請另存新檔為PYA105.py再進行評分。

# 2. 設計說明：
# 請撰寫一程式，輸入兩個正數，代表一矩形之寬和高，
# 計算並輸出此矩形之高（Height）、寬（Width）、周長（Perimeter）
# 及面積（Area）。

# 提示：輸出浮點數到小數點後第二位。

# 3. 輸入輸出：
# 輸入說明
# 高、寬

# 輸出說明
# 高
# 寬
# 周長
# 面積

# 輸入輸出範例
# 範例輸入
# 23.5
# 19
# 範例輸出
# Height = 23.50
# Width = 19.00
# Perimeter = 85.00
# Area = 446.50

h,w = 23.5,19
# h = eval(input())
# w = eval(input())
Perimeter = (w+h)*2
Area = w*h
print('Height = %.2f' % h)
print('Width = %.2f' % w)
print('Perimeter = %.2f' % Perimeter)
print('Area = %.2f' % Area)

"""
Height = _
Width = _
Perimeter = _
Area = _
"""