# 웹이아닌 파이썬으로 디비랑 연동하는 방법

#pip install cx_oracle 모듈 설치
import cx_Oracle as oci

# 접속하기(아이디/암호@서버주소:포트번호/SID)

conn = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding="utf-8")
print(conn) # 확인

# 커서 생성
cursor = conn.cursor()

# SELECT
sql = "SELECT * FROM MEMBER"
cursor.execute(sql)
data = cursor.fetchall() # [ (),(),() ]
print(data)

sql = """
    INSERT INTO MEMBER(ID,PW,NAME,AGE,JOINDATE)
    VALUES(:1, :2, :3, :4, SYSDATE)
    """
# :1 => 에서 콜론은 %s가 안 먹혀서 :으로 사용!    

arr = ['a4', 'a4', '류', 25 ] # 아이디랑 비번이 같을 수 없어서 다른 값 넣어주기
cursor.execute(sql, arr)
conn.commit()

