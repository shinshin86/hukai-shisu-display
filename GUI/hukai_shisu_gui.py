# -*- coding: utf-8 -*-
from bottle import route, run, template, static_file, url
import json
import math

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
    
    # 温度、湿度を格納するリストを用意
    temperatureList = []
    humidityList=[]
    
    # json読み込み
    f = open('./data/data.json', 'r')
    jsonData = json.load(f)
    
    # キーのリスト化
    keyList = jsonData.keys()
    
    for k in keyList:
        
        # listを取り出す
        if k == "list":
            groupList = jsonData[k]
        
            for n in groupList:
              # ケルビン係数で入っているため、273.15引いてから代入
              temperatureList.append(n["temperature"] - 273.15)

              humidityList.append(n["humidity"])


    f.close()


    # 1~6日前までの温度・湿度を取得
    result_ago_tempe = []
    result_ago_humid = []
    hukai_shisu_result_ago = []
    for i in range(6):
        result_ago_tempe.append(math.trunc(temperatureList[i]))
        result_ago_humid.append(math.trunc(humidityList[i]))
        hukai_shisu_result_ago.append(math.trunc(0.81 * float(temperatureList[i]) + 0.01 * float(humidityList[i]) * (0.99 * float(temperatureList[i]) - 14.3) + 46.3))
    
    
    # 本日の不快指数を取得、処理。
    today_temperature = temperatureList[6]
    today_humidity = humidityList[6]
    today_hukai_shisu_result = 0.81 * float(today_temperature) + 0.01 * float(today_humidity) * (0.99 * float(today_temperature) - 14.3) + 46.3
    result_tempe = str(math.trunc(today_temperature))
    result_humi = str(math.trunc(today_humidity))
    result_hukai = str(math.trunc(today_hukai_shisu_result))

    # テンプレート読み込み
    return template('index', html_today_temperature=result_tempe, html_today_humidity=result_humi,html_today_hukai_shisu_result=result_hukai,url=url,
                    ago_tempe_0 = result_ago_tempe[0],
                    ago_humid_0 = result_ago_humid[0],
                    ago_tempe_1 = result_ago_tempe[1],
                    ago_humid_1 = result_ago_humid[1],
                    ago_tempe_2 = result_ago_tempe[2],
                    ago_humid_2 = result_ago_humid[2],
                    ago_tempe_3 = result_ago_tempe[3],
                    ago_humid_3 = result_ago_humid[3],
                    ago_tempe_4 = result_ago_tempe[4],
                    ago_humid_4 = result_ago_humid[4],
                    ago_tempe_5 = result_ago_tempe[5],
                    ago_humid_5 = result_ago_humid[5],
                    ago_hukai_0 = hukai_shisu_result_ago[0],
                    ago_hukai_1 = hukai_shisu_result_ago[1],
                    ago_hukai_2 = hukai_shisu_result_ago[2],
                    ago_hukai_3 = hukai_shisu_result_ago[3],
                    ago_hukai_4 = hukai_shisu_result_ago[4],
                    ago_hukai_5 = hukai_shisu_result_ago[5]
                    )


# Debug用 - 読み込んだjsonをそのままブラウザ上に表示
@route('/array')
def returnarray():
    from bottle import response
    from json import dumps
    f = open('./data/data.json', 'r')
    jsonData = json.load(f)
    response.content_type = 'application/json'
    return dumps(jsonData)


# サーバーの設定(開発用) - debugとreloaderを有効にしている
run(host='localhost', port=8081, debug=True, reloader=True)
