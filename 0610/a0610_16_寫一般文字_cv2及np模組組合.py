import cv2 as cv
import numpy as np
# 繪圖區預設定
img = np.zeros((512,1080,3),np.uint8)
# 字型設定
font = cv.FONT_HERSHEY_SCRIPT_SIMPLEX
# 寫文字(繪圖區,'要寫的文字',(從哪裡寫),字型,字體大小,顏色,線條厚度,反鋸齒處理,True(開啟映射))
cv.putText(img, 'Open-CV', (10,350), font, 4, (255,255,255), 5, cv.LINE_AA)
cv.imshow('image', img)
cv.waitKey()
cv.destroyAllWindows()
