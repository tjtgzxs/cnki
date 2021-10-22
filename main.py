from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Firefox
from  selenium.webdriver.firefox.options import  Options
import time
def open_url():
    firefox_options=Options()
    # firefox_options.add_argument("--headless")
    # firefox_options.add_argument("User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0")
    driver = Firefox("./")

    # driver.get('https://bot.sannysoft.com/')
    # time.sleep(5)
    # driver.save_screenshot('walkaround.png')
    driver.get("https://www.cnki.net/")
    a = driver.find_element_by_class_name('sort-default')
    webdriver.ActionChains(driver).move_to_element(a).click(a).perform()
    driver.find_element_by_link_text("全文").click() #选择高级搜索这个选项，并点击
    driver.find_element_by_id("txt_SearchText").send_keys("CGSS")
    time.sleep(2)
    a=driver.find_element_by_class_name('search-btn')
    a.click()
    ch=driver.find_element_by_class_name("ch")
    ch.click()
    time.sleep(10)
    xsqk=driver.find_element_by_xpath("//ul[@class='doctype-menus keji']/li[1]/a/span")
    xsqk.click()
    time.sleep(10)
    tr_list=driver.find_elements_by_xpath("//table[@class='result-table-list']/tbody/tr")
    for tr in tr_list:
        name=tr.find_element_by_class_name("name").text
        print(name)
    time.sleep(50)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    open_url()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
