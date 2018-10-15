#!/usr/bin/env python3  
# -*- coding: utf-8 -*-

""" 
@author: Home丿pig 
@contact: home_pig@foxmail.com 
"""
import ctypes
import sys

FOREGROUND_BLUE = 0x09  # blue.
FOREGROUND_GREEN = 0x0a  # green.
FOREGROUND_RED = 0x0c  # red.
STD_OUTPUT_HANDLE = -11

# get handle
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)


def set_cmd_text_color(color, handle=std_out_handle):
    Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return Bool


# reset white
def resetColor():
    set_cmd_text_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)


# green
def printNormal(mess):
    set_cmd_text_color(FOREGROUND_GREEN)
    sys.stdout.write(mess)
    resetColor()


# red
def printWarning(mess):
    set_cmd_text_color(FOREGROUND_RED)
    sys.stdout.write(mess)
    resetColor()


def opStartAction(ACTION_NAME):
    mess = "[+] Starting action of: %s\n" % ACTION_NAME
    printNormal(mess)


def opFinishAction(ACTION_NAME):
    mess = "[+] Finish %s\n" % ACTION_NAME
    printNormal(mess)


def opError(e, ACTION_NAME):
    mess = "[-] %s Error\n" % ACTION_NAME
    printWarning(e)
    printWarning(mess)


def opStartExecOrder(order):
    mess = "[+] ready to exec order:%s\n" % order
    printNormal(mess)

def opStartInfoCollector(target):
    mess = "[+] start %s\n"%target
    printWarning(mess)


if __name__ == "__main__":
    pass
