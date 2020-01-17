# 웹에서 json파일을 가져오는 것

import requests
import json
import cx_Oracle as oci

conn = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding="utf-8")
print(conn) 
# 커서 생성
cursor = conn.cursor()
"""
{
   'ret' : {'id': 'a386', 'name': '123', 'age': 34},
   'ret1' : {'id': 'a386', 'name': '123', 'age': 36}

}
""" # 값을 그냥 보면서 하라고 하는 것

url = "http://ihongss.com/json/exam2.json"
str1 = requests.get(url).text
data1 = json.loads(str1) # loads => str로 된 객체를 dict로 바꿔주는 것str -> dict

ret = data1['ret'] # 딕셔너리에 있는 키값에 해당하는 밸류를 가져온다는 의미
# ret1 = data1['ret1']

sql = """
    INSERT INTO MEMBER(ID,PW,NAME,AGE,JOINDATE)
    VALUES(:ID, '2222', :NAME, :AGE, SYSDATE)
    """
cursor.execute(sql, ret)
conn.commit()

# print(type(ret1))
# print(ret1)



