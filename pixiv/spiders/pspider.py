# -*- coding: utf-8 -*-
import scrapy
import self_header
import sys
from pixiv.items import PixivItem
import urllib
import os
import re
reload(sys)
sys.setdefaultencoding('utf-8')

class PspiderSpider(scrapy.Spider):
    name = "pspider"
    #allowed_domains = ["pspider"]
    start_urls = ['https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index']

    def __init__(self, name=None,*args, **kwargs):
        super(PspiderSpider, self).__init__(*args, **kwargs)
        if os.name == "nt":
            self.name = name.decode("GBK").encode("UTF8")
        else:
            self.name = name
        self.max = int(self_header.pic_max())
        self.user = self_header.user()
        self.pw = self_header.pw()
        self.multiple = self_header.multiple()




    def start_requests(self):
        return [scrapy.Request(self.start_urls[0],callback=self.login)]

    def login(self,response):
        post_key = response.xpath("//input[@name='post_key']/@value").extract()[0]
        post_data = {
            'pixiv_id':self.user,
            'password':self.pw,
            'captcha':'',
            'g_recaptcha_response':'',
            'post_key':post_key,
            'source':'pc',
            'ref':'wwwtop_accounts_index',
            'return_to':'http://www.pixiv.net/'
        }
        return [scrapy.FormRequest('https://accounts.pixiv.net/api/login?lang=zh', formdata=post_data, callback=self.imgorder)]

    def imgorder(self,response):
        pages = range(1,self.max/20+1)
        for page in pages:
            pageUrl ='http://www.pixiv.net/search.php?word={}&{}&order=date_d{}&p={}'.format(urllib.quote(self.name),self_header.smode(),self_header.r18(),str(page))
            yield scrapy.Request(pageUrl,callback=self.get_page)

    def get_page(self,response):
        pixiv = PixivItem()
        if os.name == 'nt':
            pixiv['name'] = self.name.decode('UTF8').encode('GBK')
        else:
            pixiv['name'] = self.name

        if self.multiple == 'y':
            multiple = response.xpath("//a[@class='work  _work manga multiple ']/@href").extract() + response.xpath("//a[@class='work  _work multiple ']/@href").extract()
            work = response.xpath("//a[@class='work  _work ']/@href").extract()
            for wurl in work:
                wid = re.search(r"(?<=id=).+?(?=$)",wurl,re.M).group(0)
                img_master__url = 'https://www.pixiv.net/member_illust.php?mode=medium&illust_id={}'.format(wid)
                yield scrapy.Request(img_master__url,meta={'pixiv':pixiv},callback=self.get_img)

            for murl in multiple:
                mid = re.search(r"(?<=id=).+?(?=$)",murl,re.M).group(0)
                img_master__url = 'https://www.pixiv.net/member_illust.php?mode=manga&illust_id={}'.format(mid)
                yield scrapy.Request(img_master__url,meta={'pixiv':pixiv},callback=self.get_img)

        elif self.multiple == 'n':
            imageUrls150 = response.xpath("//div[@class='_layout-thumbnail']/img/@data-src").extract()
            pixiv['image_urls'] = [url.replace('/c/150x150', '') for url in imageUrls150]
            yield pixiv


    def get_img(self,response):
        pixiv = response.meta['pixiv']
        imageUrls = response.xpath("//img[@class='image ui-scroll-view']/@data-src").extract() + response.xpath("//img[@class='original-image']/@data-src").extract()
        pixiv['image_urls'] = [imageUrl for imageUrl in imageUrls]
        yield pixiv
