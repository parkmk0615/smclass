stu_title = ['국어','영어','수학']
students = {"국어":100,"영어":100,"수학":99,'합계':299}

def modify(choice):
  print("{} 점수 : {}".format(stu_title[choice-1],students[stu_title[choice-1]]))
  students[stu_title[choice-1]] =int(input(f"변경하려는 {stu_title[choice-1]} 점수 입력"))

print("점수 수정")
print("1.국어")
print("2.영어")
print("3.수학")
print("수정하려는 과목을 선택 ")

choice = int(input("숫자 입력"))

if choice ==1:
  modify(choice)
  

elif choice ==2:
  modify(choice)
  

elif choice ==3:
  modify(choice)
 

students["합계"] = students["국어"]+students["영어"]+students['수학']
print("변경: ",students)