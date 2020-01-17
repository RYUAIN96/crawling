# 파일명 : flask01.py


from flask import Flask, render_template, request, redirect

import cx_Oracle as oci # pip install cs_oracle

# 아이디/암호@서버주소:포트번호/SID
conn = oci.connect('admin/1234@192.168.99.100:32764/xe' , encoding="utf-8")
cursor = conn.cursor()


app = Flask(__name__)

@app.route("/")
def index():
    sql = "SELECT * FROM MEMBER"
    cursor.execute(sql)
    data = cursor.fetchall() # [(   ),(   ),(   )]
    return render_template('list.html', list=data)
    print(type(data))
    print(data)
 
    # for tmp in data:
    #     print(tmp[3])

    # return "index page"

@app.route("/join", methods=['GET']) # 화면 페이지 만드는 방법
def join():
    return render_template('join.html') #뒤에 적혀있는 것을 들고와서 보여주라는 의미

@app.route("/join", methods=['POST']) # 화면 페이지 만드는 방법
def join_post():
    a = request.form['id']
    b = request.form['pw']
    c = request.form['name']
    d = request.form['age']
    # print("{}:{}:{}:{}".format(a,b,c,d))
    sql = "INSERT INTO MEMBER VALUES(:id, :pw, :na, :ag, SYSDATE)"
    cursor.execute(sql, id=a, pw=b, na=c, ag=d)
    conn.commit()

    # 오라클 DB접속
    # 추가하는 SQL문 작성 => INSERT, SELECT, UPDATE, DELETE
    # SQL문 수행
    
    return redirect('/') # 127.0.0.1:5000 IP주소는 생략되어있고 /다음에 있는 부분으로 돌아가게끔 해줌
    # 크롬에서 주소를 입력한 것처럼 동작시켜 -> 자동화

@app.route("/login", methods=['GET'])
def login_post():
    print("login-post")
    return render_template('login.html')

print(__name__)

if __name__ == '__main__':
    app.run(debug=True) # 소스가 변경될 때마다 알아서 구동시키기