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




def keyword(n):
    keyword = getConfig("keyword", "name"+n)
    return keyword

def pic_max():
    pmax = getConfig("pic","max")
    return pmax

def user():
    username = getConfig("acc","username")
    return username

def pw():
    password = getConfig("acc","password")
    return password