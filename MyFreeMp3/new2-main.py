#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/21 13:13
# @Author  : sunbcy
# @File    : new2-main.py
# @Software: PyCharm
import requests
import json
import time
import execjs
from urllib.parse import quote

music_name = input("请输入歌曲或歌手姓名:")
page = int(input('请输入页码：'))
timestamp = int(time.time() * 1000)
e = f'{{"type":"YQM","text":"{music_name}","page":{page},"v":"beta","_t":{timestamp}}}'
t = 'yGz4n9XE9xYy2Oj5Ub7E6u9a5p5aIWZYe53Orq5wE5UgnjbWq0410WTvmLBO1Z2N'
encoded_url = quote(e)
# print(f"加密数据: {encoded_url}")
with open("new2-myfreemp3.js", 'r', encoding='utf-8') as f:
    token = "20230327." + execjs.compile(f.read()).call('get_token', t, encoded_url)
    # print(f"加密结果: {token}")
    headers = {
        "authority": "api.liumingye.cn",
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "cache-control": "no-cache",
        "content-type": "application/json;charset=UTF-8",
        "origin": "https://tools.liumingye.cn",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    }
    url = "https://api.liumingye.cn/m/api/search"
    data = {
        "type": "YQM",
        "text": f"{music_name}",
        "page": page,
        "v": "beta",
        "_t": timestamp,
        "token": f"{token}"
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, data=data)
    text_data = json.loads(response.text)
    try:
        for s, li in enumerate(text_data['data']['list']):
            print(s + 1, ' ', li['name'], ' ',li['artist'][0]['name']+' ')
        which_music = int(input('请输入歌曲编号:'))
        downlode_which_id = text_data['data']['list'][which_music - 1]['id']
        # print(text_data['data']['list'][which_music-1])
        quality = 128
        mus_data = f'{{"id":"{downlode_which_id}","quality":"{quality}","_t":"{timestamp}"}}'
        # print(mus_data)
        # quit()
        with open("myfreemp3.js", 'r', encoding='utf-8') as fp:
            encrypt_data = quote(mus_data)
            token_music = "20230327." + execjs.compile(fp.read()).call('get_music_token', t, encrypt_data)
            print(token_music)
            urls = "https://api.liumingye.cn/m/api/link"
            params = {
                "id": f"{downlode_which_id}",
                "quality": f"{quality}",
                "_t": f"{timestamp}",
                "token": f"{token_music}"
            }
            req = requests.Request('GET', urls, params=params)
            prepped = req.prepare()
            # 输出构建好的URL
            print('音乐地址:\n', prepped.url)
    except KeyError:
        print('暂无搜索结果')