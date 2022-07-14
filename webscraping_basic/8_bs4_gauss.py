from tokenize import Double
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=675554"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# cartoons = soup.find_all("td", attrs={"class":"title"})
# title = cartoons[0].a.get_text()

# # 属性にアクセスし、その情報を持ってくる ex) "href"
# link = cartoons[0].a["href"]

# print(title)
# print("https://comic.naver.com" + link)

# 漫画の題名とlink読み込む
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title, link)

# 評価を読み込む
total_rates = 0
cartoons = soup.find_all("div", attrs={"class":"rating_type"})

for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    total_rates += float(rate)

print("全体の点数: ", total_rates)
print("平均点数: ", total_rates / len(cartoons))
