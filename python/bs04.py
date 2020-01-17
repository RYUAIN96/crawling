from bs4 import BeautifulSoup
import requests


url = "https://news.naver.com/main/opinion/home.nhn"
str = requests.get(url)
# print(str.text)


soup = BeautifulSoup(str.text, 'html.parser')

all_p_td = soup.find_all('p', {"class":"todaycolumn_headline"})
# print(all_div_section)
for tmp in all_p_td:
    li_all = tmp.find_all("li")[3]
    print(li_all)
    # for tmp1 in li_all[0]:
    #     print(tmp1)
    #     print("="*50)
    #     a1 = tmp1.find('span')
    
    # for tmp1 in tmp:
    #     print(tmp1.find('a').text)