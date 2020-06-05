import xml.etree.ElementTree as ET
tree = ET.parse('全國細懸浮微粒手動監測資料.xml')
root = tree.getroot()

for s in root.findall('data'):
    site = s.find('SiteName').text
    county = s.find('Concentration').text
    pm = s.find('ItemUnit').text
    print('測站:', site,'--縣市', county, '--PM2.5 = ', pm)
    