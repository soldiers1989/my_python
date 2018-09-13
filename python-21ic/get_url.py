#coding:utf-8
import requests
from bs4 import BeautifulSoup

url='http://www.dianyuan.com/bbs/1529387.html'
res=requests.get(url).text
soup=BeautifulSoup(res,'html.parser')
user_name=soup.select('#username')
act_time=soup.select(' td > div > span.update.f10')
user_id=soup.select('div.content.gz > a.mess')

for i in range(0,len(user_name)):
    print user_name[i].text.strip(),'   ',act_time[i].text.strip(),'    ',user_id[i].attrs['id'].split('-')[1]
