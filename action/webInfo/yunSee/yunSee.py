#!/usr/bin/env python3  
# -*- coding: utf-8 -*-

""" 
@author: Home丿pig 
@contact: home_pig@foxmail.com
"""
import requests
import re

from lib.common import getSaveFilePath
from lib.formatOutput import *

ACTION_NAME = "yunSee"

def start(target, par):
    opStartAction(ACTION_NAME)
    url = 'http://www.yunsee.cn/'
    data = {}
    data2 = {}
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    url2 = 'http://www.yunsee.cn/home/getInfo'
    reqts = requests.get(url=url, headers=headers)
    search = re.search('_token:.*', reqts.text)
    token = '{}'.format(search.group()).replace('}', '').replace(',', '').replace('"', '').replace(':', '').replace(
        '_token', '').strip()
    datas = 'type=webcms&url={}&_token={}'.format(target, token)
    datas2 = 'type=webinfo&url={}&_token={}'.format(target, token)
    for v in datas.split('&'):
        key, value = v.split('=', 1)
        data[key] = value

    reqvs = requests.post(url=url2, headers=headers, data=data)
    jsons = reqvs.json()

    for v in datas2.split('&'):
        key, value = v.split('=', 1)
        data2[key] = value

    reqvs2 = requests.post(url=url2, headers=headers, data=data2)
    json2 = reqvs2.json()

    print(json2)
    print(jsons)
    save_path = getSaveFilePath(target)+ACTION_NAME+".html"
    if json2['code'] == 1:
        with open(save_path,'w',encoding="utf-8") as f:
            f.write("Power by "+ACTION_NAME+":<br/>\n")
            result = json2['res']
            for key,value in result.items():
                # print(key+" : "+value)
                f.write(str(key)+" : "+str(value)+"<br/>\n")

    if jsons['code'] == 1:
        with open(save_path,"w+",encoding="utf-8") as f:
            f.write("cms"+jsons['mess']+"\n")
            result = json2['res']
            for key,value in result.items():
                # print(key+" : "+value)
                f.write(str(key)+" : "+str(value)+"<br/>\n")

    opFinishAction(ACTION_NAME)

if __name__ == '__main__':
    url = "http://baidu.com"
    par = ""
    start(url,par)

