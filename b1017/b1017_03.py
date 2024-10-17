# 예외 처리 : try-except구문을 사용해서 처리
# print("프로그램 시작")
# try:
# # print("프로그램 시작) # 구문오류- 프로그램 실행 전에 오류
#   print(list_a) # 런타임 오류 - 프로그램 실행 중에 오류
# except:
#   print("에러 발생")

# print("프로그램 종료")


#-------------------------------------------------------

# n_str=input("정수를 입력하세요")
# try:
#   num = int(n_str)
#   # 원의 넓이, 원의 들레
#   print("원의 넓이 : ",(num**2)*3.14)
#   print("원의 둘레: ",2*num*3.14)
# except Exception as e:
#   print("정수가 아닙니다",e)

# if n_str.isdigit():
#   num = int(n_str)
#   # 원의 넓이, 원의 들레
#   print("원의 넓이 : ",(num**2)*3.14)
#   print("원의 둘레: ",2*num*3.14)
# else:
#   print("정수가 아닙니다")

#-------------------------------------------------------

# list_a=[1,2,3,4,5,"홍길동",5,6,7]
# list_b=[]
# try: 
#   for a in list_a:
#     list_b.append(a**2)
# except:
#   pass
# print(list_b)

#-------------------------------------------------------


#try-excepty try에서 에러가 발생하면 except 실행
# print("1")
# try:
#   print("2")
#   print(3/0)
#   print("3")
#   print("4")
# except:
#   print("5")
#   print("6")
# print("7")
# print("8")

#try-excepty-else try에서 에러가 없으면 else 실행
# print("1")
# try:
#   print("2")
#   print("3")
#   print("4")
# except:
#   print("5")
#   print("6")
# else:
#   print("에러가없음")
# print("7")
# print("8")

#try-excepty-finally try에서 에러가 발생하든 않하든 무조건 finally 실행
# print("1")
# try:
#   print("2")
#   print(3/0)
#   print("3")
#   print("4")
# except:
#   print("5")
#   print("6")
# finally:
#   print("무조건 실행")
# print("7")
# print("8")


# print("파일 open")
# try:
#   print("글쓰기1")
#   print("글쓰기2")
#   print("글쓰기3")
#   print("str -> 딕셔너리 4")
#   print("글쓰기4")
#   print("글쓰기5")
#   print("글쓰기6")
# except:
#   print("잘못된 타입이 있습니다.")


#--------------------------------------------------------

numbers=[52,273,32,103,90,10,275,1,2,1,2,12]
a="123512"
# b=a.find("9")
# print(b)
try:
  print(numbers.index(52))
  print(numbers.index(1))
  print(numbers.index(3))
  print(numbers.index(32))
  print(numbers.index(90))
except Exception as e:
  print("찾는 번호가 없습니다.",e)


# f=open("b1017/a.txt","w",encoding="utf-8")
# try:
#   f.write("안녕하세요1\n")
#   f.write("안녕하세요2\n")
#   f.write("안녕하세요3\n")
#   f.write({"a":1})
#   f.write("안녕하세요4")
# except Exception as e:
#   print(e)
# finally:
#   f.close()