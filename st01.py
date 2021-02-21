import streamlit as st


csv_file = open("birdlist.csv","r")
#rはreadの意味

#言語リストを作成
deu = []
eng = []
jap = []
lat = []
nabu = []


for line in csv_file:
#列がある限り実行しなさい
    splitter = line.split(";")
#line.splitというメソッドを使って、最初の行を;の後で分割する。
#splitterリストのそれぞれの番地0から4へ言語リストの要素を割り当てる
    deu.append(str(splitter[0]))
    eng.append(str(splitter[1]))
    jap.append(str(splitter[2]))
    lat.append(str(splitter[3]))
    nabu.append(str(splitter[4]))
#これを行がある限りリピートする。

#言語リストを辞書にまとめる
#辞書を表す変数はdata,{}はdictionary作成のためのカッコ、各言語リストに名前をつける
data = {"deu":deu,"eng":eng,"jap":jap,"lat":lat,"nabu":nabu}
linker = 0

#検索のための関数searchを定義
def search(x):
    global position
    global answer0
    global answer1
    global answer2
    global answer3
    global answer4
    global link

    #言語リストの中の位置をゼロから始める、positionと定義しました
    position = 0
    length = len(data["deu"])
    #インデックスをiとしました。ループ内で実行する回数を定義します。
    i = 0
    while i < length:
    #while これが正しければという条件設定
        if x == data["deu"][i]:
            position = i
        i = i + 1
    i = 0
    while i < length:
        if x == data["eng"][i]:
            position = i
        i = i + 1
    i = 0
    while i < length:
        if x == data["jap"][i]:
            position = i
        i = i + 1
    i = 0
    while i < length:
        if x == data["lat"][i]:
            position = i
        i = i + 1
    if position == 0:
        #一回も出てこなかったらポジションは０のままなので、
        answer0 = "見つかりませんでした"
        answer1 = ""
        answer2 = ""
        answer3 = ""
        answer4 = ""
        link = ""
        #configureとは修正するという意味
    else:
        answer0 = ""
        answer1 = "ドイツ語: " + data["deu"][position]
        answer2 = "英語: " + data["eng"][position]
        answer3 = "日本語: " + data["jap"][position]
        answer4 = "_学名: " + data["lat"][position] + "_"
        link = data["nabu"][position]
        #res1.configure(text="独: " + data["deu"][position] + "\n" + "英: " + data["eng"][position] + "\n" + "日: " + data["jap"][position])
        #res2.configure(text="学名: " + data["lat"][position] )
        #res3.configure(text="\n" + "自然保護団体NABUのサイトで該当の野鳥の画像が閲覧できます。")



st.title("ドイツの身近な野鳥 多言語辞書")


st.write("ドイツでよく見られる鳥の名前を日英独および学名で表示します。")

st.write("鳥の名前をいずれかの言語または学名で入力してください。" + "\n" + "日本語の場合はカタカナで、それ以外は最初の文字を大文字で入力してください。")

#エントリーボックス
st.write()
text = st.text_input("")

#ボタンを作成
if st.button("調べる"):
    search(text)
    st.write(answer0)
    st.write(answer1)
    st.write(answer2)
    st.write(answer3)
    st.write(answer4)


else:
    st.write("")
#Test