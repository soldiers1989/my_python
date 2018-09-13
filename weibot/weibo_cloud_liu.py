# -*- coding:utf8 -*-
import jieba.analyse
import re
from collections import Counter
from pytagcloud.colors import COLOR_SCHEMES
from pytagcloud.lang.counter import get_tag_counts
from pytagcloud import create_tag_image, create_html_data, make_tags, \
    LAYOUT_HORIZONTAL, LAYOUTS
import pymysql

conn = pymysql.connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       password='root',
                       db='yunfae',
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()
sql='select * from liu'
cur.execute(sql)
res=cur.fetchall()

fl=str(res)
tags = jieba.analyse.extract_tags(str(fl), topK=400, withWeight=True)
wd={}
for tag in tags:
    if tag[0]=='text':
        pass
    else:
        if tag[0] in ['微博','u200b','转发','...','quot']:
            pass
        else:
            wd[tag[0]] = int(tag[1]*10000)
counts = Counter(wd).items()
print(counts)
def action(counts):
    tags = make_tags(counts,minsize = 15, maxsize = 120)
    create_tag_image(tags, 'weibo_liu.png', background=(0, 0, 0, 0),
                 size=(1200, 1200),
                 fontname="simhei")

action(counts)