import requests
from bs4 import BeautifulSoup

def get_ip():
    proxy_url='https://www.kuaidaili.com/free/inha/1/'
    req=requests.get(proxy_url).text
    soup=BeautifulSoup(req,'html.parser')
    ip_list=[]
    ip={}
    len_ip=len(soup.select('#list > table > tbody > tr'))
    for i in range(1,len_ip+1):
        ip1=soup.select('#list > table > tbody > tr:nth-of-type({}) > td:nth-of-type(1)'.format(i))[0].text
        kou=soup.select('#list > table > tbody > tr:nth-of-type({}) > td:nth-of-type(2)'.format(i))[0].text
        ip['http']=str(ip1)+':'+str(kou)
        ip_list.append(ip)
    return ip_list


url='http://bbs.21dianyuan.com/forum.php?fromuid=393666'
prolist=get_ip()
for i in prolist:
    proxy=i
    try:
        re = requests.get(url,proxies=proxy).text
        print re
    except:
        print 'err'