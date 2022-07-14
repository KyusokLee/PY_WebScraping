import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status

#soupは、持ってきたページの全てのHtml文書を持っている。
soup = BeautifulSoup(res.text, "lxml")

# find_all: 設定した条件に当てはまる全てのelementを探す
# list型
# Naver Webtoon 全てのリスト読み込む
# class 属性がtitleである全ての"a" elementを返す
cartoons = soup.find_all("a", attrs={"class":"title"})

for cartoon in cartoons:
    print(cartoon.get_text())