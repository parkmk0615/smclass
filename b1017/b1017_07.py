members=[]

m_title = ['id','pw','name','nicName','address','money']
f=open('b1017/member.csv',"r",encoding="utf-8")
while True:
  line = f.readline()
  if not line:
    break
  c=line.strip().split(",")
  c[5]=int(c[5])
  members.append(dict(zip(m_title,c)))
f.close()


while True:
  print("1. 회원 등록")
  print("2. 회원 검색")
  choice= input("원하는 번호를 입력하세요")
  
  if choice =='1':
    id = input("id를 입력하세요")
    flag=0
    for m in members:
      if m['id'] ==id:
        print(f"{id}는 동일한 아이디가 있습니다.")
        flag=1
        break
    if flag == 1:
      continue
    else:
      print(f"{id}는 사용 가능합니다.")
      print()
    pw = input("pw를 입력하세요")
    name = input("이름을 입력하세요")
    nicname=input("닉네임을 입력하세요")
    money=int(input("충전 금액을 입력하세요"))
    m_list=[id,pw,name,nicname,money]
    members.append(dict(zip(m_title,m_list)))
    print(f"{id}님 회원가입이 완료되었습니다.")
    print(m_list)
    print("-"*50)
    print(members) 

  elif choice =="2":
    search = input("검색할 회원이름")
    flag=0
    mm=[]
    for m in members:
      if m['id'].find(search) != -1:
        print("검색 회원을 찾았습니다.")
        mm.append(m)
        flag=1

    if flag==0:
      print("찾지못했습니다.")
    else:
      print("총 검색된 인원: ",len(mm))
      print(mm)





# 아이디 검색
# members의 리스트에서
# 입력한 문자로 검색된 데이터를 모두 출력하시오
# a가 들어가 있는 아이디 출력