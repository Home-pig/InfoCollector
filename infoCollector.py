#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
@author: Home丿pig
@contact: home_pig@foxmail.com
@Date: 2018-10-13
@Version: 1.0
"""
import importlib
import time

from lib.common import *
from lib.formatOutput import *
from lib.cmdline import parse_args

ACTION_PATH = "action/"
ACTION_NAME = "infoCollector"


def getActionList():
    '''
    :return: the action list
    '''
    chooser_path = getProjectPath() + "/chooser.json"
    return getChooserList(chooser_path)


def sumTheResult(url):
    path = getSaveFilePath(url)
    save_path = path + "\Result.html"
    file_list = next(os.walk(path))[2]
    if len(file_list):
        # open final result file
        with open(save_path, "w+", encoding="utf-8") as f:
            show_time = time.asctime(time.localtime(time.time()))
            f.write("<p>" + show_time + "</p>")
            for file_name in file_list:
                file_path = path + file_name
                # open each result file
                with open(file_path, "r", encoding="utf-8") as g:
                    f.write(g.read())


def main():
    options,args = parse_args()
    # start
    opStartAction(ACTION_NAME)

    # get action list
    action_list = getActionList()

    # get target url
    url = args[0]
    opStartInfoCollector(url)

    # for each action chooser
    for action in action_list:
        action = action[0]
        module = importlib.import_module("action.{}.{}".format(action, action))
        module.start(url)

    # get all result to one page
    sumTheResult(url)

    opFinishAction(ACTION_NAME)


if __name__ == "__main__":
    main()
    # url = "http://www.bnuzxun.cn"
    # sumTheResult(url)
