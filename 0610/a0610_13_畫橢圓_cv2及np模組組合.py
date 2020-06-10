import cv2 as cv
import numpy as np
img = np.zeros((512,512,3),np.uint8)
img.fill(200)
        # (x軸,y軸),(x半徑,y半徑),角度,結束點,直徑,(顏色),線條類型:實心為-1
cv.ellipse(img, (256,256), (250,250), 45, 0, 360, (255, 55, 55),30)
cv.ellipse(img, (256,256), (200,200), 45, 0, 360, (55, 255, 255),40)
cv.ellipse(img, (256,256), (150,150), 45, 0, 360, (44, 22, 255),-1)
# cv.ellipse(img, (180,200), (100,60), 45, 0, 360, (128, 0, 255),2)
# cv.ellipse(img, (180,200), (50,100), 45, 0, 180, (255, 0, 128),-1)
cv.imshow('image', img)
cv.waitKey()
cv.destroyAllWindows()
