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

driver.get("http://www.newsis.com/view/?id=NISX20200114_0000888385")

time.sleep(3)
tag = driver.find_element_by_class_name('article_tbx mgt8 w970').find_elements_by_tag_name('h1')
print(tag)

# for tmp in tag:
#     print(tmp.text.split("\n"))