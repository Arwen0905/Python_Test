'''
=>RGB色彩空間
R(紅)G(綠)B(藍),三者重要性相等
"但忽略亮度資訊"
為硬體角度的色彩模型
以人眼觀看,存在一定差異程度
=>HSV色彩空間:
    視覺感知的色彩模型
    以心理學及視覺角度,指出人類視覺感知包含三部分:
1.色調(色相)Hue:光的顏色
設定值範圍:0~360
0紅、60黃、120綠、180青、240藍、300品紅

2.飽和度(Saturation):色彩深淺程度
  為 比例值,範圍:0~1
  是色彩純度值與最大純色度值之比值
  飽和度 = 0 , 即為灰階
  
3.明暗(Value):光的明暗程度
  範圍:0~1
   H S V
   0 1 1 → 深紅色(較亮)
 120 a3 a4 →淺綠(教暗)

=>函數:cvtColor()色彩空間轉換
cvtColor(src,mode) 色彩空間轉換
        原始影像
openCV色彩模型為BGR,與RGB不同
'''
import cv2 as cv
import numpy as np
img = np.random.randint(0,256,size=[2,4,3],dtype=np.uint8)
rst = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
print('img = \n',img)
print('rst = \n',rst)
print('像素點 (1,0) 直接計算得到的值 =',
      img[1,0,0]*0.114+img[1,0,1]*0.587+img[1,0,2]*0.299)
print('像素點(1,0) 使用公式 cv.cvtColor() 轉換值 =',rst[1,0])











