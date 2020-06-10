import cv2 as cv
import numpy as np
# d = 400
img = np.ones((400,500,3),dtype="uint8")*255
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,"Open CV",(20,150),font,3,(0,0,255),15,cv.LINE_AA)
cv.putText(img,"Open CV",(20,220),font,3,(0,255,0),15\
           ,cv.FONT_HERSHEY_SCRIPT_SIMPLEX,True)
cv.imshow('image',img)
cv.waitKey()
cv.destroyAllWindows()

