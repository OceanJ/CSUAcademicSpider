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
            html_contents=re.findall(r'<div class="topCont" id="vsb_content.*?">([\W\w]*?)</div>',response.body_as_unicode())[0]
            title=response.xpath('//h3[contains(@class,"newsTitle")]/text()').extract()[0]
            date=re.findall(u"间：([\W\w]+?)\r",contents)[0]
            date_tuple=re.findall(u"(\d+)月(\d+)[日号]",date)[0]
            year=response.xpath('//p[@class="newsTO"]/text()').re(r'(\d+)')[0]
            month=date_tuple[0]
            day=date_tuple[1]
            if(len(month)==1):
                month='0'+month
            if(len(day)==1):
                day='0'+day
            date_sort=year+month+day
            location=re.findall(u"点：(.+)\r",date)[0]
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
                'location_id':0
             })
            yield AcademicInfo
        except Exception,e:
            print e



class WuliSpider(scrapy.Spider):
    name = "Wuli"
    allowed_domains = ["wl.csu.edu.cn"]
    start_urls = (
        'http://wl.csu.edu.cn/Firspage.aspx?strid=a88f17dd-f1ad-4148-90ce-8e22a464197a&id=20',
    )

    def parse(self, response):
        for sel in response.xpath('//div[contains(@id,"divLr")]/table/tr/td/a/@href').extract():
            url='http://wl.csu.edu.cn/'+sel
            yield scrapy.Request(url,callback=self.parse_links_content)


    def parse_links_content(self,response):
        try:
            url=response.url
            contents=response.xpath('string(//div[@id="divLr"])').extract()[0]
            html_contents=response.xpath('//div[@id="divLr"]').extract()[0]
            title=response.xpath('//div[@id="divLr"]/table/tr[1]/td/text()').extract()[0]
            date=re.findall(u"间：([\W\w]+?)\r",contents)[0]
            date_tuple=re.findall(u"(\d+)年(\d+)月(\d+)[日号]",date)[0]
            year=date_tuple[0]
            month=date_tuple[1]
            day=date_tuple[2]
            if(len(month)==1):
                month='0'+month
            if(len(day)==1):
                day='0'+day
            date_sort=year+month+day
            location=re.findall(u"点：(.+)\r",contents)[0]
            type=u"science"
            academy=u"wuli"
            AcademicInfo=AcademicInfoItem({
                'url':url,
                'title':title,
                'time' :date,
                'date_sort':date_sort,
                'location':location,
                'academy':academy,
                'type':type,
                'html_content':html_contents,
                'location_id':''
             })
            yield AcademicInfo
        except Exception,e:
            print e



class JidianSpider(scrapy.Spider):
    name = "Jidian"
    allowed_domains = ["cmee.csu.edu.cn"]
    start_urls = (
        'http://cmee.csu.edu.cn/Content.aspx?moduleid=deba87c1-a197-4047-82bd-f9d7006418d7&id=7',
    )

    def parse(self, response):
        for sel in response.xpath('//a[contains(@class,"green")]/@href').extract():
            url="http://cmee.csu.edu.cn/"+sel
            yield scrapy.Request(url,callback=self.parse_links_content)

    def parse_links_content(self,response):
        try:
            url=response.url
            html_contents=response.xpath('//div[@id="divcontent"]').extract()[0]
            title=re.findall(u"报告题目：</span>(.+?)<br>",html_contents)[0]
            date=re.findall(u"间：\xa0\xa0</span>(.+?)<br>",html_contents)[0]
            date_tuple=re.findall(u"(\d+)年(\d+)月(\d+)[日号]",date)[0]
            year=date_tuple[0]
            month=date_tuple[1]
            day=date_tuple[2]
            if(len(month)==1):
                month='0'+month
            if(len(day)==1):
                day='0'+day
            date_sort=year+month+day
            location=re.findall(u"点：\xa0\xa0</span>(.+)</p>",html_contents)[0]
            type=u"science"
            academy=u"jidian"
            AcademicInfo=AcademicInfoItem({
                'url':url,
                'title':title,
                'time' :date,
                'date_sort':date_sort,
                'location':location,
                'academy':academy,
                'type':type,
                'html_content':html_contents,
                'location_id':''
             })
            yield AcademicInfo
        except Exception,e:
            print e


class GongguanSpider(scrapy.Spider):
    name = "Gongguan"
    allowed_domains = ["csuspa.csu.edu.cn"]
    start_urls = (
        'http://csuspa.csu.edu.cn/catalog/25/index_1.htm',
    )

    def parse(self, response):
        for url in response.xpath("//li/a[contains(@target,'_blank')]/@href").extract():
            yield scrapy.Request(url,callback=self.parse_links_content)

    def parse_links_content(self,response):
        try:
            url=response.url
            contents=response.xpath("string(//table[contains(@align,'center')])").extract()[0]
            html_contents=response.xpath("//table[contains(@align,'center')]").extract()[0]
            title=response.xpath("//div[contains(@class,'show_title STYLE20 STYLE31')]/strong/text()").extract()[0]
            date=re.findall(u"间：([\W\w]+?)[地\r]",contents)[0]
            date_tuple=re.findall(u"(\d+)年(\d+)月(\d+)[日号]",date)[0]
            year=date_tuple[0]
            month=date_tuple[1]
            day=date_tuple[2]
            if(len(month)==1):
                month='0'+month
            if(len(day)==1):
                day='0'+day
            date_sort=year+month+day
            location=re.findall(u"点：(.+)[内\r]",contents)[0]
            type=u"science"
            academy=u"gongguan"
            AcademicInfo=AcademicInfoItem({
                'url':url,
                'title':title,
                'time' :date,
                'date_sort':date_sort,
                'location':location,
                'academy':academy,
                'type':type,
                'html_content':html_contents,
                'location_id':''
             })
            yield AcademicInfo
        except Exception,e:
            print e


