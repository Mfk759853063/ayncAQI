#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/18 9:10 AM
# @Author  : Aries
# @Site    : 
# @File    : test.py.py
# @Software: PyCharm


import datetime
import os
from apscheduler.schedulers.blocking import BlockingScheduler
import json
from juhe.weather import Weather

weather_api = Weather()

def task():
    with open("citys.json") as json_file:
        citys = json.load(json_file, encoding="gb18030")
        for city in citys:
            city_name =  city["name"]
            city_code = city["code"]
            city_info = weather_api.get_info_by_city(city_name)
            sync_data = {"pm2_5": city_info["air"].get("pm25", ""),
                             "pm10": city_info["air"].get("pm10", ""),
                             "api": city_info["air"].get("aqi", ""),
                             "temp": city_info["weather"].get("tmp", ""),
                            "condTxt": city_info["weather"].get("cond_txt", ""),
                             "humidity": city_info["weather"].get("hum", ""),
                            "name": city_name,
                         "updatetime": datetime.date.today().strftime("%d, %m %Y")
                         }
            print(sync_data)

if __name__ == '__main__':
    task()