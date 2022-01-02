import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies/top?hl=ko&gl=US"
# url = "https://play.google.com/store/movies/top"
# url = "https://www.youtube.com/"
headers = {"user-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
"Accept-Language":"Ko-KR,Ko"
}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs= {"class":"N9c7d eJxoSc"})
# movies = soup.find_all("div", attrs= {"class":"ZmHEEd  fLyRuc"})
print(len(movies))

with open("movie.html", "w", encoding="utf8") as f:
  # f.write(res.text)
  f.write(soup.prettify()) # html 문서를 예쁘게 출력

for movie in movies:
  title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
  print(title)