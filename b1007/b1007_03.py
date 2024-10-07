# # 2차원 리스트
# a_list =[[1,2,3,4],[5,6,7,8],[9,10,11,12]]

# # 2차원 리스트 -> for문을 2번 사용
# for i in a_list:
#   for j in i:
#     print(j)

# # 3행 3열 리스트[1,2,3],[4,5,6],[7,8,9]
# a_list = [[1,2,3],[4,5,6],[7,8,9]]
# for i in range(3):
#   a=[]
#   for j in range(3):
#     y = (3*i)+(j+1)
#     a.append(y)
#   a_list.append(a)
# print(a_list)
   

# # 1-9까지for문을 사용해서 1차원 리스트에 추가하시오
# b_list=[]
# for i in range(1,10):
#   b_list.append(i)
# print(b_list)

# 2차원 리스트
# for문을 2번 작성해서 1번부터 25까지의 수를 [5,5] 생성
a_list = []
for i in range(5):
  a=[]
  for j in range(5):
    a.append(5*i+(j+1))
  a_list.append(a)
print(a_list)

# a_list = []
# for i in range(9):
#   a_list.append(i+1)


# b_list = []
# for i in range(9):
#   b=[]
#   if a_list[i] % 4 == 0:
#     b.append(a_list[i])


# print(b_list)