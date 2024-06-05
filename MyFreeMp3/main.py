#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/21 10:51
# @Author  : sunbcy
# @File    : main.py
# @Software: PyCharm
import requests
import execjs
from urllib.parse import quote
import time
import json
# print(time.time_ns())
# quit()

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://tools.liumingye.cn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
}


def get_token(searchkey):
    cnt = execjs.compile(open('new-myfremp3.js', 'r', encoding='utf-8').read()).call('encrypt_token', quote(searchkey))
    return cnt


search_key = '周深 baby'

# json_data = {
#     "type": "YQB",
#     "text": search_key,
#     "page": 1,
#     "v": "beta",
#     "_t": int(time.time() * 1000)#  1716280410498  # int(round(time.time() * 1000))# 1706099652039,  # int(round(time.time() * 1000))
#      # '20230327.2465ec97dfc32aa2874558d11edada22', # get_token(search_key),
# }
e = f'{{"type":"YQM","text":"{search_key}","page":{1},"v":"beta","_t":{int(time.time() * 1000)}}}'
token = get_token(e)
print(token)
json_data = {
        "type": "YQM",
        "text": f"{search_key}",
        "page": 1,
        "v": "beta",
        "_t": int(time.time() * 1000),
        "token": f"{token}"
    }
# json_data['token'] = token  # '20230327.fb845bad2941b5c6497c9a7c65ecf225'  # token
# json_data = json.dumps(json_data, separators=(',', ':'))
print(json_data)
response = requests.post('https://api.liumingye.cn/m/api/search', headers=headers, json=json_data).json()
print(response)
