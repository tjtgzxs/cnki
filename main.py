
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Firefox
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.chrome.service import Service
from io import StringIO
from selenium.webdriver.support import expected_conditions as EC
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
import  re
import xlrd
import xlwt
import os
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from xlutils.copy import  copy
import configparser
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/lib")
print(os.path.dirname(os.path.abspath(__file__))+"/lib")
from chaojiying import Chaojiying_Client
def getCode(im_path,type=1902):
    chaojiying = Chaojiying_Client('tjtgzxs', '1990lljxk', '921890')
    im = open(im_path, 'rb').read()
    return chaojiying.PostPic(im, type)
def open_url():


    config = configparser.ConfigParser()
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    config.read(os.path.join(BASE_DIR, 'conf.ini'), encoding="utf-8")
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),options=chrome_options)
    driver.maximize_window()
    print(111)
    driver.get("https://www.cnki.net/")
    time.sleep(5)
    a = driver.find_element_by_class_name('sort-default')
    webdriver.ActionChains(driver).move_to_element(a).click(a).perform()
    driver.find_element_by_link_text("全文").click()  # 选择高级搜索这个选项，并点击
    driver.find_element_by_id("txt_SearchText").send_keys("CGSS")
    time.sleep(2)
    a = driver.find_element_by_class_name('search-btn')
    a.click()
    time.sleep(20)
    ch = driver.find_element_by_class_name("ch")
    ch.click()
    time.sleep(10)
    xsqk = driver.find_element_by_xpath("//ul[@class='doctype-menus keji']/li[1]/a/span")
    xsqk.click()
    time.sleep(10)
    page_a = driver.find_element_by_id('perPageDiv')
    webdriver.ActionChains(driver).move_to_element(page_a).click(page_a).perform()
    driver.find_element_by_link_text("50").click()  #
    time.sleep(20)

    while(driver.find_element_by_id('PageNext').is_enabled()):
        time.sleep(2)
        driver.find_element_by_id('PageNext').click()
        time.sleep(20)
        get_detail(driver)
    print("爬取Finished")
    driver.close()

def get_veri(driver):
    # 处理验证码
    try:
        if driver.find_element_by_id("checkCodeBtn").is_enabled():
            c = driver.get_cookies()
            cookies = {}
            for cookie in c:
                cookies[cookie['name']] = cookie['value']
            print("需要验证码")
            with open('code.jpg', 'wb') as f:
                session = requests.session()
                img_src = driver.find_element_by_id("changeVercode").get_attribute('src')
                print(img_src)
                # img_src="https://kns.cnki.net/"+img_src
                # img_src = "https://so.gushiwen.cn" + img_src
                headers = {
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"
                }
                img_src = session.get(img_src,cookies=cookies)
                f.write(img_src.content)
            code = getCode('code.jpg')
            print(code)
            driver.find_element_by_id('vericode').send_keys(code['pic_str'])
            time.sleep(2)
            driver.find_element_by_id("checkCodeBtn").click()
            time.sleep(50)
            driver.save_screenshot("example.png")
    except:
        print("no verify")
        time.sleep(2)

