from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),options=chrome_options)
driver.get("https://www.cnki.net/")
# str="asdasdsd"
# print(str.split(";"))
