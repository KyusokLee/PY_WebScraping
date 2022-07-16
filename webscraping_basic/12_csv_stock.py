# Naverサイトから KOSPI 相場総額 1 ~ 200位までの企業のデータをscrapingする
# また、そのデータをcsvに保存する -> データの加工を容易にする

import csv
from decimal import Underflow
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

# ファイル名の指定
filename = "KOSPI時価総額1-200.csv"

# open(): ファイルを書き込みモードで開く
# newline="":改行による不要な空白を消すように
# encoding="utf-8-sig": ハングルや日本語などの文字化けを防ぐ encoding手法
f = open(filename, "w", encoding="utf-8-sig", newline="")

# ファイル書き込みのtypeを指定
# 書き込みモードでファイルを開くという内容の変数をcsv拡張子に指定
writer = csv.writer(f)

# ファイルを書き込むとき、scrapingして得られたデータが何を意味するかをわかりやすくするため、データごとのtitleを設定する
# split("\t"): tabで区切った文字をtab文字を無くした形として、listに格納 
title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t")
# ["N", "종목명", "현재가", ....]
print(type(title))
writer.writerow(title)

for page in range(1, 5):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")

        if len(columns) <= 1: #意味のないデータ(改行)をSkipする
            continue

        # 1行で実装するfor文を用いたlist生成
        # strip() : 必要としない \n\n\t\tのようなものを消したデータを読み込むように
        data = [column.get_text().strip() for column in columns]
        #print(data)
        writer.writerow(data)

