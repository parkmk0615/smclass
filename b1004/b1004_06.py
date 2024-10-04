# # enumerate()함수
# a_list = ['홍길동','유관순','이순신','강감찬','김구','김유신','홍길자','홍길순']

# # for문으로 출력
# for a in a_list:
#   print(a)

# # enumerate함수 - index 번호 출력 index,value
# for i,a in enumerate(a_list):
#   print(f"{i}:{a}")

# print(a_list)

#--------------------------------------------------------------

# a_list = [1,2,3,4,5]
# # a_list = [1*1,2*2,3*3,4*4,5*5]

# # 리스트의 값을 변경해서 리스트에 저장
# for idx,a in enumerate(a_list):
#   a_list[idx] = a*a
# print(a_list)

# # 리스트의 값을 변경해서 리스트에 저장 - 리스트 내포
# a_list =[a**2 for i in a_list]
# print(a_list)

# #리스트 값 변경
# a_list[1] = 100
# print(a_list)

# 존재 하지 않는 위치 값을 호출하면 에러
# a_list[5] = 1000
# print(a_list)

# # 리스트 슬라이싱 - 0~3까지 출력
# print(a_list[0:4])
# # 리스트 범위보다 큰 슬라이싱 출력 시, 존재하는 범위까지만 출력
# print(a_list[0:10])

#--------------------------------------------------------------

a_list = ['홍길동','유관순','이순신']
# 각 요소 뒤에 '님'자 추가하기

a_list =[a+"님" for a in a_list]
print(a_list)
