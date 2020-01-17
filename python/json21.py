import requests
import json
import pymongo

conn = pymongo.MongoClient('192.168.99.100', 32766)
db = conn.get_database("db1") #db가 없으면 만들어내고 db가 있으면 가져와주는 함수
table = db.get_collection("exam21") # collection(=table) 생성 db정보를 이용해 컬렉션 만든다 = >테이블 만든 단계,  예를들면멤버를 새로 만들음

url = "http://ihongss.com/json/exam21.json"
str1 = requests.get(url).text
data1 = json.loads(str1) 

a= data1['boxOfficeResult']['showRange']
for tmp in data1['boxOfficeResult']['dailyBoxOfficeList']:
    # print(tmp)
    dict1 = dict()
    dict1['showRange'] = a
    dict1['rankOldAndNew'] = ['rankOldAndNew']
    dict1['movieNm'] = ['movieNm']
    dict1['salesShare'] = ['salesShare']
    dict1['salesAcc'] = ['salesAcc']
    dict1['scrnCnt'] = ['scrnCnt']
    dict1['showCnt'] = ['showCnt']
    

    table.insert_one(dict1)


conn.close()