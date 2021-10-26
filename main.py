

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Firefox
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import Options
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
from xlutils.copy import  copy
def open_url():
    firefox_options = Options()
    # firefox_options.add_argument("--headless")
    # firefox_options.add_argument("User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0")
    driver = Firefox(executable_path="./geckodriver",options=firefox_options)
    # driver=Firefox()
    # driver.get('https://bot.sannysoft.com/')
    # time.sleep(5)
    # driver.save_screenshot('walkaround.png')
    driver.get("https://www.cnki.net/")
    time.sleep(5)
    a = driver.find_element_by_class_name('sort-default')
    webdriver.ActionChains(driver).move_to_element(a).click(a).perform()
    driver.find_element_by_link_text("全文").click()  # 选择高级搜索这个选项，并点击
    driver.find_element_by_id("txt_SearchText").send_keys("CGSS")
    time.sleep(2)
    a = driver.find_element_by_class_name('search-btn')
    a.click()
    time.sleep(10)
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
    next_btn=driver.find_element_by_id('PageNext')
    get_detail(driver)
    while(next_btn.is_enabled()):
        next_btn.click()
        time.sleep(20)
        get_detail(driver)


def get_detail(driver):
    tr_list = driver.find_elements_by_xpath("//table[@class='result-table-list']/tbody/tr")

    for tr in tr_list:
        data=[]
        data.append(tr.find_element_by_class_name("name").text)
        # data.append(tr.find_element_by_class_name("author").text)
        source = tr.find_element_by_class_name("source").text
        date = tr.find_element_by_class_name("date").text
        quote = tr.find_element_by_class_name("quote").text
        download = tr.find_element_by_class_name("download").text

        window=driver.current_window_handle
        detail_button=tr.find_element_by_class_name("name").click()
        time.sleep(50)
        windows = driver.window_handles
        detail=driver.switch_to.window(windows[-1])
        authorlist=driver.find_elements_by_xpath("//div[@class='brief']/div/h3[1]//a")
        companylist=driver.find_elements_by_xpath("//div[@class='brief']/div/h3[2]//a")
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
        data.append(author_data[0])
        data.append(company_data[0])
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
        data.append(quote)
        data.append(download)
        keylist = driver.find_elements_by_xpath("//p[@class='keywords']/a")
        key_data=[]
        for key in  keylist:
            key_data.append(key.text.rstrip(";"))
        for i in range(0,4):
            try:
                data.append(key_data[i])
            except:
                data.append("")


        # print( driver.find_element_by_id("ChDivSummary").text)
        driver.close()
        driver.switch_to.window(window)

    time.sleep(10)


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

def append_excel(path,value,name=""):
    index=len(value)
    workbook=xlrd.open_workbook(path)
    sheets=workbook.sheet_names()
    worksheet=workbook.sheet_by_name(sheets[0])
    rows_old=worksheet.nrows
    new_workbook=copy(workbook)
    new_worksheet=new_workbook.get_sheet(0)
    for i in range(0,index):
        for j in range(0,len(value[i])):
            new_worksheet.write(i+rows_old,j,value[i][j])
    new_workbook.save(path)
    print("{name}追加成功".format(name=name))








# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    value=open_url()
    # print(re_find("大苏打飒飒的,第5期CGSS的具体呢荣，哈哈哈哈"))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
