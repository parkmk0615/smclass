students = []
s_title =['번호','이름','국어','영어','수학','합계','평균','등수']
choice = 0 # 전역변수
stuNo = 0 # 학생 번호  생성
chk = 0 # 체크
count = 1
 # 성적 처리 
stuNo = len(students) # 리스트에 학생이 있으면, 그 인원으로 변경
no = 0; name = ""; kor = 0 ;eng = 0; math =0; total=0; avg=0; rank=0 # 성적 처리 변수

while True:
  print("[ 학생 성적 프로그램 ]")
  print("-"*60) 
  print("1. 학생 성적 입력")
  print("2. 학생 성적 출력")
  print("3. 학생 성적 수정")
  print("4. 학생 성적 검색")
  print("5. 학생 성적 삭제")
  print("6. 등수 처리")
  print("0. 프로그램 종료")
  print("-"*60) 
  choice = input("원하는 번호를 입력 하세요 >> ")
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
      students.append([no,name,kor,eng,math,total,avg,rank])
      stuNo +=1 # 학생 수 증가
      print(f"{name} 학생의 성적이 저장 되었습니다")
      print()
  elif choice == "2":
    print("                      [ 학생 성적 출력 ]")
    # 상단 타이틀 출력
    for title in s_title:
      print(f"{title}\t", end='')
    print()
   # print(f"{s_title[0]}\t{s_title[1]}\t{s_title[2]}\t{s_title[3]}\t{s_title[4]}\t{s_title[5]}\t{s_title[6]}\t{s_title[7]}\n")
    print("-"*60)
    # 학생 출력
    for s in students:
      print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}")
    print()
  elif choice == "3":
    print("[ 학생 성적 수정 ]")
    name = input("찾고자 하는 학생의 이름을 입력하세요 ")
    chk = 0
    for s in students:
      if s[1] == name:
        # 학생 성적수정
        print(f"{name} 학생을 찾았습니다.")
        print()
        print("[ 수정 과목 선택 ]")
        print("1. 국어점수")
        print("2. 영어점수")
        print("3. 수학점수")
        choice = input("원하는 번호를 입력하세요 ")
        if choice == "1":
          print("이전 국어 점수:{}".format(s[2]))
          s[2] = int(input("국어 점수를 입력하세요 "))
        elif choice =="2":
          print("이전 영어 점수:{}".format(s[3]))
          s[3] = int(input("영어 점수를 입력하세요 "))
        elif choice =="3":
          print("이전 수학 점수:{}".format(s[4]))
          s[4] = int(input("수학 점수를 입력하세요 "))

        s[5] = s[2]+s[3]+s[4] # 합계
        s[6] = s[5]/3 # 평균

        print(f"{name} 학생의 성적이 수정 되었습니다.")
        print()
        # 학생출력
        # 상단 타이틀 출력
        for title in s_title:
          print(f"{title}\t", end='')
        print()
      # print(f"{s_title[0]}\t{s_title[1]}\t{s_title[2]}\t{s_title[3]}\t{s_title[4]}\t{s_title[5]}\t{s_title[6]}\t{s_title[7]}\n")
        print("-"*60)
        print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}")
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
      if s[1] == name:
      # 학생출력
      # 상단 타이틀 출력
        for title in s_title:
          print(f"{title}\t", end='')
        print()
      # print(f"{s_title[0]}\t{s_title[1]}\t{s_title[2]}\t{s_title[3]}\t{s_title[4]}\t{s_title[5]}\t{s_title[6]}\t{s_title[7]}\n")
        print("-"*60)
        print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}\n")
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
      if s[1] == name:
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
        if s[5] < st[5]:
          count += 1
      s[7] = count # 등수 입력
    print("등수 처리가 완료 되었습니다.")
    print()
 



  elif choice == "0":
    print("[ 프로그램 종료 ]")
    print("프로그램을 종료합니다")
    break