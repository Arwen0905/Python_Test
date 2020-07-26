# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 10:20:12 2020

@author: USER
"""
#0610
#01-04 在資料視覺化

'''安裝 opencv 模組
pip install opencv-python''' 

#--------------------------------
'''
讀取影像:  
    import cv2 as cv
    cv.imread(檔案名稱,flag) 
flag 檔案類型:
影像只分 彩色(三頻) 灰階(兩頻) 兩種
IMREAD_COLOR(1)   彩色
IMREAD_GRAYSCALE(0)   灰階
IMREAD_UNCHANGED(-1)  所有影像頻道(包含透明度)

視窗命名:
    import cv2 as cv
    cv.namedWindow(視窗名稱)

顯示影像:
    import cv2 as cv
    cv.imshow(視窗名稱,顯示的影像)

關閉:(較少使用)
    視窗:
        import cv2 as cv
        cv.destoryWindow(視窗名稱)
    所有視窗:
        import cv2 as cv
        cv.destoryAllWindow()

按鍵等待: (視窗等待按鍵關閉)(較常使用)
    import cv2 as cv
    cv.waitKey(delay)
    
'''

#------------------------------讀取彩色
import cv2 as cv
img =cv.imread(r'C:\Users\USER\Desktop\cvv\Lena.jpg')
#路徑資料夾名稱為中文 會錯誤 須為全英文名稱
cv.namedWindow('image')
cv.imshow('image',img)
cv.waitKey()
#出現的大小為圖片大小 視窗不能改大小 因為為預定大小 沒有設定怕失真

'''
imwrite:
    import cv2 as cv
    cv.imwrite(寫入的檔案名稱,要寫入的檔案)
'''
#------------------------------05讀取灰階
import cv2 as cv
img =cv.imread(r'C:\Users\USER\Desktop\cvv\tpe101.jpg',0)
cv.imshow('image',img)
x =cv.waitKey()
if x ==27:#27 == 鍵盤上的esc 所以按esc 可以關閉視窗
    cv.destroyAllWindows()
elif x ==ord('s'):
    cv.imerite(r'C:\Users\USER\Desktop\cvv\tpe101gray.png',img)
    cv.destroyAllWindows()


'''
WINDOW_NORMAL:
    import cv2 as cv
    cv.namedWindow(r'C:\...',cv.WINDOW_NORMAL)  #可調整視窗大小
#要注意圖片失真的問題
'''
#----------------------------------

'''繪圖:
共同參數:
    img: 要繪製圖形的影像
    color: 色彩 *使用BGR模型* 以*數組*型態儲存 ex.(255,0,0)
    thickness: 線條粗細 預設1
    linetype: 線條類型

畫線:
    import cv2 as cv
    cv.line(img,起點座標,終點座標,color,thickness,linetype)
'''

import  cv2 as cv 
import numpy as np

img = np.zeros((512,512,3),np.uint8)
cv.line(img,(0,0),(511,511),(255,0,0),5)#最後的5違憲的粗細
cv.imshow('image',img)
cv.waitKey()

'''
numpy.zeros(): 建立一個所有元素都是0的數值
        numpy.zeros((512,512,3),np.uint8)
        建立512(行)*512(列)大小的影像圖片 每一格中有3個元素 都是0==即黑色(BGR)
        由imshow()讀入
.uint8 無號的8位元整數
'''
#------------------------07
import  cv2 as cv 
import numpy as np
n = 300
img = np.zeros((n+1,n+1,3),np.uint8)
img = cv.line(img,(0,0),(n,n),(255,0,0),3)
img = cv.line(img,(0,100),(n,100),(0,255,0),1)
img = cv.line(img,(100,0),(100,n),(0,0,255),6)
cv.imshow('image',img)
cv.waitKey()


'''畫矩形: #對角線的頂點座標
        import  cv2 as cv 
        cv.rectangle(img,頂點1,頂點2,color,thickness,linetype)
        thickness 如為 -1 ==填滿'''
#------------------------08

import cv2 as cv
img = np.zeros((512,512,3),np.uint8)
#512(行)*512(列)大小的影像圖片 每一格中有3個元素 都是0==即黑色(BGR)
        
cv.rectangle(img,(384,0),(510,128),(0,255,0),5)
cv.imshow('image',img)
cv.waitKey()

#---------------------09

import cv2 as cv 
import numpy as np
n = 300
img = np.ones((n,n,3),np.uint8)*255
#產生一個300*300大小的 3個元素 每個元素為 1*255 1*255 1*255 為白色
img = cv.rectangle(img,(50,50),(n-100,n-50),(0,0,255),-1)
cv.imshow('image',img)
cv.waitKey()

'''
.ones():建立一個所有元素都是1的數值
    numpy.zeros((512,512,3),np.uint8)
    建立512(行)*512(列)大小的影像圖片 每一格中有3個元素 
    都是1==經運算即白色(BGR)
    由imshow()讀入
    #thickness 如為 -1 ==填滿'''

#-----------------------------10
import cv2 as cv 
import numpy as np
    
img = np.zeros((512,512,3),np.uint8)
cv.circle(img,(447,63),63,(0,0,255),-1)
cv.imshow('image',img)
cv.waitKey()

'''畫圓:
    import cv2 as cv 
    cv.circle(img,圓心,半徑,color,thickness,linetype)'''
        #img 參數必須為整數
'''imread讀取:
    讀取的資料會儲存成一個 numpy的陣列(串列)
    陣列的前2個維度 為圖片的高度.寬度
        img.shape[0]行 圖片的  垂直高度
        img.shape[1]列 圖片的  水平寬度
        img.shape[2] channel數
    第三維 是圖片色彩channel
    RGB圖片: channel ==3
    灰階: channel ==1         '''

    
#----------------------11同心圓

import cv2 as cv
import numpy as np
img = np.zeros((512,512,3),dtype='uint8')
#dtype 返回陣列中元素的資料型別
#512(行)*512(列)大小的影像圖片 每一格中有3個元素 都是0==即黑色(BGR)
        
#取得中心點(img.shape[1]/2,img.shape[0]/2)
for r in range(0,175,25): #0起始 175終止　25為間隔==6個圓圈
    cv.circle(img,(img.shape[1] // 2,img.shape[0] // 2)\
              ,r,(255,255,255))
cv.imshow('image',img)
cv.waitKey()


#---------------------------------12 同心圓
import cv2 as cv
import numpy as np
d = 400
img = np.ones((d,d,3),dtype = 'uint8')*255

(centerX,centerY) = (round(img.shape[1]/2),round(img.shape[0]/2))
red = (0,0,255)
for r in range(5,round(d/2),12):
    cv.circle(img,(centerX,centerY),r,red,3)
cv.imshow('image',img)
cv.waitKey()

'''round():         #預設為整數位
    round(數值,小數位數)
    將數值取小數位 數的四捨五入值   '''
    

#=======================
'''總結:
    np.zeros(a,b,3)     黑色的背景 (0=黑色)
    np.ones(a,b,3)*255  白色      (255=白色)'''
#=======================
    
'''畫橢圓:
    cv.ellipse(img,圓心,(軸1,軸2),旋轉角度,圓弧起始角度(s),圓弧結束角度(e),\
           color,thickness,linetype)
        
s:0 e:360 完整橢圓
s:0 e:180 半橢圓
'''

#-------------------------13
import cv2 as cv
import numpy as np
img =np.zeros((512,512,3),np.uint8)
img.fill(200)

#(img,圓心,(軸1,軸2),旋轉角度,s,e,color,thickness,linetype
cv.ellipse(img,(180,200),(100,60),45,0,360,(128,0,255),2)
cv.ellipse(img,(180,200),(50,100),45,0,180,(255,0,128),-1)
cv.imshow('image',img)
cv.waitKey()
cv.destoryAllWindows()


#-------------------------------14
import cv2 as cv
import numpy as np
d = 400
img = np.ones((d,d,3),dtype = 'uint8')*255
center = (round(d/2),round(d/2))
size = (100,200)

for i in range(0,10):
    angle = np.random.randint(0,361)
    color =np.random.randint(0,high = 256,size =(3)).tolist()
    thickness =np.random.randint(1,9)
    cv.ellipse(img,center,size,angle,0,360,color,thickness)
cv.imshow('image',img)
cv.waitKey()




'''畫多邊形:
    import cv2 as cv
    cv.polylines(img,頂點座標,isClised,color,thickness,linetype)
                            #isClised 為bool
頂點座標必須是一個陣列(串列)
共資料型態 必須為numpy.int32
繪圖前必須以 reshape 重新計算調整(頂點)

reshape(頂點數量,1,2)

建立頂點座標:
    x = numpy.array([[a,b],[c,d]..],numpy.int32)
    x.reshape(-1,1,2)
#設為 -1,由其他參數計算得出

'''
#-------------------------15
import cv2 as cv
import numpy as np
img = np.zeros((512,512,3),np.uint8)
pts = np.array([[10,5],[60,90],[130,80],[110,70]],np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(0,255,255))
cv.imshow('image',img)
cv.waitKey()



'''寫文字:
    import cv2 as cv
    cv.putText(img,文字,座標,字型,大小,\
        color,thickness,lintype,bottomLeftOrigin)
        
bottomLeftOrigin 文字映射(True/False)

'''
#----------------16寫入一般文字
import cv2 as cv
import numpy as np
img = np.zeros((512,512,3),np.uint8)
#zeros...為黑色
font = cv.FONT_HERSHEY_SIMPLEX
#font這裡為字體輸入
cv.putText(img,'openCV',(10,350),font,4,(255,255,255),2,cv.LINE_AA)
#(img,寫入的文字'openCV',座標(10,350),字體font,字大小4,
#顏色(255,255,255)==這三個數字為白色,
#線條粗細(thickness)2,反鋸齒(盡量平滑)(linetype)cv.LINE_AA)

cv.imshow('image',img)
cv.waitKey()
cv.destoryAllWindow()



#--------------------------17寫入文字 並列出全部字體
import cv2 as cv
import numpy as np
img = np.zeros((512,512,3),np.uint8)
img.fill(64)#填入數值#從(0,0,0) 填入數值變(64,64,64)
#RGB數值都一樣的時候為 灰色 (64,64,64)
text = 'opencv for python'
cv.putText(img,text,(10,40),cv.FONT_HERSHEY_SIMPLEX,\
           1,(0,255,255),1,cv.LINE_AA)
cv.putText(img,text,(10,80),cv.FONT_HERSHEY_PLAIN,\
           1,(0,255,255),2,cv.LINE_AA)
cv.putText(img,text,(10,120),cv.FONT_HERSHEY_DUPLEX,\
           1,(0,255,255),1,cv.LINE_AA)
cv.putText(img,text,(10,160),cv.FONT_HERSHEY_COMPLEX,\
           1,(0,255,255),2,cv.LINE_AA)
cv.putText(img,text,(10,200),cv.FONT_HERSHEY_TRIPLEX,\
           1,(0,255,255),1,cv.LINE_AA)
cv.putText(img,text,(10,240),cv.FONT_HERSHEY_COMPLEX_SMALL,\
           1,(0,255,255),2,cv.LINE_AA)
cv.putText(img,text,(10,280),cv.FONT_HERSHEY_SCRIPT_SIMPLEX,\
           1,(0,255,255),1,cv.LINE_AA)
cv.putText(img,text,(10,320),cv.FONT_HERSHEY_SCRIPT_COMPLEX,\
           1,(0,255,255),2,cv.LINE_AA)
cv.imshow('image',img)
cv.waitKey()
cv.destroyAllWindows()

#-----------------------------18 描邊文字
import cv2 as cv
import numpy as np 
d = 400
img = np.ones((d,d,3),dtype = 'uint8')*255
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'openCV',(0,200),font,3,(0,255,0),15)#邊線
cv.putText(img,'openCV',(0,200),font,3,(0,0,255),5)#內裡
#描邊為 控制粗細
cv.imshow('image',img)
cv.waitKey()

#----------------------------------19
import cv2 as cv
import numpy as np 
d = 400
img = np.ones((d,d,3),dtype='uint8')*255
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'openCV',(20,150),font,3,(105,105,105),15,cv.LINE_AA)
cv.putText(img,'openCV',(20,220),font,3,(70,10,180),15,cv.FONT_HERSHEY_SCRIPT_SIMPLEX,True)
cv.imshow('image',img)
cv.waitKey()


'''使用自訂字型:
    載入PIL模組下的
    1.ImageFont:
       ImageFont.truetype  載入字體
    2.Image:
        Image.fromarray     將numpy陣列轉為PIL影像
    3.ImageDraw:
        ImageDraw.Draw  將PIL影像上寫文字
    4.使用TEXT方法以設定的字型即大小 寫入文字 
'''
#----------------20
from PIL import ImageFont,ImageDraw,Image
import cv2 as cv
import numpy as np 
img = np.zeros((512,512,3),dtype = 'uint8')
img.fill(64)#這裡多設 只是練習 最下面為主的設定

img[:] = (0,0,192) #img[:] 簡寫的方式 全部設定BGR
text = '恭賀\n新喜'

fontPath =r'C:\Users\USER\Desktop\word type\TaipeiSansTCBeta-Bold.TTF'
font =ImageFont.truetype(fontPath,224)
#ImageFont.truetype載入字體 224為字大小
imgPil = Image.fromarray(img)
#陣列轉為Pil影像
draw = ImageDraw.Draw(imgPil) #在影像上加上文字
draw.text((30,30),text,font=font,fill=(0,0,0,0))
#起點為30,30 寫入字 字體 填入顏色 BGR跟alpha透明度
img = np.array(imgPil)
#numpy把影像轉回陣列
cv.imshow('image',img)
cv.waitKey()
cv.destroyAllWindows()



#==========================================
#==========================================
#0615

'''pandas:
    專為python編寫的外部模組執行 數據處理及分析
    主要資料結構為:
        panel,dataframe,series =pandas的名稱由來
series:
    一維資料結構(類似二維)
    可存放整數,浮點數,字串,python物件(list set truple dict)
    類似python list 只有'索引'結構
建立series物件:
    import pandas as pd
    pd.series(data,index,dtype,name...)    

concat():資料合併
    axis=0 (預設為0==直向排列)
    axis=1 (橫向排列)

    '''

#------------------------------------02
import pandas as pd
years=range(2020,2023)
beijing=pd.Series([20,21,19],index=years)
#字串 索引為years 透過index一個一個對應前面的data
honhkong=pd.Series([25,26,31],index=years)
singapore=pd.Series([30,29,31],index=years)

citydf =pd.concat([beijing,honhkong,singapore])
#資料合併  會按照預設的組合方式 去執行 
print(type(citydf))
print(citydf)

#------------------------------------02
import pandas as pd
years=range(2020,2023)
beijing=pd.Series([20,21,19],index=years)
#字串 索引為years 透過index一個一個對應前面的data
honhkong=pd.Series([25,26,31],index=years)
singapore=pd.Series([30,29,31],index=years)

citydf =pd.concat([beijing,honhkong,singapore],axis=1)
#資料合併  會按照預設的組合方式 去執行  axis=1 橫向排列
print(type(citydf))
print(citydf)

'''資料結構方法:columns
    資料.columns (==columns名稱)
    以name參數'''
#-------------------------------03
import pandas as pd
years=range(2020,2023)
beijing=pd.Series([20,21,19],index=years)
#字串 索引為years 透過index一個一個對應前面的data
honhkong=pd.Series([25,26,31],index=years)
singapore=pd.Series([30,29,31],index=years)

citydf =pd.concat([beijing,honhkong,singapore],axis=1)
#資料合併  axis=1 橫向排列
cities =['Beijing','Honhkong','Singapore']#設定串列 
citydf.columns=cities
#把合併後的資料 以 定義好的欄位名稱做設定
print(citydf)

'''
series資料.name=名稱
    資料在concat時候 以名稱作為column名稱
'''
#----------------------------------------04
import pandas as pd
years=range(2020,2023)
beijing=pd.Series([20,21,19],index=years)
#字串 索引為years 透過index一個一個對應前面的data
honhkong=pd.Series([25,26,31],index=years)
singapore=pd.Series([30,29,31],index=years)
beijing.name='Beijing'
honhkong.name='Honhkong'
singapore.name='Singapore'
#使用name就不需要設定 columns 會自動帶入
citydf =pd.concat([beijing,honhkong,singapore],axis=1)
#資料合併  axis=1 橫向排列
print(citydf)


'''DataFrame:
    為二維資料結構(欄列結構)
    可儲放整數 浮點數 字串 python物件(list set truple dict)
    格式:
        import pandas as pd
        pd.DataFrame(data,index,dtype,name...)   
        
資料建立:
    
    字典的串列[{....},{....}...]
        字典key若無對應 則對應處將填入NaN

    字典
    以index屬性設定row的名稱   
    將字典內的元素設為index
    以numpy建立DataFrame 
'''
#----------------------------05
import pandas as pd
data=[{'apple':50,'orange':30,'grape':80},{'apple':50,'grape':80}]

fruits =pd.DataFrame(data)
print(fruits)


#-------------------------06
import pandas as pd
cities = {'country':['china','japan','singapore'],\
          'town':['beijing','tokyo','singapore'],\
              'population':[2000,1600,600]}
    #key=欄標題 []內為欄標題下的欄位資料
    
citydf =pd.DataFrame(cities)
print(citydf)

#-------------------------07
import pandas as pd
cities = {'country':['china','japan','singapore'],\
          'town':['beijing','tokyo','singapore'],\
              'population':[2000,1600,600]}
    #key=欄標題 []內為欄標題下的欄位資料
rowindex =['first','second','third']
#設定row標題的名稱
citydf =pd.DataFrame(cities,index=rowindex)
print(citydf)
'''
把字典中的元素設為index
'''
#------------------------08
import pandas as pd
cities = {'country':['china','japan','singapore'],\
          'town':['beijing','tokyo','singapore'],\
              'population':[2000,1600,600]}
    #key=欄標題 []內為欄標題下的欄位資料

citydf =pd.DataFrame(cities,columns=['town','population']\
                     ,index=cities['country'])
#把字典中的元素設為index
#把字典中的資料設為row(索引) 且columns資料不出現重複的 
print(citydf)

'''
以numpy建立DataFrame
'''
#---------------------------09
import pandas as pd
import numpy as np
df1 =pd.DataFrame(np.ones((3,4))*0,columns=['x','y','z','s'])
df2 =pd.DataFrame(np.ones((3,4))*1,columns=['x','y','z','s'])
df3 =pd.DataFrame(np.ones((3,4))*2,columns=['x','y','z','s'])
print(df1)
print(df2)
print(df3)

#---------------------------10
#亂數+numpy+pandas
import pandas as pd
import numpy as np
name=['Frank','Peter','John']
score=['first','second','final']
#建立3*3 陣列 每一格的數據在60~99之間
df=pd.DataFrame(np.random.randint(60,100,size=(3,3)),\
                columns=name,index=score)
print(df)


'''寫入csv檔案:
    csv: Comma Separated Values(以逗號間隔的檔案)
    以 to_csv()將 DataFrame物件 寫入csv檔案 
    格式:
        to_csv(path,sep,header,index,encoding...)
to_csv(檔案,分隔符號-預設為逗號,是否保留header-預設為True\
    ,是否保留index-預設為True,檔案編碼...)

    '''
#--------------------------11
import pandas as pd

course =['Chinese','English','Math','Natural','Soxiety']
chinese=[14,12,13,10,13]
eng=[13,14,11,10,15]
math=[15,9,12,8,15]
nature=[15,10,13,10,15]
social=[12,11,14,9,14]

df=pd.DataFrame([chinese,eng,math,nature,social],\
                columns=course,index=range(1,6))
df.to_csv(r'C:\Users\USER\Desktop\class\out_a.csv')
df.to_csv(r'C:\Users\USER\Desktop\class\out_b.csv',header=False,index=False)
#設定false header color不要顯示

'''資料的構成 以列row為準 每一列及一筆紀錄'''

'''讀入csv檔案:
    read_csv() 將csv檔案讀入(也可讀取txt檔)
格式:
    read_csv(path,sep,header,encoding,index_col,usecols,nrows)
read_csv(path,sep,設定哪一個row為欄位標籤,encoding,欄位column索引,讀取欄位,讀取列)
    '''

#-------------------------12
import pandas as pd

course =['Chinese','English','Math','Natural','Soxiety']
x=pd.read_csv(r'C:\Users\USER\Desktop\class\out_a.csv',index_col=0)
y=pd.read_csv(r'C:\Users\USER\Desktop\class\out_b.csv',names=course)
print(x)
print(y)

'''繪圖:
    將數據建立為Series 以pandas繪圖
    pandas繪圖使用 plot()方法
    將你的數據建立為DataFrame 以pandas繪圖

kind:繪圖模式預設為light
    '''


#-------------------------13
import pandas as pd 
import matplotlib.pyplot as plt
population=[860,1100,1450,1800,2020,2200,2260]
tw =pd.Series(population,index=range(1950,2011,10))
tw.plot(title='Pouplation in Taiwan')
plt.xlabel('year')
plt.ylabel('population')
plt.show()

#-----------------------------14
import pandas as pd 
import matplotlib.pyplot as plt
cities={'population':[1000,850,800,1500,600,800],
        'town':['New york','Chicago','Bangkok','Tokyo','Singapore','Hongkong']}
tw=pd.DataFrame(cities,columns=['population'],index=cities['town'])
tw.plot(title='population in the world')
plt.xlabel('city')
plt.ylabel('population')
plt.show()

#-----------------------------15
import pandas as pd 
import matplotlib.pyplot as plt
cities={'population':[1000,850,800,1500,600,800],
        'town':['New york','Chicago','Bangkok','Tokyo','Singapore','Hongkong']}
tw=pd.DataFrame(cities,columns=['population'],index=cities['town'])
tw.plot(title='population in the world',kind='bar')
plt.xlabel('city')
plt.ylabel('population')
plt.show()

#-----------------------------16
import pandas as pd 
import matplotlib.pyplot as plt
cities={'population':[1000,850,800,1500,600,800],
        'area':[400,500,850,300,200,320],
        'town':['New york','Chicago','Bangkok','Tokyo','Singapore','Hongkong']}
tw=pd.DataFrame(cities,columns=['population','area'],index=cities['town'])

tw.plot(title='population in the world')
plt.xlabel('city')
plt.show()

#------------------------------17不建議作法
import pandas as pd 
import matplotlib.pyplot as plt
cities={'population':[10000000,8500000,8000000,15000000,6000000,8000000],
        'area':[400,500,850,300,200,320],
        'town':['New york','Chicago','Bangkok','Tokyo','Singapore','Hongkong']}
tw=pd.DataFrame(cities,columns=['population','area'],index=cities['town'])

tw.plot(title='population in the world')
plt.xlabel('city')
plt.show()


#----------------------------------18多座標軸
import pandas as pd 
import matplotlib.pyplot as plt
cities={'population':[10000000,8500000,8000000,15000000,6000000,8000000],
        'area':[400,500,850,300,200,320],
        'town':['New york','Chicago','Bangkok','Tokyo','Singapore','Hongkong']}
tw=pd.DataFrame(cities,columns=['population','area'],index=cities['town'])

fig,ax=plt.subplots()
#fig 整體圖表物件
#ax 第一個軸
#subplots 在一個圖表中繪製 不同軸的數據
fig.suptitle('citu statistics')#標題
ax.set_xlabel('city')
ax.set_ylabel('population') #設定y跟x軸的標題文字

ax2=ax.twinx()#ax.twinx產生一個新的軸
ax2.set_ylabel('Area')
tw['population'].plot(ax=ax,rot=20)#rot旋轉座標刻度
tw['area'].plot(ax=ax2,style='r-')
ax.legend(loc=1)
ax2.legend(loc=2)#.legend()圖例 loc圖例的位置
plt.show()
'''
.subplots()在一個圖表中繪製 不同軸的數據
.suptitle()圖標題
.set_xlabel .set_ylabel y跟x軸的標題文字
.twinx() 產生一個新的軸
.legend()圖例 loc圖例的位置
rot旋轉座標刻度
'''




'''圓形(餅)圖:
    只能一組數據
    數值格式化為百分比  autopct='%格式%%'
    切開圓形圖   explode
        '''
    
import pandas as pd
import matplotlib,pyplot as plt
fruits= ['apple','bananas','grapes','pears','oranges']
s= pd.Series([2300,5000,1200,2500,2900],index=fruits,name='fruits shop')
explode=[0.4,0,0,0.2,0]
s.plot.pie(explode=explode,autopct='%12f%%')
plt.show()
    
    
    
'''時間序列:
    數據由時間順序列出
    時間為一系列的時間戳記
匯入時間模組:
    from datetime import datetime
    (年月日時分秒)
時間區間:
    時間=datetime.timedelta(week,days,hours,minutes,seconds)

'''
from datetime import datetime
tn=datetime.now()
print(type(tn))
print('現在時間:',tn)

#-----------------------------20
from datetime import datetime
tn=datetime.now()
print(type(tn))
print('現在時間:',tn)
print('年:',tn.year)
print('月:',tn.month)
print('日:',tn.day)
print('時:',tn.hour)
print('分:',tn.minute)
print('秒:',tn.second)

#--------------------------21
import pandas as pd
from datetime import datetime,timedelta
ndays=5
start=datetime(2019,3,11)
dates=[start+timedelta(days=x) for x in range(0,ndays)]
#dates  這會有五個數值
data=[34,44,65,53,39]
ts=pd.Series(data,index=dates)

print(type(ts))
print(ts)
    
#日期時間是可以做加減乘除 可運算的!    

#--------------------------22
import pandas as pd
from datetime import datetime,timedelta
ndays=5
start=datetime(2019,3,11)
dates=[start+timedelta(days=x) for x in range(0,ndays)]

data1=[34,44,65,53,39]
ts1=pd.Series(data1,index=dates)
data2=[34,44,65,53,39]
ts2=pd.Series(data2,index=dates)


addts =ts1+ts2
print('ts1+ts2')
print(addts)
meants=(ts1+ts2)/2
print('(ts1+ts2)/2')
print(meants)

#-------------------------------23
import pandas as pd 
import matplotlib.pyplot as plt

dates =pd.date_range('3/11/2019','3/15/2019')
#.date_range(起始日期,終止日期)
data =[33,44,65,53,39]
ts =pd.Series(data,index=dates)
ts.plot(title='Data in time Series')
plt.xlabel('date')
plt.ylabel('date')
plt.show()

#===============================================
#===============================================
#0624

'''影像加法運算
    灰階影像中 
        像素以8位元表示 像素值範圍為0~255 像素飽和值為255


影像加法:
    兩影像對應的像素值相加 <= 255 直接相加
                         >  255 將相加結果 mod 256得出結果
                         ex.(255+58)%256=57#取餘數
add():影像像素相加
       cv2.add(影像1,影像2)
     兩影像對應的像素值相加 <= 255 直接相加
                          >  255 直接設定為255(飽和值)
                          
影像加法:
        使用   +   變暗
        使用 add() 變亮       
       
       
'''
#--------------04
import numpy as np
img1=np.random.randint(0,256,size=[3,3],dtype=np.uint8)
#當0~255之間 必須要設定的dtype=np.uint8
img2=np.random.randint(0,256,size=[3,3],dtype=np.uint8)
print('img1 = \n',img1)
print('img2 = \n',img2)
print('img1 +img2 = \n',img1+img2)

#---------------05
import cv2 as cv
import numpy as np
img1=np.random.randint(0,256,size=[3,3],dtype=np.uint8)
#當0~255之間 必須要設定的dtype=np.uint8
img2=np.random.randint(0,256,size=[3,3],dtype=np.uint8)
print('img1 = \n',img1)
print('img2 = \n',img2)
img3=cv.add(img1,img2)
print('cv.add(img1,img2)= \n',img3)

#--------------06
import cv2 as cv
img=cv.imread(r'C:\Users\USER\Desktop\class\cvv\lena.jpg',0)
a=img
result1 =a+img
result2=cv.add(img,a)
cv.imshow('image',img)
cv.imshow('image1',result1)
cv.imshow('image2',result2)
cv.waitKey()

'''
影像加法:
        使用   +   變暗
        使用 add() 變亮
'''


#======================================================
#======================================================
#0717
'''影像加權和
        計算影像像素值和並加入加權值計算
使用函數: addWeighted
    addWeighted(src1,a,src2,b,c)
#src1 影像1  a 影像1加權   src2 影像2   b 影像2加權   c亮度調節
    
公式: src1*a + src2*b + c

'''
#01
import cv2 as cv
import numpy as np
img1=np.ones((3,4,3),dtype=np.uint8)*100
img2=np.ones((3,4,3),dtype=np.uint8)*10
a=3
img3=cv.addWeighted(img1,0.6,img2,5,a)
print(img3)

'''
兩影像的大小及類型 必須相同
'''
#02 大小不同不可讀取
import cv2 as cv
img1=cv.imread(r'D:\Desktop\class\python\landscape512.jpg')
img2=cv.imread(r'D:\Desktop\class\python\lena512.jpg')
reslt=cv.addWeighted(img1,0.6,img2,0.4,0)
cv.imshow('img1',img1)
cv.imshow('img2',img2)
cv.imshow('img3',reslt)
cv.waitKey()

'''
ROI:Regin Of Interest
    感興趣的區域 於程中自行設定 所需要處理的  區域範圍
'''
#03 加權
import cv2 as cv
img=cv.imread(r'D:\Desktop\class\python\lena_01.jpg',1)
us1=cv.imread(r'D:\Desktop\class\python\US1_600.jpg',1)
cv.imshow('image',img)
cv.imshow('banknote',us1)
img_face=img[80:230,250:370]#影像的ROI
us1_face=us1[80:230,240:360]#鈔票的ROI
add=cv.addWeighted(img_face,0.6,us1_face,0.4,0)#影像的ROI執行加權運算 
us1[80:230,240:360]=add#加權後的影像蓋在鈔票上
cv.imshow('reselt',us1)
cv.waitKey()

'''逐位元邏輯運算
bitwise_and :且
bitwise_or :或
bitwise_xor :互斥
bitwise_not :反向

and運算:
    兩個運算元(邏輯值)都為真  其結果為真
    
函數:bitwise_and
    bitwise_and(src1,src2)
 
    
任何數值n 與 數值0 做and運算 結果為0

    11011011
and)00000000
---------------
    00000000

任何數值n 與數值255 做and運算 結果為數值n 本身

    11011011
and)11111111
---------------
    11011011

以上述定理 可建立 掩膜影像
                    只有兩個值 0,255 
                 

                    
or運算:
        兩個運算元(邏輯值)有一個為真 結果為真                    
函數:bitwise_or
    bitwise_or(src1,src2)                    


not運算:
        將運算元反向                    
函數:bitwise_not
    bitwise(src1,src2)    


xor運算:
        兩個運算元(邏輯值)都不相同   結果為真                    
函數:bitwise_xor
    bitwise_xor(src1,src2)    

    11000110  (198)
xor)11011011  (219)
--------------------
    00011101  (29)

'''
#04 掩膜影像
import cv2 as cv
import numpy as np
img1 =np.random.randint(0,255,(5,5),dtype =np.uint8)
img2 =np.zeros((5,5),dtype =np.uint8)
img2[0:3,0:3] =255
img2[4,4] =255
a =cv.bitwise_and(img1,img2)
print('img1=\n',img1)
print('img2=\n',img2)
print('a=\n',a)
#05
import cv2 as cv
import numpy as np
img1=cv.imread(r'D:\Desktop\class\python\lena512.jpg',0)#設0為灰階
img2=np.zeros(img1.shape,dtype=np.uint8)
img2[100:400,200:400]=255
img2[100:500,100:200]=255#0 為黑 255 為白==白就是看得到的地方
a=cv.bitwise_and(img1,img2)
cv.imshow('img1',img1)
cv.imshow('img2',img2)
cv.imshow('a',a)
cv.waitKey()
#06 跟5一樣
import cv2 as cv
import numpy as np
img1=cv.imread(r'D:\Desktop\class\python\lena512.jpg',1)#設1為彩色
img2=np.zeros(img1.shape,dtype=np.uint8)
img2[100:400,200:400]=255
img2[100:500,100:200]=255
a=cv.bitwise_and(img1,img2)
cv.imshow('img1',img1)
cv.imshow('img2',img2)
cv.imshow('a',a)
cv.waitKey()
#07
import cv2 as cv
import numpy as np
img1 =np.ones((4,4),dtype=np.uint8)*3
img2 =np.ones((4,4),dtype=np.uint8)*5
mask =np.zeros((4,4),dtype=np.uint8)
mask[2:4,2:4] =1
img3 =np.ones((4,4),dtype=np.uint8)*66
print('img1=\n',img1)
print('img2=\n',img2)
print('mask=\n',mask)
print('初值 img3=\n',img3)
img3 =cv.add(img1,img2,mask =mask)
print('求和後 img3=\n',img3)
#08
import cv2 as cv
import numpy as np
img =cv.imread(r'D:\Desktop\class\python\lena512.jpg',1)
w,h,c =img.shape
mask =np.zeros((w,h),dtype =np.uint8)
mask[100:400,200:400] =255
mask[100:500,100:200] =255#0 為黑 255 為白==白就是看得到的地方
c =cv.bitwise_and(img,img,mask=mask)
print('img.shape =',img.shape)
print('mask.shape =',mask.shape)
cv.imshow('img',img)
cv.imshow('mask',mask)
cv.imshow('c',c)
cv.waitKey()

''' 
位元平面分解   (去掉雜訊)
    將灰階影像中同一個位元上的 二進位像素值 進行組合可得到到一個二進位影像
    該影像稱為"灰階影像的位元平面"
    其組合過程稱為為位元平面分解
    
    灰階影像中  每一項訴使用8位元 二進位值表示 值的範圍為0~255
    表示為:
        a^7 * 2^7 + a^6 * 2^6 + a^5 * 2^5 + a^4 * 2^4 + a^3 * 2^3
         ~ + a^2 * 2^2 + a^1 * 2^1 + a^0 * 2^0
    
        a^7 ~ a^0 的值為0或是1
        
        a^7值對影像影像最大
        a^0值對影像影像最小
        
        a^7 加權最高 某位元平面與原影像相關性最高 與原影像最相似
        a^0      低                          低 該為元平面最雜亂

執行步驟:
    1.影像前置處理
    2.建置分析矩陣
    3.分析位元平面
    4.設定值處理
    5.顯示影像

'''
#09
import cv2 as cv
import numpy as np 
img =cv.imread(r'D:\Desktop\class\python\lena512.jpg',0)
cv.imshow('imgage',img)
r,c=img.shape # 讀取元影像的 row column
x=np.zeros((r,c,8),dtype =np.uint8) #設定一個分析矩陣裡面都是0的 通道值==8

#分析位元平面
for i in range(8):
    x[:,:,i] =2**i #2位元矩陣  所以要有次方
r =np.zeros((r,c,8),dtype =np.uint8) 

#逐位元邏輯運算
for i in range(8):#主要要變成灰階 
    r[:,:,i] =cv.bitwise_and(img,x[:,:,i])
    mask =r[:,:,i]>0  
    r[mask] =255 # 1==255
    cv.imshow(str(i),r[:,:,i])
cv.waitKey()



'''影像加密及解密
        原始影像與金鑰影像 
            進行"互斥運算" 產生加密影像(encryption)
        加密影像與金鑰影像
            進行"互斥運算" 產生解密影像(deryption)
        
        a==原始資料(明文)
        b==金鑰
        c==加密 xor(a,b)

            xor(a,b)=c
            xor(c,b)=a
            
位元運算可實踐像素點加密
    通常需處理的像素點 為灰階值 ex像素值為216(明文)
    以178(此值由加密者自行決定)作為 加密金鑰
    將此二數值進行 互斥運算
    
    
    11011000  (216)--明文
xor)10110010  (178)--金鑰
-------------------------
    01101010  (106)---加密

bitwise_xor(216,178) =106  加密
bitwise_xor(106,178) =216  解密

    01101010  (106)
xor)10110010  (178)    
-----------------------
   11011000   (216) 
    
'''
#10
import cv2 as cv
import numpy as np
img =cv.imread(r'D:\Desktop\class\python\lena512.jpg',0)
cv.imshow('image',img)
r,c=img.shape
key =np.random.randint(0,256,size=[r,c],dtype=np.uint8)
encryption =cv.bitwise_xor(img,key)
decryption =cv.bitwise_xor(encryption,key)
cv.imshow('img',img)
cv.imshow('key',key)
cv.imshow('encryption',encryption)
cv.imshow('decryption',decryption)
cv.waitKey()

'''浮水印(==資訊隱藏) # 不是一般所理解的浮水印!

        最低有效位(Least Significant Bit;LSB)
            二進位數字中的第0位(最低位) ==a^0
        將需要隱藏的二值影像嵌入載體影像的最低位有效位
        即將載體影像的LSB取代為需要隱藏的二值影像 以達到二值影像隱藏的目的
        
        "因二值影像處於載體影像的LSB上
         對載體影像影響非常不明顯 故具較高的隱蔽性"

#二值影像==二值化的影像為灰階影像
         
嵌入過程:
    將影像二值化(處理為灰階)
    灰階二值影像中 像素值 只有 0,255 表示 黑 白色
    將255轉為1可得到二進位的灰階影像 只用一個位元表達像素值
    
ex 版權認證 身分認證 
    
'''
#11
import cv2 as cv
import numpy as np
img =cv.imread(r'D:\Desktop\class\python\lena512.jpg',0)
watermark =cv.imread(r'D:\Desktop\class\python\watermark.jpg',0)
w =watermark[:,:]>0#::== 只要大於0 的取出 (不是0就是255)所以取出255
watermark[w] =1#將灰階影像值為255的 轉為1 以方便嵌入
r,c =img.shape#取得原始影像的大小尺寸

t254 =np.ones((r,c),dtype=np.uint8)*254
# *254 為了要把255獨立出來==產生254的陣列
imgh7 =cv.bitwise_and(img, t254)#取得影像的高七位
e =cv.bitwise_or(imgh7,watermark)#再用 高七位用or做運算 把watermark 嵌入
#e ==已含載體的 圖片

t1=np.ones((r,c),dtype =np.uint8)#產生一個都是1的陣列
#用 and運算  把含有載體的e 跟
wm =cv.bitwise_and(e,t1)
#wm==從載體影像分析出來的浮水印影像
print(wm)
w =wm[:,:]>0
wm[w] =255

cv.imshow('img',img)
cv.imshow('watermark',watermark*255)
#要顯示圖片 就要把1轉乘255 才會有圖片 所以直接*255比較快
cv.imshow('e',e)
cv.imshow('wm',wm)
cv.waitKey()

#12
import cv2 as cv
import numpy as np
img =cv.imread('lena512.jpg',0)
#讀取原始影像的shape值
r,c =img.shape
mask =np.zeros((r,c),dtype =np.uint8)
mask[100:400,200:400] =1
#取得一個key(打碼與解碼所需要的金鑰)
key =np.random.randint(0, 256, size =[r,c], dtype =np.uint8)
#打碼臉部影像 使用金鑰key對原始影像加密
imgxorkey =cv.bitwise_xor(img,key)
#加密影像的臉部資訊
encryptface =cv.bitwise_and(imgxorkey, mask*255)
#將影像妹的臉部值 設定為0
noface1 =cv.bitwise_and(img,(1-mask)*255)
#取得 打碼影像
maskface =encryptface + noface1
#將打碼臉 解碼
extractoriginal =cv.bitwise_xor(maskface, key)
#將臉部打碼的影像與金樣進行互斥運算xor 得到臉部原始資訊
#將解碼的臉部 進行資料分析 extractoriginal
extractface =cv.bitwise_and(extractoriginal,mask*255)
#從臉打碼的影像分析沒有臉部資訊的影像
noface2 =cv.bitwise_and(maskface, (1-mask)*255)
#得到解碼影像
extractimg =noface2 + extractface
#顯示影像
cv.imshow('img',img)#原始影像
cv.imshow('mask',mask*255)#範本mask影像 白為1 黑為0 將1轉為255 方便顯示
cv.imshow('1-mask',(1-mask)*255)#範本mask影像的反色圖
cv.imshow('key',key)#金鑰影像
cv.imshow('imgxorkey',imgxorkey)#整體打碼臉部影像
cv.imshow('encryptface',encryptface)#從整體打碼影像中分析的臉部打碼影像
cv.imshow('noface1',noface1)#影像中分析的不包含臉部影像
cv.imshow('maskface',maskface)#打碼臉部影像
cv.imshow('extractoriginal',extractoriginal)#分析的初步原始影像
cv.imshow('extractface',extractface)#分析的臉部影像
cv.imshow('noface2',noface2)#不包含臉部資訊的影像
cv.imshow('extractimg',extractimg)#臉部解碼影像
cv.waitKey()

#----接續 0717的影像色彩













 












