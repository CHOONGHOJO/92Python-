import time
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome("./chromedriver")
browser.maximize_window() # 창 최대화

browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')
browser.switch_to.frame('iframeResult') # frame 전환
elem = browser.find_element(By.XPATH, '//*[@id="html"]') # 성공

#  선택이 안되어 있으면 선택하기
if elem.is_selected() == False:  #  라디오 버튼이  선택되어  있지 않으면
     print("1 선택 안되어 있으므로 선택하기")
     elem.click()
else:  # 라디오 버튼이 선택되어 있다면
     print("1 선택 되어 있으므로 아무것도 안함")

time.sleep(3) # 5초 대기


#  선택이 안되어 있으면 선택하기
if elem.is_selected() == False:  #  라디오 버튼이  선택되어  있지 않으면
     print("2 선택 안되어 있으므로 선택하기")
else:  # 라디오 버튼이 선택되어 있다면
     print("2 선택 되어 있으므로 아무것도 안함")

time.sleep(3) # 5초 대기

browser.quit()