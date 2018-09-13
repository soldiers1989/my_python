# -*- coding:utf8 -*-
import win32gui
import win32api
import win32con
import time
import os

#os.startfile("C:/Program Files (x86)/Tencent/QQ/Bin/QQ.exe")

#鼠标定位到
win32api.SetCursorPos([1678,1064])
#执行左单键击
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)

time.sleep(0.8)
#鼠标定位到
win32api.SetCursorPos([1677,975])
#右键单击
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
qun_id=147082902
s=str(qun_id)
#得到QQ群id的键值
keyinput=[]
for i in range(0,len(s)):
    keyinput.append(int(s[i])+48)

#清空之前的输入
i=0
for i in range(0,20):
    i+=1
    win32api.keybd_event(8,0,0,0) #退格
    win32api.keybd_event(8,0,win32con.KEYEVENTF_KEYUP,0) #Realize the F11 button


#输入QQ群id
for k in keyinput:
    win32api.keybd_event(k,0,0,0) #F11
    win32api.keybd_event(k,0,win32con.KEYEVENTF_KEYUP,0) #Realize the F11 button
#输入回车
win32api.keybd_event(13,0,0,0) #F11
win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0) #Realize the F11 button




