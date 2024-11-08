
students = [
  {"no":1, "name":"홍길동"},
  {"no":2, "name":"유관순"},
  {"no":3, "name":"이순신"}
]
stuno=len(students)

def stuinput(stuno,students):
  while True:
    no=stuno+1
    print("no: ",no)
    name=input(f"{no}번째 학생 이름을 입력하세요 (0. 이전페이지로 이동)")
    if name =='0':
      break
    students.append({"no":no,"name":name})
    stuno+=1
  return stuno
  
# 학생 성적 입력 호출
stuno=stuinput(stuno,students)
print(stuno)
print(students)