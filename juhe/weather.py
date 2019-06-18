#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/17 11:17 AM
# @Author  : Aries
# @Site    : 
# @File    : weather.py.py
# @Software: PyCharm

import json
import requests
from urllib.parse import urlencode, quote_plus

api_keys = ["bca544edfd874314bcaefc2ad6a09dd3"]

class Weather:
    def __init__(self):
        pass

    def get_info_by_city(self, city_name = ''):
        air_res = {}
        weather_res = {}
        url = "https://free-api.heweather.net/s6/air/now?parameters"
        params = {
            "location": city_name,
            "key": api_keys[0]
        }
        params = urlencode(params)
        try:
            resp = requests.get(url, params=params, timeout = 5)
            content = resp.content
            res = json.loads(content)
            air_res = res["HeWeather6"][0]["air_now_city"]

            url = "https://free-api.heweather.net/s6/weather/now"
            params = {
                "location": city_name,
                "key": api_keys[0]
            }
            params = urlencode(params)
            resp = requests.get(url, params=params)
            content = resp.content
            res = json.loads(content)
            weather_res = res["HeWeather6"][0]["now"]
        except requests.exceptions.RequestException as e:
            print(e)
        return {"air": air_res, "weather": weather_res}