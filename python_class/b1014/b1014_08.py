# 전역변수인 경우 함수내에서도 사용이 가능
# 함수 외부에서도 사용이 가능
# 지역변수는 return 없이는 값이 함수 밖으로 나오지 못함


def calc():
  global sum # 전역변수인 경우, 함수에서 변경 시 외부에서도 같이 변경 됨
  sum=200

sum=10
calc() # 함수에서 sum 값이 200으로 변경
print(sum) # 200출력





# 매개변수가 일반변수 일 경우 return 하지 않으면 변수 값이 변동 없음
# hh=100
# def add(hh):
#   hh=hh+100

# add(hh)
# print(hh)
#----------------------------


# 복합변수 - 리스트, 딕셔너리
# hong=[1,2,3,4,5]
#  매개 변수가 복합변수일 경우, return이 없어도 값이 변경되어 전달 됨
# def add(h):
#   for i in range(len(h)):
#     h[i] = h[i]+100

# add(hong)
# print(hong)


# kim= []
# kim = hong
# kim[0]=100
# print(hong)




# def calc(n1,n2):
  
#   s1 = n1+n2
#   s2 = n1-n2
#   s3 = n1*n2
#   s4 = n1/n2
#   s5=[s1,s2,s3,s4]
#   return s5
# s5 = calc(10,5)
# print(s5)



# # 함수  내에선언된 변수는 외부에서 사용 불가능
# def calc(v1,v2):
#   global sum # 전역변수
#   #sum=0  
#   for i in range(v1,v2+1):
#     sum+=i
#   return sum
# sum =100  # 외부 변수를 사용해서 계산하고 싶을 경우
# sum = calc(1,10)
# print(sum)



# print(1,2,3, sep=":",end='\t') # 가변 매개변수
# print("안녕")


# #키워드매개변수  
# def calc(n1=10,n2=20):
#   print(n1)
#   print(n2)
# calc()
# calc(20) # n1=20, n2= 키가 없으므로 20 출력
# calc(300) # 키가 없으면 첫번째로 전달  됨
# calc(n2=100) # 키가 있으면 키 값으로 전달


# def calc(n1,n2): # 기본 매개변수
#   print(n1,n2)

# calc(1,2)

# def calc(*n): # 가변매개변수
#   print(n)
#   print(len(n))
# calc(1,2,3,4,5,6,7)





# def calc(n):
#   s1=0
#   s2=0
#   s3=1
#   s4=1
#   for i in range(len(numstr2)):
#     s1+=numstr2[i]
#     s2-=numstr2[i]
#     s3*=numstr2[i]
#     s4/=numstr2[i]
#   print(f"두 수의 합 : {s1}")
#   print(f"두 수의 차 : {s2}")
#   print(f"두 수의 곱 : {s3}")
#   print(f"두 수의 나누기 : {s4}")

# numstr=input("숫자 입력")
# numstr2=numstr.split(",")
# numstr2=[int(i) for i in numstr2]
# calc(numstr2)









# # 3개의 숫자를 입력받아 숫자를 계산
# def number(a,b,c):
#   print(f"세 수의 합 : {a+b+c}")
#   print(f"세 수의 차 : {a-b-c}")
#   print(f"세 수의 곱 : {a*b*c}")
#   print(f"세 수의 나누기 : {a/b/c}")

# num1= int(input("숫자1 입력 "))
# num2= int(input("숫자2 입력 "))
# num3= int(input("숫자3 입력 "))

# number(num1,num2,num3)




# def calc(num,num2):
#   print(f"두 수의 합 : {num+num2}")
#   print(f"두 수의 빼기 : {num-num2}")
#   print(f"두 수의 곱하기 : {num*num2}")
#   print(f"두 수의 나누기 : {num/num2}")

# numstr = input("숫자를 입력하세요(x,y)")
# numstr2=numstr.split(',')
# num=numstr2[0]
# num2=numstr2[1]

# calc(int(num),int(num2))



# #def 함수사용
# def calc(num,num2):
#   print(f"두 수의 합 : {num+num2}")
#   print(f"두 수의 빼기 : {num-num2}")
#   print(f"두 수의 곱하기 : {num*num2}")
#   print(f"두 수의 나누기 : {num/num2}")

# num=[10,20,30]
# num2 =[5,7,3] 

# for i in range(len(num)):
#   calc(num[i],num2[i])

# # for문을 활용한 계산
# num=[10,20,30]
# num2 =[5,7,3] 

# for i in range(len(num)):
#   print(f"두 수의 합 : {num[i]+num2[i]}")
#   print(f"두 수의 빼기 : {num[i]-num2[i]}")
#   print(f"두 수의 곱하기 : {num[i]*num2[i]}")
#   print(f"두 수의 나누기 : {num[i]/num2[i]}")


