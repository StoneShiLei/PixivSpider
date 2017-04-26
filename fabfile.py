# -*- coding:utf-8 -*-
from fabric.api import local
from pixiv.spiders import self_header
import os
def start():
    name = self_header.keyword()
    for kw in name:
        if os.name == 'nt':
            local('start scrapy crawl pspider -a name={}'.format(kw.encode('GBK')))
        else:
            local('start scrapy crawl pspider -a name={}'.format(kw))
