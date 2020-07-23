import cv2 as cv

img = cv.imread('AAA.jpg')
pict = 'haarcascade_frontalface_default.xml'
faceCascade = cv.CascadeClassifier(pict)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(gray, scaleFactor=1.20,\
                                     minNeighbors=4, minSize=(5,5))
print(faces)
print('find{0} face!'.format(len(faces)))

for(x,y,w,h) in faces:
    # cv.rectangle(img,(x,y),(x+w,y+w),(0,255,0),2)
    cv.circle(img,(int((x+x+w)/2),int((y+y+h)/2)),int(w/2),
              (0,255,0),2)

cv.imshow('img',img)
cv.waitKey()
