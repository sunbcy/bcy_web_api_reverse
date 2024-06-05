#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/13 15:25
# @Author  : sunbcy
# @File    : main.py
# @Software: PyCharm

import requests
import execjs

cookies = {
    'mobile_iindex_uuid': '65008ff6-5bd5-5d97-93fb-a05b1b60def8',
    'Hm_lvt_2873e2b0bdd5404c734992cd3ae7253f': '1715583294',
    'Hm_lpvt_2873e2b0bdd5404c734992cd3ae7253f': '1715583561',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'mobile_iindex_uuid=65008ff6-5bd5-5d97-93fb-a05b1b60def8; Hm_lvt_2873e2b0bdd5404c734992cd3ae7253f=1715583294; Hm_lpvt_2873e2b0bdd5404c734992cd3ae7253f=1715583561',
    'Pragma': 'no-cache',
    'Referer': 'https://www.chinaindex.net/ranklist/4',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'UUID': '65008ff6-5bd5-5d97-93fb-a05b1b60def8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'funcID': 'undefined',
    'incognitoMode': '0',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'channel': 'movielist',
    'sign': '5f3cce6a40c09a221b21104cc98436a3',
}
proxies = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890'
}

response = requests.get(
    'https://www.chinaindex.net/iIndexMobileServer/mobile/movie/objectFansRank',
    params=params,
    cookies=cookies,
    headers=headers,
    proxies=proxies
).json()
data = response['data']
lastFetchTime = response['lastFetchTime']

ctx = execjs.compile(open('yulezhishu.js', 'r', encoding='utf-8').read()).call('test', data, lastFetchTime)
# print(data, lastFetchTime)

print(ctx)
