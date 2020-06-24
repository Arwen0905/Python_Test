import cv2 as cv
img = cv.imread('../0610/lena_01.jpg',0)
a = img
result1 = a+img
result2 = cv.add(img,a)
cv.imshow('imgae',img)
cv.imshow('imgae',result1)
cv.imshow('imgae',result2)
cv.waitKey()
