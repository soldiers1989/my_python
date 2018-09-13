# -*- coding:utf-8 -*-
import urllib
import urllib2
import pymysql
from bs4 import BeautifulSoup
t="""<script type="text/javascript" reload="1">if(typeof succeedhandle_showMsgBox=='function') {succeedhandle_showMsgBox('home.php?mod=space&do=pm&subop=view&touid=588', '操作成功 ', {'pmid':'155698'});}</script>"""
print t
if  t.find('pmi1d')>=0:
    print 1
else:
    print 2
