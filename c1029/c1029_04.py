# employees 테이블에서 이름이 'a'가 포함되어 있는 이름, 모든 컬럼 출력
import oracledb

#db연결 함수선언
def connections():
  try:
    conn = oracledb.connect(user="ora_user",password="1111",dsn='localhost:1521/xe')
  except Exception as e:
    print("예외 발생: ",e)
  return conn

# 함수호출
conn = connections()

# sql 창이 열림
cursor=conn.cursor()


# 월급이 4000~8000사이의 사원을 모두 출력하시오
salary1=input("값을 입력하세요")
salary2=input("값을 입력하세요")

sql="select employee_id,emp_name,salary from employees where salary between :num1 and :num2 order by salary asc"
cursor.execute(sql,num1=salary1,num2=salary2)





# sql작성, 실행
# sql=f"select * from employees where emp_name like '%{name}%'"
# 키워드
# sql="select * from employees where employee_id >=:name"
# 번호순서
# sql="select * from employees where employee_id >=:1"
# 입력한 값을 가지고 이름이 포함되어 있는 데이터를 출력하시오
# name=input("이름의 일부를 입력하세요 ")
# name='%'+name+'%'
# sql="select * from employees where emp_name like :name"
# cursor.execute(sql,name=name)

title=["employee_id","emp_name","salary"]
a_list=[]

rows=cursor.fetchall()
for row in rows:
  for idx, i in enumerate(row):
    print(i,end="\t")
  print()

for i in rows:
  a_list.append(dict(zip(title,i)))
print(a_list)