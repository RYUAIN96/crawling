import csv
import pymongo

conn = pymongo.MongoClient('192.168.99.100', 32766)
db = conn.get_database("db1") # db1생성
coll = db.get_collection("JR") # 테이블 생성


f = open('./resources/sunchang.csv', 'r')
rdr = csv.reader(f)
# print(rdr)
# next(rdr, None) # 컬럼 skip

sisul = list() # [] => 담아줄 빈 리스트를 만든다
is_cctv = list() # []
num_cctv = list()
road = list()
for line in rdr: # => 가지고 온 정보를 line 이라는 것에 담고 반복문을 돌려준다
    # 시설
    # print(line[0])
    sisul.append(line[0]) # [1,1,1,1,1, ...] => 시설이라는 리스트에 끝에서부터 요소를 추가한다 라인 리스트에 있는 0번째만 그것을 줄마다 반복한다
    # 씨씨티비 설치 여부
    # print(line[8])
    is_cctv.append(line[8]) # [1,1,1,1,1, ...]
    # 씨씨티비 설치 대수
    # print(line[9])
    num_cctv.append(line[9]) # [1,1,1,1,1, ...]
    # 보호구역 도로 폭
    # print(line[10])
    road.append(line[10]) # [1,1,1,1,1, ...]
  
print("="*50)
print(sisul) # => 그리고 프린트 해준다!
print("="*50)
print(is_cctv)
print("="*50)
print(num_cctv)
print("="*50)
print(road)