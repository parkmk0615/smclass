# # 구구단 
# # 입력한 단까지출력 3입력 -> 1,2,3단 출력
# num=int(input("숫자를 입력하시오 "))
# for i in range(2,num+1):
#   print("[{}단을 출력합니다.]".format(i))
#   for j in range(1,10):
#     print(i,"*",j,"=",i*j)
#   print("-"*10)

#--------------------------------------------------------------

# # 000
# # 001
# # ...
# # 999 까지 출력
# for i in range(1000):
#   print(f"{i:03d}")

# for i in range(10):
#   for j in range(10):
#     for k in range(10):
#       print(i,end='')
#       print(j,end='')
#       print(k)

#--------------------------------------------------------------

# # for문 출력
# # 구구단 가로 출력
# for i in range(2,10):
#   for j in range(2,10):
#     print(f"{i} * {j} = {i*j}",end='\t')
#   print()

# 구구단 세로 출력
for k in range(2,10):
  print(f"[{k}]단",end='\t\t')
print()
for i in range(2,10):
  for j in range(2,10):
    print(f"{j} * {i} = {i*j}",end='\t')
  print()
