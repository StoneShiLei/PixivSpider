# PixivSpider

这是一个定向爬取P站图片的python爬虫


# 依赖：

## python2.7

## fabric
使用pip install fabric进行安装

## scrapy
参照官方文档进行安装，http://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/install.html


# 使用说明：
按照options.ini文件内注释设置后，命令行下进入pixiv文件夹，输入fab start运行程序，下载后的图片在Images文件夹下

# 并行下载
在options.ini文件内的name标签下，以制表符\t (TAB)来分割多个人物名称即可同时多人物下载图片，***由于一个人物为一个进程，请视电脑配置量力而行***
