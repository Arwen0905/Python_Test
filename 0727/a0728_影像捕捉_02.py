import dlib
import cv2
# 偵測元件
predictor_path = "shape_predictor_5_face_landmarks.dat"
face_path = "face_trumpfamily.jpg" #讀入圖片

def renderFace(im, landmarks, color=(0,255,0), radius=3):
    for p in landmarks.parts():
        cv2.circle(im, (p.x, p.y), radius, color, -1)
        
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)

img = cv2.imread(face_path)

dets = detector(img, 1)

for k,d in enumerate(dets):
    shape = predictor(img, d)
    renderFace(img, shape)

cv2.imshow("face-rendered",img)
cv2.waitKey()