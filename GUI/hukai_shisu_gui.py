# -*- coding: utf-8 -*-
from bottle import route, run, template, static_file, url


# css,js読み込み
@route('/static/<filepath:path>',name='static_file')
def static(filepath):
    return static_file(filepath, root='./static')



# URLから温度・湿度を取得
@route('/<temperature:int>/<humidity:int>')
def print_hukaiShisu(temperature,humidity):
    hukai_shisu_result = 0.81 * float(temperature) + 0.01 * float(humidity) * (0.99 * float(temperature) - 14.3) + 46.3
    
    show_hukai_shisu = "温度 : " + str(temperature) +  " 湿度 : " + str(humidity) + " 不快指数 : " + str(hukai_shisu_result)

    return show_hukai_shisu



# 本日の不快指数を表示
@route('/today')
def today():
    
    # 本日の不快指数を取得、処理。
    today_temperature = 20
    today_humidity = 70
    today_hukai_shisu_result = 0.81 * float(today_temperature) + 0.01 * float(today_humidity) * (0.99 * float(today_temperature) - 14.3) + 46.3
    result_tempe = str(today_temperature)
    result_humi = str(today_humidity)
    result_hukai = str(today_hukai_shisu_result)

    # テンプレート読み込み
    return template('index', html_today_temperature=result_tempe, html_today_humidity=result_humi,html_today_hukai_shisu_result=result_hukai,url=url)


# サーバーの設定(開発用) - debugとreloaderを有効にしている
run(host='localhost', port=8081, debug=True, reloader=True)
