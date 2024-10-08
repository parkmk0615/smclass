# 25개 1차원 리스트 -> 1~25까지 입력 랜덤
#[5,5] 2차원 리스트
import random

aArr=[]
for i in range(25):
  aArr.append(i+1)
random.shuffle(aArr)
# print(aArr)

a_list=[]
for i in range(5):
  a=[]
  for j in range(5):
    a.append(aArr[5*i+j])
  a_list.append(a)
print(a_list,end='\t')
print()

#5,5 리스트 출력
while True:
  for i in range(5):
    for j in range(5):
      print(a_list[i][j],end='\t')
    print()
  # re = input("좌표를 입력하세요(0,0)")
  # result = re.split(",")
  # print("좌표 값: ",a_list[int(result[0])][int(result[1])])

  re=int(input("값을 입력하세요 (1-25)"))
  if 0 > re or re>26:
    print("1에서25 사이 값을 입력하셔야 됩니다.")
    continue

  for i in range(5):
    for j in range(5):
      if a_list[i][j] == re:
        print(f"좌표값 : [{i,j}]")
        break
  
  for i in range(5):
    for j in range(5):
      if a_list[i][j] == re:
        a_list[i][j] = 0
        break