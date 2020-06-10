import cv2 as cv
import numpy as np
d = 400
img = np.ones((d,d,3),dtype="uint8")
font = cv.FONT_HERSHEY_SIMPLEX
img.fill(0)
# 運用 thickness的線條粗細度來產生文字描邊
cv.putText(img,"Open CV",(0,200),font,3,(255,255,255),15)
cv.putText(img,"Open CV",(0,200),font,3,(0,0,255),5)
cv.imshow('image',img)
cv.waitKey()
cv.destroyAllWindows()
