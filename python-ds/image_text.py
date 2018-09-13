# -*- coding: UTF-8 -*_



#通过PIL pytesseract  Tesseract-OCR 三个插件识别普通验证码
#Tesseract-OCR需要单独安装并进行相关配置


from PIL import Image
import pytesseract
import requests



def downloads_pic(**kwargs):
    pic_path='G:\python_doc\\'
    pic_name = '222.png'
    url = 'http://miaobang.huinongtx.com/captcha.html'
    res = requests.get(url, stream=True)
    with open(pic_path + pic_name,'wb') as f:
        for chunk in res.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
        f.close()
downloads_pic()
text=pytesseract.image_to_string(Image.open(r'222.png'),lang="eng",config="-psm 6")
print(text)