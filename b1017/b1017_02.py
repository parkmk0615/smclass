subject=["이름","국어","영어","수학","합계","평균"]
students=[]

# 함수선언
def stuScore_update(choice,k_title,s_title,s):
  print(f"현재  {k_title} 점수 ",s[s_title] )
  s[s_title] = int(input("변경 점수를 입력하세요"))
  print()





while True:
  print("1. 학생성적 입력")
  print("2. 학생성적 출력")
  print("3. 학생성적 수정")
  choice = input("원하는 번호를 입력하세요")
  if choice== "1":
    name = input("이름을 입력하세요 ")
    score=[] #국어, 영어, 수학
    sum=0
    for i in range(3):
      num = int(input(f"{subject[i+1]} 점수를 입력하세요 "))
      score.append(num)
      sum+=num
    avg=sum/len(score)
    s={"name":name,"kor":score[0],"eng":score[1],"math":score[2],"total":sum,"avg":avg}
    students.append(s)
  elif choice =="3":
    #students에서 찾고자 하는 이름
    serach = input("찾고자 하는 이름을 입력")
    for s in students:
      if s['name'] == serach:
        print("[수정 과목 선택]")
        print("1. 국어 2.영어 3.수학 0.이전화면이동")
        choice = int(input("원하는 번호를 입력하세요"))
      
        if choice == 1:
          stuScore_update(choice,subject[choice],"kor",s)
        elif choice ==2:
          stuScore_update(choice,subject[choice],"eng",s)
        elif choice ==3:
          stuScore_update(choice,subject[choice],"math",s)
        elif choice ==0:
          break


