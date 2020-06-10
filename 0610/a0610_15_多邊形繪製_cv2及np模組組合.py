import cv2 as cv
import numpy as np
img = np.zeros((512,512,3), np.uint8)
pts = np.array([[10,5],[60,90],[130,80],[110,70]], np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(img, [pts], True, (0,255,255))
cv.imshow('image',img)
cv.waitKey()
cv.destroyAllWindows()

