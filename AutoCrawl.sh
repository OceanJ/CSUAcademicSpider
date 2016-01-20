#!/bin/sh
#rm -rf /var/www/html/csuinfo/*
rm -rf output/*

scrapy crawl Xinxi -o output/xinxi.json
scrapy crawl Wuli -o output/wuli.json
scrapy crawl Jidian -o output/jidian.json
scrapy crawl Gongguan -o output/gongguan.json
scrapy crawl Shutong -o output/shutong.json
scrapy crawl Tumu -o output/tumu.json
scrapy crawl Yejin -o output/yejin.json
scrapy crawl Gongwei -o output/gongwei.json

#cp output_xml/* /var/www/html/csuinfo/
