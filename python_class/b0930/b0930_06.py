# 원의 넓이 = 반x반x3.14
# 반지름을 입력 받아 원의 넓이를 구하시오
# r = input("반지름의 길이를 입력하시오")
# area = int(r)*int(r)*3.14
# print("원의 넓이 : %.2f" % area)

# 2개의 길이를 입력 받아, 삼각형의 넓이, 직사각형의 넓이를 구하시오
# a=int(input("길이를 입력하시오"))
# b=int(input("길이를 입력하시오"))
# t=(a*b)/2
# s=a*b
# print("삼각형의 넓이 : %.2f" %t)
# print("사각형의 넓이 : %.2f" %s)

# 1번에 2개의 길이를 입력받아,삼각형의 넓이, 직사각형의 넓이를 구하시오
# length = input("2개 길이를 입력하시오")
# print(length.split(" "))
# l_list = length.split(" ")
# print(float(l_list[0])*float(l_list[1]))






stu_title = ['번호','이름','국어','영어','수학','과학','합계','평균']
stu_datas =[[1,'유관순',100,100,100,99],[2,'이순신',100,99,98,99],[3,'김구',80,100,90,99]]
# 이순신의 평균을 출력하시오
# print("평균 : %.2f" % ((stu_datas[1][1]+stu_datas[1][2]+stu_datas[1][3]+stu_datas[1][4])/4))
# for i in stu_data: 
#   print(i, end =' ')

print("                     [ 학생 성적 프로그램 ]")
print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(stu_title[0],stu_title[1],stu_title[2],stu_title[3],stu_title[4],stu_title[5],stu_title[6],stu_title[7]))
print("-"*60)

# for s_t in stu_title:
#   print("{}".format(s_t),end='')
#   print()
#   print("-"*60)



for s in stu_datas:
  print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(s[0],s[1],s[2],s[3],s[4],s[5],s[2]+s[3]+s[4]+s[5],(s[2]+s[3]+s[4]+s[5])/4))

  # print("이름: %s, 국어 : %d, 영어 : %d, 수학: %d, 과학 : %d,  합계 : %d 평균 : %.2f" % (i[0],i[1],i[2],i[3],i[4], (i[1]+i[2]+i[3]+i[4]),(i[1]+i[2]+i[3]+i[4])/4), end='')






# stu_data =['홍길동',100,100,100,99]
# print("학생 이름 : %s" % stu_data[0])
# print("국어 : %d" % stu_data[1])
# print("영어 : %d" % stu_data[2])
# print("수학 : %d" % stu_data[3])
# print("과학 : %d" % stu_data[4])
# print("합계 : %d" % (stu_data[1]+stu_data[2]+stu_data[3]+stu_data[4]))
# print("평균 : %.2f" % ((stu_data[1]+stu_data[2]+stu_data[3]+stu_data[4])/4))






# 복합대입연산자 +=,-=,*=,/=, //=
# a=10
# a+=5
# print(a)
# a-=5
# print(a)
# a*=5
# print(a)
# a/=5
# print(a)
# a//=5
# print(a)
# a%=5
# print(a)
# a**=5
# print(a)



# 숫자를문자열로 변환
# a= 100
# b=10
# print(str(a)+str(b))


# 1줄 선언
# a=10;b=5
# c,d=10,20
# s1,s2,s3=1,2,3


# a = "100"
# b = "10.5"
# c="안녕"
# print(float(a)) # 정수형 -> 정수 타입, 실수 타입 변경 가능
# print(int(b)) # 실수형 -> 실수 타입 변경 가능
# print(float(c)) # 문자형 -> 글자는 숫자형 타입으로 변경 불가

# print(2+2-2*2/2*2)



# a=5; b=3  # 1줄 형태
# # /,%,//,**
# print("{},{},{},{}".format(a/b, a%b, a//b, a**b))