class ShutongSpider(scrapy.Spider):
    name = "Shutong"
    allowed_domains = ["math.csu.edu.cn"]
    start_urls = (
        'http://math.csu.edu.cn/lb.jsp?urltype=tree.TreeTempUrl&wbtreeid=1217',
    )

    def parse(self, response):
        for sel in response.xpath("//a[contains(@target,'_blank')]/@href").extract():
            url="http://math.csu.edu.cn/"+sel
            yield scrapy.Request(url,callback=self.parse_links_content)

    def parse_links_content(self,response):
        try:
            url=response.url
            contents=response.xpath("string(//div[contains(@id,'vsb_content_4')])").extract()[0]
            html_contents=response.xpath("//div[contains(@id,'vsb_content_4')]").extract()[0]
            title=re.findall(u"目[:：]([\W\w]+?)\r",contents)[0]
            date=re.findall(u"间：([\W\w]+?)\r",contents)[0]
            date_tuple=re.findall(u"(\d+)年(.+)月(\d+)[日号]",date)[0]
            year=date_tuple[0]
            month=date_tuple[1]
            day=date_tuple[2]
            if(month==u"元"):
                month='1'
            if(len(month)==1):
                month='0'+month
            if(len(day)==1):
                day='0'+day
            date_sort=year+month+day
            location=re.findall(u"点：(.+)\r",contents)[0]
            type=u"science"
            academy=u"shuxue"
            AcademicInfo=AcademicInfoItem({
                'url':url,
                'title':title,
                'time' :date,
                'date_sort':date_sort,
                'location':location,
                'academy':academy,
                'type':type,
                'html_content':html_contents,
                'location_id':''
             })
            yield AcademicInfo
        except Exception,e:
            print e


class TumuSpider(scrapy.Spider):
    name = "Tumu"
    allowed_domains = ["civil.csu.edu.cn"]
    start_urls = (
        'http://civil.csu.edu.cn/Content.aspx?moduleid=0104&id=8',
    )

    def parse(self, response):
        for sel in response.xpath('//a[contains(@class,"green")]/@href').extract():
            url="http://civil.csu.edu.cn/"+sel
            yield scrapy.Request(url,callback=self.parse_links_content)

    def parse_links_content(self,response):
        try:
            url=response.url
            html_contents=response.xpath('//div[@id="divcontent"]').extract()[0]
            title=re.findall(u"报告题目：</span>(.+?)<br>",html_contents)[0]
            date=re.findall(u"间：\xa0\xa0</span>(.+?)<br>",html_contents)[0]
            date_tuple=re.findall(u"(\d+)年(\d+)月(\d+)[日号]",date)[0]
            year=date_tuple[0]
            month=date_tuple[1]
            day=date_tuple[2]
            if(len(month)==1):
                month='0'+month
            if(len(day)==1):
                day='0'+day
            date_sort=year+month+day
            location=re.findall(u"点：\xa0\xa0</span>(.+)</p>",html_contents)[0]
            type=u"science"
            academy=u"tumu"
            AcademicInfo=AcademicInfoItem({
                'url':url,
                'title':title,
                'time' :date,
                'date_sort':date_sort,
                'location':location,
                'academy':academy,
                'type':type,
                'html_content':html_contents,
                'location_id':''
             })
            yield AcademicInfo
        except Exception,e:
            print e

class YejinSpider(scrapy.Spider):
    name = "Yejin"
    allowed_domains = ["smse.csu.edu.cn"]
    start_urls = (
        'http://smse.csu.edu.cn/Firspage.aspx?strId=8d553b06-83bd-4273-9942-477ab75616c9&id=0',
    )

    def parse(self, response):
        for sel in response.xpath('//div[contains(@id,"divLr")]/table/tr/td/a/@href').extract():
            url='http://smse.csu.edu.cn/'+sel
            yield scrapy.Request(url,callback=self.parse_links_content)


    def parse_links_content(self,response):
        try:
            url=response.url
            contents=response.xpath('string(//div[@id="divLr"])').extract()[0]
            html_contents=response.xpath('//div[@id="divLr"]').extract()[0]
            title=response.xpath('//div[@id="divLr"]/table/tr[1]/td/text()').extract()[0]
            date=re.findall(u"[间期]：([\W\w]+?)\r",contents)[0]
            date_tuple=re.findall(u"(\d+)月(\d+)[日号]",date)[0]
            year=re.findall(u"(\d+)-\d+-\d+\xa0",html_contents)[0]
            month=date_tuple[0]
            day=date_tuple[1]
            if(len(month)==1):
                month='0'+month
            if(len(day)==1):
                day='0'+day
            date_sort=year+month+day
            location=re.findall(u"点：(.+)\r",contents)[0]
            type=u"science"
            academy=u"yejin"
            AcademicInfo=AcademicInfoItem({
                'url':url,
                'title':title,
                'time' :date,
                'date_sort':date_sort,
                'location':location,
                'academy':academy,
                'type':type,
                'html_content':html_contents,
                'location_id':''
             })
            yield AcademicInfo
        except Exception,e:
            print e

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

