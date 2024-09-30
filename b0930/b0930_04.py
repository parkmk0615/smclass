# name, kor, eng, math,total, avg 출력
# input으로 입력을 받기
# 홍길동, 100, 100, 99 합계, 평균 1줄에 출력
# format 함수,f함수 사용
name = input("이름을 입력 하시오 ") 
kor = input("국어 점수를 입력하세여") # kor = int(input("국어 점수를 입력하세요"))  -> 점수를 입력 받자마자 str 타입을 int 타입으로 변경
eng = input("영어 점수를 입력하세여") # eng = int(input("영어 점수를 입력하세요"))  -> 점수를 입력 받자마자 str 타입을 int 타입으로 변경
math = input("수학 점수를 입력하세여") # math = int(input("수학 점수를 입력하세요"))  -> 점수를 입력 받자마자 str 타입을 int 타입으로 변경
total = int(kor)+int(eng)+int(math)
avg = total/3
# print(type(kor)) --> str타입
# print(type(eng)) --> str타입
# print(type(math)) --> str타입

print("{}의 국어점수 : {}, 영어점수 : {}, 수학점수 : {}, 합계 : {}, 평균 : {:.2f}".format(name, kor, eng, math, total, avg))
print(f"{name}의 국어점수: {kor}, 영어점수 {eng}, 수학점수{math}, 합계 : {total}, 평균 : {avg:.2f}")












# a ='100'
# b="200"
# print(type(a))
# print(type(b))
# print(a+b) #문자 연결 연산자 -> 100200

# print(int(a)+int(b)) # 타입 변경
# name="홍길동"
# #print(int(name)) # 문자는 숫자로 변경 불가능, 숫자를 문자로 변경 가능
# c="3.14"
# print(int(float(c))) # 실수형으로 변경 후 정수형으로 변경
# #print(int(c)) # 문자실수형은 바로 정수형으로 변경 불가
# print(str(c))  # 실수형을 문자열로 변경

# d="True"
# print(bool(d)) # 문자불형을 불형으로 변경

#타입 변경 -str, int, float, bool 
 



# name ="홍길동"
# print(type(name))

# level='3레벨'
# print(type(level))

# n=3.14
# print(type(n))

# num =100
# print(type(num))

# a_bool=True
# print(type(a_bool))


# var1 = 100
# var2 = var1
# var3 = var2 
# var4 = var3

# print(var4)

# v4=v3=v2=v1 = 100
# print(v4, v3, v2, v1)