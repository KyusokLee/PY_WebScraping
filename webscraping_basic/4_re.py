#正規式表現
# re: 正規式ライブラリ
import re
# ex) abcd, book, desk などの車両番号
#状況の設定: 道を歩いているAさんが、さっき見た車の車両番号を覚えてない。しかし、ある程度は覚えていたとうする
# このとき、車両番号が何であったかをどのように見つけ出すのか？ -> このとき、必要なのが 正規式表現　である
# ca?e
# care, cafe, case, cave, cade ...

# 正規式の定義を行う
p = re.compile("ca.e") 
#. : 一つの文字を意味する 
# ex) (ca.e) -> care, cafe, case (O)  | caffe (X)

# ^ : 文字列の始まりを意味する
# ex) (^de) -> desk, destination (O) | fade (X)

# $ : 文字列の終わりを意味する
# ex) (se$) -> case, base (O) | face (X)


def print_match(m):
    if m:
        # m.group(): 一致している文字列のみを返す
        print("m.group(): ", m.group())
        # m.string: 入力された文字列を返す
        print("m.string: ", m.string)
        # m.start(): 一致している文字列のstart indexを返す
        print("m.start(): ", m.start())
        # m.end(): 一致している文字列の end indexを返す
        print("m.end(): ", m.end())
        # m.span(): 一致している文字列のstartと end　indexを一緒に返す (start index, end index)
        print("m.span(): ", m.span())

    else:
        print("マッチしていません")

# m = p.match("careless") #compileで定義した正規式とマッチしているかを確認する
# # match: 与えられた文字列の先頭から一致しているかどうかを確認するlogic
# # -> そのため、carelessの場合は、最初からチェックを行い、careの部分までmatchしているため、errorがでなくなる
# print_match(m)

# m = p.search("good care") #search: 与えられた文字列の中、一致しているのがあるかを確認するlogic
# print_match(m)

# findall: 一致する全てをリスト型で返す
lst = p.findall("good care cafe")
print(lst)

#正規式の使い方
#1. p = re.compile("求めたい形")
#2. m = p.match("比較する文字列") -> 与えられた文字列の最初からcheckする
#3. m = p.search("比較する文字列") -> 与えられた文字列の中、一致しているのがあるかをcheckする
#4. lst = p.findall("比較する文字列") -> 一致する全てをlist型で返す

#求めたい形
#. : 一つの文字を意味する (ca.e) -> care, cafe, case (O)  | caffe (X)
# ^ : 文字列の始まりを意味する (^de) -> desk, destination (O) | fade (X)
# $ : 文字列の終わりを意味する (se$) -> case, base (O) | face (X)