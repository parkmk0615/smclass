# list1=[52,273,32,72,100]
# try:
#   ninput=int(input("정수 입력"))
#   print(f"{ninput}는 리스트의 {list1[ninput]}")

# except ValueError as e:
#   print("값을 잘못입력하셨습니다.",type(e),e)

# except IndexError as e:
#   print("번호가 범위를 벗어났습니다.",type(e),e)

# except Exception as e:
#   print("모든 예외처리의 부모")
# finally:
#   pass

# Exception :모든 예외의 부모, 예외처리에서 마지막에 위치
# as e: e 변수는 예외에 대한 설명문, type(e): 예외 객체
# 리스트 범위 밖 호출 에러 : IndexError
# 입력된 값의 변환 에러 : ValueError 
# raise 키워드 : 강제 에러 발생


print("프로그램을 시작")
print("1")
print("2")
try:
  print("3")
  print("4")
  raise NotImplementedError("프로그램을 구현해야 함") # 프로그래밍을 모두 구현되어 있지 않음
  #print(10/0)
  print("5")
except Exception as e:
  print(e)
  print("6")
  print("7")
finally:
  print("8")
  print("9")
print("10")

print("프로그램 종료")