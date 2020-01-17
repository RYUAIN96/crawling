# 임의로 만들어준 html파일에서 크롤링하기

from bs4 import BeautifulSoup

# with open('./resources/exam1.html') as fp:
# C:\Users\admin\Desktop\python\resources
# with open('C:\\Users\\admin\\Desktop\\python_crawling\\python_crawling\\resources\\exam1.html') as fp:
with open('C:\\Users\\admin\\Desktop\\python\\templates\\exam1.html') as fp:
    soup = BeautifulSoup(fp, 'html.parser') # fp 는 파일을 가져오기

    # div태그 첫번째 찾기
    first_divs = soup.find("div")
    # print(first_divs)

    # div태그 전체 찾기
    all_divs = soup.find_all("div")
    soup.find_all("div", {"class":"first"})
    # <div class="first"> => div의 클래스중에 first 클래스를 찾아라

    # print(all_divs)
    for tmp in all_divs:
        print(tmp)
        all_p = tmp.find_all("p")
        for tmp1 in all_p:
            print(tmp1)
            print(tmp1.text)

    