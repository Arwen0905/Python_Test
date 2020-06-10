import cv2 as cv
import numpy as np
d = 400
# 產生白色底圖 *255
img = np.ones((d,d,3),dtype="uint8")*255
                    # round(數值,小數位數)
(centerX,centerY) = (round(img.shape[1]/2),round(img.shape[0]/2))
color = (0,0,0)
                # round(d變數/2)
for r in range(5,round(d/2),12):
    cv.circle(img,(centerX,centerY),r,color,3)
cv.imshow('image',img)
x = cv.waitKey()
cv.destroyAllWindows()


'''
└ 畫圓:
cv2.dllipse(img, 圓心, (軸1,軸2),旋轉角度,
圓弧結束角度,color, thickness, linetype)

round函數:		┌ 預設維整數位
round(數值, 小數位數,)
	將數值取小數位數的四捨五入值
'''