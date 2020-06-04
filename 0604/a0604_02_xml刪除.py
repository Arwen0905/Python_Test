import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
root = tree.getroot() #取得根節點<data>
print(root,'<< root') # 最外層的標籤<data>
#以 findall() 方法取得根節點下的子節點標籤中符合country的標籤取出
#再以迴圈執行根節點下所有 country 標籤
for i in root.findall('country'):
    #以find()方法尋找 country 標籤下的子節點 rank 標籤的文字並轉換為整數
    rank = int(i.find('rank').text)
    
    if rank > 50:#若 rank 標籤顯示文字大於 50
         #則使用 remove() 方法移除根節點下的 country 標籤
        root.remove(i)

tree.write('country_data_output02_刪除.xml')
#利用write()方法寫入 XML 資料
for i in root.iter('year'):
    year = 