# pip install pymongo
import pymongo

import cx_Oracle as oci # pip install cx_Oracle
conn_o = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding="utf-8")
cursor = conn_o.cursor()

conn = pymongo.MongoClient('192.168.99.100', 32766)
db = conn.get_database("db1") #db가 없으면 만들어내고 db가 있으면 가져와주는 함수
coll = db.get_collection("p20200115") # collection(=table) 생성 db정보를 이용해 컬렉션 만든다 = >테이블 만든 단계,  예를들면멤버를 새로 만들음



# dict1 = {"id":"a","name":"abc", "age":15}
# coll.insert_one(dict1)

# dict1 = {"id":"b", "name":"bcd", "age":66}
# coll.insert_one(dict1)

# dict1 = {"id":"c", "name":"fff", "age":22}
# coll.insert_one(dict1)                       => 자료 넣어주기


#################################################################################

# < robo에 있는 자료를 찾아서 꺼낼 때 사용하는 명령문 => sql 문이랑 비슷 >

# #SELECT * FROM p202001015
# data1 = coll.find() 

# #SELECT * FROM p202001015 WHERE ID='a'
# data2 = coll.find({'id':'a'}) 

# # SELECT ID, NAME FROM p20200115 WHERE ID='a'
# data3 = coll.find({'id':'a'},{'id':1, 'name':1}) 

# # SELECT * FROM TABLE WHERE age > 10
# data4 = coll.find({'age':{"$gt":10}})

# # SELECT * FROM TABLE ORDER BY name ASC
# data5 = coll.find().sort('name', 1)  # 1 (ASC), -1(DESC)
# for tmp in data5:
#     print(tmp)

# # SELECT * FROM TABLE WHERE age>=10 AND age<=30
# data6 = coll.find({"age":{"$gte":10, "$lte":30}})

# # SELECT COUNT(*) FROM TABLE
# data7 = coll.find().count()
# print(data7) # 반복문 X, 딕셔너리 아님

# # SELECT * FROM TABLE WHERE ID='a' OR NAME='b'
# data8  = coll.find({'$or':[{"id":'a'},{"name":'b'}]})


####################################################################################################

# CREATE SEQUENCE SEQ_TABLE1_NO   => 시퀀스 만들기 기본값을 지정해 줌(변수 저장)
# START WITH 1                       원래 모델에서 하던 부분을 DB에서 해주는 것(알아놓기만 하기)
# INCREMENT BY 1
# NOMAXVALUE
# NOCACHE;

# COMMIT;

# -- SEQ_TABLE1_NO = SEQ_TABLE1_NO+1    => TABLE1에 NO값만 연속적으로 증가시켜주는 것
# INSERT INTO TABLE1(NO, ID, NAME, AGE)
# VALUES(SEQ_TABLE1_NO.nextval, 'a', 'name', 34);
# COMMIT;

##############################################################################

# 이제 할 것 => robo에 있는 자료를 sqldeveloper로 가져가는 작업

# SELECT ID,NAME,AGE FROM p20201015
data1 = coll.find({},{'_id':False}) # robo에 있는 자료를 받아서 data1에 넣어주는 것
for tmp in data1:
    # print(tmp)
    sql = """
        INSERT INTO TABLE1(NO, ID, NAME, AGE)
        VALUES(SEQ_TABLE1_NO.nextval, :id , :name, :age)
    """

    cursor.execute(sql, tmp)
    conn_o.commit()


conn_o.close()
conn.close()