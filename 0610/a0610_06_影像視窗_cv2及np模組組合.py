import cv2 as cv
import numpy as np
img = np.zeros((512,512,3), np.uint8)
# cv2.line(img, (起點座標,終點座標),(color),thickness,linetype)
cv.line(img,(0,0),(511,511),(255,0,0),2)
cv.imshow('image', img)
cv.waitKey()
