from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import requests
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/lib")
from chaojiying import Chaojiying_Client
def getCode(im_path,type=1902):
    chaojiying = Chaojiying_Client('tjtgzxs', '1990lljxk', '921890')
    im = open(im_path, 'rb').read()
    return chaojiying.PostPic(im, type)
# session=requests.session()
# img_src=session.get("https://kns.cnki.net/KNS8/Brief/VerifyCode?t=589aaffd-354c-475b-8e15-4828f3889abdhttps://kns.cnki.net/KNS8/Brief/VerifyCode?t=589aaffd-354c-475b-8e15-4828f3889abdhttps://kns.cnki.net/KNS8/Brief/VerifyCode?t=589aaffd-354c-475b-8e15-4828f3889abdhttps://kns.cnki.net/KNS8/Brief/VerifyCode?t=589aaffd-354c-475b-8e15-4828f3889abd")
# with open('code.jpg', 'wb') as f:
#     f.write(img_src.content)
# code = getCode('code.jpg')
# print(code)
chrome_options = Options()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),options=chrome_options)
driver.get("https://www.cnki.net/")

