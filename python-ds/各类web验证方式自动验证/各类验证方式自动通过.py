# -*- coding: UTF-8 -*-
# 参考https://www.cnblogs.com/jianqingwang/p/6978724.html
#环境配置完成后需要重启机器（也许重启pycharm即可）
from PIL import Image
import PIL.ImageOps
import pytesseract

#tesseract-ocr识别简单的验证码
#相当于把扫描件中文字读出来
def easy_pic():
    image = Image.open(r'F:\python-ds\1.png')
    code = pytesseract.image_to_string(image, lang='chi_sim')  # eng 英文，chi_sim简体中文。默认问英文
    return (code)

#略微有些遮挡的字符
#只能识别书写正确的文本
def initTable(threshold=140):
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    return table

def nomorl_pic():
    im = Image.open(r'F:\python-ds\222.png')
    # 图片的处理过程
    im = im.convert('L')  # 转为灰度图
    binaryImage = im.point(initTable(), '1')  # 图片二值化
    im1 = binaryImage.convert('L')  # 图片二值化后转灰度
    im2 = PIL.ImageOps.invert(im1)  # 图片取反色
    im3 = im2.convert('1')  # 图片二值化
    im4 = im3.convert('L')  # 图片二值化后转灰度

    # 将图片中字符裁剪保留(非必须的，看具体图片情况）
    box = (0, 0, 120, 38)
    region = im4.crop(box)  # 表示为坐标是 (left, upper, right, lower) 左上角为 (0, 0)的坐标系统

    out = region.resize((120, 38))  # 将图片字符放大
    code = pytesseract.image_to_string(out)
    print code
    # print (out.show())


print(easy_pic())