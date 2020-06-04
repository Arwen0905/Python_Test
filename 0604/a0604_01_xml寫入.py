import xml.etree.ElementTree as ET #套件
tree = ET.parse(r'../0603/country_data.xml') #以parse讀取解析XML檔案
root = tree.getroot() #取得根節點<data>

    #以迴圈取得<root>節點下符合rank的節點，執行修改 rank 標籤
for rank in root.iter('rank'):
    #設定 rank 標籤顯示的文字轉換為整數後 + 1，並設定給變數new_rank
    new_rank = int(rank.text)+1 ##int數值型態才可以※執行運算##
    #將加 1 後的顯示文字轉換回字串，並設定給變數rank.text
    rank.text = str(new_rank) ##再轉回去字串型態丟給 rank的text
    
    #以set()方法設定 rank 標籤的屬性、屬性值
    #Element.set(屬性 , 屬性值)：設定元素的屬性、屬性值
    rank.set('updated','yes')

tree.write('country_data_output_修改寫入.xml',encoding='utf8')
#利用write()方法寫入 XML 資料