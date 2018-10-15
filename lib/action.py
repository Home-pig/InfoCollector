#!/usr/bin/env python3  
# -*- coding: utf-8 -*-

""" 
@author: Home丿pig 
@contact: home_pig@foxmail.com 
"""
import importlib

from lib.common import getProjectPath, getChooserList
from lib.formatOutput import *

ACTION_ROOT_NAME = "action"
CHOOSER_NAME = "chooser"

def startAction(url, ACTION_NAME):
    # start the action
    opStartAction(ACTION_NAME)

    # get the chooser of ture
    path = getProjectPath() + "\\"+ACTION_ROOT_NAME+"\\" + ACTION_NAME + "\\"+CHOOSER_NAME+".json"
    # get the chooser of ture
    allow_action = getChooserList(path)
    # start the action
    for allow in allow_action:
        action_name = allow[0]
        action_args = allow[1]
        module = importlib.import_module("{}.{}.{}.{}".format(ACTION_ROOT_NAME, ACTION_NAME, action_name, action_name))
        module.start(url, action_args)

    opFinishAction(ACTION_NAME)

if __name__ == "__main__":
    pass
