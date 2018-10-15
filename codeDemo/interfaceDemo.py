#!/usr/bin/env python3  
# -*- coding: utf-8 -*-

""" 
@author: Home丿pig 
@contact: home_pig@foxmail.com 
"""
from lib.common import getSaveFilePath
from lib.formatOutput import *

ACTION_NAME = ""


def start(target, arg):
    # start the actionc
    opStartAction(ACTION_NAME)

    # do action

    # save file
    save_path = getSaveFilePath(target) + ACTION_NAME.upper() + ".html"
    with open(save_path, "w", encoding="utf-8") as f:
        f.write("Power By " + ACTION_NAME + ":" + "<br/>\n")
        # write the result here

    opFinishAction(ACTION_NAME)

if __name__ == "__main__":
    pass
