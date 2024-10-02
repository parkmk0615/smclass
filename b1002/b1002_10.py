fruit = []

while True:
  # strip() 앞쪽 여백, 뒤쪽 여백 제거
  # replace(" ","") : 문자 대체
  search = input("과일이름을 입력하세요 (종료: x) ").replace(" ","")
  # search = input("과일이름을 입력하세요 (종료: x) ").strip()
  if search in fruit:
    print("같은 이름의 과일이 존재해서 추가하지 않겠습니다.")
  elif(search == 'x'):
    break
  # 입력된 과일 이름을 리스트에 추가 하시오
  else:
    fruit.append(search)
  print(fruit)




# 반복문을 종료할때: break 사용
# while True:
#   break
# print("프로그램 종료")

# 무한반복은 while True: 입력
# a=0
# while True: # 무한 반복
#   print(a)
#   a+=1

# while a < 10:
#   a+=1
#   print(a)

# print("프로그램 종료")