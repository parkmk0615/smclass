def operate(count):
  for i in range(count):
      print("한국어 인사 : 안녕하세요")

while True:
  print("[ 외국어 인사 ]")
  print("1. 한국어 인사")
  print("2. 일본어 인사")
  print("3. 영어 인사")
  print("4. 프랑스 인사")

  choice = input("원하는 번호를 입력하세요")
  count = int(input("반복횟수를 입력하세요"))

  if choice == "1":
    operate(count) # 함수 호출
    print("영어 인사 : Hello")
  elif choice == "2":
    print("한국어 인사 : 안녕하세요")
    print("일본어 인사 : 오하이요")
  elif choice == "3":
    print("한국어 인사 : 안녕하세요")
    print("중국어 인사 : 니하오")
  elif choice == "4":
    print("한국어 인사 : 안녕하세요")
    print("프랑스어 인사 :봉주르o")