PixivSpider
===
这是一个定向爬取P站图片的python爬虫

依赖：
---
python2.7  

fabric  

scrapy  

Pillow  

pypiwin32  



安装依赖：
---
1. 安装Python2.7 
 
根据操作系统选择32/64位python2.7.msi文件进行安装，注意勾选Add python.exe to Path以自动加入环境变量，python3用户请在安装python2.7后自行更改环境变量


2. 安装pip 
 
命令行进入get-pip.py文件所在目录(requirements)，在命令行输入python get-pip.py


3. Windows用户需要安装VC++9.0 
 
下载地址：http://www.microsoft.com/en-us/download/details.aspx?id=44266


4. 安装依赖  

在同上目录下(requirements)，于命令行输入pip install -r requirements.txt



定制搜索模式:
---

     [keyword]
     name = 角色1	角色2	角色3	……	角色12450
     ;角色名，多个角色名使用制表符TAB（\t）分割开，建议使用角色日文原名进行搜索

     [pic]
     max = 20
     ;图集模式关闭为图片数量，开启则为图集数量，数值越大图片越多
     multiple = n
     ;y/n 图集模式，是否下载图集内其他图片，关闭则只下载图集封面页，此功能会降低运行速度

     [acc]
     username = youracc@hulu.com
     password = yourpassword
     ;P站账号密码

     [mode]
     **--数据删除--** = n
     ;y/n 是否开启**--数据删除--**搜索

     smode = n
     ;f/n 完全一致/部分一致搜索

     [star]
     star = 0
     ;只搜索star数量高于值的图片
---


使用方法  
---
在options.ini文件内设置好想要的搜索模式以及搜索关键字后，使用cmd、powershell等命令行工具进入fabfile.py文件所在目录，输入fab start，回车


注意事项  
---
请使用文本编辑器或IDE软件打开options.ini,以防选项输入错误，多角色搜索以及图集搜索会对电脑配置造成一定压力，使用**--数据删除--**模式搜索时，必须确认P站账号密码输入正确，否则无法正常运行
