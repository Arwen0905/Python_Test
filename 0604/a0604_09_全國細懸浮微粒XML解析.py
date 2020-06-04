import xml.etree.ElementTree as ET
tree = ET.parse('全國細懸浮微粒手動監測資料.xml')
root = tree.getroot()
print('取得根節點:',root.tag)
print('取得跟節點標籤與屬性值',str(root.attrib))
for child in root.findall('data'):
    county = child.find('SiteName').text
    site = child.find('Concentration').text
    print('測站 (%s) 縣市PM2.5值為: %s'%(county,site))
