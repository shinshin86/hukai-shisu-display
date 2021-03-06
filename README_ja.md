# hukai-shisu-display
#### 不快指数を表示するプログラム。
習作です。<br>
GUI版とCLI版の2種類が存在します。

[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](./LICENSE)

-----
#### GUI版の使い方
* "本日の不快指数"、ならびに温度と湿度を数値で表示する機能を実装予定。
* ５日前までの不快指数、並びに温度と湿度をグラフで表示。


##### ---デモ画面---

[DEMO PAGE on Heroku](https://hukai-shisu-display.herokuapp.com/)

![デモ画面](./image/demo.png)

##### ---動作環境---

* Python3で実装・動作検証を行っていきます。

* PythonのFrameworkである"Bottle"を使用しています。

* グラフ描画にJavascriptのライブラリ"Chart.js"を使用します。


#### ---API---
気象情報を取得するため、気象データの無料APIを提供するオンラインサービスである[Openweathermap](http://openweathermap.org/)のデータを使用します。<br>



-------

#### CLI版の使い方
温度 湿度の順で引数を２つ入力して、当スクリプトを実行することで不快指数を計算して表示します。

例：温度30度、湿度80%の場合

※Python2版とPython3版を用意しました。
	
	Python2版
	python hukai_shisu_python2.py 30 80
	
	Python3版
	python hukai_shisu_python3.py 30 80
	

