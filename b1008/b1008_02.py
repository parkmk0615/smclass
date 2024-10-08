# #[4,5] 2차원 리스트
# num=0
# a_list = []
# for i in range(4):
#   a=[]  
#   for j in range(5):
#     # print(5*3*i+(3*j),end='\t')
#     a.append(5*3*i+(3*j))
#   a_list.append(a)
# print(a_list)

#[0,3,6,9,12....57]
aArr=[]
for i in range(20):
  aArr.append(3*i)
print(aArr)

a_list=[]
for i in range(4):
  a=[]
  for j in range(5):
    a.append(aArr[5*i+j])
  a_list.append(a)
print(a_list)