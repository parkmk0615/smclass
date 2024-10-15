students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]
stu="6,홍길자,100,100,100,300,100.0"
sarr=stu.split(',')
print(sarr)

#문자열-> 리스트변경 -> 타입을 변경 
for i,s in enumerate(sarr):
  if str.isdigit(s): #int 타입이 변경 가능한지?
    sarr[i]=int(s)
  elif str.isdigit(s):
    sarr[i]=float(s)
sarr[6]=float(sarr[6])
print(sarr)
# students 리스트에 1명 추가
students.append(sarr)

print(students)


# s='11'
# print(str.isdigit(s))
# ss='a'
# print(str.isdigit(s))




# stu1="6,홍길자,100,100,100,300,100.0"
# sarr=stu1.split(',')
# key_1=["no","name","kor","eng","math","total","avg","rank"]

# print(sarr)

# # 딕셔너리 생성방법
# dict1 ={"no":int(sarr[0]),"name":sarr[1]}
# print(dict1)
# # zip
# dict_list =dict(zip(key_1,sarr))
# print(dict_list)