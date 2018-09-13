# coding=utf-8
import xlrd
import pymysql
from openpyxl import Workbook
def get_id():
    workbook = xlrd.open_workbook('F:\python-21ic\id.xlsx')
    sheet2 = workbook.sheet_by_name('Sheet1')
    rows_need = []
    cols = sheet2.col_values(0)  # 获取第一列内容
    for i in range(0, len(cols)):
        rows_need.append(int(sheet2.row_values(i)[0]))  # 获取第i 行内容
    return rows_need
conn = pymysql.connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       password='root',
                       db='21ic',
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)

cur = conn.cursor()
pro_id=get_id()
for i in range(0,len(pro_id)):
    sql='insert into 21ic_project set project_id={}'.format(pro_id[i])
    cur.execute(sql)
    conn.commit()