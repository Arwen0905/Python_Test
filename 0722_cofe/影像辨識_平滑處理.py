# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 15:42:11 2020

@author: Amanda Lu
"""

#0721
#前為色彩幾何處理

'''影像平滑處理   (平滑處理 == 影像濾波)
        在儲存影像細節特徵之條件下
        對影像進行 雜訊(噪點) 抑制
        
    濾波的目的:
        清除(抑制)雜訊
        提取影像特徵---->辨識依據
    濾波的要求:
        清晰  完整  不可損壞影像的邊緣(輪廓)

共有5大濾波
    
    1.均值濾波:
        以目前像素點周圍 n * n 範圍的像素值的平均值
        *雜質去除後 就會變模糊 去掉越多雜質 越模糊
        
    均值:
        即平均值 將類似的影像 先找一個中心點 以 n*n 範圍的像素值加總平均
        寫入覆蓋原影像像素值
        通常用於銳利度較高的影像使其顯示較為自然
        
    blur()
    
    cv.blur(src,ksize,anchor,borderType)
        
    src 原始影像
    ksize 濾波大小 均值處理中鄰近範圍的高度 寬度
    anchor 錨點 目前計算均值的點
                位於該 核中心點的位置
                使用預設值即可   預設值X=-1 Y=-1
    borderType  自動填充圖像邊界



'''

#前12個為色彩 幾何處理

#13  去噪點
import cv2 as cv
img =cv.imread(r'D:\Desktop\class\python\lena512_noisy.png')
r5 =cv.blur(img, (5,5)) #去掉噪點越多越容易模糊
r30 =cv.blur(img, (30,30))
cv.imshow('img', img)
cv.imshow('r5', r5)
cv.imshow('r30', r30)
cv.waitKey()

#14  加噪點
import cv2 as cv
import numpy as np
img =cv.imread(r'D:\Desktop\class\python\lena512.jpg',1)
rows,cols,ch =img.shape #shape 取出三個==高 寬 色彩通道
for i in range(10000):
    x =np.random.randint(0,rows) 
    y =np.random.randint(0,cols)
    img[x,y,:] =255 #當時所在的像點 :不設影像通道
cv.imshow('noise', img)
cv.imwrite(r'D:\Desktop\class\python\lena512_no1.jpg', img)
cv.waitKey()
#均值濾波 把14的噪點濾掉
import cv2 as cv
img =cv.imread(r'D:\Desktop\class\python\lena512_no1.jpg')
r5 =cv.blur(img, (5,5)) #去掉噪點越多越容易模糊
r30 =cv.blur(img, (30,30))
cv.imshow('img', img)
cv.imshow('r5', r5)
cv.imshow('r30', r30)#噪點去掉 就會變模糊
cv.waitKey()


#15
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img =cv.imread(r'D:\Desktop\class\python\lena512_no1.jpg',1)
rst =cv.cvtColor(img, cv.COLOR_BGR2RGB)

final =cv.blur(rst,(5,5))
titles =['Source','Blur']
images =[rst,final]
for i in range(2):
    plt.subplot(1, 2,i+1),plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()


#16 水平堆疊 兩張圖放一起
import cv2 as cv
import numpy as np
img =cv.imread(r'D:\Desktop\class\python\lena512_noisy.png',1)
bl =np.hstack([cv.blur(img,(3,3)), cv.blur(img, (15,15))])
cv.imshow('img', img)
cv.imshow('result', bl)
cv.waitKey()


'''

np.hstack 水平方向堆疊 

np.vstack 垂直方向堆疊


'''


'''
   2.方框濾波:
       可自行設定濾波結果為 平均值 或 加總覆蓋原像素值
       
       boxFilter()
       
       cv.boxFilter(src,ddepth,ksize,amchor,normalize,borderType)
       
       ddepth 影像深度 ==表達的顏色數(顏色度越多表示越深)
       每一像素能展示的顏色數 一般使用 -1 表示與原始影像持用相同的影像深度
       
       normalize 
           1:為預設值   即為均值濾波 功能同 blur()
           0:若加總超過255(最大值) 則會得到白色影像



'''

#17 方框濾波 同均值濾波(平均值)
import cv2 as cv
img =cv.imread(r'D:\Desktop\class\python\lena512_noisy.png',0)
r =cv.boxFilter(img, -1, (5,5)) 
cv.imshow('img', img)   
cv.imshow('result', r)
cv.waitKey()   #去掉大部分噪點 以及出現模糊


#18 方框濾波 加總
import cv2 as cv
img =cv.imread(r'D:\Desktop\class\python\lena512_noisy.png',0)
r =cv.boxFilter(img, -1, (5,5),normalize =0) 
cv.imshow('img', img)   
cv.imshow('result', r)
cv.waitKey() #超過255 ==白色一片























































