#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/16 11:52
# @Author  : sunbcy
# @File    : main.py
# @Software: PyCharm

"""缺json_data的加密参数逆向就完整了"""
import requests
import execjs

cookies = {
    'btoken': 'LVXW9A8E3XXHCQ6HCPGWDCRTCQ4KCE93',
    'Hm_lvt_42317524c1662a500d12d3784dbea0f8': '1715825981',
    'hy_data_2020_id': '18f7f32b6b6b1b-0ca1b457681818-26001d51-3686400-18f7f32b6b717ec',
    'hy_data_2020_js_sdk': '%7B%22distinct_id%22%3A%2218f7f32b6b6b1b-0ca1b457681818-26001d51-3686400-18f7f32b6b717ec%22%2C%22site_id%22%3A211%2C%22user_company%22%3A105%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%2218f7f32b6b6b1b-0ca1b457681818-26001d51-3686400-18f7f32b6b717ec%22%7D',
    'sajssdk_2020_cross_new_user': '1',
    'utoken': 'QNF0Y9XV6V16OQSRY0QN3T3MC1C3B201',
    'username': '%E9%A3%9E%E9%B8%9F',
    'Hm_lpvt_42317524c1662a500d12d3784dbea0f8': '1715832557',
}

headers = {
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    # 'cookie': 'btoken=LVXW9A8E3XXHCQ6HCPGWDCRTCQ4KCE93; Hm_lvt_42317524c1662a500d12d3784dbea0f8=1715825981; hy_data_2020_id=18f7f32b6b6b1b-0ca1b457681818-26001d51-3686400-18f7f32b6b717ec; hy_data_2020_js_sdk=%7B%22distinct_id%22%3A%2218f7f32b6b6b1b-0ca1b457681818-26001d51-3686400-18f7f32b6b717ec%22%2C%22site_id%22%3A211%2C%22user_company%22%3A105%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%2218f7f32b6b6b1b-0ca1b457681818-26001d51-3686400-18f7f32b6b717ec%22%7D; sajssdk_2020_cross_new_user=1; utoken=QNF0Y9XV6V16OQSRY0QN3T3MC1C3B201; username=%E9%A3%9E%E9%B8%9F; Hm_lpvt_42317524c1662a500d12d3784dbea0f8=1715832557',
    'origin': 'https://www.xiniudata.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.xiniudata.com/project/lib',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

json_data = {
    'payload': 'LBcwWVcRKDslJCpgAh4IZRA3WUZJPSZTOSsNPzMiWyA5fCBLEnQdaxVteyFXNyUmQDVCUWYiJl07JzwuMwxWPHUPH2UcbCU1OjE2MFkxMBZRPUJNcDYnEHcVD2F0Jl09J1o2WUQrGT4hMi0wUSYhAFYnFA5iD3gQLiEgPTk3UzsyaiFLRC8kNiEyMQZZMTAWQSBXRk1wblw4Ij5hdCZdPSdaNllEKxk/OzU4IFQsJiF2NUJRZjc6Vm90PDg6KR5tMUAqXFkgIQUuNDcmUSsyDVMgU2tKJjVAOWxoIyMpXmN1UzFWVCcoPRcnLCxcLDsudjVCUWY3OlZvdDw4OikebTRaNkhfPCcuLR41LVskISBdOn9QSnBuaRBicC45N0IgJVQwXW88KS8mJSpgAh4IZRA7RlFLMyBdP2xobzcrVm17FypXRAg0NSUGNixfNj0oXDMUDk0gIVdhbCEiJDEQdWADdAgGYmQ1OiU8MBp/eHgedkVAWCAgEHd+fm86LF8mIxd+CgBiZD4nLDwxTCw2awg6Q1hVLw==',
    'sig': 'A236664381265C63CD04B6A3806F0A20',
    'v': 1,
}

response = requests.post(
    'https://www.xiniudata.com/api/search3/company/search_company_for_lib',
    cookies=cookies,
    headers=headers,
    json=json_data,
).json()

data = response['d']
print(data)
# cnt = execjs.compile(open('xiniudata.js', 'r', encoding='utf-8').read()).call('decode1', data)
#
# print(cnt)

# import requests
#
# cookies = {
#     'btoken': 'LVXW9A8E3XXHCQ6HCPGWDCRTCQ4KCE93',
#     'Hm_lvt_42317524c1662a500d12d3784dbea0f8': '1715825981',
#     'hy_data_2020_id': '18f7f32b6b6b1b-0ca1b457681818-26001d51-3686400-18f7f32b6b717ec',
#     'hy_data_2020_js_sdk': '%7B%22distinct_id%22%3A%2218f7f32b6b6b1b-0ca1b457681818-26001d51-3686400-18f7f32b6b717ec%22%2C%22site_id%22%3A211%2C%22user_company%22%3A105%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%2218f7f32b6b6b1b-0ca1b457681818-26001d51-3686400-18f7f32b6b717ec%22%7D',
#     'sajssdk_2020_cross_new_user': '1',
#     'utoken': 'QNF0Y9XV6V16OQSRY0QN3T3MC1C3B201',
#     'username': '%E9%A3%9E%E9%B8%9F',
#     'Hm_lpvt_42317524c1662a500d12d3784dbea0f8': '1715832557',
# }
#
# headers = {
#     'accept': 'application/json',
#     'accept-language': 'zh-CN,zh;q=0.9',
#     'cache-control': 'no-cache',
#     'content-type': 'application/json',
#     # 'cookie': 'btoken=LVXW9A8E3XXHCQ6HCPGWDCRTCQ4KCE93; Hm_lvt_42317524c1662a500d12d3784dbea0f8=1715825981; hy_data_2020_id=18f7f32b6b6b1b-0ca1b457681818-26001d51-3686400-18f7f32b6b717ec; hy_data_2020_js_sdk=%7B%22distinct_id%22%3A%2218f7f32b6b6b1b-0ca1b457681818-26001d51-3686400-18f7f32b6b717ec%22%2C%22site_id%22%3A211%2C%22user_company%22%3A105%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%2218f7f32b6b6b1b-0ca1b457681818-26001d51-3686400-18f7f32b6b717ec%22%7D; sajssdk_2020_cross_new_user=1; utoken=QNF0Y9XV6V16OQSRY0QN3T3MC1C3B201; username=%E9%A3%9E%E9%B8%9F; Hm_lpvt_42317524c1662a500d12d3784dbea0f8=1715832557',
#     'origin': 'https://www.xiniudata.com',
#     'pragma': 'no-cache',
#     'priority': 'u=1, i',
#     'referer': 'https://www.xiniudata.com/project/lib',
#     'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-origin',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
# }
#
# json_data = {
#     'payload': 'LBcnV1QrNXhyGnsUbw4XDGIdYhYVcDNHJSsoJT8rVyEwF2gacwl0AHpwGwsaaXcnUC5eWFI4LFU+bH5vISBbNiJUKlJZNy80am17LlE1NCBVIVdaXjg9XCp4Y296Z1ohJF0uQlg9LjBqbXsRaxBjeQoFfhYVcGF8Hg9lAWVxEGN1AwJyag0KCR5jdWB6DhN4exZiDRt+dnsdFx8fYQ56bXsXd1tUKCI5KnNpJAgjZHhXMQ4BCjZkAnx4YShlclYuNFdmFBIpMzMyKTY3QSQsJkcsX1paMz1eJC89b3pnSyYzXCVWSSciM3F1e24aIiAgSDxZQUo6O0c8JzMjdGkQOz1bL1BTJi0wam17Kk0kLSBcP1MWFXAzRyQjJyc/NFs9MltmFBIpMz4tJzwrVCw/IFM6RVxcPHZvMA==',
#     'sig': '8BF293F29DF6180A02B9857CFBC0A0EA',
#     'v': 1,
# }
#
# response = requests.post(
#     'https://www.xiniudata.com/api2/service/x_service/person_company4_list/list_companies4_list_by_codes',
#     cookies=cookies,
#     headers=headers,
#     json=json_data,
# ).json()
#
# data = response['d']
# cnt = execjs.compile(open('xiniudata.js', 'r', encoding='utf-8').read()).call('decode1', data)
# print(cnt)