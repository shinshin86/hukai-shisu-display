# -*- coding: utf-8 -*-
from bottle import route, run, template, static_file, url
import json
import math
import weather_data

# Read a "css" & "js"
@route('/static/<filepath:path>',name='static_file')
def static(filepath):
    return static_file(filepath, root='./static')


# Get the temperature and humidity from URL
@route('/<temperature:int>/<humidity:int>')
def print_hukaiShisu(temperature,humidity):
    hukai_shisu_result = 0.81 * float(temperature) + 0.01 * float(humidity) * (0.99 * float(temperature) - 14.3) + 46.3
    
    show_hukai_shisu = "温度 : " + str(temperature) +  " 湿度 : " + str(humidity) + " 不快指数 : " + str(hukai_shisu_result)

    return show_hukai_shisu



# Display a today's temperature-humidity index.
@route('/today')
def today():
    
    # temperature & humidity list
    temperatureList = []
    humidityList=[]
    
    # Get a weather data & Read a "json"
    jsonData = json.loads(weather_data.get_weather("Please put a city id(string).", "Your API Key"))
    
    # Get a data in list
    for i in range(5):
        list_data = jsonData['list'][i]
        
        # This data is Kelvin coefficient. Before assignment, minus 273.15
        temperatureList.append(list_data['main']['temp'] - 273.15)
        humidityList.append(list_data['main']['humidity'])



    # Get a data(temperature & humidity) of since 5 days ago.
    result_ago_tempe = []
    result_ago_humid = []
    hukai_shisu_result_ago = []
    for i in range(5):
        result_ago_tempe.append(math.trunc(temperatureList[i]))
        result_ago_humid.append(math.trunc(humidityList[i]))
        hukai_shisu_result_ago.append(math.trunc(0.81 * float(temperatureList[i]) + 0.01 * float(humidityList[i]) * (0.99 * float(temperatureList[i]) - 14.3) + 46.3))
    
    
    # Get a today's temperature-humidity index.
    today_temperature = temperatureList[4]
    today_humidity = humidityList[4]
    today_hukai_shisu_result = 0.81 * float(today_temperature) + 0.01 * float(today_humidity) * (0.99 * float(today_temperature) - 14.3) + 46.3
    result_tempe = str(math.trunc(today_temperature))
    result_humi = str(math.trunc(today_humidity))
    result_hukai = str(math.trunc(today_hukai_shisu_result))

    # Read a template
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
                    ago_hukai_0 = hukai_shisu_result_ago[0],
                    ago_hukai_1 = hukai_shisu_result_ago[1],
                    ago_hukai_2 = hukai_shisu_result_ago[2],
                    ago_hukai_3 = hukai_shisu_result_ago[3],
                    ago_hukai_4 = hukai_shisu_result_ago[4]
                    )


# Debug function : Display a json data on browser
'''
@route('/array')
def returnarray():
    from bottle import response
    from json import dumps
    jsonData = json.loads(weather_data.get_weather("Please put a city id(string).", "Your API Key"))
    response.content_type = 'application/json'
    return dumps(jsonData)
'''

# Server setting (To develop) - Enable a debug & reloader
run(host='localhost', port=8081, debug=True, reloader=True)
