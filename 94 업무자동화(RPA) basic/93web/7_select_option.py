import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome("./chromedriver")
# browser.maximize_window() # 창 최대화

browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option")

browser.switch_to.frame('iframeResult') # frame 전환

# 1. option 에서 cars에 해당하는 element 를 찾고, 드롭다운 내부에 있는 x번째 옵션을 선택
# elem = browser.find_element(By.XPATH, '//*[@id="cars"]/option[3]') # option[3]  :  3번째 항목
# elem.click()
time.sleep(3) #  x초 대기

# 2. option 에서  text 값을 통해서 선택
# elem = browser.find_element(By.XPATH, '//*[@id="cars"]/option[text() ="Audi"]') # option[3]  :  3번째 항목
# elem.click()
# time.sleep(3) #  x초 대기

# 3. option 에서  text 값이 부분일치 하는 항목 선택
elem = browser.find_element(By.XPATH, '//*[@id="cars"]/option[contains(text(), "Au")]') # option[3]  :  3번째 항목
elem.click()
time.sleep(3) #  x초 대기

browser.quit()