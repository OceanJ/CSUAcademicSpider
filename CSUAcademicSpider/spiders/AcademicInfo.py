# -*- coding: utf-8 -*-
import re
import scrapy
from CSUAcademicSpider.items import AcademicInfoItem

class XinxiSpider(scrapy.Spider):
    name = "Xinxi"
    allowed_domains=["sise.csu.edu.cn"]
    start_urls=["http://sise.csu.edu.cn/index/xsbg.htm"]
    def parse(self,response):
        for sel in response.xpath('//ul[contains(@class,"eduList")]/li'):
            url_re_words = re.compile(u"info(.+)")
            _urls=sel.xpath('a/@href').extract()[0]
            sub_url=url_re_words.search(_urls,0).group(1)
            news_urls='http://sise.csu.edu.cn/info'+sub_url
            yield scrapy.Request(news_urls,callback=self.parse_links_content)

    def parse_links_content(self,response):
        try:
            url=response.url
            contents=response.xpath('string(//div[@class="topCont"])').extract()[0]
            html_contents=re.findall(r'<div class="topCont" id="vsb_content_2">([\W\w]*?)</div>',response.body_as_unicode())[0]
            title=response.xpath('//h3[contains(@class,"newsTitle")]/text()').extract()[0]
            date=re.findall(u"间：(.+)\r",contents)[0]
            date_tuple=re.findall(u"(\d+)月(\d+)[日号]",date)[0]
            year=response.xpath('//p[@class="newsTO"]/text()').re(r'(\d+)')[0]
            month=date_tuple[0]
            day=date_tuple[1]
            if(len(month)==1):
                month='0'+month
            if(len(day)==1):
                day='0'+day
            date_sort=year+month+day
            location_re_words = re.compile(u"点：(.+)\r")
            location=location_re_words.search(contents, 0).group(1)
            type=u"science"
            academy=u"xinxi"
            AcademicInfo=AcademicInfoItem({
                'url':url,
                'title':title,
                'time' :date,
                'date_sort':date_sort,
                'location':location,
                'academy':academy,
                'type':type,
                'html_content':html_contents,
             })
            yield AcademicInfo
        except Exception,e:
            pass
            #print e



class WuliSpider(scrapy.Spider):
    name = "Wuli"
    allowed_domains = ["http://sise.csu.edu.cn/index/xsbg.htm"]
    start_urls = (
        'http://www.http://sise.csu.edu.cn/index/xsbg.htm/',
    )

    def parse(self, response):
        pass


class JidianSpider(scrapy.Spider):
    name = "Jidian"
    allowed_domains = ["http://sise.csu.edu.cn/index/xsbg.htm"]
    start_urls = (
        'http://www.http://sise.csu.edu.cn/index/xsbg.htm/',
    )

    def parse(self, response):
        pass


class GongguanSpider(scrapy.Spider):
    name = "Gongguan"
    allowed_domains = ["http://sise.csu.edu.cn/index/xsbg.htm"]
    start_urls = (
        'http://www.http://sise.csu.edu.cn/index/xsbg.htm/',
    )

    def parse(self, response):
        pass

class ShutongSpider(scrapy.Spider):
    name = "Shutong"
    allowed_domains = ["http://sise.csu.edu.cn/index/xsbg.htm"]
    start_urls = (
        'http://www.http://sise.csu.edu.cn/index/xsbg.htm/',
    )

    def parse(self, response):
        pass

class FenyeSpider(scrapy.Spider):
    name = "Fenye"
    allowed_domains = ["http://sise.csu.edu.cn/index/xsbg.htm"]
    start_urls = (
        'http://www.http://sise.csu.edu.cn/index/xsbg.htm/',
    )

    def parse(self, response):
        pass

class TumuSpider(scrapy.Spider):
    name = "Tumu"
    allowed_domains = ["http://sise.csu.edu.cn/index/xsbg.htm"]
    start_urls = (
        'http://www.http://sise.csu.edu.cn/index/xsbg.htm/',
    )

    def parse(self, response):
        pass

class YejinSpider(scrapy.Spider):
    name = "Yejin"
    allowed_domains = ["http://sise.csu.edu.cn/index/xsbg.htm"]
    start_urls = (
        'http://www.http://sise.csu.edu.cn/index/xsbg.htm/',
    )

    def parse(self, response):
        pass

class GongweiSpider(scrapy.Spider):
    name = "Gongwei"
    allowed_domains = ["http://sise.csu.edu.cn/index/xsbg.htm"]
    start_urls = (
        'http://www.http://sise.csu.edu.cn/index/xsbg.htm/',
    )

    def parse(self, response):
        pass

class YaoSpider(scrapy.Spider):
    name = "Yao"
    allowed_domains = ["http://sise.csu.edu.cn/index/xsbg.htm"]
    start_urls = (
        'http://www.http://sise.csu.edu.cn/index/xsbg.htm/',
    )

    def parse(self, response):
        pass

