import requests
import json
import pymongo

conn = pymongo.MongoClient('192.168.99.100', 32766)
db = conn.get_database("db1") #db가 없으면 만들어내고 db가 있으면 가져와주는 함수
table = db.get_collection("exam4") # collection(=table) 생성 db정보를 이용해 컬렉션 만든다 = >테이블 만든 단계,  예를들면멤버를 새로 만들음

url = "http://ihongss.com/json/exam4.json"
str1 = requests.get(url).text
data1 = json.loads(str1) 

# insert_one({})
# insert_many ([{},{},{}])
for tmp in data1:
    # print(tmp['name'])
    # print(tmp['species'])
    # print(tmp['foods']['likes'][0]) # { , }
    # print(tmp['foods']['dislikes'][0])    ----------------------> 확인하는 작업
    dict1 = dict()
    dict1['name'] = tmp['name']
    dict1['species'] = tmp['species']
    dict1['likes'] = tmp['foods']['likes'][0]
    dict1['dislikes'] = tmp['foods']['dislikes'][0]

    table.insert_one(dict1)
    
conn.close()