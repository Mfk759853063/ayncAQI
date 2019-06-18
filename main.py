#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/17 10:22 AM
# @Author  : Aries
# @Site    : 
# @File    : main.py.py
# @Software: PyCharm


import datetime
import os
from apscheduler.schedulers.blocking import BlockingScheduler
import json
from juhe.weather import Weather
import redis

weather_api = Weather()
r = redis.Redis(host='127.0.0.1', port=6379)


def task():
    with open("citys.json", 'r', encoding="UTF-8") as json_file:
        citys = json.load(json_file)
        print(str.format("准备同步以下城市的数据 {}", citys))
        for city in citys:
            city_name =  city["name"]
            city_code = city["code"]
            city_info = weather_api.get_info_by_city(city_name)
            sync_data = {"pm2_5": city_info["air"].get("pm25", ""),
                             "pm10": city_info["air"].get("pm10", ""),
                             "api": city_info["air"].get("aqi", ""),
                             "condTxt": city_info["weather"].get("cond_txt", ""),
                             "temp": city_info["weather"].get("tmp", ""),
                             "humidity": city_info["weather"].get("hum", ""),
                            "name": city_name,
                         "updatetime": datetime.date.today().strftime("%d, %m %Y")
                         }
            r.set(str.format("syncaqi{}", city_code), json.dumps(sync_data))
            print(sync_data)

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(task, 'cron', hour = "5")
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass