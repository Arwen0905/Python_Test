import cv2 as cv
import numpy as np
n = 300
# 先產生一個 n等於300，所以 (300 * 300 , 每個元素都是3，再*255，結果為白色圖片
img = np.ones((n,n,3),np.uint8)*255
                                                # -1 等於條滿
img = cv.rectangle(img, (50,50), (n-100,n-50), (0,0,255),-1)
cv.imshow('image',img)
cv.waitKey()
