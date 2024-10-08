students = []
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수']
no = 1
while True:
  print("[ 학생 성적 프로그램 ]")
  print("-"*60)
  print("1. 학생 성적 입력")
  print("2. 학생 성적 출력")
  print("3. 학생 성적 수정")
  print("4. 학생 성적 검색")
  print("5. 학생 성적 삭제")
  print("6. 등수처리")
  print("0. 프로그램 종료")
  print("-"*60)
  choice = input("원하는 번호를 입력하세요(0. 종료)")

  if choice == "1":
    while True:
      print("[ 학생 성적 입력 ]")
      name = input("이름을 입력하세요 ")
      if name=="0":
        print("이전 화면으로")
        break
      kor = int(input("국어 점수를 입력하세요"))
      eng = int(input("영어 점수를 입력하세요"))
      math = int(input("수학 점수를 입력하세요"))
      total = kor+eng+math
      avg=total/3
      rank=0
      print(f"{no}\t{name}\t{kor}\t{eng}\t{math}\t{total}\t{avg:.2f}\t{rank}")

      s=[no,name,kor,eng,math,total,avg,rank]
      students.append(s)
      no=no+1

  elif choice =="2":
    print("[ 학생 성적 출력 ]")
    for i in s_title:
      print(i,end='\t')
    print()
    print("-"*60)   
    for s in students:
      print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}")
    print()

  elif choice =="3":
    print("[ 학생 성적 수정 ]")
    
    name = input("수정할 학생 이름을 입력하세요 ")
    for s in students:
      if name == s[1]:
        print("학생을 찾았습니다.")
        print("1.국어점수")
        print("2.영어점수")
        print("3.수학점수")
        num = input("수정할 번호를 입력하세요")
        if num == "1":
          print("현재 국어 점수: {}".format(s[2]))
          s[2] = int(input("국어 점수를 입력하세요 "))
        elif num == "2":
          print("현재 영어 점수: {}".format(s[3]))
          s[3] = int(input("영어 점수를 입력하세요 "))
        elif num == "3":
          print("현재 수학 점수: {}".format(s[4]))
          s[4] = int(input("수학 점수를 입력하세요 "))
        elif num =="0":
          print("이전 화면으로")
          break
        s[5] = s[2]+s[3]+s[4]
        s[6] = s[5]/3
      
  elif choice =="4":
    print("[ 학생 성적 검색 ]")
    name = input("찾고자 하는 학생 이름을 입력하세요 ")
    count=0
    for s in students:
      if name == s[1]:
        print("학생을 찾았습니다.")
        for i in s_title:
          print(i,end="\t")
        print()
        print("-"*60)
        print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]}\t{s[7]}\t")
        print()
        print("-"*60)
        count=1
        break
    if count == 0:
      print("학생을 찾지 못했습니다.")
  

