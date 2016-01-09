# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AcademicInfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url=scrapy.Field()
    title=scrapy.Field()
    time=scrapy.Field()
    date_sort=scrapy.Field()
    location=scrapy.Field()
    location_id=scrapy.Field()
    academy=scrapy.Field()
    type=scrapy.Field()
    html_content=scrapy.Field()

