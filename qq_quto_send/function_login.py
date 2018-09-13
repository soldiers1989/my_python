# -*- coding:utf8 -*-
import aircv as ac
import win32gui
import win32api
import win32con
import time
import os
from PIL import ImageGrab


# 匹配图片并返回图片的中间点坐标
def matchImg(imgsrc, confidencevalue=0.8):
    im = ImageGrab.grab()
    x='cap.png'
    im.save(x, 'png')
    imsrc = ac.imread(imgsrc)
    imobj = ac.imread(x)
    match_result = ac.find_template(imsrc, imobj)
    if match_result is not None:
        match_result['shape'] = (imsrc.shape[1], imsrc.shape[0])  # 0为高，1为宽
        match_result['click']=(int(match_result['rectangle'][0][0]+match_result['shape'][0]/2),int(match_result['rectangle'][0][1]+match_result['shape'][1]/2))
        mov = match_result['click']
        win32api.SetCursorPos([mov[0], mov[1]])
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    else:
        return 'err'
#鼠标定位到

print(matchImg('type_to_get.png'))