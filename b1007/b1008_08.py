import random
a_list=[]

for i in range(5):
  for j in range(5):
    a_list.append(random.randint(1,5))
  print()
print(a_list)