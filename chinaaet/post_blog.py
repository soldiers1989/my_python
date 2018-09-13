# -*- coding:utf-8 -*-
import urllib
import urllib2
import pymysql
from bs4 import BeautifulSoup
import time

def get_new_name():
    conn = pymysql.connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           password='root',
                           db='company_tel',
                           charset='utf8',
                           cursorclass=pymysql.cursors.DictCursor)
    cur = conn.cursor()
    sql='SELECT DISTINCT link_name from chinaaet where have_send=0'
    cur.execute(sql)
    re=cur.fetchall()
    res=[]
    for i in re:
        res.append(i['link_name'])
    return (res)
#从列表中取出所有没用用过的用户id

def get_single_page(x):
    sql="""select link_title from chinaaet where link_name=\"{}\" and have_send=0 limit 1""".format(x.encode('UTF8'))
    conn = pymysql.connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           password='root',
                           db='company_tel',
                           charset='utf8',
                           cursorclass=pymysql.cursors.DictCursor)
    cur = conn.cursor()
    cur.execute(sql)
    re =cur.fetchone()
    return re
#根据一个用户id，取一个他之前的文章，且没有被用过的

def post_content(data,url,headers):
    params = urllib.urlencode(data)
    request = urllib2.Request(url=url, data=params, headers=headers)
    response = urllib2.urlopen(request)
    soup = BeautifulSoup(response, "html.parser")
    return soup.text
#根据id，请求网页，进行回复

def update_id(id):
    conn = pymysql.connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           password='root',
                           db='company_tel',
                           charset='utf8',
                           cursorclass=pymysql.cursors.DictCursor)
    cur = conn.cursor()
    sql = 'update chinaaet set have_send=1 where link_title={}'.format(id)
    cur.execute(sql)
    conn.commit()
    return 'sucess'
