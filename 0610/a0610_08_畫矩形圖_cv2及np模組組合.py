import cv2 as cv
import numpy as np
img = np.zeros((512,512,3),np.uint8)
cv.rectangle(img,(384,0),(510,128),(0,255,0),5)
cv.imshow('image',img)
cv.waitKey()
