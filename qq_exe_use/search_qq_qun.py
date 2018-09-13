# -*- coding:utf8 -*-
from bs4 import BeautifulSoup
import urllib
import pymysql
import time
import requests

def GetBkn(skey):
    hash = 5381
    i=0
    for i in xrange(len(skey)):
        hash+=(hash<<5)+ord(skey[i])
        i+=1
    return hash & 2147483647
def insert_qun_id(cookies,keywords,page):
    url = 'http://qun.qq.com/cgi-bin/group_search/pc_group_search'
    headers={'Host': 'qun.qq.com',
             'Connection': 'keep-alive',

             'Accept': 'application/json, text/javascript, */*; q=0.01',
             'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
             'Origin': 'http://find.qq.com',
             'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) QQ/9.0.4.23786 Chrome/43.0.2357.134 Safari/537.36 QBCore/3.43.915.400 QQBrowser/9.0.2524.400',
             'Referer': 'http://find.qq.com/index.html?version=1&im_version=5581&width=910&height=610&search_target=0',
             'Accept-Encoding': 'gzip, deflate',
             'Accept-Language': 'en-US,en;q=0.8',
             'Cookie': cookies}
    data1 = 'k=%E4%BA%A4%E5%8F%8B&n=8&st=1&iso=1&src=1&v=5581&bkn=1684538292&isRecommend=false&city_id=0&from=1&newSearch=true&keyword=%E7%94%B5%E6%BA%90%E7%94%B5%E5%AD%90&sort=0&wantnum=24&page=0&ldw=428160423'
    data = {}
    list = headers['Cookie'].split('; ')
    dis_qq = {}
    for i in range(0, len(list)):
        dis_qq[list[i].split('=')[0]] = list[i].split('=')[1]
    skey = dis_qq['skey']
    for i in (data1.split('&')):
        j = i.split('=')
        data[j[0]] = j[1].encode('utf8')
    data['keyword'] = keywords
    data['bkn'] = GetBkn(skey)
    data['sort'] = 1
    data['page'] = page
    data['k'] = '交友'
    data = urllib.urlencode(data)
    req = requests.post(url=url, data=data, headers=headers)
    id_all = req.json()
    if id_all['endflag']==1:
        return 'err'
    else:
        if id_all.has_key('errcode'):
            return
        else:
            conn = pymysql.connect(host='127.0.0.1',
                                   port=3306,
                                   user='root',
                                   password='root',
                                   db='company_tel',
                                   charset='utf8',
                                   cursorclass=pymysql.cursors.DictCursor)
            cur = conn.cursor()
            for i in range(0, len(id_all['group_list'])):
                qun_id = id_all['group_list'][i]['code']
                qun_name = id_all['group_list'][i]['name'].encode('utf-8')
                member_num=id_all['group_list'][i]['member_num']
                if member_num>20:
                    sql = 'select id from qun_id_check where id={}'.format(qun_id)
                    cur.execute(sql)
                    res = cur.fetchone()
                    if res is None:
                        try:
                            sql = 'insert into qun_id_check set id={},name=\"{}\",keywords=\"{}\",member_num={}'.format(
                                qun_id, qun_name,
                                keywords, member_num)
                            cur.execute(sql)
                            conn.commit()
                        except:
                            qun_name = '未知'
                            sql = 'insert into qun_id_check set id={},name=\"{}\",keywords=\"{}\",member_num={}'.format(qun_id,
                                                                                                                        qun_name,
                                                                                                                        keywords,member_num)
                            cur.execute(sql)
                            conn.commit()
                    else:
                        pass
                else:
                    pass
    return (page,qun_id,qun_name,member_num)





