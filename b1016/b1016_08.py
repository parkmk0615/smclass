# sm shop
member=[]
m_keys = ['id','pw','name','nicName','address','money']

product = [
  {"pno":1,"pCode":"t001","pName":"삼성TV","price":2000000,"color":"black"},
  {"pno":2,"pCode":"g001","pName":"LG냉장고","price":3000000,"color":"white"},
  {"pno":3,"pCode":"h001","pName":"하만카돈스피커","price":500000,"color":"gray"},
  {"pno":4,"pCode":"w001","pName":"세탁기","price":1000000,"color":"yellow"},
]


###########################
def buy():
  print(f"{product[choice-1]['pName']}을 구매 하셨습니다.")
  print()


###########################

f = open("member.txt","r",encoding='utf-8')
while True:
  line = f.readline()
  if not line: 
    break
  m = line.strip().split(",")
  m[5] = int(m[5]) # 금액
  member.append(dict(zip(m_keys,m)))



while True:
  id=input("아이디를 입력하세요")
  pw=input("비밀번호를 입력하세요")
  flag=0
  for i in member:
    if id == i['id'] and pw == i['pw']:
      print("로그인 성공")
      flag=1
      break
  if flag == 0:
    print('로그인 실패')
  else:
    break

  

while True:  
  print("1. 티비 - 1,000,000")
  print("2. 냉장고 - 2,000,000" )
  print("3. 스피커 - 3,000,000")
  print("4. 청소기 - 4,000,000")
  print()
  print("현재 금액: ")
  choice = int(input("구매할 번호를 입력하세요: "))
  if choice == 1:
    buy()