#对回复过的页面id标记
max_id=len(get_new_name())
for i in range(1,18):
    new_name=get_new_name()[i]
    id = get_single_page(new_name)['link_title']
    url = 'http://blog.chinaaet.com/blog/postreply'
    if i%2==0:
        data = {
            '__RequestVerificationToken': 's7F_h2eOe7FU0QvZTYNu3eG-7V688zXAIGdot9z7g9BnDmvrRJ9MKZZGorAwiPpqNtlPeZ7qUaooQtg2Kjm46wmm4hA1',
            'BlogPostId': id,
            'content': '<p>感谢分享！<a href="http://www.doorock.com">http://www.doorock.com</a> 提供FAE(IC应用技术支持)共享服务的，有兴趣可以去看看。</p>'
        }
        header = {
            'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,ja;q=0.6',
            'Referer': 'http://www.dianyuan.com/index.php?do=community_mail_create&touid=759833',
            'Cookie': 'UM_distinctid=16481f6955d20d-0f7b6f1db5ef4a-5e442e19-1fa400-16481f6955e55; bdshare_firstime=1531293395861; Hm_lvt_0bc2b0756b170cff90e37c9e9628af4b=1531188778,1531271595,1531302772; CNZZDATA3455603=cnzz_eid%3D523849821-1531183947-http%253A%252F%252Fwww.chinaaet.com%252F%26ntime%3D1531300543; __RequestVerificationToken=h3viX_68MvbvzAVYtqijHJOgsTdOj1O6Bg84m5yL6COIwQhvIPzBZhqVE583XNtlAdvc_sU7UIwykGZetw0d_br76I01; __RequestVerificationToken=WCw1pebEgK7vRiqqWhaah40D8kol7y8pnELyreC4x7H2UH33gJaYvAyOe5ikwWQY0AmfDWpQ0Il6fJtyaedHBD-a29A1; ChinaaetAuth=BFDD8CBDCC938951A3BF038E97D2D50A067F9E8EB1597AB9730BC6E3C08F3C93B22D170FA3CD23EC4864831D42739ABD43AF3BD32FB2A1D28D3D53157B3CD517EE701A644E17004F18F088C3A2B61FDD8C3CCAEA633FDC52D984AA16E5B22D5663B9AFAF1D2B369C44405FCF5EFBBC4197CE85D32163BF6245A58F5BDE7BBD4C73F3F60A193C00F8DFEB8AAD5B913AA29677BDFEAB81B03F8940C405DA46D27627688DEE2188AFAEA06A0DE787CD163E86DB31428F572542667E1B4EBA2D359C54CBD2F30F4CF17630E5245115F29F55D0235198645C859B5AEAB6EA94D81F4157C3DFAD668DF200B175C34417E499ECB67772EA0BE0735DE98B8BA959A9365391A599BCBD9134FB9C864540E7CE0BA382374DD422BC9684C3CAD4F5C4919F36AD6811E51A78B43E1E9FD7FD8A99890857DA3B1BC35F69007545570E7324DD8C2633E325D39864308A85BF5D102304BB63B0CAE31A379589EEF68769F1EF572E467003E2915F38E5D678010BD779A3A5BFD501FA75F065C79EDE81132F57A2A7F57F890D6B0023FEC10E79A0693C5F3D67A8E8C54ED094CB0AAACF9B133DF6DD1D67B8E77D9F1B46393C92AAE2D7D3E6BCAA9F82A626EA6D7A07895205843A7DFEB15355649365F01BFEB0D57E73203FABD167518CF609530F9EF16DF312AAC2BA3BD4E366047BD67782EDB95953818A72EE5D0E6FAE87893A9C95052FC9707D1EEC18671D8847001F284E94B5B76B3575B74429; Hm_lpvt_0bc2b0756b170cff90e37c9e9628af4b=1531303266'}
    else:
        data = {
            '__RequestVerificationToken': 'GPLBwBSA8_if-GH6zBxwOFRhLBiqSDyh5au9xBKSfM9HzCaJFRVmyzye9PTRRCHpqs4PKWw774-qPXuoJk0L-joRp-s1',
            'BlogPostId': id,
            'content': '<p>感谢分享！<a href="http://www.doorock.com">http://www.doorock.com</a> 提供FAE(IC应用技术支持)共享服务的，有兴趣可以去看看。</p>'
        }
        header = {
            'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,ja;q=0.6',
            'Referer': 'http://www.dianyuan.com/index.php?do=community_mail_create&touid=759833',
            'Cookie': 'UM_distinctid=16481f6955d20d-0f7b6f1db5ef4a-5e442e19-1fa400-16481f6955e55; bdshare_firstime=1531293395861; Hm_lvt_0bc2b0756b170cff90e37c9e9628af4b=1531188778,1531271595,1531302772; __RequestVerificationToken=h3viX_68MvbvzAVYtqijHJOgsTdOj1O6Bg84m5yL6COIwQhvIPzBZhqVE583XNtlAdvc_sU7UIwykGZetw0d_br76I01; __RequestVerificationToken=WCw1pebEgK7vRiqqWhaah40D8kol7y8pnELyreC4x7H2UH33gJaYvAyOe5ikwWQY0AmfDWpQ0Il6fJtyaedHBD-a29A1; CNZZDATA3455603=cnzz_eid%3D523849821-1531183947-http%253A%252F%252Fwww.chinaaet.com%252F%26ntime%3D1531353455; ChinaaetAuth=0B24846BDA5CDD44107AA77D61599FD8738932F1E983C4833289F1B4BC81B5AFC8ABA50F03069856DCD80A1F0B00B874D800696878B9ACC90998AC6CAA75395B520C3C7945B1D3B187F4F89BCEA124DC3E3669F468880021D94A7E5F8E6E424652F24653B21D38EE22B9FF4DB8EEEE4B9F7459940DAE8D4C348F7839DF4FD1050E0858D262A15F7563CBDC557F4D38C693BD30165A8A423C4647D2A5F363A8E338387DB38F3E398883334E8920E5DDFEE21781BF22B9060A239B3EAFF0C256BEEB48DDFC226E6DF2A652B7FDBD1EC27445698F2D6C4158EDD6C8A1CBE5F4AD04A45127F555B318B0959C3993644A15FAEF29DE1D2A2A4E449EE039819CB157D6EEF06702D709B4D7F8378EAF5579993F5FBC63EE1866E440AE2F9550CDE1FC97FEFF9AE4DC5C8C9B503137C22AFC74258A29AB87E4ABFA2C5AF0A4845E5C01A8DE73D54A8695A4EBFB22FC2357F2DFBBABF37D24077147D65FCE45325C05AEFBC421A865DE0510527BB41EB92E454D0820EC6EC3E676FBA34DE616D4300D042424361CF420F5BA929B3AE93BD6EAC5C4A1E970D2F970D6AEAECD0945E0BEBB09ED501659020CF92D84F297A3EC82C3DF63608B15B229184F2800383F7C7B2B7E074EA599207B097418426872D862DB71FB6CDBAE0A617EDC038D6C7D65025FC0D9C9DF1E188ADB6AAEB7534464E345F2D9DE1820F69FC65C404A76522A8BD9160DFA0B2C9DC6D4FA9CE06659A0A496DDBE7C8F329E352226CC52224E9B0793DABAE4AEEB316D74B851FD8EC6C94A704ACC754587; Hm_lpvt_0bc2b0756b170cff90e37c9e9628af4b=1531357350'}
    print post_content(data,url,header)
    time.sleep(30)
    print(id,update_id(id))


