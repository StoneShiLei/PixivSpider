# -*- coding:utf-8 -*-
from fabric.api import local

def start():
    #启动第1-5个爬虫 range(1,6)
    for x in range(1,6):
        local('start scrapy crawl pspider' + str(x))