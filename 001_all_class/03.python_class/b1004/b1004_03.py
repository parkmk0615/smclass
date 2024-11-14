# 0부터 1씩 증가하면서, 10번 실행
for i in range(10):
  print(i)


print("-"*50)
# 5부터 9까지 실행
for j in range(5,10):
  print(j)


print("-"*50)
a_list = [1,2,3,4,5]
for k in a_list:
  print(k)

print("-"*50)
# 파이썬 - 문자열(str), 정수형(int), 실수형(float), 논리형(bool)
# 리스트 타입 - []
b_list = [3,5,9,10,3,20]
for m in b_list:
  print(m)

print("-"*50)
# 딕셔너리 타입 - {} 키와 값으로 이루어짐
dic = {"번호": 1, "이름": "홍길동", "국어": 100, "영어": 100, "수학": 99}
print(dic["번호"])
print(dic["이름"])
for n in dic:
  print(n,": ", end ='') # dic의 키 값 출력
  print(dic[n]) # dic의 value 값 출력


print("-"*50)
# count(값) 값의 갯수 출력
print(b_list.count(3))
# b_list 안에 요소 갯수 출력
print(len(b_list))


# 리스트 추가 - append, insert, extend([2,3])
# 리스트 삭제 - del, remove, clear(모두 삭제)