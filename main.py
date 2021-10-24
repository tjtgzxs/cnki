from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Firefox
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import Options
import time
from selenium.webdriver.chrome.service import Service
from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
import  re
def open_url():
    firefox_options = Options()
    # firefox_options.add_argument("--headless")
    # firefox_options.add_argument("User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0")
    driver = Firefox("./",options=firefox_options)

    # driver.get('https://bot.sannysoft.com/')
    # time.sleep(5)
    # driver.save_screenshot('walkaround.png')
    driver.get("https://www.cnki.net/")
    a = driver.find_element_by_class_name('sort-default')
    webdriver.ActionChains(driver).move_to_element(a).click(a).perform()
    driver.find_element_by_link_text("全文").click()  # 选择高级搜索这个选项，并点击
    driver.find_element_by_id("txt_SearchText").send_keys("CGSS")
    time.sleep(2)
    a = driver.find_element_by_class_name('search-btn')
    a.click()
    ch = driver.find_element_by_class_name("ch")
    ch.click()
    time.sleep(10)
    xsqk = driver.find_element_by_xpath("//ul[@class='doctype-menus keji']/li[1]/a/span")
    xsqk.click()
    time.sleep(10)
    tr_list = driver.find_elements_by_xpath("//table[@class='result-table-list']/tbody/tr")
    for tr in tr_list:
        name = tr.find_element_by_class_name("name").text
        author = tr.find_element_by_class_name("author").text
        source = tr.find_element_by_class_name("source").text
        date = tr.find_element_by_class_name("date").text
        quote = tr.find_element_by_class_name("quote").text
        download = tr.find_element_by_class_name("download").text
        handles = driver.window_handles
        driver.switch_to.window(handles[1])
        print(name)
    time.sleep(50)

def PDFHandle():
    output_string = StringIO()
    with open('test.pdf', 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)

    return  output_string.getvalue(),
def re_find(value):

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
    return None










# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    value=PDFHandle()
    print(re_find("大苏打飒飒的,第5期CGSS的具体呢荣，哈哈哈哈"))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
