#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/4/15 14:20
# @Author  : sunbcy
# @File    : test.py.py
# @Software: PyCharm
import requests
import json
import execjs

cookies = {
    'Hm_lvt_1521e0fb49013136e79181f2888214a7': '1713159369',
    'Hm_lpvt_1521e0fb49013136e79181f2888214a7': '1713159419',
    'JSESSIONID': '0A18AFA1101379DF3AF1C4E0E8D70F1D',
    '_ACCOUNT_': 'ZWVjMGIwNDcwZjYzNDVkYWI4NTY2N2Q0YzQzOTExNTYlNDAlNDBtb2JpbGU6MTcxNDM3MTM2NTQzMzo4NjA1ZTdjZmIxMWU5ZDdiM2QxNTQ3NjZjNzZiZGYzNQ',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Auth-Plus': '',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Origin': 'https://www.hanghangcha.com',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'clientInfo': 'web',
    'clientVersion': '1.0.5',
    'currentHref': 'https://www.hanghangcha.com/products-local',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'filter': '{"specialTag":null,"city":"","lv":null,"province":"","userId":6352106,"companyId":null,"limit":20,"skip":0,"keyword":null,"companyType":"local","industry":""}',
}

response = requests.get(
    'https://api.hanghangcha.com/hhc/member/invest/getProduct',
    params=params,
    cookies=cookies,
    headers=headers,
).json()  # json字符串和python字符串不一样
encrypted_data = response  # ['data']
jscode = open('hanghangcha.js', 'r', encoding='utf-8').read()
ctx = execjs.compile(jscode)
ret = ctx.call('decrypt', encrypted_data)
print(ret)
