# PixivSpider

这是一个python爬虫
定向爬取P站图片


# 依赖：

## python2.7

## fabric
使用pip install fabric进行安装

## scrapy
参照官方文档进行安装
http://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/install.html


# 使用说明：
按照options.ini文件内注释设置
命令行下进入pixiv文件夹，输入fab start运行程序
下载后的图片在Images文件夹下

# 自定义并行数量
进入pixiv/spiders/文件夹下，复制spider1，命名为spider6、spider7等
打开复制后的spider，按照文件内注释修改name属性