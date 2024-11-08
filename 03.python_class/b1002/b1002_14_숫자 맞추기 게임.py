# 1~100까지의 랜덤숫자 생성
# 입력한 숫자가 랜덤 숫자보다 크면 입력한 숫자가 큽니다. 출력
# 입력한 숫자가 랜덤 숫자보다 작으면 입력한 숫자가 작습니다. 출력
import random

num1 = random.randint(1,100)
i = 0
# # while문
# while i<10:
#   num = int(input("숫자를 입력하세요 "))
#   if num == num1:
#     print("정답입니다. 정답 숫자는 : ", num1)
#     break
#   elif num>num1:
#     print("입력한 숫자가 큽니다.")
#   elif num<num1:
#     print("입력한 숫자가 작습니다.")
#   i=i+1
#   if i == 10:
#     print("패배. 정답 숫자는 : ",num1)


# # for문
for i in range(11):
  if i == 10:
    print("패배. 정답 숫자는 : ",num1)
    break
  num = int(input("숫자를 입력하세요 "))
  if num == num1:
    print("정답입니다. 정답 숫자는 : ", num1)
    break
  elif num>num1:
    print("입력한 숫자가 큽니다.")
  elif num<num1:
    print("입력한 숫자가 작습니다.")