def get_detail(driver):
    # 处理验证码
    try:
        if driver.find_element_by_id("checkCodeBtn").is_enabled():
            c=driver.get_cookies()
            cookies = {}
            for cookie in c:
                cookies[cookie['name']] = cookie['value']
            print("需要验证码")
            with open('code.jpg', 'wb') as f:
                session = requests.session()
                img_src = driver.find_element_by_id("changeVercode").get_attribute('src')
                print(img_src)
                # img_src="https://kns.cnki.net/"+img_src
                # img_src = "https://so.gushiwen.cn" + img_src
                headers = {
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"
                }
                img_src = session.get(img_src,cookies=cookies)
                f.write(img_src.content)
            code = getCode('code.jpg')
            print(code)
            driver.find_element_by_id('vericode').send_keys(code['pic_str'])
            time.sleep(2)
            driver.find_element_by_id("checkCodeBtn").click()
            time.sleep(50)
            driver.save_screenshot("example.png")
    except:
        print("no verify")
        time.sleep(2)
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    tr_list = driver.find_elements_by_xpath("//table[@class='result-table-list']/tbody/tr")

    for tr in tr_list:
        data=[]
        name=tr.find_element_by_class_name("name").text
        data.append(tr.find_element_by_class_name("name").text)
        # data.append(tr.find_element_by_class_name("author").text)
        source = tr.find_element_by_class_name("source").text
        date = tr.find_element_by_class_name("date").text
        quote = tr.find_element_by_class_name("quote").text
        download = tr.find_element_by_class_name("download").text
        # print(quote,download)
        window=driver.current_window_handle
        detail_button=tr.find_element_by_class_name("fz14").click()
        # webdriver.ActionChains(driver).move_to_element(name).click(name).perform()
        time.sleep(10)
        windows = driver.window_handles
        detail=driver.switch_to.window(windows[-1])
        authorlist=driver.find_elements_by_xpath("//div[@class='brief']/div/h3[1]//a")
        try:
            companylist=driver.find_elements_by_xpath("//div[@class='brief']/div/h3[2]//a|//div[@class='brief']/div/h3[2]//span")
        except:
            companylist=[]
        company_data=[]
        author_data=[]
        for author in authorlist:
            author_text=author.text
            author_data.append(author_text.rstrip('123456789'))

        for company in companylist:
            company_text=company.text
            if company_text.find(".")>-1:
                company_data.append(company_text[company_text.find(".")+1:])
            else:
                company_data.append(company_text)
        try:
            data.append(author_data[0])
        except:
            data.append("")
        try:
            data.append(company_data[0])
        except:
            data.append("")

        try:
            data.append(author_data[1])
        except:
            data.append("")
        try:
            data.append(company_data[1])
        except:
            data.append("")
        try:
            data.append(author_data[2])
        except:
            data.append("")
        try:
            data.append(company_data[2])
        except:
            data.append("")
        data.append("期刊")
        data.append(date)
        data.append(source)
        toplist = driver.find_elements_by_xpath("//div[@class='top-tip']/a")
        core_flag=False
        CS_flag=False
        for top in toplist:
            print(top.text)
            if top.text.find("核心")>-1:
                core_flag=True
            if top.text.find("CSSCI")>-1:
                CS_flag=True
        if core_flag==True:
            data.append("1")
        else:
            data.append("0")
        if CS_flag == True:
            data.append("1")
        else:
            data.append("0")
        data.append(str(quote))
        data.append(str(download))
        keylist = driver.find_elements_by_xpath("//p[@class='keywords']/a")
        key_data=[]
        for key in  keylist:
            key_data.append(key.text.rstrip(";"))
        for i in range(0,4):
            try:
                data.append(key_data[i])
            except:
                data.append("")
        try:
            topic=driver.find_element_by_xpath("//div[@class='doc-top']//li[last()-1]/p").text
            topic_list=topic.split(";")
            for i in range(0,2):
                try:
                    data.append(topic_list[i])
                except:
                    data.append("")
        except:
            data.append("")
            data.append("")

        try:
            summary=driver.find_element_by_class_name("abstract-text").text
            last_year=re_find(summary)
            if last_year==False:
                pdf_value=PDFHandle(name=os.path.join(BASE_DIR,os.path.join("pdf", (str(name)))))
                if pdf_value==False:
                    data.append("")
                else:
                    last_year2=re_find(pdf_value)
                    if last_year2==False:
                        data.append("")
                    else:
                        data.append(last_year2)
            else:
                data.append(last_year)
        except:
            data.append("")
        append_excel(os.path.join(BASE_DIR,'output.xls'),data,name)
        # print( driver.find_element_by_id("ChDivSummary").text)
        driver.close()
        driver.switch_to.window(window)

    time.sleep(10)


def PDFHandle(name):
    output_string = StringIO()
    try:
        print(name)
        with open(name, 'rb') as in_file:
            parser = PDFParser(in_file)
            doc = PDFDocument(parser)
            rsrcmgr = PDFResourceManager()
            device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            for page in PDFPage.create_pages(doc):
                interpreter.process_page(page)
            return output_string.getvalue()
    except:
        print("未找到{name}".format(name=name))
        return  False

def re_find(value):
    value=value.replace("'","")
    value=value.replace("\"","")
    value=value.replace("-","")
    value=value.replace(";","")
    list1=[r'第\d+期CGSS',r"第d+期中国综合社会调查",r"CGSS第\d+期",r"中国综合社会调查第\d+期"]
    dict1=[2003,2005,2006,2008,2010,2011,2012,2013,2015,2017]
    for item in list1:
        m=re.findall(item,value)
        if len(m)>0:
            number=re.findall(r"\d+",m[0])
            return  dict1[int(number[0])-1]
    list2=[r'\d+年CGSS',r'\d+年中国综合社会调查',r'CGSS\d+',r'中国综合社会调查\d+']
    for item in list2:
        m=re.findall(item,value)
        if len(m)>0:
            number=re.findall(r"\d+",m[0])
            return  number[0]
    return False

def append_excel(path,value,name=""):
    index=len(value)
    workbook=xlrd.open_workbook(path)
    sheets=workbook.sheet_names()
    worksheet=workbook.sheet_by_name(sheets[0])
    rows_old=worksheet.nrows
    new_workbook=copy(workbook)
    new_worksheet=new_workbook.get_sheet(0)
    for i in range(0,index):
       new_worksheet.write(rows_old,i,value[i])
    new_workbook.save(path)
    print("{name}追加成功".format(name=name))








# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    value=open_url()
    # print(re_find("大苏打飒飒的,第5期CGSS的具体呢荣，哈哈哈哈"))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# ['检验环境关心量表的中国版(CNEP)——基于CGSS2010数据的再分析', '洪大用', ' 中国人民大学社会学系', '范叶超', ' 美利坚大学社会学系', '肖晨阳', '', '期刊', '2014-07-20', '社会学表', '心态体系', '专辑：', '']
