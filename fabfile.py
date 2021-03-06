# -*- coding:utf-8 -*-
from fabric.api import local
from pixiv.spiders import self_header
import os
import urllib
def start():
    name = self_header.keyword()
    for kw in name:
        if os.name == 'nt':
            local('start scrapy crawl pspider -a name={}'.format(urllib.quote(kw.encode('UTF8'))))
        else:
            local('scrapy crawl pspider -a name={} >out.file 2>&1 &'.format(urllib.quote(kw).encode('UTF8')))