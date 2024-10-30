import oracledb
import random
# email 발송관련
import smtplib
from email.mime.text import MIMEText
smtpName = "smtp.naver.com"
smtpPort = 587


def connects():
  user="ora_user"
  password = "1111"
  dsn = "localhost:1521/xe"
  try:
    conn = oracledb.connect(user=user, password=password, dsn=dsn)
  except Exception as e:
    print("예외 발생 :",e)
  return conn


while True:
  print("[ 커뮤니티 ]")
  print("1.로그인")
  print("2.비밀번호 찾기")
  print("3.회원가입")
  print("0.프로그램 종료")
  print("-"*50)
  choice= input("원하는 번호를 입력하세요 ")

  if choice == "1" :
    print("[ 로그인 ]")
    user_id = input("아이디를 입력하세요")
    user_pw = input("비밀번호를 입력하세요")
    # db접속
    conn = connects()
    cursor = conn.cursor()
    sql="select * from member where id=:id and pw=:pw"
    cursor.execute(sql,id=user_id,pw=user_pw)
    row=cursor.fetchone()
    #print(row)
    if row != None:
      print(f"로그인 성공! {row[2]}님 환영합니다.")
    else:
      print("아이디 또는 패스워드가 일치하지 않습니다.")
    cursor.close()


    # 오라클 db 접속, member 테이블에서 검색 후 가져오기
    
    # if user_id == 'aaa' and uesr_pw == '1111':
    #   print("로그인 성공")
    # else:
    #   print("로그인 실패" )
    #   continue

    print("[ 학생 성적 프로그램에 접속 ]")
    ### 프로그램 구형 ###

  elif choice == "2":
    print("[ 비밀번호 찾기 ]")
    
    search=input("아이디를 입력하세요 ")
    
    # 아이디가 존재하는지 확인
    conn = connects()
    cursor = conn.cursor()
    sql ="select * from member where id = :id"
    cursor.execute(sql,id=search)
    row = cursor.fetchone()
    
    if row!= None:
      print("아이디가 존재합니다. 임시 패스워드를 발급합니다.")
      # 임시 비밀번호를 생성
      # 이메일로 보냅니다.
      # 아이디에 비밀번호를 임시 비밀번호로 수정
      # 임시 번호로 로그인이 나오도록
    
      a = random.randrange(0,10000) # 0-9999
      ran_num = f"{a:04}"
      # 랜덤 4자리 숫자
      print(ran_num)

      
      
      # 자신의 네이버메일주소,pw, 받는사람이메일주소
      sendEmail = "parkmk0615@naver.com"
      pw = "@@@@@@"
      recvEmail="parkmk0615@naver.com"
      title="임시 비밀번호"
      content=f"임시비밀번호 {ran_num}"

      # 설정
      msg = MIMEText(content)
      msg['Subject'] = title
      msg['From'] = sendEmail
      msg['To'] = recvEmail
      print("msg 데이터 : ",msg.as_string())

      #서버이름
      s = smtplib.SMTP(smtpName,smtpPort)
      s.starttls()
      s.login(sendEmail,pw)
      s.sendmail(sendEmail,recvEmail,msg.as_string())
      s.quit()

      # 메일 발송 완료
      print("발송 완료")

      # 입력
      user_id = search
      user_pw = ran_num 
      # 데이터 수정
      sql="update member set pw = :pw where id = :id"
      cursor.execute(sql,id=user_id,pw=user_pw)
      conn.commit()

      print("파일이 수정 되었습니다.")
      cursor.close()

    else:
      print("아이디가 존재하지 않습니다.")
      cursor.close()
  



  elif choice == "3":
    pass  
  elif choice == "0":
    print("프로그램 종료")
    break