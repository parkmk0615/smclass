def stuinput(stuno,students):
  while True:
    no=stuno+1
    print("no: ",no)
    name=input(f"{no}번째 학생 이름을 입력하세요 (0. 이전페이지로 이동)")
    students.append({"no":no,"name":name})
    print(students)
    stuno+=1
    return stuno