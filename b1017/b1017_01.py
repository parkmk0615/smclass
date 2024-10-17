# subject=[ "국어","영어"]

# def output(subject):
#   for i in subject:
#     print(i)


# while True:
#   print(" [ 과목 생성 ] ")
#   s_input = input("원하는 과목을 입력하세요")
#   subject.append(s_input)
#   output(subject)


#-----------------------------------------------


# a=10
# def func():
#   a=50
#   print(a) # 50 출력
#   return a
# a=func()
# print(a) # 50 출력


#---------------


# a=10
# b=20
# c=30
# sum=0

# def add(a,b,c):
#   a=a+b+c
#   print(a)

# add(a,b,c)
# print(a)


#---------------


subject=["국어","영어","수학","과학","역사"]
score=[]

while True:
  print("1.과목추가")
  print("0. 종료")
  choice = input("번호 입력")
  if choice == "1":
    s_input=input("과목 추가")
    subject.append(s_input)
  elif choice =="0":
    break

for i in range(len(subject)):
  score.append(int(input(f"{subject[i]}점수를 입력하세요 ")))

sum=0
for i in range(len(subject)):
  print(f"{subject[i]}:",score[i])
  sum+=score[i]
print("합계: ",sum)



# while True:
#   num1 = int(input("국어 점수를 입력하세요 "))
#   num2 = int(input("영어 점수를 입력하세요 "))
#   num3 = int(input("수학 점수를 입력하세요 "))
#   num4 = int(input("과학 점수를 입력하세요 "))
#   num5 = int(input("역사 점수를 입력하세요 "))

  # print("국어: ", num1)
  # print("영어: ", num2)
  # print("수학: ", num3)
  # print("과학: ", num4)
  # print("역사: ", num5)
  # print("합계: ", num1+num2+num3+num4+num5)








# def output(subject):
#   for i in subject:
#     print(i)


# while True:
#   print(" [ 과목 생성 ] ")
#   s_input = input("원하는 과목을 입력하세요")
#   subject.append(s_input)
#   output(subject)