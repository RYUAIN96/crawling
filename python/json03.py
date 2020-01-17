# 웹에 있는 여러 데이터를 읽어오기 -> 반복문을 돌린다

import requests
import json
import cx_Oracle as oci

conn = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding="utf-8")
print(conn) 
# 커서 생성
cursor = conn.cursor()


url = "http://ihongss.com/json/exam3.json"
str1 = requests.get(url).text
data1 = json.loads(str1) # str -> dict
# data1 => {ret:[{},{},{}]} , ret1:[{},{},{}]}
ret1 = data1['ret1'] # [{},{},{},{}] 꺼내면 이렇게 됨 => [A,B,C,D] 이런 모양
# A,B,C,D를 출력하기 위해 반복문을 돌리면 됨
for tmp in ret1: # 4번 수행
    print(tmp) # { id: "a2001", name: "123", age: 34} 
    sql="INSERT INTO MEMBER VALUES(:id,'aaa',:name,:age,SYSDATE)"
    cursor.execute(sql, tmp)

conn.commit()    