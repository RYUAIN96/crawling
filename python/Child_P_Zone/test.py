## csv01.py #################################
import csv
import readline
# import pymongo

#http://ihongss.com/csv/exam1.csv

# conn = pymongo.MongoClient('192.168.99.100', 32766)
# db = conn.get_database("db1")
# coll = db.get_collection("exam1") 

for i in range(100, 150):
    string = "C:\\Users\\admin\\Desktop\\python\\Child_P_Zone\\" + str(i) + ".csv"  # => for 문으로 이 리스트를 다 자동화해서 db로 들어가는 것

# f = open('C:\\Users\\admin\\Desktop\\python_crawling\\python_crawling\\resources\\incheon_ongjin.csv', 'r')
f = open('C:\\Users\\admin\\Desktop\\python\\Child_P_Zone\\전라남도_담양군_어린이보호구역_20190917.csv', 'r')
rdr = csv.reader(f)
column = next(rdr) #[컬러명 읽기]

sisul = list()
cctv_is = list()
cctv_num = list()
road = list()
bigaddr = list()
smalladdr = list()

for line in rdr:
    dict1 = dict()    
    for idx, val in enumerate(line):
        if val == "":
            val = "0"
        dict1[column[idx]] = val
    # print(dict1)
    addr = dict1["소재지도로명주소"].split(" ")
    # print(addr)
    sisul.append(dict1["시설종류"])
    cctv_is.append(dict1["CCTV설치여부"])
    cctv_num.append(dict1["CCTV설치대수"])
    road.append(dict1["보호구역도로폭"])
    bigaddr.append(addr[0])
    smalladdr.append(addr[1])

print(bigaddr)
print(smalladdr)

print("시설종류 : "); print(sisul)
print("CCTV설치여부 : "); print(cctv_is)
print("CCTV설치대수 : "); print(cctv_num)
print("보호구역도로폭 : "); print(road)

# print("="*50)

# print("전체     : " + str(len(sisul)))
# print("유치원   : " + str(sisul.count("유치원")))
# print("어린이집 : " + str(sisul.count("어린이집")))
# print("초등학교 : " + str(sisul.count("초등학교")))
# print("특수학교 : " + str(sisul.count("특수학교")))

# print("="*50)

# print("전체 : " + str(len(cctv_is)))
# print("Y    : " + str(sisul.count("Y")))
# print("N    : " + str(sisul.count("N")))

# print("="*50)

    # coll.insert_one(dict1)
# conn.close()