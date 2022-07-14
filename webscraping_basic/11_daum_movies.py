import requests
from bs4 import BeautifulSoup

# イメージscraping して、ダウンロードする
# 2015年から2019年までの人気映画を上位5個まで読み込む
for year in range(2015, 2020):
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class":"thumb_img"})

    for index, image in enumerate(images):
        image_url = image["src"]
        if image_url.startswith("//"):
            image_url = "https:" + image_url
        
        print(image_url)
        #image_urlに対し、再びrequests getを通してアクセスする
        image_res = requests.get(image_url)
        image_res.raise_for_status()

        # imageなどは、textじゃないから binaryとして扱うと言う意味で、wbにする
        with open("{}_moive{}.jpg".format(year, index + 1), "wb") as f:
            f.write(image_res.content)

        if index >= 4: #上位5個のイメージまでをダウンロードする
            break
