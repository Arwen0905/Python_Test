import cv2 as cv
import numpy as np
img = np.zeros((512,512,3), np.uint8)
cv.circle(img, (477,63), 63, (0,0,255), -1)
cv.imshow('image', img)
x = cv.waitKey()
if x == 27:
    cv.destroyAllWindows()
