import dlib
import cv2
import imutils
img = cv2.imread("face_francefoot.jpg")
img = imutils.resize(img, width=1280)
detector = dlib.get_frontal_face_detector()
face_rects = detector(img, 0) #0:一般偵測、1:臉部較小
for i,d in enumerate(face_rects):
    x1 = d.left()
    y1 = d.top()
    x2 = d.right()
    y2 = d.bottom()
    cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 4, cv2.LINE_AA)
cv2.imshow("Face_Detection",img)
cv2.waitKey()
