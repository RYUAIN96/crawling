# < 자바스트립트 기반인 동적 사이트에 있는 데이터를 크롤링하는 방법 >

from selenium import webdriver
import time
options = webdriver.ChromeOptions()
options.add_argument('headless') # 화면표시 안되게끔 하는 것


options.add_argument("disable-gpu") # 크래픽카드 가속을 사용하지 않음 = 왜? 
options.add_argument("lang=ko_KR") # 언어를 한글로 설정
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent
# 가상을 만드니까 정보를 주지 않음 브라우저 없이 접속하지 못해서 비정상으로 인식을 해버림
# 마지막줄이 진짜 브라우저에 연결해주는 것처럼 보이게 해주는 것 로봇이 아니게끔

driver = webdriver.Chrome('./chromedriver.exe', 
    chrome_options=options)

driver.get("https://datalab.naver.com/shoppingInsight/sCategory.naver")

time.sleep(3)
tag = driver.find_element_by_class_name('rank_top1000_list').find_elements_by_tag_name('li')
# print(tag)

for tmp in tag:
    print(tmp.text.split("\n"))

#########################################################################

# headless ? 브라우저 창을 실제로 운영체제의 창으로 띄우지 않고 대신 화면을
# 그려주는 작업을 가상으로 진행해주는 방법

# headline 모드가 감춰졌는지 아닌지 확인해보기
# User-Agent 값을 확인해 보는 것

# headline => ('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) ************Chrome*****************/61.0.3163.100 Safari/537.36')
                                                                                                                        # 이 부분이 헤드라인

# headline 탐지 막기
# 기본적으로 가지고 있는 User-Agent값을 변경해주기 HeadlessChrome 을 Chrome 으로 변경

# slelnium => 웹 앱을 테스트하는 웹 프레임워크 webdriver API를 통해 브라우져를 제어

# time.sleep(3) => 자바스크립트에 의해 페이지 로딩이 완전히 이루어질 때까지 기다리기 위해 삽입
