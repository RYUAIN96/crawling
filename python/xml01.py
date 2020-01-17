# xml파일에서 크롤링하기

from xml.etree.ElementTree import parse # => 파스 패키지를 가져오는 것


# doc = parse('C:\\Users\\admin\\Desktop\\python\\templates\\exam1.html')
doc = parse('./resources/exam1.xml') # => 경로에 있는 자료를 태그별로 잘라서 변수에 보관!!

a = doc.findall("student") # => 변수에 있는 student라는 태그를 모두 찾아서 a에 저장!

for tmp in a: # => a를 반복문 돌려서 필요한 것만 뽑아주기!
    tmp.findtext("name") #<name>a</name> => 태그 안에 있는 내용을 뽑아주는 findtext
    # print(tmp.findtext("age")) #<age>12</age>
    print(tmp.find('name').attrib) #<addr id="a">addr1</addr> => 태그를 뽑아주는 find에 태그 안에있는 내용이아닌 다른 요소를 뽑아주는 attrib 
            # {"id":"a"}
    print(tmp.find("addr").attrib)
    print(tmp.find("addr").text) # <= 태그를 뽑아주고 텍스트를 뽑아줌.!

# http://ihongss.com/xml/exam1.xml

# xml은 타고타고 상위에서 순서대로 들어가야함!
# html은 중간에 내가 할 부분만 먼저 정해서 들어가서 뽑아 낼 수 있음!