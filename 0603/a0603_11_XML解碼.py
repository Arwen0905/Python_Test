import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml') #以parse讀取解析XML檔案
root = tree.getroot() #取得根節點 ※<data></data>標籤，設定給root變數
print('coutrt_data.xml的根節點'+root.tag) #輸出根節點(標籤名)
print('根節點標籤的屬性和屬性值'+str(root.attrib)) #輸出根節點的屬性與屬性值
                                        # attrib挖出該元素的屬性值{}
for child in root: 
    #以迴圈取得子節點標籤、屬性、屬性值 ※子節點=>country
    print(child.tag, child.attrib,'挖出標籤與其屬性值')
print('排名:'+root[0][0].text,'國內生產總值:'+root[0][2].text)
                        #以text輸出 country 標籤下的子標籤內容
for neighbor in root.iter('neighbor'):
    #Element.iter(目標)※尋找所有元素內，符合目標值的項目
    #以迴圈取得 neighbor 標籤屬性與屬性值
    print(neighbor.attrib)

for country in root.findall('country'):
    #以 findall() 方法取得根節點下的子節點標籤中符合的標籤取出顯示
    rank = country.find('rank').text #用find方法，country內尋找'rank'並text表示
    name = country.get('name') #用get方法，於country尋找name屬性
    print(name,rank)
