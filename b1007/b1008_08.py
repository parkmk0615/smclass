import random

a=[]
for i in range(5):
  for j in range(5):
    num = random.randint(1,25)
    print(3*i+j,end='\t')
  print()