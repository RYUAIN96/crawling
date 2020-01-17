# 파일명 : json01.py > 파일에서 가져오는 것

import json
import cx_Oracle as oci

# 접속하기
conn = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding="utf-8")
print(conn) 
# 커서 생성
cursor = conn.cursor()

# 파일 읽기
file1 = open('./resources/exam2.json')
# str to dict로 변경 > 파일을 변경해서 읽어줌
data1 = json.load(file1) # load는 파일 객체를 바꿔주는 거
# {"ID","aaa","PW":"34"}

sql = """
    INSERT INTO MEMBER(ID,PW,NAME,AGE,JOINDATE)
    VALUES(:ID, :PW, :NAME, :AGE, SYSDATE)
    """
cursor.execute(sql, data1)
conn.commit()
