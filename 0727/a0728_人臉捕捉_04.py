import numpy as np
import cv2 as cv
import dlib

predictor_path = "shape_predictor_5_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)
img = cv.imread("face_nbagsw.jpg")
img_gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
nums = detector(img_gray,0)
for i in range(len(nums)):
    landmarks = np.matrix([[p.x, p.y]for p in predictor(img,nums[i]).parts()])
    for idx, point in enumerate(landmarks):
        pos = (point[0,0], point[0,1])
        print(idx,pos)
        cv.circle(img, pos, 3, color=(0,255,0))
        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(img, str(idx+1), pos, font, 0.4, (0,0,255), 1, cv.LINE_AA)
cv.imshow("img",img)
cv.waitKey()
