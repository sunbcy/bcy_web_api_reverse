#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/4/15 9:25
# @Author  : sunbcy
# @File    : test.py
# @Software: PyCharm
"""
1 确定需要处理的参数
    模拟请求测试
    明确了需要携带cookie
    明确了cookie里面字段 __zpToken__ 需要携带
    明确明文信息 (new a).z(e, parseInt(t) + 60 * (480 + (new Date).getTimezoneOffset()) * 1e3)


分析关键参数
    1.先搜索
    2.hook调试
参考视频的boss.js版本 2023.11.26 本次逆向需要rpc技术(简单的方法处理)  远程调用 控制台开一个websocket服务
成功过一次 但是次数过多会被封IP,因此要确保代理成功后再投入生产.
"""
import requests

cookies = {
    'wd_guid': '6c2bc80f-17c6-45da-a76c-308b3d8e7f60',
    'historyState': 'state',
    '__g': '-',
    '_bl_uid': 'Iglznvs31z0tnmo71chC0yggLd8a',
    'collection_pop_window': '1',
    'Hm_lvt_194df3105ad7148dcf2b98a91b5e727a': '1713240010',
    '__fid': '226d4c1258dd9cf48ebe3e96d854a8ab',
    'lastCity': '101280600',
    '__l': 'r=https%3A%2F%2Fyoule.zhipin.com%2F&l=%2F%3Fka%3Dheader-home-logo&s=1',
    '__zp_seo_uuid__': '2a8bb53a-79e9-487d-abb1-445747df9dec',
    'Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a': '1713265180',
    '__zp_stoken__': '9f2afTTLDlcKyQ8OOTycbAhwDBkkkSjIwF0xNJjg1OE0yNjdKTTJOFTQ9aD18FmDDhcKPNSZNMkk1MzMyNjgWTU7FgMKyMkwoYz56GG%2FDgQbClcOKASrCtRBdAUUeNMOMJiTDvcKzSjVJMsKUwrE1w49aw49Kw4tZw4k0wrQ1MTI0MDEaBB8cMTFBRW8HQ21EVW1fEF1DXCMyT0wywpvCjMO0JkAGBQMdAgYFAx0CBgUDEB8aGR8BHggbHQMcPjXCoMOKwp5zw7Ziw7bEk8Kgw4nDom3Cp8OKwppBwrPCusOLwrLCtsKmwqhowpfCpMKSXsKjbMKxwr3Di8K3WsKOwr5xSMK0YW7Cp3PCpsOAb2fCi3Vich9qGmwHMRlrecOQ',
    '__c': '1713238009',
    '__a': '70049739.1713144353.1713237807.1713238009.95.4.50.95',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://www.zhipin.com/web/geek/job?query=Java&city=101280600',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'scene': '1',
    'query': 'Java',
    'city': '101280600',
    'experience': '',
    'payType': '',
    'partTime': '',
    'degree': '',
    'industry': '',
    'scale': '',
    'stage': '',
    'position': '',
    'jobType': '',
    'salary': '',
    'multiBusinessDistrict': '',
    'multiSubway': '',
    'page': '1',
    'pageSize': '30',
}

response = requests.get('https://www.zhipin.com/wapi/zpgeek/search/joblist.json', params=params, cookies=cookies, headers=headers)

data = response.json()

if data['code'] == 0:
    print(data)
else:
    seed = data['zpData']['seed']
    ts = data['zpData']['ts']

    s_url = f'http://127.0.0.1:5612/business-demo/invoke?group=test_web&action=get_token&t={seed}&n={ts}'
    try:
        zp_stoken = requests.get(s_url).json()['data']
        # print(zp_stoken)
        cookies['__zp_stoken__'] = zp_stoken
        # headers['cookies'] = '__zp_stoken__=' + zp_stoken
        print(cookies)
    except Exception as e:
        print(requests.get(s_url).json())
        quit()
for page in range(1, 11):
    print(f'正在打印第{page}页')
    # url = f'https://www.zhipin.com/wapi/zpgeek/search/joblist.json?scene=1&query=Java&city=101280600&experience=&payType=&partTime=&degree=&industry=&scale=&stage=&position=&jobType=&salary=&multiBusinessDistrict=&multiSubway=&page=1&pageSize=30'
    response = requests.get('https://www.zhipin.com/wapi/zpgeek/search/joblist.json', params=params, cookies=cookies, headers=headers)
    json_data = response.json()

    if json_data['code'] == 37:
        seed = json_data['zpData']['seed']
        ts = json_data['zpData']['ts']
        # print(seed, ts)
        s_url = f'http://127.0.0.1:5612/business-demo/invoke?group=test_web&action=get_token&t={seed}&n={ts}'
        zp_stoken = requests.get(s_url).json()['data']
        cookies['__zp_stoken__'] = zp_stoken
        print(zp_stoken)
        # headers['cookies'] = '__zp_stoken__=' + zp_stoken
        response = requests.get('https://www.zhipin.com/wapi/zpgeek/search/joblist.json', params=params, cookies=cookies, headers=headers)
        json_data = response.json()
        print(json_data)
    else:
        print(json_data)
    break