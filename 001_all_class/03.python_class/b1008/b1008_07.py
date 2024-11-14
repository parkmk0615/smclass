import operator

# zip() 함수
name =["홍길동","유관순","이순신"]
score = [100,90,95]
# 튜플 타입 리스트 생성
n_list = list(zip(name,score))
print(n_list)

# 딕셔너리 타입 리스트 생성
d_dic = dict(zip(name,score))
print(d_dic)







# n_list=[]
# 동시에 여러개 리스트에 접근
# for n,s in zip(name,score):
#   n_list.append([n,s])
# print(n_list)






# numlist=[]
# #리스트 =1,2,3,4,5 추가
# for i in range(1,6):
#   numlist.append(i)
# print(numlist)

# # for 문을 1줄로 사용해서 처리
# # 리스트 내포, 컴프리헨션
# nlist = [i+1 for i in range(5)]
# print(nlist)

# a_list = [i*i for i in range(5)]
# print(a_list)

# # 정수형 -> 문자열
# b_list=[str(i) for i in range(5)]
# print(b_list)

# # 문자열 -> 정수형
# c_list = ["5","9","0","3","2"]
# cc_list = [int(i) for i in c_list]
# print(cc_list)

# d_str = "1,2,23,5,9"
# d_sp = [int(i) for i in d_str.split(",")]
# print(d_sp)

# # 문자열을 입력받아 정수형 리스트로 변경
# score = input("좌표를입력하세요.(0.0)>> ")
# sc=[int(i) for i in score.split(".")]
# print(score)
# print(sc)


# students = [
#   {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":0}
#   {"no":2,"name":"유관순","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":0}
#   {"no":3,"name":"이순신","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":0}
#   {"no":4,"name":"강감찬","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":0}
#   {"no":5,"name":"김구","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":0}
# ]

# 리스트 딕셔너리 정렬
# for s in students:
#   print(s)


# print(students)
# x=sorted(students.items())
# print("-"*50)
# print(students)








#------------------------------------------------------------------------

#nameDic = {'홍길동':100,'유관순':80,'이순신':95,'강감찬':82,'김구':97}

# key,value - nameDic.items()
# key - nameDic.keys()
# value - nameDic.values()
# print(nameDic)
# key- [0], value[1]
# (key,value) : [0,1]

# lambda x:x[0], lambda x:x[1]
# nameDics = sorted(nameDic.items(),key=lambda x:x[0]) # 람다식구현
# nameDics=sorted(nameDic.items(),key=operator.itemgetter(1),reverse=True)
# nameDics=sorted(nameDic.items(),key=operator.itemgetter(1)) # [1]번쨰로 정렬

# nameDics = sorted(nameDic.items()) # [0]번째로 순차정렬
# nameDics = sorted(nameDic.items(),reverse=True) # [0]번째로 역순정렬
# print("-"*50)
# print(nameDics)