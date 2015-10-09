# hukai-shisu-display
####不快指数を表示するプログラム。
習作です。<br>
GUIとCLIの2種類を作成予定。

-----
####GUI版の使い方
"本日の不快指数"を表示する機能を実装予定。

#####---動作環境---
~~Python 2で実装・動作検証を行いました。~~<br>
###### Python2 ⇒ Python3
* Python3で実装・動作検証を行っていきます。

* PythonのFrameworkである"Bottle"を使用しています。

* グラフ描画にJavascriptのライブラリ"Chart.js"を使用します。


####---API---
~~気象情報を取得するため、気象データの無料APIを提供するオンラインサービスである[Openweathermap](http://openweathermap.org/)のデータを使用します。~~

使用するにはAPIキーの取得が必要とのことだったので、ひとまず今回は上記APIは使わずに、"温度"、"湿度"の２つの値を取得したと仮定して、そこから"不快指数"を計算して表示するところまでを実装します。

※温度、湿度の値については適当なJSONデータを自作して使用します。
######---使用方法---



-------

####CLI版の使い方
温度 湿度の順で引数を２つ入力して、当スクリプトを実行することで不快指数を計算して表示します。

例：温度30度、湿度80%の場合

※Python2版とPython3版を用意しました。
	
	Python2版
	python hukai_shisu_python2.py 30 80
	
	Python3版
	python hukai_shisu_python3.py 30 80
	

