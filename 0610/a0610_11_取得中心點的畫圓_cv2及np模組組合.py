import cv2 as cv
import numpy as np
# 產生黑色底圖
img = np.zeros((512,512,3),dtype="uint8")
for r in range(100,175,25): #(起始數,半徑,線條間距)
    cv.circle(img,(img.shape[1] // 2,img.shape[0] // 2),r,(44,22,255))

cv.imshow('image',img)
x = cv.waitKey()
if x == 27:
    cv.destroyAllWindows()
    
'''
陣列的前2個維度為圖片的高度、寬度
img.shape[0] → (行)圖片垂直高度
img.shape[1] → (列)圖片水直高度
img.shape[2] → 圖片channel數
第三維是圖片色彩 channel →
RGB圖片: channel=3
        灰階: channel=1
'''