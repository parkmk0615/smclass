# email 발송관련
import random
import smtplib
from email.mime.text import MIMEText
import oracledb



# 시작화면 함수 선언
def screen():
  print("[ 커뮤니티 ]")
  print("1. 로그인")
  print("2. 비밀번호 찾기")
  print("3. 회원가입")
  print("4. 프로그램 종료")
  
  choice = input("원하는 번호를 입력하세요 : ")
  return choice

# 1. 로그인 함수 선언
def memlogin():
  user_id = input("아이디를 입력하세요")
  user_pw = input("비밀번호를 입력하세요")
  # db 접속
  conn = connects()
  cursor = conn.cursor()
  sql = "select * from member where id = :id and pw = :pw"
  cursor.execute(sql,id=user_id,pw=user_pw)
  row=cursor.fetchone()
  cursor.close()  
  if row == None:
    print("아이디 또는 패스워드가 일치하지 않습니다. 다시 입력하세요 ")
    return 

  # 이후 프로그램 구성
  print(f"{row[2]}님 환영합니다.")
  print()



# 2. 비밀번호 찾기 함수선언
def search_pw():
  user_id = input("아이디를 입력하세요 ")
  conn = connects()
  cursor = conn.cursor()
  sql = "select * from member where id = :id"
  cursor.execute(sql,id=user_id,)
  row=cursor.fetchone()

  if row == None:
    print("아이디가 존재하지 않습니다. ")
    return

  input(f"{row[0]} 아이디가 존재합니다. 메일을 보내려면 enter를 입력하세요")
  print("이메일 : ",row[3])
  
  #####이메일 발송 함수 호출########
  ran_num = emailsend(row[3])
  #######################################

  # 임시 비밀번호 업데이트
  sql ="update member set pw = :pw where id = :id"
  cursor.execute(sql,pw=ran_num, id=user_id)
  conn.commit()



# db연결 함수 선언
def connects():
  user = "ora_user"
  password ="1111"
  dsn = "localhost:1521/xe"
  try:
    conn = oracledb.connect(user=user,password=password,dsn=dsn)
  except Exception as e:
    print("예외처리 : ",e)
  return conn




# 랜덤 비밀번호 함수 선언
def random_pw():
  a = random.randrange(0,10000) # 0-9999
  ran_num=f"{a:04}"
  print("랜덤번호 : ",ran_num)
  return ran_num




# 메일발송 함수선언
def emailsend(email):
  # email 발송
  smtpname = "smtp.naver.com"
  smtpport = 587

  sendemail ="parkmk0615@naver.com"
  pw="f1063412@"
  recvemail = email

  title = "[ 메일 발송 ] 임시번호 안내"
  # random_pw = random_pw()
  a = random.randrange(0,10000) # 0-9999
  ran_num=f"{a:04}"
  print("랜덤번호 : ",ran_num) 

  # 설정
  content = f"임시 비밀번호: {ran_num}"
  print("content random_pw : ",content)
  msg = MIMEText(content)
  msg['Subject'] = title
  msg['From'] = sendemail
  msg['To'] = recvemail

  # 서버이름, 서버포트
  s= smtplib.SMTP(smtpname,smtpport)
  s.starttls()
  s.login(sendemail,pw)
  s.sendmail(sendemail,recvemail,msg.as_string())
  s.quit()

  # 메일 발송 완료
  print("메일이 발송 되었습니다.")

  return ran_num


