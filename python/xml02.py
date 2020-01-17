from xml.etree.ElementTree import parse
# import requests
from urllib.request import urlopen

url = 'http://ihongss.com/xml/exam1.xml'
# str = requests.get(url)
# doc = parse(str.text)
# print(doc)

str1 = urlopen(url)
doc1 = parse(str1)
print(doc1)

for item in doc1.iterfind('items/item'): # => 'items/item' path경로를 정해주는거
    print(item.attrib) # <item id="a"> => attrib : item 을 잘라주는 거 태그 안에 있는 요소를 가져오기
    print(item.findtext("name")) # <name>a</name>