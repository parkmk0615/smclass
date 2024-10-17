import datetime
import os
members = []
m_title = ['id','pw','name','nicName','address','money']
#### member.csv파일 불러오기
f = open('b1017/member.csv',"r",encoding="utf-8")
while True:
  line = f.readline()
  if not line: break
  # c리스트 저장
  c = line.strip().split(",")
  c[5] = int(c[5])  # money
  # members리스트에 딕셔너리 저장
  members.append(dict(zip(m_title,c)))
f.close()
#-----------------------------
# cart.txt파일 읽기, member딕셔너리 저장
cartNo = 0
cart = []
c_keys = ["cno","id","name","pCode","pName","price","date"]
# isfile : 파일인지확인, isdir : 디렉토리인지 확인, exists : 파일이 존재하는지 확인
if os.path.exists("b1017/cart.txt"):
  f = open('b1017/cart.txt','r',encoding='utf-8')
  while True:
    line = f.readline()
    if not line: break
    c = line.strip().split(",")
    c[0] = int(c[0])
    c[5] = int(c[5])
    cart.append(dict(zip(c_keys,c)))
  f.close()
#-----------------------------------------
# 함수
def buy(chocie):
  print("TV 상품을 구매하였습니다.")
  print()
  session_info['money'] = session_info['money']-product[choice-1]['price']
  print("현재 남은 잔액: ",session_info['money'])

# 파일 저장해서 불러오기
product = [
  {"pno":1,"pCode":"t001","pName":"삼성TV","price":2000000,"color":"black"},
  {"pno":2,"pCode":"g001","pName":"LG냉장고","price":3000000,"color":"white"},
  {"pno":3,"pCode":"h001","pName":"하만카돈스피커","price":500000,"color":"gray"},
  {"pno":4,"pCode":"w001","pName":"세탁기","price":1000000,"color":"yellow"}
]
f= open("b1017/product.txt","w",encoding="utf-8")
line = f.readline()
print(line.strip())

session_info = {}
p_title = ["번호","아이디","이름","코드","상품명","가격","구매일자"]
#####  프로그램 시작  #####
while True:
  print("[ 메인화면 ]")
  print("1. 로그인")
  print("2. 회원가입")
  print("0. 프로그램 종료")
  print("-"*30)
  choice = input("원하는 번호를 입력하세요.>>")
  if choice == "1":
    # 프로그램 구현
    flag=0
    id = input("아이디를 입력하세요")
    pw = input("비밀번호를 입력하세요")
    for i in members:
      if i['id']==id and i['pw'] == pw:
        print("로그인에 성공하셨습니다.")
        session_info = i
        flag=1
        break
    if flag==0:
      print("로그인에 실패했습니다.")
    else:
      break

  elif choice == "2":
    flag=0
    input_id = input("아이디를 입력하세요.>> ")
    input_pw = input("패스워드를 입력하세요.>> ")
    for m in members:
      if m['id']==input_id:
        print("동일한 아이디가 있습니다.")
        flag=1
        break
    if flag==1:
      continue
    else:
      print(f"{input_id}는 사용 가능합니다.")
      print()

    name = input("이름을 입력하세요")
    nicname = input("닉네임을 입력하세요")
    address = input("주소를 입력하세요")
    money = int(input("충전 금액을 입력하세요"))
    
    m_list=[input_id, input_pw, name, nicname, address, money]
    members.append(dict(zip(m_title,m_list)))
    print(f"{id}님 회원가입이 완료되었습니다.")
    print(m_list)
    print("-"*50)
    print(members)
    # 프로그램 구현
  elif choice == "0":
    print("프로그램을 종료합니다.")
    break




# 프로그램을 구현하시오.
while True:
  print("           [ SM-SHOP ]")
  print(f"                       닉네임:{session_info['nicName']}님")
  print(f"                       금액 :{session_info['money']:,} 원")
  print("1. 삼성TV - 2,000,000")
  print("2. LG냉장고 - 3,000,000")
  print("3. 하만카돈스피커 - 500,000")
  print("4. 세탁기 - 1,000,000")
  print("7. 내용저장")
  print("8. 구매내역 ")
  print("9. 금액충전 ")
  choice = int(input("구매하려는 상품번호를 입력하세요.>> "))
  # 프로그램 구현


  if choice == 1:
    buy(choice)
  elif choice == 2:
    buy(choice)
  elif choice == 3:
    buy(choice)
  elif choice == 4:
    buy(choice)