from selenium import webdriver
import urllib.request  # 이 라이브러리에 다운하는게 있음

options = webdriver.ChromeOptions()

options.add_argument('headless')  
options.add_argument("disable-gpu") 
options.add_argument("lang=ko_KR") 
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')

driver = webdriver.Chrome('./chromedriver.exe', 
    chrome_options=options)

url = "http://www.newsis.com/view/?id=NISX20200114_0000888385"
driver.get(url)
#image_view_0 copy-selector로 복사
img = driver.find_element_by_css_selector('#imgartitable_NISI20200114_0000462249 > tbody > tr:nth-child(1) > td > img')
# print(img)

# <selenium.webdriver.remote.webelement.WebElement (session="606a290182e19acfb094ccba333072b0", element="3222320d-9877-40bf-8ec3-b334a0c89685")>
# PS C:\Users\admin\Desktop\python> => 이미지를 찾았다는 표시가 터미널에 뜸

file = img.get_attribute("src") # 찾은 태그 중에서 src의 값 가져옴
# print(file)
urllib.request.urlretrieve(file, "./newsis/a11.png") # 다운로드 폴더안에 a2.png로 저장되는 명령어 => 다운로드 폴더가서 확인

driver.close() # 드라이버 닫아주기