# -*- coding:gb2312 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import function
id_list=[452193182,1125354542,547575116]
for id in id_list:
    cookies = function.get_cookies(id)[1]
    qun_id_from_id = function.get_qun_id_need(cookies, id)

    for i in qun_id_from_id:
        qun_id = i['qun_id']
        from_id = i['from_id']
        s = function.get_qun_user_id(qun_id, function.get_cookies(from_id)[1])
        if type(s) is list:
            for i in xrange(0, len(s)):
                function.insert_qq_id([s[i][0], s[i][1], s[i][2]])
            function.update_qq_qun_list(qun_id)
            print qun_id
        else:
            pass
print raw_input('活干完了，按enter退出！')



