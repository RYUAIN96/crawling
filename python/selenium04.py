# < 네이버에서 여러 이미지 한번에 크롤링하는 방법 > => 다른 검색 페이지에서도 해보기

from selenium import webdriver
import urllib.request  # 이 라이브러리에 다운하는게 있음
# import time
from selenium.webdriver.common.keys import Keys # keys를 임포트!!!

# 절대 경로 가져오기
import os

## :\Users\admin\Desktop
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # => 폴더의 경로가 다를 경우 절대경로를 잡아준다.장고에서 셋팅 파일에 이렇게 경로를 잡아 줌
# :\Users\admin\Desktop\python => 경로로 이동
print(os.path.join(BASE_DIR,'python'))

options = webdriver.ChromeOptions()

# options.add_argument('headless')  
options.add_argument("disable-gpu") 
options.add_argument("lang=ko_KR") 
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')

driver = webdriver.Chrome(
    os.path.join(BASE_DIR,'python','chromedriver.exe'), 
    options=options)

driver.get('https://www.naver.com/')

driver.find_element_by_xpath('//*[@id="query"]').send_keys('정해인')
driver.find_element_by_xpath('//*[@id="query"]').send_keys(Keys.ENTER) # 엔터키 눌러주는 것
driver.find_element_by_xpath('//*[@id="lnb"]/div/div[1]/ul/li[2]/a/span').click() # 클릭

# < 가지고 오고 싶은 이미지를 순차적으로 xpath로 복사하면 반복되는 구간이 있음 그 부분을 변수로 바꿔서 반복문 돌려주기


link = []
for i in range(1, 30): 
    try:
        img = driver.find_element_by_xpath('//*[@id="_sau_imageTab"]/div[2]/div[1]/div['+ str(i) +']/a[1]/img') 
    except:
        img = driver.find_element_by_xpath('//*[@id="_sau_imageTab"]/div[2]/div[2]/div['+ str(i) +']/a[1]/img')  
    # print(img)
    link.append(img.get_attribute("src")) # 이미지의 소스에 src 태그 안에 포함된 것을 link에 넣음

for idx,tmp in enumerate(link): # link에서 순서와 값을 반복해서 뽑아내기
    urllib.request.urlretrieve(tmp,os.path.join(BASE_DIR,'python', 'download', "n" + str(idx)+".jpg"))
                                # tmp라는 기값을 불러오고 경로에 맞는 것에 n에 숫자를 붙여서 저장!