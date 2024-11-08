students = []
no = 1
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수']
# 학생  
while True:
  print("[  학생 성적 프로그램 ]")
  print("-"*60)
  print("0. 프로그램 종료")
  print("1. 학생 성적 입력")
  print("2. 학생 성적 출력")
  print("3. 학생 성적 수정")
  print("4. 학생 성적 검색")
  print("5. 학생 성적 삭제")
  print("6. 등수 처리")
  print("-"*60)
  choice= input("원하는 번호를 입력하세요: (종료: 0)")

  if choice == '1':
    while True:
      print("[ 학생 성적을 입력합니다. ]")
      name = input(f"{no}번째 이름을 입력하세요: (메인 메뉴 이동 : 0)")
      if name == '0':
        print("메인메뉴로 이동합니다.")
        break
      kor = int(input("국어 점수를 입력하세요: "))
      eng = int(input("영어 점수를 입력하세요: "))
      math = int(input("수학 점수를 입력하세요: "))
      total = kor+eng+math
      avg=total/3
      rank=0
      print(f"{no}\t{name}\t{kor}\t{eng}\t{math}\t{total}\t{avg:.2f}\t{rank}")

      s=[no,name,kor,eng,math,total,avg,rank]
      students.append(s)
      no=no+1
     

  elif choice == '2':
    print("[ 학생 성적을 출력합니다. ]")
    # 찾은 학생의 데이터 출력
    # 상단 출력
    for st in s_title:
      print(st,end='\t')
    print()
    print("-"*60)
    # 학생 성적 출력
    for s in students:
      print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}")
      print()


  elif choice == '3':
    print("[ 학생 성적 수정 ]")
    name = input("수정 하는 학생 이름을 입력하세요 ")

    count =0
    for s in students:
      if name == s[1]:
        print(f"{name} 학생을 찾았습니다.")
        print("[과목선택]")
        print("1. 국어점수")
        print("2. 영어점수")
        print("3. 수학점수")
        print("0. 성적수정안함")
        choice = input("숫자를 입력하세요")

        if choice == '1':
          s[2] = int(input("국어 점수를 변경 하세요"))
        elif choice == '2':
          s[3] = int(input("영어 점수를 변경 하세요"))
        elif choice == '3':
          s[4] = int(input("수학 점수를 변경 하세요"))
        elif choice == '0':
          print("성적수정을 취소합니다.")
          count=1
        if choice != '0':
          s[5] = s[2]+s[3]+s[4]
          s[6] = s[5]/3
          print(f"{name} 학생의 성적을 변경 하였습니다.")
         
      # 없을 경우
      if count == 0:
        print("수정하고자하는 학생 이름이 없습니다.")
        print()


  elif choice == '4':
    print("[ 학생 성적 검색 ]")
    name = input("찾고자 하는 학생 이름을 입력하세요 ")

    count = 0
    for s in students:
      if name == s[1]:
        print(f"{name} 학생을 찾았습니다.")
        # 찾은 학생의 데이터 출력
        # 상단 출력
        for st in s_title:
          print(st, end='\t')
        print()
        print("-"*60)
        # 학생 성적 출력
        print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]}\t{s[7]}")
        print()
        count = 1
        break
    if count == 0:
      print("찾고자 하는 학생이 이름이 없습니다.")
      print()

  elif choice == '5':
    print("[ 학생 성적 삭제 ]")
    name = input("삭제 하려는 학생 이름을 입력하세요 ")

  elif choice == '0':
    print("프로그램을 종료합니다")
    break