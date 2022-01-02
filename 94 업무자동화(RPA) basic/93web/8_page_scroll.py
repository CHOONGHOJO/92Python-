import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("./chromedriver")
# browser.maximize_window() # 창 최대화
browser.get("https://search.shopping.naver.com/allmall")

# allmall click
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div/div[2]/div/div[4]/a[2]').click()

# # 무선 마우스 입력
# elem = browser.find_element(By.XPATH, '//*[@class="autoComplete_layer_auto__3y-0p autoComplete_active__3HkBd"' ).send_keys('무선마우스')
# time.sleep(1) # 1초 대기
# elem.send_keys(Keys.ENTER) # 검색 버튼 클릭을 위해 Enter 처리

# 1. 지정한 위치로 스크롤 내리기
# 모니터 해상도 높이인 1080 위치로 스크롤 내리기
# browser.execute_script('window.scrollTo(0, 1080)') # 모니터 해상도에 따라 조정
# browser.execute_script('window.scrollTo(0, 2080)') # 모니터 해상도에 따라 조정

# 2. 화면 가장 아래로 스크롤 내리기
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)') # 모니터 해상도에 따라 조정


# 3. 동적 페이지에 대해 마지막까지 스크롤 다운 반복 수행
interval = 2 # 2 처에 한 번씩 스크롤 내리기

# 현재 문서 높이  가져와서 저장
prev_height = browser.execute_script('return document.body.scrollHeight')

#반목수행
while True:
     # scroll down
     browser.execute_script('window.scrollTo(0, document.body.scrollHeight)') # 모니터 해상도에 따라 조정

     #  page loading time standby
     time.sleep(interval)

     # 현재 문서 높이 가져와 저장
     curr_height  = browser.execute_script('return  document.body.scrollHeight')
     if curr_height == prev_height: # 직전 높이와  같으면, 높이 변화가 없으면
          break
     prev_height = curr_height

# 4. 화면 가장  위로 스크롤 올리기
browser.execute_script('window.scrollTo(0, 0)') 

time.sleep(3)

browser.quit()

