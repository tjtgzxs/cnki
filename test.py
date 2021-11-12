from selenium  import webdriver
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
session=requests.session()
headers={
    "Cookie":"Ecp_ClientId=2211112092401868164; Ecp_IpLoginFail=21111260.30.241.14; ASP.NET_SessionId=xp1puvpq4eo5ydnmpjhmxhiw; SID_kns8=123105; cnkiUserKey=b32cf363-e222-3dd9-ad2c-0350c21c05dc; _pk_ref=%5B%22%22%2C%22%22%2C1636688448%2C%22https%3A%2F%2Fwww.cnki.net%2F%22%5D; _pk_ses=*; CurrSortField=%e7%9b%b8%e5%85%b3%e5%ba%a6%2f(ffd%2c%27rank%27); CurrSortFieldType=DESC; SID_kns_new=kns123120; Ecp_ClientIp=60.30.241.14; dstyle=listmode; dSearchFold=undefined; dsorder=pubdate; language=undefined; knsLeftGroupSelectItem=; dperpage=50; searchTimeFlag=1; _pk_id=f68ed718-3ce2-4f0e-8640-5d6d4795cc38.1636680244.2.1636688526.1636688448."
}
img_src=session.get("https://kns.cnki.net/KNS8/Brief/VerifyCode?t=cdc9bd6d-d84b-4841-839d-4ac5e45a97ba",headers=headers)
with open('code.jpg', 'wb') as f:
    f.write(img_src.content)
code = getCode('example.png')
print(code)
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),options=chrome_options)
# driver.get("https://www.cnki.net/")
# for request in driver.requests:
#     print(request.headers)

