# 두 수를 입력 받아 더하기를 출력
def plus(n1,n2):
  result = n1+n2
  return result

num1=int(input("숫자를 입력"))
num2=int(input("숫자를 입력"))

print(plus(num1,num2))







# def plus(n1,n2):
#   result = n1+n2
#   return result

# print(plus(1,2))
# print(plus(55,45))
# print(plus(50,50))










# #2-50 까지의 합
# #3-7 까지의 합
# #5-50 까지의 합을 모두 더해서 출력 하세요
# def nsum(a,b):
#   sum=0
#   for i in range(a,b):
#     sum += i
#   return sum

# total = 0
# print(f"2-50까지의합: {nsum(2,50):,d}")
# print("3-7까지의합: ",nsum(3,7))
# print("5-50까지의합: ",nsum(5,50))

# total=nsum(2,50)+nsum(3,7)+nsum(5,50)

# print("합계 ",total)













# def num_sum(st,end):
#   sum=0
#   for i in range(st,end):
#     sum+=i
#   return sum

# total = 0
# num_sum(1,10)
# num_sum(1,100)
# total = num_sum(1,10)+num_sum(1,100)
# print("합계: ",total)

# print("프로그램 종료")












# def num_sum(st,end): # num_sum(매개변수,매개변수)
#   sum=0
#   for i in range(st,end+1):
#     sum+= i
#   print("합계 : ",sum)

# # 두 숫자를 입력 받아,그 사이의 숫자 합을 구하시오

# num1=int(input("숫자를 입력"))
# num2=int(input("숫자를 입력"))

# num_sum(num1,num2)




# # 1-10
# num_sum(1,10)

# # 1-100
# num_sum(1,100)


# #2-50
# num_sum(2,50)


# #100-1000
# num_sum(100,1000)