# students 리스트 타입
students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]
stuNo = len(students)+1  # 학생번호 생성
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] #전역변수
choice = 0 # 전역변수
chk = 0    # 체크변수
count = 1  # 성적처리
stuNo = len(students)  # 리스트에 학생이 있으면, 그 인원으로 변경
no=0;name="";kor=0;eng=0;math=0;total=0;avg=0;rank=0 #성적처리변수

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

  if choice == "1":
    while True:
      print("[ 학생 성적 입력 ]")
      # 학생 성적 직접 입력
      no = stuNo + 1 # 리스트 - 학생 수
      name = input(f"{no}번째 학생 이름을 입력하세요(0. 이전 화면) ")
      if name == "0":
        print("성적 입력을 취소합니다")
        print()
        break
      kor = int(input("국어 점수를 입력하세요"))
      eng = int(input("영어 점수를 입력하세요"))
      math = int(input("수학 점수를 입력하세요"))
      total = kor+eng+math
      avg=total/3
      rank=0
      ss={"no":no,"name":name,"kor":kor,"eng":eng,"math":math,"total":total,"avg":avg,"rank":rank}
      students.append(ss)
      stuNo +=1 # 학생 수 증가
      print(f"{name} 학생의 성적이 저장 되었습니다")
      print()

  elif choice =="2":
    print("[ 학생 성적 출력 ]")
    for i in s_title:
      print(i,end='\t')
    print()
    print("-"*60)   
    for s in students:
      print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
    print()

  elif choice == "3":
    print("[ 학생 성적 수정 ]")
    name = input("찾고자 하는 학생의 이름을 입력하세요 ")
    chk = 0
    for s in students:
      if s["name"] == name:
        # 학생 성적수정
        print(f"{name} 학생을 찾았습니다.")
        print()
        print("[ 수정 과목 선택 ]")
        print("1. 국어점수")
        print("2. 영어점수")
        print("3. 수학점수")
        choice = input("원하는 번호를 입력하세요 ")
        if choice == "1":
          print("이전 국어 점수:{}".format(s["kor"]))
          s["kor"] = int(input("국어 점수를 입력하세요 "))
        elif choice =="2":
          print("이전 영어 점수:{}".format(s["eng"]))
          s["eng"] = int(input("영어 점수를 입력하세요 "))
        elif choice =="3":
          print("이전 수학 점수:{}".format(s["math"]))
          s["math"] = int(input("수학 점수를 입력하세요 "))

        s["total"] = s["kor"]+s["eng"]+s["math"] # 합계
        s["avg"] = s["total"]/3 # 평균

        print(f"{name} 학생의 성적이 수정 되었습니다.")
        print()
        # 학생출력
        # 상단 타이틀 출력
        for title in s_title:
          print(f"{title}\t", end='')
        print()
      # print(f"{s_title[0]}\t{s_title[1]}\t{s_title[2]}\t{s_title[3]}\t{s_title[4]}\t{s_title[5]}\t{s_title[6]}\t{s_title[7]}\n")
        print("-"*60)
        print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
        print()
        chk =1
    # 모든 학생 비교가 끝난 이후, chk 확인
    if chk == 0:
      print(f"{name} 학생이 없습니다. 다시 입력하세요") 
    print()

  elif choice == "4":
    print("[ 학생 성적 검색 ]")
    name = input("찾고자 하는 학생의 이름을 입력하세요 ")
    chk = 0
    for s in students:
      if s["name"] == name:
      # 학생출력
      # 상단 타이틀 출력
        for title in s_title:
          print(f"{title}\t", end='')
        print()
      # print(f"{s_title[0]}\t{s_title[1]}\t{s_title[2]}\t{s_title[3]}\t{s_title[4]}\t{s_title[5]}\t{s_title[6]}\t{s_title[7]}\n")
        print("-"*60)
        print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
        print()
        chk =1
    # 모든 학생 비교가 끝난 이후, chk 확인
    if chk == 0:
      print(f"{name} 학생이 없습니다. 다시 입력하세요") 

  elif choice == "5":
    print("[ 학생 성적 삭제 ]")
    name = input("찾고자 하는 학생의 이름을 입력하세요 ")
    chk = 0
    for idx,s in enumerate(students):
      if s["name"] == name:
        chk =1
        choice = input(f"{name} 학생 성적을 삭제하시겠습니까?(삭제 복구불가)\n1.삭제 2.취소")
        if choice == "1":
          del students[idx]
          print(f"{name} 학생 성적이 삭제 되었습니다")
        else:
          print("학생 성적 삭제가 취소 되엇습니다.")
          break

    # 모든 학생 비교가 끝난 이후, chk 확인
    if chk == 0:
      print(f"{name} 학생이 없습니다. 다시 입력하세요") 

  elif choice == "6":
    print("[ 등수 처리 ]")
    for s in students:
      count = 1
      for st in students:
        if s["total"] < st["total"]:
          count += 1
      s["rank"] = count # 등수 입력
    print("등수 처리가 완료 되었습니다.")
    print()

  elif choice == "7":
    while True:
      print("[ 학생 성적 정렬 ]")
      print("1. 이름 오름차순 정렬")
      print("2. 이름으로 내림차순 정렬")
      print("3. 합계 오름차순 정렬")
      print("4. 합계 내림차순 정렬")
      print("5. 번호 오름차순 정렬")
      print("0. 이전 페이지")
      print("-"*40)
      choice = input("원하는 번호를 입력하세요 ")

      if choice == "1":
        students.sort(key=lambda x:x['name'])
      elif choice =="2":
        students.sort(key=lambda x:x['name'],reverse=True)
      elif choice == "3":
        students.sort(key=lambda x:x['total'])  
      elif choice == "4":
        students.sort(key=lambda x:x['total'],reverse=True)  
      elif choice =="0":
        break
      print("정렬이 완료 되었습니다.")

  elif choice == "0":
    print("프로그램을 종료합니다")
  break









# 
# 학생 성적 입력 부분을 구현
# dic타입으로 입력을 할 것
# 번호 이름 국어 영어 수학 합계 평균 등수
# 입력이 완료되면 출력이 바로 되도록

# students =[]
# stu={}
# stu["no"]=input("번호를 입력하세요 ")
# stu["name"]=input("이름 입력하세요 ")
# stu["kor"]=int(input("국어 입력하세요 "))
# stu["eng"]=int(input("영어 입력하세요 "))
# stu["math"]=int(input("수학 입력하세요 "))
# stu["total"]=stu["kor"]+stu["eng"]+stu["math"]
# stu["avg"]= stu["total"]/3
# stu["rank"]=0
# students.append(stu)
# print(students)