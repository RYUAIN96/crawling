import pandas as pd
import csv
import pymongo

conn = pymongo.MongoClient('192.168.99.100', 32766)
db = conn.get_database("db1") # db1생성
coll = db.get_collection("csv04") # 테이블 생성


# # csv는 구분자 , \t => 탭
# df = pd.read_csv('./resources/exam1.csv', delimiter=",")
# # print(df)

# # 프린트하면 8라인에 NaN이라는 게 있는데 그건 데이터가 없다는 소리
# # 그 값을 없애주기

# df = df.dropna() # NaN 제거 : 결측치 제거
# # print(df)

# list1 = df.values.tolist() # df를 list로 바꾸는 것
# # print(list1)
# dict1 = df.to_dict() # df를 dict로 바꾸는 것
# # print(dict1)


# df = pd.read_csv('./resources/exam1.csv')
# print(df)
# dict1 = df.to_dict()

# for key, value in dict1.items():
#     print(key,value[0])

f = open('./resources/exam1.csv', 'r', encoding="utf-8")

rdr = csv.reader(f)
# print(rdr)
column = next(rdr) #[컬럼명 읽기]
print(column)
# [manager_name,client_name,client_gender,client_age,response_time,statisfaction_level]

# [a,b,c,d,e,f] => 0,a 1,b 2,c 3,d
for line in rdr: 
    print("=============================")
    print(line)
    dict1 = dict() # 빈 딕셔너리를 만듦
    for idx, val in enumerate(line): #[1,2,3,4,5,6] # enumerate 원소의 순서와 값, 2개를 동시에 돌려주는 것
        # 0, Kumar / 1 , Nigam /2 ,male     ... / 5 , 0.5
        dict1[column[idx]] = val # column[idx] 은 리스트를 인덱싱하는 과정 # dict1[column[idx]] = val => 딕셔너리에 키랑 값을 넣는 과정
        print(dict1)

    coll.insert_one(dict1) # db몽고에 넣기
conn.close()
