# -*- coding:utf8 -*-
import threading
import itchat
import re
import random
import jieba.analyse
from collections import Counter
from pytagcloud.colors import COLOR_SCHEMES
from pytagcloud.lang.counter import get_tag_counts
from pytagcloud import create_tag_image, create_html_data, make_tags, \
    LAYOUT_HORIZONTAL, LAYOUTS
from operator import itemgetter
itchat.auto_login(hotReload=True)


friends_list=itchat.get_friends()
print(friends_list)
#print(friends_list)
fl=[]
# 去除内容中的非法字符 (Windows)
def validatecontent(content):
    # '/\:*?"<>|'
    re1=r"<span\sclass=[^\s]*\s[^\s]*"
    re4=r'class'
    re3 = r'emoji'
    re6 = r'span'
    re7 = r'1f446'
    re5 = r'[1-9][0-9]{5,}'
    new_content = re.sub(re1, "", content)
    new_content = re.sub(re3, "", new_content)
    new_content = re.sub(re4, "", new_content)
    new_content = re.sub(re5, "", new_content)
    new_content = re.sub(re6, "", new_content)
    new_content = re.sub(re7, "", new_content)
    return new_content

for i in friends_list:
    if i['Signature']=='':
        pass
    else:
        Signature=i['Signature']
        fl.append(validatecontent(Signature))
wd={}
tags = jieba.analyse.extract_tags(str(fl), topK=200, withWeight=True)

for tag in tags:
        wd[tag[0]] = int(tag[1]*10000)

from collections import Counter
counts = Counter(wd).items()
print(fl)
print(counts)

def action(counts):
    tags = make_tags(counts,minsize = 5, maxsize = 120)
    create_tag_image(tags, 'wanglu.png', background=(0, 0, 0, 0),
                 size=(1200, 1500),
                 fontname="simhei")

action(counts)