import re
import requests
from bs4 import BeautifulSoup

def create_soup(url):
  res = requests.get(url)
  res.raise_for_status()
  soup = BeautifulSoup(res.text, "lxml")
  return soup

def print_news(idx, title, link):
  print("{}. {}".format(idx+1, title))
  print("  링크 : {}".format(link))

##############################################################
# [오늘의 날씨]
# 흐림, 어제보다 oo도 높아요
# 현재 oo도c (최저 oo도 / 최고 oo도)
# 오전 깅수확율 oo% / 오후 강수확율 oo%

# 미세먼지 oo/xx/xx 좋음
# 초미세먼지 oo/xx/xx 좋음

  # 흐림, 어제보다 oo도 높아요

def scrape_weather():
  print("[오늘의 날씨]")
  url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8"
  soup = create_soup(url)

  cast = soup.find("p", attrs={"class":"summary"}).get_text()
  # 현재 oo도c (최저 oo도 / 최고 oo도)
  curr_temp = soup.find("p", attrs={"class":"info_temperature"}).get_text().replace("도씨", "") # 현재 온도
  min_temp = soup.find("span", attrs={"class":"min"}).get_text() # 최저 온도
  max_temp = soup.find("span", attrs={"class":"max"}).get_text() # 최고 온도
  # 오전 깅수확율 oo% / 오후 강수확율 oo%
  morning_rain_rate = soup.find("span", attrs={"class":"point_time morning"}.get_text().strip())
  afternoon_rain_rate = soup.find("span", attrs={"class":"point_time afternoon"}.get_text().strip())

  # 미세먼지 oo/xx/xx 좋음
  # 초미세먼지 oo/xx/xx 좋음
  # dust = soup.find("dl", attrs={"class":"indicator"}, text=["미세먼지", "초미세먼지"])
  dust = soup.find("dl", attrs={"class":"indicator"})
  pm10 = dust.find_all("dd")[0].get_text() # 미세먼지
  pm25 = dust.find_all("dd")[1].get_text() # 초미세먼지

  # 출력
  print(cast)
  print("현재 {} (최저 {} / 최고 {})").format(curr_temp, min_temp, max_temp)
  print("오전 {} / 오후 {}".format(morning_rain_rate, afternoon_rain_rate))
  print() # 줄바꿈
  print("미세먼지 {}".format(pm10))
  print("초미세먼지 {}".format(pm25))
  print() # 줄바꿈

##############################################################
# [헤드라인 뉴스]
# 1. 무슨 무슨 일이...
#   (링크 : https://...)
# 2. 어떤 어떤 일이
#   (링크 : https://...)
# 3. 이런 저런 일이...
#  [헤드라인 뉴스] (링크 : https://...)

def scrape_headline_news():
  print("[헤드라인 뉴스]")
  url = "https://news.naver.com/"
  soup = create_soup(url)
  news_list = soup.find("ul", attrs={"class":"rankingnews_list"}).find_all("li", limit=3)
  for idx, news in enumerate(news_list):
    title = news.find("a").get_text().strip()
    link = url + news.find("a")["href"]
    print_news(idx, title, link)
    # print("{}. {}".format(idx+1, title))
    # print("  링크 : {}".format(link))
    print("-"*80)

##############################################################
# [IT 뉴스]
# 1. 무슨 무슨 일이...
#   (링크 : https://...)
# 2. 어떤 어떤 일이
#   (링크 : https://...)
# 3. 이런 저런 일이...
#   (링크 : https://...)

def scrape_it_news():
  print("[IT 뉴스]")
  url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105"
  soup = create_soup(url)
  news_list = soup.find("ul", attrs={"class":"cluster_list"}).find_all("li", limit=3)
  for idx, news in enumerate(news_list):
    a_idx = 0
    img = news.find("img")
    if img:
      a_idx = 1 # img tag가 있으면 1번째 a tag의 정보를 사용

    a_tag = news.find_all("a")[a_idx]
    title = a_tag.get_text().strip()
    link = url + a_tag["href"]
    print_news(idx, title, link)
    # print("{}. {}".format(idx+1, title))
    # print("  링크 : {}".format(link))
    print("-"*80)
  print()

##############################################################
# [오늘의 영어 회화]
# (영어 지문)
# Jason : How do you think bla bla ...?
# Kim : Well, I think ...

# (한글 지문)
# Jason : 어짜구 저쩌구 어떻게 생각하세요?
# Kim : 글쎄요, 저는 어쩌구 저쩌구

def scrape_english():
  print("[오늘의 영어 회화]")
  url = "https://www.hackers.co.kr/?c=s_lec/lec_study/lec_I_others_english&keywd=haceng_submain_lnb_lec_I_others_english&logger_kw=haceng_submain_lnb_lec_I_others_english"
  soup = create_soup(url)
  sentences = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})
  print("(영어 지문)")
  for sentence in sentences[len(sentences)//2:]: # 8문장이 있다고 가정할 때, index 기준 4~7까지 잘라서 가져옴
    print(sentence.get_text().strip())

  print()
  print("(한글 지문)")
  for sentence in sentences[:len(sentences)//2]: # 8문장이 있다고 가정할 때, index 기준 0~3까지 잘라서 가져옴
    print(sentence.get_text().strip())

  print()

####################################:
# ##########################
# main
if __name__ == "__main__":
  # scrape_weather() # 오늘의 날씨 정보 가져오기
  # scrape_headline_news() # headline news 가져오기
  # scrape_it_news() # it news 가져오기
  scrape_english() # 오늘의 영어 회화 가져오기