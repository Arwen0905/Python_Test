from PIL import ImageFont, ImageDraw, Image
import cv2 as cv
import numpy as np
img = np.zeros((512,512,3),np.uint8)
img.fill(64)
img[:]=(0,0,192) #bgr 呈現紅色
text = '恭賀\n新囍'

fontPath = 'TaipeiSansTCBeta-Bold.ttf'

font = ImageFont.truetype(fontPath, 224)

# 將numpy陣列，轉成pil影像
imgPil = Image.fromarray(img)

draw = ImageDraw.Draw(imgPil)
draw.text((30,30), text, font=font, fill=(0,0,0,0))

img = np.array(imgPil)
cv.imshow('image',img)
cv.waitKey()
cv.destroyAllWindows()
