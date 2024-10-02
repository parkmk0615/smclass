import random
num1 = random.randint(1,100)


for i in range(11):
  if i == 10:
    print("패배. 정답은 :",num1)
    break
  print(f"{i+1}번째 도전 입니다.")
  num=int(input("숫자를 입력하세요"))

  if num == num1:
    print("정답입니다.")
    break
  elif num>num1:
    print("입력한 숫자가 큽니다.")
  elif num<num1:
    print("입력한 숫자가 작습니다.")
