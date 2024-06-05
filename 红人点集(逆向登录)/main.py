#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/16 8:21
# @Author  : sunbcy
# @File    : main.py
# @Software: PyCharm
import requests
import execjs

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://www.hh1024.com',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

# json_data = {
#     'phoneNum': '13216077035',
#     'pwd': 'f6ba3bc8fb16582e89a596b8de4bf466',
#     't': 1715822409309,
#     'tenant': 1,
#     'sig': 'fb29fe22da54d659892e203c09a079be',
# }

json_data = execjs.compile(open('hongrendianji.js', 'r', encoding='utf-8').read()).call('get_token')
response = requests.post('https://user.hrdjyun.com/wechat/phonePwdLogin', headers=headers, json=json_data).json()

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"phoneNum":"13216077035","pwd":"f6ba3bc8fb16582e89a596b8de4bf466","t":1715822409309,"tenant":1,"sig":"fb29fe22da54d659892e203c09a079be"}'
#response = requests.post('https://user.hrdjyun.com/wechat/phonePwdLogin', headers=headers, data=data)

print(response)
