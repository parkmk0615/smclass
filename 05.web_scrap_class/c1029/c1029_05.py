# a=1
# b=2

# a_list = [a,b]
# print(a_list)

# print(type(a_list))

# # 튜플 만드는 법
# a_tuple = (a,b)
# print(type(a_tuple))

# # 튜플 만드는 법 / ()괄호 안에 하나의 값만 넣을 때는 쉼표를 넣지 않으면 int 타입으로 정의 됨
# b_tuple = (a,)
# print(b_tuple)
# print(type(b_tuple))

# name='홍길동'
# a='안녕하세요. 이름은 %s입니다.'%name
# print(a)
# # format함수
# print("hello. my name is {}".format(name))
# # 문자 f함수
# print(f"hello. my name is {name}")




# 리스트 타입을 가지고 딕셔너리 타입으로 변경 하는 법
title =['e_id','e_name','salary']
a=[196, 'Alana Walsh', 3100.0]
#print(dict(zip(title,a)))
aa=[
(196, 'Alana Walsh', 3100.0),
(125, 'Julia Nayer', 3200.0),
(180, 'Winston Taylor', 3200.0),
(194, 'Samuel McCain', 3200.0),
(138, 'Stephen Stiles', 3200.0),
]
a_list=[]

for i in aa:
  a_list.append(dict(zip(title,i)))
print(a_list)
