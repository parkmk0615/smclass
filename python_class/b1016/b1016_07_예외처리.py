# try except 프로그래밍 예외를 처리하는 명령어
# while True:
#   score:100
#   nstr = input("숫자만 입력 가능")
#   try:
#     num=int(nstr)
#     print("입력된 숫자로 100을 나눔: ",score/num)
#   except:
#     print("숫자로 변환안됨")
try:
  print("입력된 숫자: ",int(input("숫자를 입력하세요 : ")))
except:
  pass