#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Home丿pig
@contact: home_pig@foxmail.com
"""
from lib.common import *

ACTION_NAME = "Set Action Name Here"


def start(url, args):
    # start the action
    print("Starting action of " + ACTION_NAME)

    git_url = "Set the git project here"
    # do action
    # install judge insatll or not
    downloadGitInit(git_url, ACTION_NAME)
    domain = getUrlDomain(url)
    save_path = getSaveFilePath(url) + ACTION_NAME + ".html"
    order = ["python", ACTION_NAME+".py", domain, "-o", save_path]
    if args.get("args") != None:
        for key, value in args['args'].items():
            order.append(key)
            order.append(value)
    print(order)
    execPythonCode(ACTION_NAME, order)
    # format file
    addEndingLineFeedOfFile(save_path)

    print("Finish " + ACTION_NAME)


if __name__ == "__main__":
    pass
