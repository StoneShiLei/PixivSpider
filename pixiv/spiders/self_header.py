# -*- coding:utf-8 -*-
import ConfigParser
import os
from time import time,localtime,strftime
import codecs

def getConfig(section, key):
    config = ConfigParser.ConfigParser()
    path = os.path.abspath('options.ini')
    config.readfp(codecs.open(path, "r", "utf-8-sig"))
    return config.get(section, key)




def keyword():
    keyword = getConfig("keyword", "name")
    return keyword.split('\t')

def pic_max():
    pmax = getConfig("pic","max")
    return pmax

def user():
    username = getConfig("acc","username")
    return username

def pw():
    password = getConfig("acc","password")
    return password

def smode():
    smode = getConfig("mode","smode")
    if smode == "f":
        return "s_mode=s_tag_full"
    elif smode == "n":
        return "s_mode=s_tag"
    else:
        raise ValueError

def r18():
    r18 = getConfig("mode","r18")
    if r18 == "y":
        return "&r18=1"
    elif r18 == "n":
        return ""
    else:
        raise ValueError

def multiple():
    multiple = getConfig("pic","multiple")
    return multiple