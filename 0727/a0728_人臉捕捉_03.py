import cv2
import imutils
import dlib
from imutils.face_utils import FaceAligner
from imutils import face_utils

predictor_path = "shape_predictor_5_face_landmarks.dat"
face_path = "lena_01.jpg"

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)
fa = FaceAligner(predictor, desiredFaceWidth=256)

image = cv2.imread(face_path)
image = imutils.resize(image, width=800)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Input",image)
rects = detector(gray, 2)

for rect in rects:
    (x, y, w, h) = face_utils.rect_to_bb(rect)
    faceOrig = imutils.resize(image[y:y + h, x:x + w], width=256)
    faceAligned = fa.align(image, gray, rect)
    
    cv2.imshow("Original", faceOrig)
    cv2.imshow("Aligned", faceAligned)
    cv2.waitKey()


