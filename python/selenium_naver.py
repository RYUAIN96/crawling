from selenium import webdriver # selenium의 웹 드라이버 크롬의 기능을 도와주는 드라이버(장치)
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions()

options.add_argument('window-size=1920x1080')

driver = webdriver.Chrome('./chromedriver.exe', chrome_options=options)

driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")

driver.find_element_by_name("id").send_keys('ttmdrl4561')
driver.find_element_by_name("pw").send_keys('jw1109srh@')
driver.find_element_by_xpath('//*[@id="log.login"]').click()

driver.get("https://www.naver.com/") # 값을 넣고나서 돌아갈 페이지를 정해줄 것
html = driver.page_source
soup = BeautifulSoup(html, 'html_parser') # html을 가져와서 파싱 

driver.close() 
