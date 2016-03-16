#!/bin/sh
#rm -rf /var/www/html/csuinfo/*
cd ~/workspace/CSUAcademicSpider/
rm -rf output/*

scrapy crawl Xinxi
scrapy crawl Wuli
scrapy crawl Jidian
scrapy crawl Gongguan
scrapy crawl Shutong
scrapy crawl Tumu -o
scrapy crawl Yejin -o
scrapy crawl Gongwei -o

#cp output_xml/* /var/www/html/csuinfo/
