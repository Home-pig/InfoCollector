#!/usr/bin/env python3  
# -*- coding: utf-8 -*-

""" 
@author: Home丿pig 
@contact: home_pig@foxmail.com 
"""
from lib.common import getSaveFilePath
from lib.formatOutput import *
import requests
import urllib3

# remove the warning when the requests arguments verify set as False
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

ACTION_NAME = "whatWeb"

def start(target, arg):
    # set the ACTION NAME
    opStartAction(ACTION_NAME)

    # do action
    url = "https://whatweb.net/whatweb.php"
    data = {'target': target}
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}

    try:
        r = requests.post(url=url, headers=headers, data=data, verify=False)
    except Exception as e:
        opError(e,ACTION_NAME)
        return 0
    print(r.text)

    # save file
    save_path = getSaveFilePath(target) + ACTION_NAME + ".html"
    with open(save_path, "w", encoding="utf-8") as f:
        f.write("Power By " + ACTION_NAME + ":<br/>\n")
        f.write(r.text.replace("],", "],<br/>\n").replace("]，", "],<br/>\n"))

    opFinishAction(ACTION_NAME)


if __name__ == "__main__":
    start("https://www.baidu.com", "dasf")
