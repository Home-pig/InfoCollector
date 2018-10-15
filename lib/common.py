#!/usr/bin/env python3  
# -*- coding: utf-8 -*-

""" 
@author: Home丿pig 
@contact: home_pig@foxmail.com 
"""

import json
import subprocess

import os
from urllib.parse import urlparse


def getChooserList(path):
    '''
    :return:the chooser.json file info where is sign of true
    '''
    result = []
    with open(path, encoding="utf-8") as data:
        json_content = json.load(data)
    for i in json_content:
        if json_content[i]['action'].upper() == "TRUE":
            del json_content[i]['action']
            result.append((i,json_content[i]))
    return result

def getProjectPath():
    project_name = "InfoCollector"
    path = os.getcwd()[:os.getcwd().index(project_name) + len(project_name)]
    return path

def downloadGitInit(url, project_name):
    path = getProjectPath() + "\depend\\" + project_name
    if not os.path.exists(path):
        downloadDependFileByGit(url)

def downloadDependFileByGit(url):
    ppath = os.getcwd()
    path = getProjectPath() + "\depend"
    os.chdir(path)
    subprocess.call(["git", "clone", url])
    os.chdir(ppath)


def execPythonCode(project_name, order):
    '''
    warning:delect python in python3 file
    :param file_name: the project name in depend
    :param order: need to be execed
    :return:
    '''
    ppath = os.getcwd()
    path = getProjectPath() + "\depend\\" + project_name
    print(path)
    print(os.environ['Path'])
    os.chdir(path)
    subprocess.call(order)
    os.chdir(ppath)


def getUrlDomain(url):
    url_domain = urlparse(url)[1]
    if ":" in url_domain:
        url_domain = url_domain[:url_domain.index(":")]
    url_domain = url_domain[url_domain.index(".") + 1:]
    # print(url_domain)
    return url_domain

def getSaveFilePath(url):
    domain = getUrlDomain(url).replace(".","")
    path = getProjectPath()+"\output\\"+domain+"\\"
    if not os.path.exists(path):
        os.mkdir(path)
    return path

def addEndingLineFeedOfFile(path):
    content = []
    with open(path,"r",encoding="utf-8") as f:
        content = f.readlines()
    with open(path,"w",encoding="utf-8") as g_w:
        for c in content:
            g_w.write(c+"<br/>")

if __name__ == "__main__":
    path = "H:\pycharm_project\InfoCollector\output\\bnuzeducn\subDomainsBrute.html"
    addEndingLineFeedOfFile(path)