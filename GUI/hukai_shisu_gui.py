# -*- coding: utf-8 -*-
from bottle import route, run


# 現在はURLから温度・湿度を取得
# TODO - 別の取得方法を後々実装する
@route('/<temperature:int>/<humidity:int>')
def print_hukaiShisu(temperature,humidity):
    hukai_shisu_result = 0.81 * float(temperature) + 0.01 * float(humidity) * (0.99 * float(temperature) - 14.3) + 46.3
    print("run hukai_shisu_gui")
    return "温度 : " + str(temperature) +  " 湿度 : " + str(humidity) + " 不快指数 : " + str(hukai_shisu_result)

# サーバーの設定(開発用) - debugとreloaderを有効にしている
run(host='localhost', port=8081, debug=True, reloader=True)
