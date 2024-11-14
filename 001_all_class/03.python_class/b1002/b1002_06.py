students = [[1,'홍길동', 100,100,99],[2,'유관순',100,100,99],[3,'이순신',100,100,99]]

# # 이름이 유관순인 것을 출력 하시오
# for s in students:
#   print(s)
#   if s[1] == '유관순':
#     print("유관순을 찾았습니다.")
#   else:
#     print("찾지 못했습니다.")


# students에 ss를 추가하시오
ss = [4,'강감찬',100,100,99]

students.append(ss)
print(students)

# students의 '이순신'인 데이터를  지우시오
# remove를 이용해서 삭제
# for i in students:
#   if i[1]=='이순신':
#     students.remove(i)
# print(students)

# del을 이용해서 삭제
for i,data in enumerate(students):
  if data[1]=='이순신':
    del students[i] 
print(students)