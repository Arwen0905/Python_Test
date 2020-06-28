import time
import numpy as np
def calculator():
    a = np.random.rand(1000)
    b = list(a)
    start_time=time.time()
    for _ in range(100):
        sum_a = np.sum(a)
        
    print(sum_a,"using NumPy\t%f sec"%(time.time()-start_time))    
    start_time=time.time()
    
    for _ in range(100):
        sum_b = sum(b)
        
    print(sum_b,"Not using NumPy\t %f sec"%(time.time()-start_time))
    
# calculator()


x = np.array( ((1,2,3),(4,5,6)) )
y = np.array( [[1,2,3],[4,5,6]] )
print(x)
print(y)

n=5
def rand():
    lstRand = [np.random.randint(1000) for i in range(n)]
    return lstRand

data = [rand(),rand()]
print(data)
ar1 = np.array(data,dtype=float)
print(ar1)
ar1 = np.array(data,dtype=bool)
print(ar1)
#========================================================
# print(np.zeros((3,3)),'\n')
# print(np.ones((3,3)),'\n')
# print(np.arange(0,10,2),'\n')
# print(np.linspace(0,10,3),'\n')
# =======================================================
print("相關屬性=================================================")
ar2 = np.array([rand(),rand()])
print(ar2)
print(ar2.ndim,'ndim << 幾維資料')
print(ar2.shape,'shape << 顯示tuple行列數')
# print(ar2.T,'T << 行列顛倒')
print(ar2.data,'data << 記憶體位置')
print(ar2.dtype,'dtype << ndarray資料型別')
print(ar2.flat,'flat << 可將ndarray轉換成一維陣列')
print(ar2.imag,'imag << 圖片虛數 imaginary part')
print(ar2.real,'real << 將虛數轉回實數 real part')
print(ar2.size,'size << 顯示ndarray的元素數量')
print(ar2.itemsize,'itemsize << 顯示byte單位的記憶體使用量')
print(ar2.nbytes,'nbytes << 顯示byte單位的所有記憶體使用量')
print(ar2.strides,'strides << 步長,用tuple顯示各維移動元素')

print("聚合函式=================================================")
ar3 = np.array([i for i in range(1,11)])
print(ar3.prod(),'prod << 乘積')
print(ar3.mean(),'mean << 平均=總數/數量')
print(np.median(ar3) ,'median << 中位元元數')
print(ar3.min(),'min << 最小值')
print(ar3.max(),'max << 最大值')
print(np.argmax(ar3),'argmax << 最大值索引')
print(np.argmin(ar3),'argmin << 最小值索引')
print(np.std(ar3),'std << 計算標準差')
print(np.var(ar3),'var << 計算均差，std的平方等於var')
print(np.any(ar3),'any << 是否部分為真')
print(np.all(ar3),'all << 是否全部為真')
print(np.percentile(ar3,30),'percentile << 計算元素排名，需要附加一個參數')
# print(ar3)
print(np.cumsum(ar3),'cumsum << 回傳累積的數值')
# ==============================================================
print("np實用技巧=================================================")
x = np.arange(12).reshape(2,6)
print(x)
y = x[1][1:]
print(y,'<< 乾淨的y')
print(x,'<< 原來的x')
y[1]=200
print(x,'<< y[1]=200。被牽動的x')
# np.array的型態是參照形式，若是以參照形式傳遞地址，改了任一方值，其它參照於此地址的內容皆會更改
x[1][1]=666
print(type(y),'<< 類型')
print(y,'<< x[1][1]=666。被改牽動的y')


a = [[np.random.randint(10) for a in range(6)]for i in range(2)]
print(a)
b = a[0:][0:]
print(b,'<< b改動前')
b[0][0] = 200
print(b,'<< b改200後')
print(a,'<< a 檢查這裡有沒有被改') # 正常的list傳值是 傳遞內容，非地址
print()
a = [a for a in range(10)]
a = np.array(a)
print(a)

a = [10,20]
b = a 
b[0]=200
print(a,'<< a沒事')
print('Numpy索引==================================================')
lst = []
for i in range(6):
    lst.append([])
    for j in range(6):
        lst[i].append(j+i*10)
# lst = np.array(lst)
print(lst)
print(lst[0][3:5])


b = np.array([[i+(j*10) for i in range(6)] for j in range(6)])
print(b)

print(b[0,3:5])
print(b[4:,4:])
print(b[:,2])
print(b[3::2,0::2]) # np索引，這蠻特別的

c = np.arange(12).reshape(3,4)
print(c)
print(c[[0,1,2],[2,1,0]]) # 運用陣列的形式，索引陣列裡面的值，也很特別
print(c[np.ix_([1,2],)]) # 
print(c[np.ix_([0,2],[1,3])]) # []方框裡每個數字，都是"單一索引值"，np.ix([col],[row]) #特別用法

print("\nNumpy的切割(Slicing)")
arr = np.arange(10)
print(arr)
slice = arr[5:8]

arr[5:8]=7
print(slice)

slice[1]=87
print(slice)

print(arr) # np.arange方法，用[索引]切割出去的變數，若改變值也會改變原本陣列，解釋為切割地址記憶體出去。





























