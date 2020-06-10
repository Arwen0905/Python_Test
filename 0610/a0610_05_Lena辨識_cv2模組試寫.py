import cv2 as cv
# 基本使用 cv影像辨識
# img = cv.imread('lena.jpg')
# cv.namedWindow('image')
# cv.imshow('image',img)
# cv.waitKey()


# 裁切圖片
# x,y = 100,100
# w,h = 150,250
# crop_img = img[y:y+h,x:x+w]
# cv.imshow('lena',crop_img)
# cv.waitKey(5)

# a0610範例05
img = cv.imread('tpe101.jpg',0)
cv.imshow('image',img)
x = cv.waitKey()
# 27 等於 (鍵盤按鍵:ESC)
if x == 27:
    cv.destroyAllWindows()
elif x == ord('s'):
    cv.imwrite('tpe101gray.png',img)
    cv.destroyAllWindows()
# 可調整的視窗大小
    
print(ord('s'))