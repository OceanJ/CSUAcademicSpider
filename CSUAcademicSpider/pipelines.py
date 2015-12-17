# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb

db=MySQLdb.connect("localhost","spider","xyz","csuspider")
cursor = db.cursor()
db.set_character_set('utf8')
cursor.execute('SET NAMES utf8;')
cursor.execute('SET CHARACTER SET utf8;')
cursor.execute('SET character_set_connection=utf8;')
insert_sql = "insert into academic(url,title,time,date_sort,location,academy,type,html_content) values ('%s','%s','%s','%s','%s','%s','%s','%s')"

class CsuacademicspiderPipeline(object):
    def process_item(self, item, spider):
        item['html_content']=item['html_content'].replace(u'&', u'&amp;')
        item['html_content']=item['html_content'].replace(u'<',u'&lt;')
        item['html_content']=item['html_content'].replace(u'>',u'&gt;')
        item['html_content']=item['html_content'].replace(u"'",u'&apos;')
        item['html_content']=item['html_content'].replace(u'"',u'&quot;')
        sql=insert_sql%(item['url'].encode('utf-8'),item['title'].encode('utf-8'),item['time'].encode('utf-8'),item['date_sort'].encode('utf-8'),\
                        item['location'].encode('utf-8'),item['academy'].encode('utf-8'),item['type'].encode('utf-8'),item['html_content'].encode('utf-8'))
        try:
            cursor.execute(sql)
            db.commit()
        except Exception,e:
            print e

        return item
