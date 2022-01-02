from  selenium  import  webdriver
browser = webdriver.Chrome("./chromedriver")
# browser = webdriver.Chrome()

browser.get("http://naver.com")
elem = browser.find_element_by_link_text("카페")
# elem = browser.find_element("카페")
# print(elem)
# print(elem.get_attribute("href"))
# print(elem.get_attribute("class"))
elem.click() # click
browser.back() # 뒤로 가기
browser.forward() #  앞으로 가기
browser.refresh() # 새로 고침
browser.back() # 뒤로 가기

# 검색창 id=query
elem = browser.find_element_by_id("query")
elem .send_keys("나도코딩") # 입력창에 글자 입력
from selenium.webdriver.common.keys import Keys
elem.send_keys(Keys.ENTER)

elem = browser.find_element_by_tag_name("a")
elem.get_attribute("href")
elems = browser.find_elements_by_tag_name("a")

for e in elems:
    e.get_attribute("href")

##############################
browser.get("http://daum.net")
elem = browser.find_element_by_name("q")
elem.clear()
elem.send_keys("나도코딩")
elem.send_keys(Keys.ENTER)

elem = browser.find_element_by_xpath('//*[@id="daumSearch"]/fieldset/div/div/button[2]')
elem.click() # click

# screen shot
browser.save_screenshot('daum.png')

# source code in browser
browser.page_source()
browser.close() # 현재 창,tab 닫기
browser.quit() # 작업  종료


##############################
# 강의내용
from selenium import webdriver

#browser = webdriver.Chrome('./chromedriver.exe')
browser = webdriver.Chrome()

# 네이버 이동
browser.get('http://naver.com')

# 카페 메뉴 찾기
elem = browser.find_element_by_link_text('카페')

# 속성 가져오기
elem.get_attribute('href')
elem.get_attribute('class')

# 클릭
elem.click()

# 뒤로 가기
browser.back()

# 앞으로 가기
browser.forward()

# 새로고침
browser.refresh()

# 뒤로 가기
browser.back()

# 검색창 찾기 (개발자 도구 이용)
elem = browser.find_element_by_id('query')

# 글자 입력하기
elem.send_keys('나도코딩')

# enter 치기
from selenium.webdriver.common.keys import Keys
elem.send_keys(Keys.ENTER)

# a 태그 찾기
elem = browser.find_element_by_tag_name('a')
elem.get_attribute('href')

# a 태그 모두 찾기
elems = browser.find_elements_by_tag_name('a')
for e in elems:
    e.get_attribute('href')

# 다음으로 이동
browser.get('http://daum.net')

# 검색창 찾기
elem = browser.find_element_by_name('q')

# 글자 입력하기
elem.send_keys("나도코딩")

# 글자 지우기
elem.clear()

# 글자 입력하기
elem.send_keys("나도코딩")

# 검색 버튼 찾기
elem = browser.find_element_by_xpath('//*[@id="daumSearch"]/fieldset/div/div/button[2]')

# 클릭하기
elem.click()

# 스크린샷 찍기
browser.save_screenshot('daum.png')

# 페이지 소스 보기
browser.page_source

# 브라우저 종료
browser.close() # 현재 탭 닫기
browser.quit() # 브라우저 종료하기

# 참고 URL : https://selenium-python.readthedocs.io/