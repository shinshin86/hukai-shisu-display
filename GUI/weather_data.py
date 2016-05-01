# -*- coding: utf-8 -*-
from urllib.request import urlopen

def get_weather(city_id, app_id):
    
    access_api_text = "http://api.openweathermap.org/data/2.5/forecast?id=" + str(city_id) + "&APPID=" + str(app_id)
    response = urlopen(access_api_text)
    
    # Convert bytes to string type and string type to dict
    rep_data = response.read().decode('utf-8')

    return rep_data