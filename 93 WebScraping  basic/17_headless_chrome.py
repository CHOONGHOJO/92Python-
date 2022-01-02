from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")

browser = webdriver.Chrome("./chromedriver", options=options)
browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/movies/collection/cluster?clp=0g4XChUKD3RvcHNlbGxpbmdfcGFpZBAHGAQ%3D:S:ANO1ljJvXQM&gsr=ChrSDhcKFQoPdG9wc2VsbGluZ19wYWlkEAcYBA%3D%3D:S:ANO1ljK7jAA&hl=ko&gl=US"
browser.get(url)

# 화면 가장 아래로 scroll 내리기
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)") #

import time
inbterval = 2 # 2초에 한번씩 스크롤 내림

# 현재 문서 높이를 가져 와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤을 가장 아래로 내림
    print("prev_height!!", prev_height)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)") #

    # page loading 대기
    time.sleep(inbterval)

    # 현재 문서 높이를 가져 와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")

    if curr_height == prev_height:
      break

    prev_height = curr_height


print("스크롤 완료")

browser.get_screenshot_as_file("google_movie.png")

##########################################################

import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml")

movies = soup.find_all("div", attrs= {"class":"Vpfmgd"})

print(len(movies))

for movie in movies:
  title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
  # print(title)

  # 할인 전 가격
  original_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})
  if original_price:
    original_price = original_price.get_text()
  else:
    # print(title, "<할인되지 않은 영화 제외>")
    continue

  # 할인된 가격
  price = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()

  # link
  link = movie.find("a", attrs={"class":"JC71ub"})["href"]
  #올바른 링크 : https://play.google.com + link

  print(f"제목 : {title}")
  print(f"할인 전 금액 : {original_price}")
  print(f"할인 후 금액 : {price}")
  print("링크 : ","https://play.google.com" + link + "&hl=ko&gl=US")
  print("-"*80)

browser.quit()

