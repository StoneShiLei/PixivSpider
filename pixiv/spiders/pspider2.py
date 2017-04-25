# -*- coding: utf-8 -*-
import scrapy
import self_header
import sys
from pixiv.items import PixivItem
reload(sys)
sys.setdefaultencoding('utf-8')

class PspiderSpider(scrapy.Spider):
    name = "pspider2"
    #allowed_domains = ["pspider"]
    start_urls = ['https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index']

    def __init__(self, name=None,*args, **kwargs):
        super(PspiderSpider, self).__init__(*args, **kwargs)

        self.name = self_header.keyword(self.name[-1])
        self.max = int(self_header.pic_max())
        self.user = self_header.user()
        self.pw = self_header.pw()




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
            pageUrl ='http://www.pixiv.net/search.php?word={}&s_mode=s_tag_full&order=date_d&p={}'.format(self.name,str(page))
            yield scrapy.Request(pageUrl,callback=self.get_page)

    def get_page(self,response):
        pixiv = PixivItem()
        imageUrl = response.xpath("//div[@class='_layout-thumbnail']/img/@data-src").extract()
        pixiv['image_urls'] = [url.replace('/c/150x150', '') for url in imageUrl]
        #pixiv['image_urls'] = [url.replace('/c/150x150/img-master', '/img-original').replace('_master1200','') for url in imageUrl]
        pixiv['name'] = self.name
        yield pixiv


