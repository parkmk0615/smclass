# print(students)
# print("-"*50)
# students.sort(key=lambda x: x[total],reverse=True)
# print(students)

#------------------------------------------------------------------------

# 리스트 정렬 -> sort는 리스트에서만 사용가능한 정렬 함수
# students = [
#   [1,"홍길동",100,100,99,299,99.67,0],
#   [2,"유관순",80,80,85,245,81.67,0],
#   [3,"이순신",90,90,91,271,90.33,0],
#   [4,"강감찬",60,65,67,192,64.00,0],
#   [5,"김구",100,100,84,284,94.67,0]
# ]

# students.sort(key=lambda x: x[1]) # 이름순 순차정렬
# print(students)
# students.sort(key=lambda x: x[1],reverse=True) # 이름순 내림차순 정렬 
# print(students)
# students.sort(key=lambda x: x[5]) # 합계순 오름차순 정렬
# print(students)
# students.sort(key=lambda x: -x[5]) # 합계순 내림차순 정렬
# print(students)
# x= sorted(students,key=lambda x:x[1])
# print(students)
# print(x)


# 함수를 사용해서 정렬
# def stu_sort(x):
#   return x[1]
# students.sort(key=stu_sort)
# print(students)

#------------------------------------------------------------------------

# aArr =[4,5,6,1,2]
# aArr.sort() # 오름차순 정렬
# aArr.sort(reverse=True) # 내림차순 정렬
# aArr.reverse() # 역순 출력
# print(aArr)

