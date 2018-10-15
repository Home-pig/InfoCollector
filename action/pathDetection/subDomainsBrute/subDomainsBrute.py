#!/usr/bin/env python3  
# -*- coding: utf-8 -*-

"""
@author: Home丿pig
@contact: home_pig@foxmail.com
"""
from lib.common import *
from lib.formatOutput import *

ACTION_NAME = "subDomainsBrute"


def start(url, args):
    # start the action
    opStartAction(ACTION_NAME)

    git_url = "https://github.com/lijiejie/subDomainsBrute.git"
    # do action
    # install judge insatll or not
    try:
        downloadGitInit(git_url, ACTION_NAME)
    except Exception as e:
        opError(e,ACTION_NAME)

    domain = getUrlDomain(url)
    save_path = getSaveFilePath(url) + ACTION_NAME + ".html"
    order = ["python", ACTION_NAME+".py", domain, "-o", save_path]
    if args.get("args") != None:
        for key, value in args['args'].items():
            order.append(key)
            order.append(value)

    execPythonCode(ACTION_NAME, order)

    # format file
    addEndingLineFeedOfFile(save_path)

    opFinishAction(ACTION_NAME)

if __name__ == "__main__":
    url = "https://www.baidu.com"
    args = {"-o": "a.txt", "-t": "5"}
    start(url, args)
