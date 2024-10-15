# students 리스트 타입
students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] #전역변수
choice = 0 # 전역변수
chk = 0    # 체크변수
count = 1  # 성적처리
stuNo = len(students)  # 리스트에 학생이 있으면, 그 인원으로 변경
no=0;name="";kor=0;eng=0;math=0;total=0;avg=0;rank=0 #성적처리변수

# 학생 성적 입력 함수
def stu_input(stuNo):
  while True:
    print("[ 학생 성적 입력 ]")
    no=stuNo+1
    name=input(f"{no}번째 이름을 입력하세요")
    if name=='0':
      print("이전화면으로")
      break
    kor=int(input("국어점수"))
    eng=int(input("영어점수"))
    math=int(input("수학점수"))
    total=kor+eng+math
    avg=total/3
    rank=0

    ss={"no":no,"name":name,"kor":kor,"eng":eng,"math":math,"total":total,"avg":avg,"rank":rank}
    students.append(ss)
    stuNo+=1

    print(f"{name}학생이 저장되었습니다.")
    print()
    return stuNo

# 학생성적출력 함수
def stu_output(stuNo):
  print("[ 학생성적 출력 ]")
  print()
  
  for s in s_title:
    print(s,end='\t')
  print()
  print("-"*60)

  for s in students:
    print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
  print()

# 학생성적수정 함수
def stu_update(stuNo):
  print("[ 학생 성적 수정 ]")
  flag=0
  name = input("이름을 입력하세요 ")
  for s in students:
    if name == s['name']:
      print("학생을 찾았습니다.")
      flag=1
      print("1.국어점수변경")
      print("2.영어점수변경")
      print("3.수학점수변경")
      choice =input("숫자를 입력하세요 ")
      if choice == '1':
        s['kor']=int(input("국어 점수를 입력하세요 "))
      elif choice =='2':
        s['eng']=int(input("영어 점수를 입력하세요 "))
      elif choice =='3':
        s['math']=int(input("수학 점수를 입력하세요 "))
      
      s['total']=s['kor']+s['eng']+s['math']
      s['avg']=s['total']/3
      
      print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")

    if flag==0:
      print("학생을 찾지 못했습니다. ")
      
# 학생성적검색 함수
def stu_select(stuNO):
  flag=0
  name = input("이름을 입력하세요 ")
  for s in students:
    if name == s['name']:
        print("학생을 찾았습니다.")
        flag=1
        print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")

  if flag==0:
    print("학생을 찾지 못했습니다. ")


#------------------------------------------
while True:
  print("[ 학생성적프로그램 ]")
  print("-"*60)
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적수정")
  print("4. 학생성적검색")
  print("5. 학생성적삭제")
  print("6. 등수처리")
  print("7. 학생성적정렬")
  print("0. 프로그램 종료")
  print("-"*60)
  choice = input("원하는 번호를 입력하세요.(0.종료)>> ")

  if choice == '1':
    stu_input(stuNo)

  elif choice== '2':
    stu_output(stuNo)
  elif choice== '3':
    stu_update(stuNo)
  elif choice== '4':
    stu_select(stuNo)
  elif choice== '5':
    pass
  elif choice== '6':
    pass