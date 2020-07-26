# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 16:51:25 2020

@author: Amanda Lu
"""
#0717 前為影像辨識 接續色彩

'''色彩空間類型轉換
        
    RGB色彩空間:
        
        R 紅           G 綠         B 藍
        三者為重要性相等  "但忽略亮度資訊"
        為硬體角度的色彩模型 以人眼觀看  存在一定的差異程度
        
    HSV(HSB)色彩空間:
        視覺感知的色彩模型 以心理學及視覺角度 指出人類視覺感知包含三部分:
            1.色調 2.飽和度 3.明度
            
        Hue色調(色相)
            光的顏色 範圍為 0~360
            
            基本款:
                0   紅色
                60  黃色
                120 綠色
                180 青色
                240 藍色
                300 品紅
        
        Saturation飽和度
            色彩顏色深淺程度 為一比例值  範圍 0~1
            是色彩純度值 與 最大純度值 之比值
            飽和度為0==灰階
            
        Value明暗 
            光的明暗程度  範圍 0~1
            
        
        
函數:                     src 原始影像
    色彩空間轉換  cvtColor(src,mode)
                                mode 色彩空間轉換

 
    *opneCV色彩模型為 "BGR"  與 RGB 不同
       RGB / BGR轉換到 GRAY灰階
        
       GRAY灰階=0.299*R + 0.587*G + 0.114*B
'''

#前12在影像辨識

#13
import cv2 as cv
import numpy as np 
img =np.random.randint(0,256,size =[2,4,3],dtype =np.uint8)
rst =cv.cvtColor(img,cv.COLOR_BGR2GRAY)
print('img =\n',img)
print('rst =\n',rst)
print('像素點(1,0) 直接計算得到的值 =',img[1,0,0]*0.114+img[1,0,1]*0.587+img[1,0,2]*0.299)
print('像素點(1,0) 使用公式cv.cvColor() 轉換值 = ',rst[1,0])
     






#=============================================================================
#=============================================================================       
#0720           

#01  灰階轉BGR
import cv2 as cv
import numpy as np
img =np.random.randint(0,256,size =[2,4],dtype =np.uint8)
rst =cv.cvtColor(img, cv.COLOR_GRAY2BGR)
print('img =\n',img)
print('tst =\n',rst)
#當影像由GRAY色彩空間轉換到BGR色彩空間時  最後所有通道值是相同的

#02 RGB to BGR
import cv2 as cv
import numpy as np
img =np.random.randint(0,256,size =[2,4,3],dtype =np.uint8)
rgb =cv.cvtColor(img, cv.COLOR_BGR2RGB)
bgr =cv.cvtColor(img, cv.COLOR_RGB2BGR)
print('img =\n',img)
print('rgb =\n',rgb)
print('bgr =\n',bgr)
#[R G B] [B G R]
#RGB 與 BGR 互相轉換 R通道 與 B通道值互換 

#03 轉灰階要再轉回彩色==彩色裡面的灰階 
import cv2 as cv
import numpy as np
img =cv.imread(r'D:\Desktop\class\python\lena512.jpg')
gray =cv.cvtColor(img, cv.COLOR_BGR2GRAY) #轉灰階
bgr =cv.cvtColor(gray, cv.COLOR_GRAY2BGR)#灰階轉彩色 雖然最後看到還是灰階 但為彩色的灰階

print('img.shape',img.shape)#shape 前兩個數值為尺寸 第三為通道值
print('gray.shape',gray.shape)
print('bgr.shape =',bgr.shape)


cv.imshow('img',img)
cv.imshow('gray',gray)
cv.imshow('bgr',bgr)
print('bgr =\n',bgr)
#cv.imshow('')
cv.waitKey()
#BGR轉換為 GRAY 時 即為灰階影像
#再將該影像轉換為BGR時
#B G R值均為相同  顯示結果仍為灰階



#04
import cv2 as cv
img =cv.imread(r'D:\Desktop\class\python\lena512.jpg')
rgb =cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('img',img)
cv.imshow('rgb',rgb)
cv.waitKey()
            

#print('')
#cv.imshow('')
                     
'''
    色調 H值 
    
    設定範圍為 0~360 
    8位元影像 每個像速點能表示的灰階等級 2^8 =256個
    故8位元影像要以 HSV 表示時 必須將 H值 調整為 0~255
    處理方式:
        將 H值 /2   得到 0~180 之間的值 (適應8位元  二進位儲存即表示)
        
        0:紅        90:青
       30:黃色     120:藍色
       60:綠       150:品紅
-------------------------------------------------------------------------------
    飽和度 S值
    
    設定範圍為 0~1
    因灰階影像之 R G B值 成分相等 相當於一種程度 不飽和的色彩
    故灰階影像其 飽和度 ==0
    灰階影像顯示時 較亮區域 對應之色彩具有較高飽和度
    極低飽和度  所得之色調值==不可靠  (通常不將這種的列入處理範圍)
------------------------------------------------------------------------------
    
    亮度 V值
    
    設定範圍為0~1   對應到 0 255 
    
    BGR2HSV
    
'''          
            
            
#05
import cv2 as cv
import numpy as np
imgblue =np.zeros([1,1,3],dtype =np.uint8)
imgblue[0,0,0] =255 #把0全部設成255
blue =imgblue #測試藍色的HSV值
blue_hsv =cv.cvtColor(blue, cv.COLOR_BGR2HSV)
print('blue =\n',blue)
print('blue_hsv',blue_hsv) #所以第一個為 120==藍色

imggreen =np.zeros([1,1,3],dtype =np.uint8)
imggreen[0,0,1] =255
green =imggreen
green_hsv =cv.cvtColor(green, cv.COLOR_BGR2HSV)
print('blue =\n',green)
print('blue_hsv',green_hsv)
            
imgred =np.zeros([1,1,3],dtype =np.uint8)
imgred[0,0,2] =255
red =imgred
red_hsv =cv.cvtColor(red, cv.COLOR_BGR2HSV)
print('blue =\n',red)
print('blue_hsv',red_hsv)
# HSV色彩主要差異是在 H通道
# 可對 H通道 進行篩選 已選出特定色彩     

'''
    inRange()
        針對像素點 之像素值是否在某範圍內
        
    cv.inRange(src影像,lower範圍下限,upper範圍上限)
                
'''         
#06
import cv2 as cv
import numpy as np
img =np.random.randint(0,256,size =[5,5],dtype =np.uint8)
min =100
max =200
mask =cv.inRange(img,min,max)
print('img =\n',img)
print('mask',mask)   
#若src值  在範圍內  則傳回值中對應位置上之 值為255 否則為0          


#07
import cv2 as cv
import numpy as np
img =np.ones([5,5],dtype =np.uint8)*9
mask =np.zeros([5,5],dtype =np.uint8)
mask[0:3,0] =1
mask[2:5,2:4] =1 #設定要把要顯示出來的設定為1  看不到的預設為0
roi =cv.bitwise_and(img, img,mask=mask) #逐位元運算 mask遮罩 
print('img =\n',img)
print('mask =\n',mask)
print('roi =\n',roi)

''' 
    HSV 色彩空間分布 色彩分析時  並非以分析  特定值
    而是分析 色彩區間
    
    ex藍色的 H值為120
    分析藍色 會以其附近值 作為區間 通常附近值為半徑10
    即 120+10 ,120-10 作為分析區間
    
    S值 V值 通道分析區間為100~255
    因飽和度 亮度太低時 得到的 H值不可靠

    
    HSV色彩區間:
        [H-10,100,100]~[H+10,255,255]
    紅色
        [0,100,100]~[10,255,255] #紅色最低為0 沒有負值
    綠色
        [50,100,100]~[70,255,255]
    藍色
        [110,100,100]~[130,255,255]

    *這上面的為顏色的預設區間 但實際上可以自己設定 並沒有規定一定要在這區間內
    且有時候超過顏色區間 分析出來的顏色較為準確 
    還是要依照 實際的影像去做調整

'''

#08
import cv2 as cv
import numpy as np
img =cv.imread(r'D:\Desktop\class\python\opencv-logo.png')
hsv =cv.cvtColor(img,cv.COLOR_BGR2HSV)#原始圖檔 轉換格式
cv.imshow('img', img)

min_b =np.array([110,50,50])
max_b =np.array([133,255,255]) #指定藍色值的範圍
mask =cv.inRange(hsv, min_b, max_b) #確定藍色的區域  0為不顯示 255為顯示
blue =cv.bitwise_and(img, img,mask=mask)#透過遮罩 and 兩個都為1才為1  1顯示 0不顯示
#兩張做and運算(有影像才會==1 才會顯示) +mask(遮色片) ==藍色顯示出來
cv.imshow('blue', blue)

min_g =np.array([50,50,50])
max_g =np.array([70,255,255])
mask =cv.inRange(hsv, min_g, max_g)
green =cv.bitwise_and(img, img,mask=mask)
cv.imshow('green', green)

min_r =np.array([0,50,50])
max_r =np.array([30,255,255])
mask =cv.inRange(hsv, min_r, max_r)
red =cv.bitwise_and(img, img,mask=mask)
cv.imshow('red', red)

cv.waitKey()


'''
    HSV 膚色分析
    
    一般可設定為:
        色調值 5~170
        飽和度 25~166

    處理並設定 HSV值
    並將其設定為遮罩(mask ; 即 掩膜) ==遮色片(將不要的蓋起來)
    在將影像即遮罩 作位元 and運算
    達到以遮罩控制影像 顯示的目的

'''

#09
import cv2 as cv
import numpy as np
img =cv.imread(r'D:\Desktop\class\python\lena512.jpg')
hsv =cv.cvtColor(img,cv.COLOR_BGR2HSV)
h,s,v =cv.split(hsv)

min_hue =5
max_hue =160
huemask =cv.inRange(h, min_hue, max_hue)

min_sat =25
max_sat =160
satmask =cv.inRange(s, min_sat, max_sat) 

mask =huemask & satmask
roi =cv.bitwise_and(img, img,mask =mask)
cv.imshow('img',img)
cv.imshoe('roi',roi)
cv.waitKey()
            
            

'''
    RGB BGR 原有3個通道 
    再加一個通道名為 alpha 為透明度通道
    即為4個通道的影像 ==  RGBA BGRA 色彩空間
    設定值範圍為:
        
        預設為255
        
        0 ~ 255 or 0透明 ~ 1不透明

    BGR2BGRA
    
'''

#10 alpha通道的性質
import cv2 as cv
import numpy as np
img =np.random.randint(0,256,size =[2,3,3],dtype =np.uint8)
bgra =cv.cvtColor(img, cv.COLOR_BGR2BGRA) #加上alpha
print('img =\n',img)
print('bgra =\n',bgra)

b,g,r,a =cv.split(bgra)
print('a =\n',a) #檢視alpha 預設為255

a[:,:] =125 # :為全部
bgra =cv.merge([b,g,r,a])#.merge(組合成影像 因為剛剛拆開現在重新組合
print('bgra =\n',bgra)



#11
import cv2 as cv
img =cv.imread(r'D:\Desktop\class\python\lena512.jpg')
bgra =cv.cvtColor(img, cv.COLOR_BGR2BGRA)
b,g,r,a =cv.split(bgra)
a[:,:] =125 #透明度 alpha 0~255 
bgra125 =cv.merge([b,g,r,a])

a[:,:] =0
bgra0 =cv.merge([b,g,r,a])
cv.imshow('img',img)
cv.imshow('bgra',bgra)
cv.imshow('bgra125',bgra125)
cv.imshow('bgra0', bgra0)
cv.waitKey()

cv.destroyAllWindows()            
cv.imwrite(r'D:\Desktop\class\python\bgra.png', bgra)
cv.imwrite(r'D:\Desktop\class\python\bgra125.png', bgra125)
cv.imwrite(r'D:\Desktop\class\python\bgra0.png', bgra0)



#12
import cv2 as cv
import numpy as np
img =cv.imread(r'D:\Desktop\class\python\lena_01.jpg')
cv.imshow('img', img)

hsv_low =np.array([0,0,0])
hsv_high =np.array([0,0,0])
def h_low(value):
    hsv_low[0] =value
def h_high(value):
    hsv_high[0] =value
    
def s_low(value):
    hsv_low[1] =value
def s_high(value):
    hsv_high[1] =value

def v_low(value):
    hsv_low[2] =value
def v_high(value):
    hsv_high[2] =value
cv.namedWindow('image')

cv.createTrackbar('h_low', 'image', 0, 255, h_low)
cv.createTrackbar('h_high', 'image', 0, 255, h_high)
cv.createTrackbar('s_low', 'image', 0, 255, s_low)
cv.createTrackbar('s_high', 'image', 0, 255, s_high)
cv.createTrackbar('v_low', 'image', 0, 255, v_low)
cv.createTrackbar('v_high', 'image', 0, 255, v_high)
while(1):
    hsv =cv.cvtColor(img, cv.COLOR_BGR2HSV)
    hsv =cv.inrange(hsv,hsv_low,hsv_high)
    cv.imshow('hsv', hsv)
    if cv.waitKey(1) & 0xFF ==27 :
        break
cv.destroyAllWindows()
        
#-----------------------------------------------------------------------------
#幾何轉換

'''幾何轉換

    影像執行幾何處理時 若無法直接透過對映值 獲得像素點新值時
    則採用 內插法處理(通常放大影像使用)
    內插處理:
        1 INTER_AREA      區域內插  ---->鄰近,最接近區域
        2 INTER_NEAREST   最鄰近內插---->鄰近,最接近區域
最慢 -  3 INTER_CUBIC     三次樣得內插-->像點附近 4*4區域
最快 -  4 INTER_LINEAR    線性內插------>預設
    
    
 影像縮放: resize()
        cv.resize(src,disze,fx,fy,interpolation)
        src 原始影像
        disze 輸出影像大小
        fx 水平縮放比例
        fy 重直縮放比例
        interpolation 內插方式           

'''

#13
import cv2 as cv
import numpy as np
img =np.ones([2,4,3],dtype =np.uint8)
size =img.shape[:2]
rst =cv.resize(img, size)
print('img.shape =\n',img.shape)
print('img =\n',img)
print('rst.shape',rst.shape)
print('rst =\n',rst)
'''

原始影像大小: 2行4列
resize後大小:4行2列
*結果的行數為原始的列數
--------------------------
shape屬性: 第一個值:行   第二個值:列
     
dsize屬性: 第一個值:列   第二個值:行

'''

#14 
import cv2 as cv
img =cv.imread(r'D:\Desktop\class\python\lena512.jpg')
rows,cols =img.shape[:2]

size =(int(cols*0.9),int(rows*0.5))
rst =cv.resize(img,size)

print('img.shape =\n',img.shape)
print('rst.shape =\n',rst.shape)
cv.imshow('img', img)
cv.imshow('rst', rst)
cv.waitKey()


#15
import cv2 as cv
img1 =cv.imread(r'D:\Desktop\class\python\lena512.jpg')
img2 =cv.imread(r'D:\Desktop\class\python\lena512.jpg')
img3 =cv.imread(r'D:\Desktop\class\python\lena512.jpg')

res1 =cv.resize(img1,None,fx =1.5,fy =1.5,interpolation =cv.INTER_AREA)
res2 =cv.resize(img2,None,fx =1.5,fy =1.5,interpolation =cv.INTER_LINEAR)
res3 =cv.resize(img3,None,fx =1.5,fy =1.5,interpolation =cv.INTER_CUBIC)
cv.imshow('img1', img1)
cv.imshow('img2', img2)
cv.imshow('img3', img3)
cv.imwrite(r'D:\Desktop\class\python\lena512_a.jpg', res1)
cv.imwrite(r'D:\Desktop\class\python\lena512_l.jpg', res2)
cv.imwrite(r'D:\Desktop\class\python\lena512_c.jpg', res3)
while True:
    if (cv.waitKey() & 0xFF) == ord('q'):
        break
    else:
        pass
cv.destroyAllWindows()




'''影像翻轉:flip()
        cv2.flip(src,flipcode)
        src原始影像
        flipcode翻轉(翻轉!=旋轉)
        
        flipcode
               0:繞 X軸翻轉
            正數:繞 Y軸翻轉 (1)
            負數:繞 X,Y軸翻轉 (-1)
            
'''


#16
import cv2 as cv
img =cv.imread(r'D:\Desktop\class\python\lena512.jpg')
x =cv.flip(img, 0)
y =cv.flip(img, 1)
xy =cv.flip(img, -1)
cv.imshow('img', img)
cv.imshow('x', x)
cv.imshow('y', y)
cv.imshow('xy', xy)
cv.waitKey()





#==============================================================================
#==============================================================================

#0721



'''仿射轉換
        透過幾何轉換執行平移 旋轉...
        "此旋轉可保持影像的平行性 及 平直性"
        
    warpAffine()
    
    cv.warpAffine(src,M,dsize,flags,borderMode,borderValue)
         src     原始影像
        " M      轉換矩陣"
        dsize   輸出影像尺寸大小
        flags   內插方法 預設INTER_LINEAR
        borderMode  框線模式 BORDER_CONSTANT
        borderValue 框線值 預設0

'''

#01
import cv2 as cv
import numpy as np
img =cv.imread(r'D:\Desktop\class\python\lena512.jpg')
height,width =img.shape[:2]
x =100
y =200
M =np.float32([[1,0,x],[0,1,y]])
# np.單精度浮點數
move =cv.warpAffine(img, M, (width,height))
                #影像 轉換為矩陣 輸出的影像尺寸
cv.imshow('img', img)
cv.imshow('move', move)
cv.waitKey()

'''仿射轉換
    平移:
        透過3*3(或2*2) M矩陣執行轉換
        
       | 1  0  tx  |   將每一像點 移到 x+t  y+t
  M   | 0  1  ty  |

   M(11)=1      M(21)=0
   M(12)=0      M(22)=1
   M(13)=100    M(23)=200    src(x*1 + y*0 + 100,
                                 x*0 + y*1 +200)
'''




'''仿射轉換
    旋轉:
       產生以warpAffine()進行旋轉轉換時的轉換矩陣 
    
    .getRotationMatrix2D():
       cv.getRotationMatrix2D(center,angle,scale)
       
       center 旋轉中心點
       angle 旋轉角度(逆時針為正)
       scale 縮放比例


    *通常會以getRotationMatrix2D() 函式進行 不進行自訂
    原點旋轉:(自訂矩陣)    
            原點 ==影像的左上角
            
         | cos0   -sin0    0  |
         | sin0    cos0    0 |
         |  00      0      1 |
------------------------------------------------------------------------------
    以(x,y) 旋轉:(自訂矩陣)
    
    |cos0   -sin0   x - xcos0 + ysin0 |
    |sin0    cos0   y - xsin0 + ycos0 |
    |  0       0            1         |

'''

#02 旋轉45度
import cv2 as cv
img =cv.imread(r'D:\Desktop\class\python\lena512.jpg')
height,width =img.shape[:2]
M =cv.getRotationMatrix2D((width/2,height/2), 45 ,0.6)
                            #旋轉中心點    旋轉角度  縮放比例
rotate =cv.warpAffine(img, M, (width,height))
cv.imshow('img', img)
cv.imshow('rotate',rotate)
cv.waitKey()

'''仿射轉換
    傾斜:
   .getAffineTransform()
       產生以wrapAffine()進行仿射轉換時的轉換矩陣  
       以三個點進行轉換
    
    cv.getAffineTransform(src,dst)
        src  影像的三個點座標
        dst 轉換的三個點座標   
                            (以上都為二維陣列)
       
'''

#03 傾斜
import cv2 as cv
import numpy as np 
img =cv.imread(r'D:\Desktop\class\python\lena512.jpg')
rows,cols,ch =img.shape
p1 =np.float32([[0,0],[cols-1,0],[0,rows-1]])
p2 =np.float32([[0,rows*0.33],[cols*0.85,rows*0.25],[cols*0.15,rows*0.7]])
#p1 p2三個點為自己設定的
M =cv.getAffineTransform(p1, p2)
                    #產生矩陣
dst =cv.warpAffine(img, M, (cols,rows))
                #原始影像 矩陣 輸出的大小尺寸
cv.imshow('img', img)   
cv.imshow('result', dst)
cv.waitKey()


'''透視轉換(跟仿射的傾斜很像但不一樣)

        將矩形轉換為"任意四邊形" (無須維持平行性 平直性)
        
    warpPerspective() 透視轉換

    cv.warpPerspective(src,M,dsize,flags,borderMode,borderValue)
       
         src     原始影像
        " M      轉換矩陣  "
        dsize   輸出影像尺寸大小
        flags   內插方法 預設INTER_LINEAR
        borderMode  框線模式 BORDER_CONSTANT
        borderValue 框線值 預設0

    getPerspedtiveTransform()
        產生warpPerspective() 執行時的轉換 矩陣 M
        
        **必須先有這個才會有上面的
    
    cv.getPerspedtiveTransform(src,dst)   
        
        src 原影像的 "四個點座標"
        dst 轉換影像的 "四個點座標"
                            任意四邊形 無須平行性 平直性
        

'''

#04 透視
import cv2 as cv
import numpy as np 
img =cv.imread(r'D:\Desktop\class\python\lena512.jpg')
rows,cols =img.shape[:2]
print(rows,cols)

pts1 =np.float32([[150,50],[300,50],[60,450],[210,450]])
pts2 =np.float32([[50,50],[rows-50,50],[50,cols-50],[rows-50,cols-50]])
M =cv.getPerspectiveTransform(pts1, pts2)
dst =cv.warpPerspective(img, M, (cols,rows))
cv.imshow('img', img)
cv.imshow('dst', dst)
cv.waitKey()


#05 只讓藍色的c出現 其他不要
import cv2 as cv
import numpy as np 
img =cv.imread(r'D:\Desktop\class\python\opencv-logo.png')
rows,cols =img.shape[:2]
print(rows,cols)

pts1 =np.float32([[300,290],[500,290],[300,400],[500,400]])
pts2 =np.float32([[50,50],[rows-170,100],[50,cols+100],[rows-240,cols-200]])

M =cv.getPerspectiveTransform(pts1, pts2)
dst =cv.warpPerspective(img, M, (cols,rows))
cv.imshow('img', img)
cv.imshow('dst', dst)
cv.waitKey()


'''重對映
        將影像中的像素點放到另一個位置
        
    remap()
    
    cv.remap(src,x,y,interpolation,borderMode,borderValue)
    
    
              src 原始影像
    interpolation 內插方式
              x   對映的 x座標
              y   對映的 y座標
    
 '''

#06

import numpy as np 
img =np.random.randint(0,256,size =[4,5],dtype =np.uint8)
rows,cols =img.shape
mapx =np.ones(img.shape,np.float32)*3
mapy =np.ones(img.shape,np.float32)*0

rst =cv.remap(img,mapx,mapy,cv.INTER_LINEAR)
#目標陣列中的rst 所有像素點 都對映到原影像img 中的 第0行(橫的)第3列(直的)
print('img =\n',img)
print('mapx =\n',mapx)
print('mapy =\n',mapy)
print('rst =\n',rst)#


#07 像素點複製(影像複製)
import numpy as np 
img =np.random.randint(0,256,size =[4,5],dtype =np.uint8)
rows,cols =img.shape #取得外觀參數
mapx =np.ones(img.shape,np.float32)
mapy =np.ones(img.shape,np.float32)#產生都是零的陣列 新的x,y
for i in range(rows):
    for j in range(cols):
        mapx.itemset((i,j),j) #.itemset(設定裡面的項目 
        mapy.itemset((i,j),i)
                     
rst =cv.remap(img,mapx,mapy,cv.INTER_LINEAR) #利用新的x,y去做對映 並做出影像複製
print('img =\n',img)
print('mapx =\n',mapx)
print('mapy =\n',mapy)
print('rst =\n',rst)#


#07-1 影像複製
import cv2 as cv
import numpy as np 
img =cv.imread(r'D:\Desktop\class\python\lena512.jpg')
rows,cols =img.shape[:2]
mapx =np.ones(img.shape[:2],np.float32)
mapy =np.ones(img.shape[:2],np.float32)#產生都是零的陣列 新的x,y
for i in range(rows):
    for j in range(cols):
        mapx.itemset((i,j),j) #.itemset(設定裡面的項目 
        mapy.itemset((i,j),i)
                     
rst =cv.remap(img,mapx,mapy,cv.INTER_LINEAR) #利用新的x,y去做對映 並做出影像複製
cv.imshow('img =\n',img)
cv.imshow('rst', rst)
cv.waitKey()

'''繞 x軸翻轉:         
    
    對映過程中:  x 軸座標值不變
                y 軸座標以 x軸 作為對稱軸進行交換
    
    對稱關係維:  (行號索引值為0開始) 行號==對稱關係
            目前行號 + 對稱行號 =總行數-1
 
    反映於 x ,y上:  (mapx,mapy)
            mapx值保持不變   mapy = 總行數-1-目前行數
            
            ex  [3,3,3,3,3]
                4-1-0=3
'''


#08  繞x軸翻轉的 ==上下顛倒
import cv2 as cv
import numpy as np 
img =np.random.randint(0,256,size =[4,5],dtype =np.uint8)
rows,cols =img.shape 
mapx =np.ones(img.shape,np.float32)
mapy =np.ones(img.shape,np.float32)
for i in range(rows):
    for j in range(cols):
        mapx.itemset((i,j),j)
        mapy.itemset((i,j),rows-1-i)
                     
rst =cv.remap(img,mapx,mapy,cv.INTER_LINEAR) 
print('img =\n',img)
print('mapx =\n',mapx)
print('mapy =\n',mapy)
print('rst =\n',rst)


#08-1 照片版  繞x軸翻轉的 ==上下顛倒
import cv2 as cv
import numpy as np 
img =cv.imread(r'D:\Desktop\class\python\lena512.jpg')
rows,cols =img.shape[:2]
mapx =np.ones(img.shape[:2],np.float32)
mapy =np.ones(img.shape[:2],np.float32)#產生都是零的陣列 新的x,y
for i in range(rows):
    for j in range(cols):
        mapx.itemset((i,j),j) #.itemset(設定裡面的項目 
        mapy.itemset((i,j),rows-1-i)
                     
rst =cv.remap(img,mapx,mapy,cv.INTER_LINEAR) #利用新的x,y去做對映 並做出影像複製
cv.imshow('img',img)
cv.imshow('rst', rst)
cv.waitKey()


'''繞 y軸翻轉:         
    
    對映過程中:   y 軸座標值不變
                 x 軸座標以 y軸 作為對稱軸進行交換
    
    對稱關係維:  (行號索引值為0開始) (行號==對稱關係)
            目前行號 + 對稱行號 =總行數-1
 
    反映於 x ,y上:  (mapx,mapy)
            mapx值保持不變   mapy = 總行數-1-目前行數
            
            ex  [3,3,3,3,3]
                4-1-0=3
'''

#09 y軸翻轉  左右相反
import cv2 as cv
import numpy as np 
img =np.random.randint(0,256,size =[4,5],dtype =np.uint8)
rows,cols =img.shape 
mapx =np.zeros(img.shape,np.float32)
mapy =np.zeros(img.shape,np.float32)
for i in range(rows):
    for j in range(cols):
        mapx.itemset((i,j),cols-1-j)
        mapy.itemset((i,j),i)
                     
rst =cv.remap(img,mapx,mapy,cv.INTER_LINEAR) 
print('img =\n',img)
print('mapx =\n',mapx)
print('mapy =\n',mapy)
print('rst =\n',rst)

#09-1 照片版  繞y軸翻轉的 ==左右顛倒
import cv2 as cv
import numpy as np 
img =cv.imread(r'D:\Desktop\class\python\lena512.jpg')
rows,cols =img.shape[:2]
mapx =np.ones(img.shape[:2],np.float32)#zeros都可以 沒有關係
mapy =np.ones(img.shape[:2],np.float32)#產生都是零的陣列 新的x,y
for i in range(rows):
    for j in range(cols):
        mapx.itemset((i,j),cols-1-j) #.itemset(設定裡面的項目 這裡是左右
        mapy.itemset((i,j),i)#這是上下
                     
rst =cv.remap(img,mapx,mapy,cv.INTER_LINEAR) #利用新的x,y去做對映 並做出影像複製
cv.imshow('img',img)
cv.imshow('rst', rst)
cv.waitKey()



'''繞 x, y軸翻轉:         
    
    對映過程中:   y 軸座標值 x軸 作為對稱軸進行交換
                 x 軸座標以 y軸 作為對稱軸進行交換
    
    對稱關係維:  (行號索引值為0開始) (行號==對稱關係)
 
             目前 列 號 + 對稱 列 號 =總 列 數-1
             目前 行 號 + 對稱 行 號 =總 行 數-1
            
 
    反映於 x ,y上:  (mapx,mapy)
            mapx值 =總 行 數-1-目前 行 號
            mapy值 =總 列 數-1-目前 列 號
            
            ex  [3,3,3,3,3]
                4-1-0=3
'''


#10 x,y軸翻轉  上下左右相反
import cv2 as cv
import numpy as np 
img =np.random.randint(0,256,size =[4,5],dtype =np.uint8)
rows,cols =img.shape 
mapx =np.zeros(img.shape,np.float32)
mapy =np.zeros(img.shape,np.float32)
for i in range(rows):
    for j in range(cols):
        mapx.itemset((i,j),cols-1-j)
        mapy.itemset((i,j),rows-1-i)
                     
rst =cv.remap(img,mapx,mapy,cv.INTER_LINEAR) 
print('img =\n',img)
print('mapx =\n',mapx)
print('mapy =\n',mapy)
print('rst =\n',rst)

#10-1 照片版  繞 x ,y軸翻轉的 =上下左右顛倒
import cv2 as cv
import numpy as np 
img =cv.imread(r'D:\Desktop\class\python\lena512.jpg')
rows,cols =img.shape[:2]
mapx =np.ones(img.shape[:2],np.float32)#zeros都可以 沒有關係
mapy =np.ones(img.shape[:2],np.float32)#產生都是零的陣列 新的x,y
for i in range(rows):
    for j in range(cols):
        mapx.itemset((i,j),cols-1-j) #.itemset(設定裡面的項目 這裡是左右
        mapy.itemset((i,j),rows-1-i)#這是上下
                     
rst =cv.remap(img,mapx,mapy,cv.INTER_LINEAR) #利用新的x,y去做對映 並做出影像複製
cv.imshow('img',img)
cv.imshow('rst', rst)
cv.waitKey()
 


'''
    x , y 軸 互換
        mapx調整為所在 行 的行號
        mapy調整為所在 列 的列號
        
        *若行列數量不相同
            則無法完成對映的值會設為0
'''

#11
import cv2 as cv
import numpy as np 
img =np.random.randint(0,256,size =[4,6],dtype =np.uint8)
rows,cols =img.shape 
mapx =np.zeros(img.shape,np.float32)
mapy =np.zeros(img.shape,np.float32)
for i in range(rows):
    for j in range(cols):
        mapx.itemset((i,j),i)
        mapy.itemset((i,j),j)#互換 最後的 i j 互換
                     
rst =cv.remap(img,mapx,mapy,cv.INTER_LINEAR) 
print('img =\n',img)
print('mapx =\n',mapx)
print('mapy =\n',mapy)
print('rst =\n',rst)

#11-1 照片版  繞 x ,y軸 互換
import cv2 as cv
import numpy as np 
img =cv.imread(r'D:\Desktop\class\python\opencv-logo.png')
rows,cols =img.shape[:2]
mapx =np.ones(img.shape[:2],np.float32)
mapy =np.ones(img.shape[:2],np.float32)
for i in range(rows):
    for j in range(cols):
        mapx.itemset((i,j),i) 
        mapy.itemset((i,j),j)#互換 最後的 i j 互換
                     
rst =cv.remap(img,mapx,mapy,cv.INTER_LINEAR) 
cv.imshow('img',img)
cv.imshow('rst', rst)
cv.waitKey()
 


#12  縮放
import cv2 as cv
import numpy as np 
img =cv.imread(r'D:\Desktop\class\python\lena_01.jpg')
rows,cols =img.shape[:2]
mapx =np.ones(img.shape[:2],np.float32)
mapy =np.ones(img.shape[:2],np.float32)
for i in range(rows):
    for j in range(cols):
        if 0.25*cols<i<0.75*cols and 0.25*rows <j<0.75*rows:
            mapx.itemset((i,j),2*(j-cols*0.25)+0.5) 
            mapy.itemset((i,j),2*(i-rows*0.25)+0.5)
        else:
             mapx.itemset((i,j),0) 
             mapy.itemset((i,j),0)
             
rst =cv.remap(img,mapx,mapy,cv.INTER_LINEAR) 
cv.imshow('img',img)
cv.imshow('rst', rst)
cv.waitKey()
 
#接續平滑處理 



































































































































































