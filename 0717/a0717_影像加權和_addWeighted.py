'''
影像加權和:
    計算影像像素值合併加入
    加權值計算
使用函數:addWeighted
addWeighted(src1,a,src2,b,c)
            影像1、影像1加權、影像2、影像2加值、亮度調節
公式:src1*a+src2*b+c
'''
import cv2 as cv
import numpy as np
# img1 = np.ones((3,4,3),dtype=np.uint8)*100
# img2 = np.ones((3,4,3),dtype=np.uint8)*10
# a = 3
# img3 = cv.addWeighted(img1, 0.6, img2, 5, a)
# print(img3)
# ========================================================
# 透明合成
# img1 = cv.imread('landscape512.jpg')
# img2 = cv.imread('Lena512.jpg')
# result = cv.addWeighted(img1,0.6,img2,0.4,0)
# cv.imshow('image1',img1)
# cv.imshow('image2',img2)
# cv.imshow('image3',result)
# cv.waitKey()
# ========================================================
'''
※兩影像大小及類型必須相同
=>ROI:Region Of Interest
'''
# 鈔票合成
# img = cv.imread('lena_01.jpg')
# US1 = cv.imread('US1_600.jpg')
# cv.imshow("image",img)
# cv.imshow("banknote",US1)
# img_face = img[80:230,250:370]
# US1_face = img[80:230,240:360]
# add = cv.addWeighted(img_face, 0.6, US1_face, 0.4, 0)
# US1[80:230,240:360] = add
# cv.imshow('result',US1)
# cv.waitKey()
'''
逐位元邏輯運算
bitwise_and:且
bitwise_or:或
bitwise_xor:拆
bitwise_not:反向
and運算:
兩個運算元(邏轉值)都為真
其結果為真
函數:bitwise_and
bitwise_and(src1.src2)
任何數值n與數值0 and運算，結果為0
任何數值n與數值255做and運算結果為數值n本身
    1101
and)1011
    1001
以上述定理可建立掩膜影像，只有兩個值 0.255
'''
# img1 = np.random.randint(0,255,(5,5),dtype=np.uint8)
# img2 = np.zeros((5,5),dtype=np.uint8)
# img2[0:3,0:3] = 255
# img2[4,4] = 255
# a = cv.bitwise_and(img1,img2)
# print("img1 = \n",img1)
# print("img2 = \n",img2)
# print("a = \n",a)
#============================================================
# 缺一塊區域
# img1 = cv.imread('lena512.jpg',0)
# img2 = np.zeros(img1.shape,dtype=np.uint8)
# img2[100:400,200:400] = 255
# img2[100:500,100:200] = 255
# a = cv.bitwise_and(img1,img2)
# cv.imshow("img1",img1)
# cv.imshow("img2",img2)
# cv.imshow("a",a)
# cv.waitKey()
'''
or運算:
    兩個運算元(邏輯值)有一個為真
    結果為真
函數:bitwise_or
'''
# img1 = cv.imread('lena512.jpg',1)
# img2 = np.zeros(img1.shape,dtype=np.uint8)
# img2[100:400,200:400] = 255
# img2[100:500,100:200] = 255
# a = cv.bitwise_and(img1,img2)
# cv.imshow("img1",img1.shape)
# cv.imshow("img2",img2.shape)
# cv.imshow("a",a)
# cv.waitKey()
'''
not運算:
    將運算元反向
    函數 bitwise_not(src)
add函數:
    add(src1,src2,mask) #有必要加入第三項參數，則會稱為"mask"(掩膜特定範圍)
'''
# img1 = np.ones((4,4),dtype=np.uint8)*3
# img2 = np.ones((4,4),dtype=np.uint8)*5
# mask = np.zeros((4,4),dtype=np.uint8)
# mask[2:4,2:4]=1
# img3 = np.ones((4,4),dtype = np.uint8)*66
# print("img1 = \n",img1)
# print("img2 = \n",img2)
# print("mask = \n",mask)
# print("初值 img3 = \n",img3)
# img3 = cv.add(img1,img2,mask = mask) # mask:意旨跟0運算就為0
# print("求和後 img3 = \n",img3)
# ======================================================
'''
位元平面分解
=>將灰階影像中同一個位元上的二進位像素值進行組合
可得到一個二進位影像
該影像稱為"灰階影像的位元平面"
其組合過程稱為"位元平面分解"
=>灰階影像中，每一項似使用8位元，
二進位值表示值的範圍為0~255，

表示為:a7*2^7 + a6*2^6 + a5*2^5 + a4*2^4 + 
       a3*2^3 + a2*2^2 + a1*2^1 + a0*2^0

a7~a0 的值為0或1
a7值對影像影響最大
a0值對影像影響最小

a7加權最高，其位元平面與後影像相關性最高

'''
# img = cv.imread('Lena512.jpg',1)
# w,h,c= img.shape
# mask =np.zeros((w,h),dtype=np.uint8)
# mask[100:400,200:400]=255
# mask[100:500,100:200]=255
# c=cv.bitwise_and(img,img,mask=mask)
# print("img.shape= ",img.shape)
# print("mask.shape= ",mask.shape)
# cv.imshow("img",img)
# cv.imshow("mask",mask)
# cv.imshow("c",c)
# cv.waitKey()
# =====================================================
# img = cv.imread('Lena512.jpg',0)
# cv.imshow('image',img)
# r,c = img.shape
# x = np.zeros((r,c,8),dtype=np.uint8)

