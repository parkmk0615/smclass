def calc():
  print(a)
  print('프로그램 종료')

a= 10
calc()






# 함수 - 매개변수 (일반변수, 복합변수)
# 3. 함수에서 복합매개변수 - return 없이 값이 함수 밖 값 사용
def calc(harr):
  for i in range(len(harr)):
    harr [i] += 100

harr =[1,2,3,4,5] # 복합 변수 - 주소 값이 저장됨
calc(harr)
print(harr)


#  2. 전역변수 - 일반 매개 변수 return 없이 함수 밖 값 사용
def calc():
  global h
  h+=100

h=20
calc() # 함수 호출 후 h에 값을 할당할 필요 없음
print(h)

#  1. 함수 일반 매개변수 - return이 아니면 값이 함수 밖으로 나올 수 없음
def calc(hh):
  hh+=100
  return hh

h=20
h=calc(h) # 호출만하고 일반 변수 값을 넣어주지 않으면 값이 변경되지 않음
# calc(h) # 호출만 하였기에 h 값은 변경되지 않음
print(h)


