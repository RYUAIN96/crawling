import requests
import json
import pymongo

conn = pymongo.MongoClient('192.168.99.100', 32766)
db = conn.get_database("db1") #db가 없으면 만들어내고 db가 있으면 가져와주는 함수
table = db.get_collection("exam10") # collection(=table) 생성 db정보를 이용해 컬렉션 만든다 = >테이블 만든 단계,  예를들면멤버를 새로 만들음

url = "http://ihongss.com/json/exam10.json"
str1 = requests.get(url).text
data1 = json.loads(str1) 

# insert_one({})
# insert_many ([{},{},{}])
for tmp in data1['data']:
    # print(tmp['id'])
    # print(tmp['name'])
    # print(tmp['score']['math']) # { , }
    # print(tmp['score']['kor']) 
    dict1 = dict()
    dict1['id'] = tmp['id']
    dict1['name'] = tmp['name']
    dict1['age'] = tmp['age']
    dict1['math'] = tmp['score']['math']
    dict1['kor'] = tmp['score']['kor']

    table.insert_one(dict1)
    
conn.close()