import random

lotto =[0]*6+[1]*3
random.shuffle(lotto)

a_list = [[0,1,0],[0,0,1],[1,0,0]]

for i in range(3):
  for j in range(3):
    a_list[i] = lotto[3*1+j]

aa_list = [["로또","로또","로또"],["로또","로또","로또"],["로또","로또","로또"]]
while True:
  money = int(input("얼마를 투자 하시겠습니까? "))

  print("     [i,j좌표]")
  print("\t0\t1\t2")
  print("-"*30)

  for i in range(3):
    print(i,"|",end='\t')
    for j in range(3):
      print(aa_list[i][j],end='\t')
    print()

  code = input("좌표를 입력하세요 (0.0)>> ")
  codeArr = code.split(".")
  print(f"{codeArr} 좌표 값: ",a_list[int(codeArr[0])][int(codeArr[1])])
  if a_list[int(codeArr[0])][int(codeArr[1])] == 1:
    aa_list[int(codeArr[0])][int(codeArr[1])] = "당첨"
    print(f"당첨금 : {money**10:,d}")

  elif a_list[int(codeArr[0])][int(codeArr[1])] == 0:
    aa_list[int(codeArr[0])][int(codeArr[1])] = "꽝"
    print(f"다음 기회에 : {money}")