# 학생성적 프로그램 
# 1. 학생 성적 입력
# 2. 학생 성적 출력
# 3. 학생 성적 검색
# students 테이블 사용
# 시퀀스 students_seq 생성
# 번호, 김유신 99,98,96, 합계 평균 등수  입력
###

import oracledb
def connects():
  user="ora_user"
  password="1111"
  dsn="localhost:1521/xe"
  try:
    conn = oracledb.connect(user=user,password=password,dsn=dsn)
  except Exception as e:
    print("예외처리 : ",e)
  return conn

print("1. 학생 성적 입력")
print("2. 학생 성적 출력")
print("3. 학생 성적 검색")

choice = input("번호를 입력하세요")

if choice == "1":
  print("[ 학생성적 입력 ]")
  no=6
  name = input("이름을 입력하세요")
  kor = int(input("국어점수를 입력하세요"))
  eng = int(input("영어점수를 입력하세요"))
  math = int(input("수학점수를 입력하세요"))
  total =kor+eng+math
  avg=total/3
  

  conn=connects()
  cursor=conn.cursor()
  sql="insert into students values(students_seq.nextval,:name,:kor,:eng,:math,:total,:avg,1,sysdate)"
  cursor.execute(sql,name=name,kor=kor,eng=eng,math=math,total=total,avg=avg)
  conn.commit()
  conn.close()

  print("학생 성적이 저장되었습니다.")

elif choice =='2':
  print("[ 학생 성적 출력 ]")
  conn=connects()
  cursor=conn.cursor()
  sql="select no,name,kor,eng,math,total,avg,rank,sdate from students order by no asc"
  cursor.execute(sql)
  rows=cursor.fetchall()
  
  for row in rows:
    print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\t{row[6]:.2f}\t{row[7]}\t{row[8]}\t") 
  conn.close()

elif choice=='3':
  print("[ 학생 성적 검색 ]")

  name=input("이름을 입력하세요")

  conn=connects()
  cursor=conn.cursor()
  sql="select no,name,kor,eng,math,total,avg,rank,sdate from students where name=:name order by no asc"
  cursor.execute(sql,name=name)
  row=cursor.fetchone()
  print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\t{row[6]:.2f}\t{row[7]}\t{row[8]}\t") 



