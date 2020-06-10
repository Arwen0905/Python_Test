import cv2 as cv
import numpy as np
d = 400
# 產生繪圖區，高400寬400，彩色通道3，type設定，最後將pixel像素*255
img = np.ones((d,d,3),dtype="uint8")*255
# 運用 round取取整數的方法，以(直徑400/2) 取得正整數
center = (round(d/2),round(d/2))
# 尺寸設定(100,200)
size = (100,200)
for i in range(0,10):
    # 角度設定: 以numpy的隨機產生值設定
    angle = np.random.randint(0,361)
    # 顏色設定: 以numpy的隨機產生值設定 ※
    color = np.random.randint(0, high=256, size=(3,)).tolist()
    # thickness → 線條粗細設定: 以numpy的隨機產生值設定(x,y)
    thickness = np.random.randint(1,9)
    # 橢圓形:參數設置
    cv.ellipse(img,center,size,angle,0,360,color,thickness)
    
cv.imshow('image',img) # 呈現
cv.waitKey() # 關閉
cv.destroyAllWindows() # ESC關閉

'''
└ 畫多邊形:
cv2.polylines(img, 頂點座標, isClosed, color, thickness, linetype)
頂點座標必須是一個陣列(串列)
其資料型態必須為 numpy.int32
繪圖前必須以 reshape 為頂點→重新計算調整
reshape = 形狀
'''