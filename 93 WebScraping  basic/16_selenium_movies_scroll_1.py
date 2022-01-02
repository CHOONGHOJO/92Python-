# import requests
# from bs4 import BeautifulSoup

# url = "https://play.google.com/store/movies/top?hl=ko&gl=US"
# url = "https://play.google.com/store/movies/top"
# url = "https://www.youtube.com/"
# headers = {"user-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
# "Accept-Language":"Ko-KR,Ko"
# }
# res = requests.get(url, headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")

# movies = soup.find_all("div", attrs= {"class":"N9c7d eJxoSc"})
# # movies = soup.find_all("div", attrs= {"class":"ZmHEEd  fLyRuc"})
# print(len(movies))

# with open("movie.html", "w", encoding="utf8") as f:
#   # f.write(res.text)
#   f.write(soup.prettify()) # html 문서를 예쁘게 출력

# for movie in movies:
#   title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
#   print(title)


##########################################################

from selenium import webdriver
browser = webdriver.Chrome("./chromedriver")
browser.maximize_window()

# 페이지 이동
# url = "https://www.youtube.com"
url = "https://play.google.com/store/movies/top?hl=ko&gl=US"
browser.get(url)

# 지정한 위치로 scroll 내리기
# 모니터(해상도) 높이인 1080 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, 1080)") # 1920 x 1080
# browser.execute_script("window.scrollTo(0, 2080)") # 1920 x 1080

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

    print("curr_height!!", curr_height)

    if curr_height == prev_height:
      break

    prev_height = curr_height


print("스크롤 완료")