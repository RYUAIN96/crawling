from selenium import webdriver
import urllib. request
import time

options = webdriver.ChromeOptions()

options.add_argument('headless')
options.add_argument("disable-gpu")   
options.add_argument("lang=ko_KR")    
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')


driver = webdriver.Chrome("C:\\Users\\admin\\Desktop\\python\\chromedriver.exe", chrome_options=options)

# 1페이지 - 6개만
# url = "http://www.newsis.com/search/?val=%25EC%2596%25B4%25EB%25A6%25B0%25EC%259D%25B4%25EB%25B3%25B4%25ED%2598%25B8%25EA%25B5%25AC%25EC%2597%25AD&sort=acc&jo=sub&bun=all_bun&sdate=&term=allday&edate=&s_yn=Y&catg=0&t=0&page=1&"
# 추가 - 20개 
url = "http://www.newsis.com/search/schlist/?val=%25EC%2596%25B4%25EB%25A6%25B0%25EC%259D%25B4%25EB%25B3%25B4%25ED%2598%25B8%25EA%25B5%25AC%25EC%2597%25AD&sort=acc&jo=sub&bun=all_bun&sdate=&term=allday&edate=&s_yn=Y&catg=1&t=1&page=1&"
driver.get(url)

print("start")

title = list()
link = list()
date = list()
content = list() 

articles = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[3]/ul')
article = articles.find_elements_by_class_name('bundle') # []
for tmp in article:
    title.append(tmp.find_element_by_tag_name("a").text)
    link.append(tmp.find_element_by_tag_name("a").get_attribute("href"))
    date.append(tmp.find_element_by_class_name('date').text)
    content.append(tmp.find_element_by_class_name('date').text)


print("="*50)
print("title")
print("="*50)
for i in title:
    print(i)

print("="*50)
print("date")
print("="*50)
for i in date:
    print(i)

print("="*50)
print("content")
print("="*50)
for i in content:
    print(i)

print("="*50)
print("link")
print("="*50)




# idx = 0
# for i in link:
#     driver.get(i)
#     time.sleep(1)
#     tmp = driver.find_element_by_xpath('//*[@id="textBody"]')
#     img_table = tmp.find_element_by_tag_name('table')
#     try:
#         file = img_table.find_element_by_tag_name('img').get_attribute("src")

#         # C:\Users\admin\Desktop\python\newsis
#         path = "C:\\Users\\admin\\Desktop\\python\\newsis\\"
#         file_name = "newsis" + str(idx) + ".png"
#         urllib.request.urlretrieve(file, path + file_name)
#         print("image save!!")
#         idx += 1
#     except Exception as e:
#         idx += 1
#         continue


#     """
#     C:\\Users\\admin\\Desktop\\python\\newsis\\newsis4.png
#     """