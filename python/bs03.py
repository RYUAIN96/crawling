from bs4 import BeautifulSoup
import requests


url = "https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=100"
str = requests.get(url)
# print(str.text)


soup = BeautifulSoup(str.text, 'html.parser')

all_div_cluster = soup.find_all('div', {"class":"cluster_text"})
# print(all_div_cluster)
for tmp in all_div_cluster:
    print(tmp.find("a").text) # a 태그만 뽑는 것 
    

# print(tmp.find("a").text) 가나다 순으로
# print(tmp.find("a").attrs) {'href':'#, 'id':'aaa'}
# <a href="javascript:melon.play.playSong('1903010
