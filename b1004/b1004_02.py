import random

 
# 10번의 도전에서 입력한 숫자가 더 크면 작은 수를 입력하셔야 합니다 출력
# 입력한 숫자가 더 작으면 큰 수를 입력하셔야 합니다 출력
# 랜덤숫자 : 1~100

num = random.randint(1,100)
# for i in range(11):
#   if i == 10:
#     print("도전에 실패하셨습니다. 랜덤숫자 :", num)
#     break
#   print(f"{i+1}번째 도전")
#   num1 = int(input("숫자를 입력하세요: "))
#   if num1 == num:
#     print("정답입니다. 랜덤숫자: ",num)
#     break
#   elif num1 > num:
#     print("큰 수를 입력하셨습니다.")
#   elif num1 < num:
#     print("작은 수를 입력하셨습니다.")



i = 0
while i < 10:
  print(f"{i+1}번째 도전")
  num1 = int(input("숫자를 입력하세요: "))
  if num1 == num:
    print("정답입니다. 랜덤숫자: ",num)
    break
  elif num1 > num:
    print("큰 수를 입력하셨습니다.")
  elif num1 < num:
    print("작은 수를 입력하셨습니다.")
  i = i+1
  if i == 10:
    print("도전에 실패하셨습니다. 랜덤숫자 :", num)
    break