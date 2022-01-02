# browser 마다 handle값을 가지고 있다.
import time
from selenium import webdriver

browser = webdriver.Chrome( "./chromedriver")
browser.maximize_window()
browser.get("https://www.w3schools.com/tags/att_input_type_radio.asp")

curr_handle = browser.current_window_handle
print(curr_handle)

# Try it yourself
browser.find_element_by_xpath('//*[@id="main"]/div[2]/a').click()
handles = browser.window_handles # 모든 핸들 정보
for handle in handles:
     print(handle) # 각 핸들 정보
     browser.switch_to.window(handle) # 각 핸들로 이동
     print(browser.title) # 현재 핸들의 제목 표시


# 새로 이동된 브라우져에서 뭔가 자동화 작업 수 행 ...

# 그 브라우져를 종료
print('현재 핸들 닫기')
browser.close()

# 이전 핸들로 돌아오기
print('이전 핸들로 돌아 오기 ')
browser.switch_to.window(curr_handle) # 각 핸들로 이동

print(browser.title) # HTML input type="radio"

# 브라우져 컨트롤이 가능한지 확인

time.sleep(3)
browser.get('http://daum.net')
time.sleep(3)

browser.quit()