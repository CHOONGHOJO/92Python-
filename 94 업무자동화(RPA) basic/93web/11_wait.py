import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome( "./chromedriver")
browser.maximize_window()
browser.get("https://m-flight.naver.com/")

# elem = browser.find_element(By.XPATH,  '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]')
# elem.click()

# 가는 날 클릭
browser.find_element_by_link_text('가는날 선택').click()
browser.find_elements_by_link_text('30')[0].click()

# 오는 날
browser.find_elements_by_link_text('5')[1].click()

# 제주도 클릭
browser.find_element(By.XPATH,  '//*[@id="recommendationList"]/ul/li[1]').click()

# 항공권검색 클릭
browser.find_element_by_link_text('항공권 검색').click()

try:
     elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')))
     print(elem.text)
except:
     print("실패")

# 첫번째 결과 출력
# elem = browser.find_element(By.XPATH,  '//*[@id="content"]/div[2]/div/div[4]/ul/li[1]') #  element 내에 있는 text 부분을 출력
# print(elem.text) # element 내에 있는 text 부분을 출력


time.sleep(3)
browser.quit()

