import cv2 as cv
import numpy as np
n = 300
img = np.zeros((n+1,n+1,3), np.uint8)
img = cv.line(img,(0,0),(n,n),(255,0,0),3)
img = cv.line(img,(0,100),(n,100),(0,255,0),1)
img = cv.line(img,(100,0),(100,n),(0,0,255),6)
cv.imshow('image',img)
# cv.waitKey()
x = cv.waitKey()
if x == 27:
    cv.destroyAllWindows()