cookies_all=['gr_user_id=648d5ce2-52eb-4d32-b1fc-4d9a71f37acb; pgv_pvi=9296552960; pgv_pvid=2622093390; RK=NAjxoQ5BaA; ptcz=6e8e5da7bb8b37cda07027f63b790af1541da3da19c0373d9b0a244159f2b38a; LW_sid=h155J2o8F4C8V6O0D7K909H4c6; LW_uid=V1d5Y24814H8I6t0r7l9Y924d7; eas_sid=Y185R22834t856U0s8o0M0X6R2; o_cookie=3287148066; _ga=GA1.2.1380941232.1530818815; pac_uid=1_3287148066; ptui_loginuin=3287148066; pgv_si=s5513222144; _qpsvr_localtk=0.05159056753578195; ptisp=ctc; pgv_info=ssid=s6768566684; pt2gguin=o3287148066; IED_LOG_INFO2=userUin%3D3287148066%26nickName%3D%2525E9%25259D%252592%2525E8%25259B%252599%2525E9%25259D%252592%2525E8%25259B%252599%26userLoginTime%3D1533518459; ADTAG_KEY=EXTERNAL.MEDIA.ANALYSIS_BD09; mtaH5CloseMenuId=#; uin=o3287148066; skey=@nMinbsjG4; p_uin=o3287148066; pt4_token=JpBXIT-UcaM9JZOSi-AFPLHP2Ialo3vwsEg*m6nTVLg_; p_skey=sY9xD9WcqzpGiXcf1mrX6JioXKCpqknWOBCHYXBZJbM_',
             'gr_user_id=648d5ce2-52eb-4d32-b1fc-4d9a71f37acb; pgv_pvi=9296552960; pgv_pvid=2622093390; RK=NAjxoQ5BaA; ptcz=6e8e5da7bb8b37cda07027f63b790af1541da3da19c0373d9b0a244159f2b38a; LW_sid=h155J2o8F4C8V6O0D7K909H4c6; LW_uid=V1d5Y24814H8I6t0r7l9Y924d7; eas_sid=Y185R22834t856U0s8o0M0X6R2; o_cookie=3287148066; _ga=GA1.2.1380941232.1530818815; pac_uid=1_3287148066; ptui_loginuin=3287148066; pgv_si=s5513222144; _qpsvr_localtk=0.05159056753578195; ptisp=ctc; pgv_info=ssid=s6768566684; IED_LOG_INFO2=userUin%3D3287148066%26nickName%3D%2525E9%25259D%252592%2525E8%25259B%252599%2525E9%25259D%252592%2525E8%25259B%252599%26userLoginTime%3D1533518459; ADTAG_KEY=EXTERNAL.MEDIA.ANALYSIS_BD09; mtaH5CloseMenuId=#; pt2gguin=o0452193182; uin=o0452193182; skey=@Pnj1BfwaM; p_uin=o0452193182; pt4_token=*Uh*Qul8sbB1TYfIpyADXInLspSM59EH8ACBNFcd8iI_; p_skey=1MiZmcwzvX5pcYPJbzhwxk2s7c9yH*e8wOw12HzgfzI_',
             'gr_user_id=648d5ce2-52eb-4d32-b1fc-4d9a71f37acb; pgv_pvi=9296552960; pgv_pvid=2622093390; RK=NAjxoQ5BaA; ptcz=6e8e5da7bb8b37cda07027f63b790af1541da3da19c0373d9b0a244159f2b38a; LW_sid=h155J2o8F4C8V6O0D7K909H4c6; LW_uid=V1d5Y24814H8I6t0r7l9Y924d7; eas_sid=Y185R22834t856U0s8o0M0X6R2; o_cookie=3287148066; _ga=GA1.2.1380941232.1530818815; pac_uid=1_3287148066; ptui_loginuin=3287148066; pgv_si=s5513222144; _qpsvr_localtk=0.05159056753578195; ptisp=ctc; pgv_info=ssid=s6768566684; IED_LOG_INFO2=userUin%3D3287148066%26nickName%3D%2525E9%25259D%252592%2525E8%25259B%252599%2525E9%25259D%252592%2525E8%25259B%252599%26userLoginTime%3D1533518459; ADTAG_KEY=EXTERNAL.MEDIA.ANALYSIS_BD09; mtaH5CloseMenuId=#; pt2gguin=o1125354542; uin=o1125354542; skey=@SVnzMIf0C; p_uin=o1125354542; pt4_token=Qowut1qVW-XIQzv6oTUBthGnlNEiHqFIrVKPsenT4ik_; p_skey=7N6*317PPNYVAJyxlleaRvxaobHW2NDd*nyY*4IMugE_']
keywords_all=['mcu',
              'led显示屏幕',
              '技术支持centralfae',
              '电子电路',
              '电子电路图',
              'pcb layout',
              'pcb设计',
              '移动电源',
              '升压电源',
              '降压电源',
              '锂电池保护',
              '锂电池',
              '不间断电源',
              'acdc /dcdc',
              'LED显示屏',
              'LED光源',
              'LED驱动光源',
              'LED驱动芯片',
              'LED芯片',
              'LED驱动电源',
              'LED背光源',
              'LED仪器',
              'LED外延',
              'LED测试',
              '大功率芯片',
              'oled',
              'LED工程设计',
              '恒压驱动电源',
              '恒流驱动电源'
              ]
for keywords in keywords_all:
    for page in range(0, 100):
        cookies=cookies_all[page%3]
        s = (insert_qun_id(cookies, keywords, page))
        if s == 'err':
            break
        else:
            print s
            time.sleep(5)
print ('20秒后关闭')
time.sleep(20)