# for i in range(8):
#     x[:,:,i] = 2**i
# r = np.zeros((r,c,8),dtype=np.uint8)

# for i in range(8):
#     r[:,:,i] = cv.bitwise_and(img,x[:,:,i])
#     mask = r[:,:,i]>0
#     r[mask]=255
#     cv.imshow(str(i),r[:,:,i])
# cv.waitKey()
'''
=>原始影像與金鑰影像
進行"互斥運算"，產生加密影像(encruption)
=>加密影像與金鑰影像
進行"互斥運算"，產生解密影像(decryption)
=>a:原始資料(明文)，b:金鑰
C:加密(xor(a,b))
xor(a,b)=c , xor(c,b)=a
=>位元運算可實踐像素點加密
通常須處理的像素點為灰階值，如某項素點值為216(明文)
以178(此值油加密者自行決定)作為加密金鑰將此二數值進行互斥運算

bitwise_xor(216,178) = 106 加密
bitwise_xor(106,178) = 216 解密

    11011000(216) <<明文
xor)10110010(178) <<金鑰
    -------------
    01101010(106) <<加密

'''
# img = cv.imread('Lena512.jpg',0)
# cv.imshow('image',img)
# r,c = img.shape
# key = np.random.randint(0,256,size=[r,c],dtype=np.uint8)
# encryption = cv.bitwise_xor(img,key)
# decryption = cv.bitwise_xor(encryption,key)
# cv.imshow('image',img)
# cv.imshow('key',key)
# cv.imshow('encryption',encryption)
# cv.imshow('decryption',decryption)
# cv.waitKey()
'''
浮水印(資訊隱藏)
=>最低有數位(Least Significant Bit;LSB)
  └ 二進位數字中的第0位(最低有效位)
  即將載體影像的LSB取代為需要隱藏的"二值影像"，以達到二值影像隱藏的目的
  因二值影像處於載體影像的LSB上，
  對載體影像影響非常不明顯，故具較高的隱僻性
  
=>將影像二值化(處理為灰階)
灰階二值影像中，像素值
只有 0 , 255，表示為黑色、白色 (注意 0,255 非二進位)
將255轉為1，可得到二進位的灰階影像，只用一個位元表達像素值.
'''
# img = cv.imread('Lena512.jpg',0)
# watermark = cv.imread('watermark.jpg',0)
# w = watermark[:,:]>0 
# watermark[w] = 1 #將255轉成1 變成2次方 (0,1) 否則255並不是2次方
# r,c = img.shape #取得原始影像的大小尺寸

# #254以下的分出來，目的將255獨立出來，產生陣列
# t254 = np.ones((r,c),dtype=np.uint8)*254
# imgh7 = cv.bitwise_and(img,t254) #先and運算，取得影像的高7位
# #再or運算，將高7位與watermark運算，藉此將watermark遷入至高7位
# # === 在此之前為 處理浮水印運算 ===
# e = cv.bitwise_or(imgh7,watermark)
# t1 = np.ones((r,c),dtype=np.uint8)
# wm = cv.bitwise_and(e,t1) #透過and運算，載體e 與 t1 作運算
# print(wm)
# w = wm[:,:]>0
# wm[w] = 255

# cv.imshow('ima',img)
# cv.imshow('watermark',watermark)
# cv.imshow('e',e)
# cv.imshow('wm',wm)
# cv.waitKey()
# ===================================================
img = cv.imread('Lena512.jpg',0)

r,c = img.shape
mask = np.zeros((r,c),dtype = np.uint8)
mask[100:400,200:400] = 1

key = np.random.randint(0,256,size=[r,c],dtype=np.uint8)
imgxorkey = cv.bitwise_xor(img,key)
encryptFace = cv.bitwise_and(imgxorkey,mask*255)
noface1 = cv.bitwise_and(img,(1-mask)*255)
maskface = encryptFace + noface1
extract0riginal = cv.bitwise_xor(maskface,key)
extractFace = cv.bitwise_and(extract0riginal,mask*255)
noface2 = cv.bitwise_and(maskface,(1-mask)*255)
extractimg = noface2 + extractFace

cv.imshow('img',img)
cv.imshow('mask',mask*255)
cv.imshow('1-mask',(1-mask)*255)
cv.imshow('key',key)
cv.imshow('imgxorkey',imgxorkey)
cv.imshow('encryptFace',encryptFace)
cv.imshow('noface1',noface1)
cv.imshow('maskface',maskface)
cv.imshow('extract0riginal',extract0riginal)
cv.imshow('extractFace',extractFace)
cv.imshow('noface2',noface2)
cv.imshow('extractimg',extractimg)
cv.waitKey()
