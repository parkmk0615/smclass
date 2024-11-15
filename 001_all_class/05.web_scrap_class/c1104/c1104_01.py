# 학생성적 프로그램 
# 1. 학생 성적 입력
# 2. 학생 성적 출력
# 3. 학생 성적 검색
# students 테이블 사용
# 시퀀스 students_seq 생성
# 번호, 김유신 99,98,96, 합계 평균 등수  입력
###


import oracledb

# db접속
def connects():
  user="ora_user"
  password="1111"
  dsn="localhost:1521/xe"
  try:
    conn = oracledb.connect(user=user,password=password,dsn=dsn)
  except Exception as e:
    print("예외처리 : ",e)
  return conn

while True:
  print("[학생 성적 프로그램]")
  print("1.학생성적입력")
  print("2.학생성적출력")
  print("3.학생성적검색")
  print("0.프로그램 종료")
  choice =input("원하는 번호를 입력하세요 >>")

  if choice =="1":
    conn=connects()
    cursor=conn.cursor()
    print("[학성성적을 입력하세요]")
    sql="select sutudents_seq.currval from dual"
    cursor.execute(sql)
    row=cursor.fetchone()
    no=row[0]
    name=input(f"{no}번 학생 이름을 입력하세요 >> ")
    kor=int(input("국어 성적을 입력하세요 >> "))
    eng=int(input("영어 성적을 입력하세요 >> "))
    math=int(input("수학 성적을 입력하세요 >> "))
  elif choice =="2":
    pass
  elif choice =="3":
    pass
  elif choice =="0":
    print("프로그램 을 종료 합니다")
    break