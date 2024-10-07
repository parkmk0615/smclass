import random
# 1-25 사이의 랜덤 숫자를 생성하시오

# num = int(random.random()*25)+1

num2 = random.randint(1,25)
a_list = []
# 25번 반복해서 1-25 랜덤 숫자를 입력, 중복 제거하고 출력
# for i in range(25):
#   num = random.randint(1,25)
#   if len(a_list)<25:
#     if num not in a_list:
#       a_list.append(num)
    
# print(a_list)

# 1-25까지 랜덤배치 - random.choices
# 중복 추출 가능
# a_list = []
# for i in range(25):
#   a_list.append(i+1)

# b_list = random.choices(a_list,k=25)
# print(b_list)

 
# 1-25까지 랜덤배치 - random.sample
# 중복 추출 안됨
# random.sample()
# b_list = random.sample(a_list,25)
# print(b_list)