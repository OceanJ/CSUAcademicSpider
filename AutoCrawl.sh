#!/bin/sh
rm -rf /var/www/html/csuinfo/*
rm -rf output_xml/*

scrapy crawl Xinxi -o output_xml/xinxi.xml
scrapy crawl Wuli -o output_xml/wuli.xml
scrapy crawl Jidian -o output_xml/jidian.xml
scrapy crawl Gongguan -o output_xml/gongguan.xml
scrapy crawl Shutong -o output_xml/shutong.xml
scrapy crawl Tumu -o output_xml/tumu.xml
scrapy crawl Yejin -o output_xml/yejin.xml
scrapy crawl Gongwei -o output_xml/gongwei.xml

cp output_xml/* /var/www/html/csuinfo/

