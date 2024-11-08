import random

aArr = []
# 0~9까지의 10개의 랜덤숫자 추출해서 10번  저장하시오
# 같은 수가 존재하면 제외

# for i in range(10):
#   r_num = random.randint(0,9)
#   if r_num not in aArr:
#     aArr.append(r_num)

i=0
while i< 10: # 무조건 10개일 때 종료
  r_num = random.randint(0,9)
  if r_num not in aArr:
    aArr.append(r_num)
    i+=1

print("개수: ", len(aArr))
print(aArr)
