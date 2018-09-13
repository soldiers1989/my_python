# -*- coding:gb2312 -*-
import config
import time
data = time.strftime("%m-%d %H%M", time.localtime())
sql_dr='TRUNCATE TABLE qq_id_copy'
sql='insert into qq_id_copy (SELECT DISTINCT * FROM qq_id)'
config.mysql_local_update_insert(sql_dr)
config.mysql_local_update_insert(sql)
sql_id='SELECT DISTINCT id FROM qq_id_copy'
n=config.mysql_local_select(sql_id)
f = open('qq_id-{}.txt'.format(data),'w')
for i in n:
    f.write(str(i['id']) + '\n')
f.close()

print '已导出txt文件,10秒后程序自动关闭！'
time.sleep(5)




