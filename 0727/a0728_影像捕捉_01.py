import dlib
import cv2 as cv
cap = cv.VideoCapture("short_hamilton_clip.mp4")
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
fourcc = cv.VideoWriter_fourcc(*"XVID")
out = cv.VideoWriter("output.avi",fourcc,20.0,(width,height))
detector = dlib.get_frontal_face_detector()

while(cap.isOpened()):
    ret, frame = cap.read()
    
    face_rects, scores, idx = detector.run(frame,0)
    
    for i,d in enumerate(face_rects):
        x1 = d.left()
        y1 = d.top()
        x2 = d.right()
        y2 = d.bottom()
        text = "%2.2f(%d)" % (scores[i], idx[i])
        
        cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 4, cv.LINE_AA)
        
        cv.putText(frame, text, (x1, y1), cv.FONT_HERSHEY_DUPLEX,
                   0.7, (255, 255, 255), 1, cv.LINE_AA)
    out.write(frame)
    
    cv.imshow("Video face Detection", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
out.release()
cv.destroyALLWindows()