# 4*3*2*1

result =1
for i in range(1,5):
  result*=1

# 퀴즈
a=[1,2,3,4,5]
# a 리스트에 전부 10을 더해서 출력(리스트 내포, 람다식 사용)

a=list(map(lambda x:x+10, a)) # 람다식
print(a)

b=[i+10 for i in a] # 리스트 내포
print(b)


# def func(a):
#   for i in a:
#     arr.append(i*i)
#   return arr
# print(func(a))




#a+b =[11,22,33,44]
#함수구현
# a=[1,2,3,4]
# b=[10,20,30,40]
# def func(a,b):
#   arr=[i+j for i,j in zip(a,b)]
#   return arr

# print(func(a,b))

#람다식 구현
# a=[1,2,3,4]
# b=[10,20,30,40]
# #map(lambda 매개변수1, 매개변수2: 수식)
# arr=list(map(lambda i,j:i+j,zip(a,b)))
# print(arr)


# def func(v1,v2):
#   return v1*v2

# lambda v1,v2:v1*v2



# filter(함수,반복 가능한 자료형)- 리스트,튜플, 딕셔너리
# def func(v):
#   if v%2 ==0:
#     return True
#   else:
#     return False
  
# zip 함수 :2개 리스트 1개로 변경
# a=[1,2,3,4]
# b=[10,20,30,40]
# print(list(zip(a,b)))
# print(dict(zip(a,b)))

# arr=[1,2,3,4]
# barr=list(filter(func,arr))
# print(barr)



# filte함수 사용, 람다식 사용
# 람다식 변경
# arr=[1,2,3,4]
# barr=list(filter(lambda x:x%2==0,arr))
# print(barr)



# 기본함수사용방법
# arr=[1,2,3,4]
# barr=[]
# for i in arr:
#   if func(i) !=None:
#     barr.append(func(i))
# print(barr)




# def func(v):
#   return v*2

# arr=[1,2,3,4]

# #람다

# barr=list(map(lambda x:x*2,arr))


# #map 함수 map(함수,리스트): 리스트의 내용을 1개씩 함수에 전달해서 결값을 리스트에 저장
# barr=list(map(func,arr))
# print(barr)


# #리스트 내포
# arr=[1,2,3,4]
# barr=[a*2 for a in arr]
# print(barr)


# 기본적인 함수 사용
# print(func(2))

# arr=[1,2,3,4]

# barr=[]
# for i in arr:
#   barr.append(func(i))
# print(barr)


