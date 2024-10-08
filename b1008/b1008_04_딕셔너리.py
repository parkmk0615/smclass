dic1 ={"번호":1,"이름":"홍길동","kor":100,"eng":100}
print(dic1["번호"]) # 출력하는 방법
print(dic1["이름"])
dic1["math"]= 100 # 키와 값을 추가하는 방법
dic1["kor"]= 90 # 기존 키의 값을 수정하는 방법

del(dic1["eng"]) # 삭제하는 방법
print(dic1)
print(dic1["이름"])
print(dic1.get("이름"))
# print(dic1["합계"]) # 없는 값을 출력하면 에러 발생
print(dic1.get("학번")) # 이 형태에서 없는 키 값을 입력하면 None 출력, 에러 발생 x 
print(dic1.keys()) # dic1의 모든 키 값을 출력
print(dic1.values()) # dic1의 모든 벨류 값 출력

print(type(dic1.keys())) # type : class 객체
print(list(dic1.keys())) # dic1의 키 값을 리스트 형태로 출력

# 모든 키와 값을 출력
for key in dic1.keys():
  print(key,dic1[key])
  print()
print(dic1.items()) # 튜플 형태로 dic1의 모든 키와 벨류 값을 출력
for key,val in dic1.items():
  print(key,val)



# dic1안에 '평균'이 없을때만'평균' 추가, 존재하면 추가x
if "평균" not in dic1:
  dic1["평균"] = 99.0
print(dic1)
# a_list =[1,2,3,"홍길동"]
# print(a_list[0])
#추가
#append,insert,extend