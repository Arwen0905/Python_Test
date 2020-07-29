import cv2 as cv
img = cv.imread('AAA.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (5,5), 0)
cny = cv.Canny(blur, 30, 150)
cv.imshow("img",img)
cv.imshow("gray" ,gray)
cv.imshow("blur",blur)
cv.imshow("cny",cny)
cv.waitKey()