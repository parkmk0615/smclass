

for i in range(10):  # 0~9까지 출력
  print(i)

for i in range(2,5): # 2~4까지 출력
  print(i)

for i in range(1,10,2): # 1~9까지 2씩 증가해서 출력
  print(i)

aArr = [1,2,5,7,8]
for i in aArr: # aArr의 값을 하나씩 가져와서 i에 넣고 출력
  print(i)

for i,data in enumerate(aArr): # enumerate는 리스트에 있는 index 번호를 함께 출력
  print(i,":",data)


aStr = "안녕하세요" # aStr의 값을 하나씩 가져와서 i에 넣고 출력 
for i in aStr:
  print(i)
for i,data in enumerate(aStr): # enumerate는 리스트에 있는 index 번호를 함께 출력
  print(i,":",data)



# students = [[1,'홍길동', 100,100,99],[2,'유관순',100,100,99],[3,'이순신',100,100,99]]
# s = [4,'강감찬',100,100,99]
# s 리스트의 합계와 평균을 추가하시오

# s.append(s[2]+s[3]+s[4])
# s.append((s[2]+s[3]+s[4])/3)






# list 추가 - append- 뒤에 추가, insert- 원하는 위치에 추가
# 삭제 del - 위치삭제, remove - 삭제하고 싶은 값 입력으로 삭제
# a_list = [1,2,3]

# # 마지막에 10추가
# a_list.append(10)
# print(a_list)

# # 2번째에 100추가
# a_list.insert(2,100)
# print(a_list)

# # 삭제
# del a_list[1] # index 1번 삭제 (2값 삭제)
# print(a_list)

# a_list.remove(100) # index에 존재하는 100 값 삭제
# print(a_list)




#-----------------------------------------------------------------------------

# 문자열 슬라이싱
# str = "좋은 하루되세요. 많은 행복받으세요. 많은 감사! 많은 돈"

# print(len(str))

# # 뒤쪽에서 5자리 전까지 출력

# print(str[-5:])
# print(str[-1])
# print(str[::-1])