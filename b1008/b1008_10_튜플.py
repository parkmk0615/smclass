# # 튜플 - 리스트 타입과 같음,순서 존재 // 수정, 추가 불가능
# t=(1,2,3,4)
# print(t[0])
# # t[0]=100 # 튜플은 수정 불가
# # t.append(100) # 튜플은 추가 불가
# print(len(t))
# print(t)

# # 더하기 연산자는 추가 가능
# t=t+(3,5)
# print(t)
# # 곱하기 연산자 가능
# tt=(1,2,3,4)
# tArr= tt*2
# print(tArr)


# tArr=[1,2,3,4]
# tArr[0] =100



#--------------------------------------------------------

# t=[3,5,1,2]
# t.sort() # t리스트에 반영
# print(t)

# t[1:3]  # t리스트에 반영되지 않음

# print(t+[3,7])
# t.extend([3,7])
# print(t)
#--------------------------------------------------------
# aArr=[[1,2],[[1,2],[3,4]],[5,6],[7,8]]
# a_list=[1,2,1,2,3,4,5,6,7,8]

# b_list=[]
# for i in aArr:
#   if type(i) == list:
#     for j in i: #2차원 배열
#       if type(j) == list:
#         for k in j: # 3차원 배열
#           b_list.append(k)
#       else: 
#         b_list.append(j)
# print(b_list) 

#--------------------------------------------------------

# 일반적인 a,b 치환
a='우유'
b='커피'
c=""
print(a,b)
c=a
a=b
b=c
print(a,b)

# 파이썬 a,b 치환
a,b=b,a

#--------------------------------------------------------

a=((1,2),(3,4),(5,6))
print(a[0])
print(a[0][1])

# 문자열을 tuple로 타입 변경
# a_str ="abcde"
# print(a_str)
# print(a_str[1])

# a_tu=tuple(a_str)
# print(a_tu)
# print(list(a_tu))