from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver_path = 'chromedriver.exe'
driver = webdriver.Chrome(driver_path)
driver.get("http://www.imdb.com/")
search_elem = driver.find_element_by_css_selector("#suggestion-search") ##navbar-query
search_elem.send_keys("The Shape of water")
time.sleep(3)
search_button_elem = driver.find_element_by_css_selector(".ipc-icon.ipc-icon--magnify")
search_button_elem.click()                              # #navbar-submit-button .navbarSprite
time.sleep(3)
first_result_elem = driver.find_element_by_css_selector("#findSubHeader+ .findSection .odd:nth-child(1) .result_text a")
first_result_elem.click()
time.sleep(3)
rating_elem = driver.find_element_by_css_selector("strong span")
rating =float(rating_elem.text)
cast_elem = driver.find_elements_by_css_selector("#titleCast") # .itemprop .itemprop
cast_list = [cast.text for cast in cast_elem] #對像不可迭代??? 要加s 表示此資料為 複數，才可以進行疊代
# driver.close()
print(rating, cast_list) # 試試看 我忘了把text拿掉了
# print(rating, cast_elem.text)
# OK! 掰囉


# 以上為 6/5 imdb範例，因選擇器定位"標籤"大部份被更動了，所以要重新尋找當前的標籤做定位
# 提供基本的定位方法，同學可參考

# 以下標籤知識小補充: 可先暫停看一下
# 有id 請以id做定位，因為id通常不重複使用，例如 #main
# class定位前面要加一個點，例如 .items，倘若有重複class名稱則需找他上層(爸爸)或是上上層(爺爺)，例如 ("#爺爺 .爸爸 .items")
# 要注意如果同一個標籤下的class是由多個單字組成的話，請把中間空白字元替換成一個點
# 例如你要取的元素長這樣 class="How are you" 這裡要注意，因為是"同一個標籤"下的class請把他黏起來寫成 ".How.are.you"
# 如果你看到的不是id 也不是class，而是最前端的名稱，那應該就是html標籤名稱，例如 <div> <title> <span> <a> 這有很多種請谷歌
# CSS選擇器就是用這些標籤、屬性做定位，方可取得你想爬的資料，或拿來點擊進入另一頁的元素。
