# request.text を用いて持ってきたデータは、text型の htmlである。

# beautifulsoup4 -> テキスト形式のデータから欲しいhtmlタグを抽出することを可能とさせるライブラリ
# lxml: parsingを支援するライブラリ

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status

#soupは、持ってきたページの全てのHtml文書を持っている。
soup = BeautifulSoup(res.text, "lxml")

# print(soup.title) #Webページの htmlコードを出力する
# print(soup.title.get_text()) # Htmlコードから、文字だけを抽出できる
# print(soup.a) #持ってきたhtml文書から一番最初のaタグの情報を読み込む
# print(soup.a.attrs) #attrs -> aタグが持っている属性を表示する (Dictionary型)
# print(soup.a["href"]) # a elementのhref属性の値の情報を読み込む

# soupにある全てのobjectの中、aタグに当てはまる最初のelementを探す
# tagの後のattrs(属性)を示して、ターゲットを探す
# print(soup.find("a", attrs={"class":"Nbtn_upload"})) #class = "Nbtn_upload"である a elementを探してくれ！

# print(soup.find(attrs={"class":"Nbtn_upload"})) #唯一なattrsの場合は、aタグ省略可能である
#class = "Nbtn_upload"のある element を探してくれ！

# print(soup.find("li", attrs={"class":"rank01"}))
# rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a) #rank1 objectからaタグの情報だけを抽出する
# print(rank1.a.get_text()) #rank1 objectからaタグの情報だけを抽出し、その文字だけを読み込む

# # next_sibling = 指定したelementを用いて、兄弟関係である次のelementを探すことが可能
# # previous_sibling = 指定したelementを用いて、兄弟関係である前の順にあるelementを探すことが可能
# # print(rank1.next_sibling) #タグ間で改行文字があると、何も表示されなくなる
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())

# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())

# # parent : 指定したtagの親のタグを探すことが可能
# print(rank1.parent)

# find_next_sibling: 兄弟関係である次のelementを探す 改行文字とか無視して、次のelementを探す
# rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())

# find_next_siblings : 兄弟関係である全てのelementを全て持ってくる
# print(rank1.find_next_siblings("li"))

# 指定したtextを持つa タグを探す
webtoon = soup.find("a", text="현실퀘스트-38화")
print(webtoon)