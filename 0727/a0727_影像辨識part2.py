# import cv2 as cv
# pict = "haarcascade_frontalface_default.xml"
# faceCascade = cv.CascadeClassifier(pict)

# img = cv.imread("face_francefoot.jpg")
# faces = faceCascade.detectMultiScale(img, scaleFactor=1.1,
#          minNeighbors=5, minSize=(25,25),flags = cv.CASCADE_SCALE_IMAGE)

# cv.rectangle(img, (10,img.shape[0]-20),(110,img.shape[0]), (0,0,0),-1)
# cv.putText(img,"Find "+str(len(faces)) + " face!",
#             (10,img.shape[0]-5),cv.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)

# for (x,y,w,h) in faces:
#     cv.rectangle(img,(x,y),(x+w, y+h),(128,255,0),2)
# cv.namedWindow("facedetect")
# cv.imshow("facedetect",img)
# cv.waitKey()

# import cv2 as cv
# pict = "haarcascade_frontalface_default.xml"
# # faceCascade 分類器物件
# faceCascade = cv.CascadeClassifier(pict)
# # 讀入待辨識影像
# img = cv.imread("face_execuite.jpg")
# # 偵測影像的方法
# faces = faceCascade.detectMultiScale(img, scaleFactor=1.2, #原1.1
#          minNeighbors=3, minSize=(20,20),flags = cv.CASCADE_SCALE_IMAGE)
#                     # 越小對小臉越敏銳
# # 執行完畢傳回(臉部)資訊
# cv.rectangle(img, (img.shape[1]-140 ,img.shape[0]-20),
#             (img.shape[1],img.shape[0]),(0,255,255),-1)

# cv.putText(img,"Finding "+str(len(faces)) + " face!",
#             (img.shape[1]-135, img.shape[0]-5),
#             cv.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 1)

# for (x,y,w,h) in faces:
#     cv.rectangle(img,(x,y),(x+w, y+h),(255,0,0),2)
# cv.namedWindow("Face",cv.WINDOW_NORMAL)
# cv.imshow("Face",img)
# cv.waitKey()

# import cv2 as cv
# pict = "haarcascade_frontalface_default.xml"
# # faceCascade 分類器物件
# face_cascade = cv.CascadeClassifier(pict)

# eyepict = "haarcascade_eye.xml"
# eye_cascade = cv.CascadeClassifier(eyepict)

# img = cv.imread('face_trumpfamily.jpg')
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# # 偵測影像的方法
# faces = face_cascade.detectMultiScale(gray, scaleFactor=1.15,
#           minNeighbors=10, minSize=(20,20))


# for (x,y,w,h) in faces:
#     cv.rectangle(img,(x,y),(x+w, y+h),(255,0,0),2)
#     roi_gray = gray[y:y+h , x:x+w]
#     roi_color = img[y:y+h , x:x+w]
    
#     eyes = eye_cascade.detectMultiScale(roi_gray)
#     for(ex,ey,ew,eh) in eyes:
#         cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
# cv.imshow("Face",img)
# cv.waitKey()


# import cv2 as cv
# from PIL import Image
# case_pict = "haarcascade_frontalface_default.xml"
# # faceCascade 分類器物件
# faceCascade = cv.CascadeClassifier(case_pict)
# # 讀入待辨識影像
# imagename = "face_trumpfamily.jpg"
# image = cv.imread(imagename)
# # 偵測影像的方法
# faces = faceCascade.detectMultiScale(image, scaleFactor=1.1,
#           minNeighbors=9, minSize=(30,30),flags= cv.CASCADE_SCALE_IMAGE)
# count = 1
# for (x,y,w,h) in faces:
#     cv.rectangle(image, (x,y), (x+w,y+h),(128,255,0),2)
#     filename = str(count)+ '.jpg'
#     image1 = Image.open(imagename)
#     image2 = image1.crop((x,y,x+w,y+h)) # crop裁切
#     image3 = image2.resize((200,200),Image.ANTIALIAS) # resize重置
#                                           # 影像最佳化
#     res = ".\face" + filename
# cv.namedWindow("facedetect")
# cv.imshow("facedetect",image)
# cv.waitKey()

import cv2 as cv
from PIL import Image

pictPict = "haarcascade_mcs_nose.xml"
face_cascade = cv.CascadeClassifier(pictPict)

# 讀入待辨識影像
img = cv.imread("people_01.jpg")
# 偵測影像的方法
faces = face_cascade.detectMultiScale(img, scaleFactor=1.1,
          minNeighbors=5, minSize=(10,10))

cv.rectangle(img,(img.shape[1]-140,img.shape[0]-20),
             (img.shape[1]-135, img.shape[0]),(0,255,255),-1)

cv.putText(img, 'Finded '+str(len(faces))+ ' face',
           (img.shape[1]-135, img.shape[0]-5),
             cv.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0), 1)

num = 1
for (x,y,w,h) in faces:
    cv.rectangle(img, (x,y), (x+w,y+h),(255,0,0),2)
    filename = str(num) + '.jpg'
    image = Image.open("people_01.jpg")
    imageCrop = image.crop((x,y,x+w,y+h)) # crop裁切
    imageResize = imageCrop.resize((150,150),Image.ANTIALIAS) # resize重置
    res = "face" + filename
    imageResize.save(res)
    num += 1

cv.imshow("Face",img)
cv.waitKey()