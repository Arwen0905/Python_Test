import xml.etree.ElementTree as et
#載入xml.etree.ElementTree套件
tree = et.ElementTree(file='menu.xml')
#讀取XML檔，儲存到 tree 變數
root = tree.getroot()
#取得根節點(即XML標籤)
print(root.tag)
#輸出根節點(menu標籤名)
# for i in root: #(menu標籤下的子標籤)
#     print('tag:',i.tag,'attributes:',i.attrib)
#     #tag：取得標籤、attrib：取得標籤屬性
#     for j in i: #子標籤下的子標籤
#         print('\ttag:',j.tag,'attributes:',j.attrib)
for child in root:
    print('tag:',child.tag,'attributes:',child.attrib)
    for grandchild in child:
        print('\t tag:',grandchild.tag,'attributes:',grandchild.attrib)
print(len(root))    # 菜單選項的數目
print(len(root[0])) # 早餐選項的數目
# =====================================================================
#   XML：eXtensible Markup Language；可延伸標記語言
#   是一種電腦標記語言
#   規則特性：
#       是一種標籤語法
#       以<名稱>開頭，後面接一段內容，再以</名稱>結尾。
#       忽略空格
#       <名稱>下可能有<子名稱>，層層結構。
#       <名稱>可稱為一個節點
#       <名稱 屬性=屬性值>：代表該名稱的設定功能
#        通常用於資料傳遞與消息發佈，如RSS....，
#        一般業界會自訂客製化的XML格式。
