import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

browser = webdriver.Chrome("./chromedriver")
browser.maximize_window() # 창 최대화
browser.get("https://www.w3schools.com/html/")

time.sleep(3)

# 특정 영역 scroll
elem = browser.find_element(By.XPATH,  '//*[@id="leftmenuinnerinner"]/a[62]')

# 1. ActionChain
# actions = ActionChains(browser)
# actions.move_to_element(elem).perform()

# 2. 방법 2 :
# xy = elem.location_once_scrolled_into_view # 함수가 아니므로 () 사용하지 않음
# print("type : ", type(xy)) # dict
# print("value : ", xy) # dict

elem.click()


time.sleep(3)
browser.quit()

