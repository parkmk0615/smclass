# 학생 성적 출력
import oracledb

# sql developer 실행
conn=oracledb.connect(user="ora_user",password='1111',dsn='localhost:1521/xe')

# sql 창이 열림
cursor=conn.cursor()

# sql작성, 실행
# no가 10,20,30을 검색해서 출력하시오
num1 = input("숫자를 입력하세요 ")
num2 = input("숫자를 입력하세요 ")
num3 = input("숫자를 입력하세요 ")

# excute 함수: 변수 추가
# excute 뒤에는 딕셔너리, 리스트, 튜플 타입만 가능
##sql=f"select * from students where no >= {num}"
sql="select * from students where no in (:no,:na,:nu)"
cursor.execute(sql,no=num1,na=num2,nu=num3)

# 데이터 가져오기 - fetchone(): 1개, fetchmany(10): 정해진 숫자 10만큼가져오기, fetchall(): 모든 데이터 가져오기
rows = cursor.fetchall()

titles=['번호','이름','국어','영어','수학','합계','평균','등수','등록일']

for idx,title in enumerate(titles):
  if idx == 1:
    print(title,end="\t\t")
    continue
  print(title,end="\t")
print()
print("-"*80)

for row in rows:
  for i,r in enumerate(row):
    if i==1:
      print(f"{r:10s}",end="\t")
      continue
    if i==6:
      print(f"{r:.2f}",end="\t")
      continue
    if i == 8:
      print(r.strftime("%y-%m-%d"),end="\t")
      continue
    print(r,end="\t")
  print()