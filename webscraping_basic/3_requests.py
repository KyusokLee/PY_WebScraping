import requests as rq

# get(""): URLに接続して、情報を読み込むメソッド
res = rq.get("http://google.com")
# res = rq.get("http://nadocoding.tistory.com")
print("status code:", res.status_code) #200: 正常 #403: ページにアクセスできる権限がないということ

#403の場合は、他の方法でアクセスして、web scrappingを行う

# if res.status_code == rq.codes.ok:
#     print("正常です.")
# else:
#     print("問題が生じました.  [Error Code ", res.status_code, "]")

res.raise_for_status() #errorの場合は、プログラムを直ちに終了させる
print("Web Scrappingを行います")

print(res.text) #URLのtextを持ってくる

# ファイルの生成 -> with open() 
# 書き込みモード : "w"
# encoding="utf8": utf8にencodingを行う
# as f: fという変数としてこのコードで扱うという意味
with open("mygoogle.html", "w", encoding="utf8") as f:
    #f.write() -> ()中にある内容をfileとして生成する -> workplaceのdirectoryに作成される
    f.write(res.text)