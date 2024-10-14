subname=["국어","영어","수학",]
score={"국어":100,"영어":95,"수학":80,}

print(score)
print(score["국어"])
print(subname[0])
print(score[subname[0]])

for i in subname:
  print(i,":",score[i])

for k,v in score.items():
  print(k,":",v)





# def cartion(b):
#   for i in range(2,b+1):
#     print(i,"단")
#     for j in range(2,10):
#       print("{}*{}={}".format(i,j,i*j))


# narr=[9,5,7]

# for i in narr:
#   cartion(i)
#   print("-"*50)




# def cartion(a,b):
#   for i in range(a,b+1):
#     print(i,"단")
#     for j in range(1,10):
#       print(i,"*",j,"=",i*j)
#   print('-'*60)

# a=int(input("숫자를 입력"))
# b=int(input("숫자를 입력"))

# cartion(a,b)





# # 구구단 출력 (2단~5단)
# for i in range(2,6):
#   for j in range(1,10):
#     print(i,"*",j,"=",i*j)
# print('-'*60)

# # 구구단 (3단~9단)
# for i in range(3,10):
#   for j in range(1,10):
#     print(i,"*",j,"=",i*j)
# print('-'*60)


# # 구구단 (5단~8단)
# for i in range(5,9):
#   for j in range(1,10):
#     print(i,"*",j,"=",i*j)
# print('-'*60)
