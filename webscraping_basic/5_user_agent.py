#user agent: request　先のURLから　status code 403が表示されたときの対処方法
# browser ごとに、もしくは、端末ごとに異なるページに対応できるメリットがある
# User-Agentを入れることで、実際にchromeから接続して見れるページと同様な結果を読み込むことができる

import requests as rq
url = "http://nadocoding.tistory.com"
headers = {"User-Agent": "Your User Agent String"}
res = rq.get(url, headers=headers)
res.raise_for_status()

with open("nadocoding.html", "w", encoding="utf8") as f:
    #f.write() -> ()中にある内容をfileとして生成する -> workplaceのdirectoryに作成される
    f.write(res.text)