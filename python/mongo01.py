# pip install pymongo
import pymongo

conn = pymongo.MongoClient('192.168.99.100', 32766)
db = conn.get_database("db1") #db가 없으면 만들어내고 db가 있으면 가져와주는 함수
table = db.get_collection("table1") # collection(=table) 생성 db정보를 이용해 컬렉션 만든다 = >테이블 만든 단계,  예를들면멤버를 새로 만들음

dict1 = {"id":"a", "age":35}

table.insert_one(dict1) # 추가하기
data1 = table.find()
for tmp in data1:
    print(tmp)
conn.close()
