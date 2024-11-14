# 문자열

# 문자열 숫자
a ="123"
int(a)
print(type(int(a)))  # int타입
print(type(a))  # str타입
print(type(float(a)))  # float타입

b = "12.3"
# print(type(int(b)))  # 에러 - 소수점이 있는 문자열 숫자는 float으로 변경해야 함
print(type(float(b))) # float타입

s1 = "안녕"
s2 = "하세요"
print(s1+s2) # 안녕하세요 출력
print(a+b) # 문자형 연결 연산자 , 12312.3 출력
# print(a*b) # 에러 - 문자열은 -,*,/ 불가능

# 문자열 반복 연산자
print("안녕"*3) # 안녕안녕안녕 출력
print("--"* 5) # ---------- 출력

# 문자열 슬라이싱
str1 = "안녕하세요.반갑습니다." 
print(str1[6]) # 반 출력
print(str1[2:5]) # 하세요 출력, [위치:위치-1]
print(str1[:5]) # 안녕하세요 출력, [처음부터:위치-1]
print(str1[2:]) # 하세요.반갑습니다. 출력, [위치:끝까지]
print(str1[1:10:2]) #녕세.갑니 출력, [위치:위치-1:2스텝]
print(str1[::-1]) # .다니습갑반.요세하녕안 출력 [처음부터:끝까지:거꾸로]
print(str1[::-2]) # .다니습갑반.요세하녕안 출력 [처음부터:끝까지:거꾸로2스텝]


# [] - 배열 : 배열은 한번 범위가 정해지면 수정이 불가  : c,자바
# [] - 리스트 : 범위상관없음




c=12.3
print(type(int(c))) # 실수는 int 타입으로 변경이 가능.
print(int(c))




# input_str=input("글자를 입력하세요 ")

# # 문자가 입력되지 않았을때
# if input_str =='':
#   print("글자를 입력하셔야 합니다.")
# else:
#   print("입력문자: ", input_str)

# # 문자가 입력 되었을때
# if input_str !='':
#   print("입력문자: ", input_str)
#   print("프로그램이 종료됩니다.")
# else:
#   print("글자를 입력하셔야 합니다.")


