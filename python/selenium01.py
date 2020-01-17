# < 로그인이후 페이지랑 자바 스크립트 페이지를 가져올 때 크롬을 이용해서 가져옴 >

# pip install selenium 먼저 깔아주고

# from selenium import webdriver

# options = webdriver.ChromeOptions()
# # options.add_argument('headless') # 화면표시 안됨
# # 
# options.add_argument('window-size=1920x1080')

# driver = webdriver.Chrome('./chromedriver.exe', chrome_options=options)

# driver.get("http://ihongss.com")

#=================================================== 여기까진 로그인 전 페이지

from selenium import webdriver
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions() # 크롬으로 창 열어주기
# options.add_argument('headless') # 화면표시 안됨
options.add_argument('window-size=1920x1080') # 화면 사이즈

driver = webdriver.Chrome('./chromedriver.exe', chrome_options=options) # 드라이버는 웹드라이버
# 웹드라이버를 실행해주는데 다운받은 웹드라이버를 실행해주고 크롬 옵션은 크롬으로 열어주는 것을 드라이버에 담음

driver.get("http://ihongss.com/webboard") # 필요한 곳으로 주소 바꾸기 => 드라이버가 이 페이지를 가져오게끔 하는 것

driver.execute_script("document.getElementsByName('email')[0].value='20191216'") # 밑에꺼랑 똑같은 창 다른방법
# driver.find_element_by_name("email").send_keys('20191216') # 로그인 하게 해주는거
driver.find_element_by_name("pw").send_keys("20191216") # 패스워드 입력해줌 => 드라이버에 네임이라는 값을 찾아 키를 넣어서 주라는 것 
driver.find_element_by_css_selector('#form1 > div:nth-child(4) > input').click() # => 로그인 페이지를 찾아서 클릭하게 해주는 것
# selector
# selector 가 안될 경우 xpath로 해볼 것!
#form1 > div:nth-child(4) > input  => 원하는 창으로 들어가게 찾는 방법
# (아이디) (div)   (input 타입이다)


time.sleep(3) # 3초뒤에
driver.execute_script("alert('hello')") # 알림창이 뜨게 해주는 것 => 중간중간에 스크립트도 넣을 수 있다!


"""
driver.get("http://daum.net") #  로그인 이후의 페이지
html = driver.page_source
soup = BeautifulSoup(html, 'html_parser') # html을 가져와서 파싱 

driver.close()
"""

