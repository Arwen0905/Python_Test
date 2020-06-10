import cv2 as cv
import numpy as np
img = np.zeros((512,512,3),np.uint8)
# 填充像素
img.fill(64)
text = "OpenCV for Python"
cv.putText(img, text, (10,40),cv.FONT_HERSHEY_SIMPLEX,\
           1,(0,255,255),1,cv.LINE_AA)
cv.putText(img, text, (10,80),cv.FONT_HERSHEY_PLAIN,\
           1,(0,255,255),2,cv.LINE_AA)
cv.putText(img, text, (10,120),cv.FONT_HERSHEY_DUPLEX,\
           1,(0,255,255),1,cv.LINE_AA)
cv.putText(img, text, (10,160),cv.FONT_HERSHEY_COMPLEX,\
           1,(0,255,255),2,cv.LINE_AA)
cv.putText(img, text, (10,200),cv.FONT_HERSHEY_TRIPLEX,\
           1,(0,255,255),1,cv.LINE_AA)
cv.putText(img, text, (10,240),cv.FONT_HERSHEY_COMPLEX_SMALL,\
           1,(0,255,255),2,cv.LINE_AA)
cv.putText(img, text, (10,280),cv.FONT_HERSHEY_SCRIPT_SIMPLEX,\
           1,(0,255,255),1,cv.LINE_AA)
cv.putText(img, text, (10,320),cv.FONT_HERSHEY_SCRIPT_COMPLEX,\
           1,(0,255,255),2,cv.LINE_AA)
cv.imshow('imgae',img)
cv.waitKey()
cv.destroyAllWindows()
