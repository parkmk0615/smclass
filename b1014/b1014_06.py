import random
fname = ["바나나","오렌지","체리","파인애플","코코넛"]
fruit={"바나나":"banana","오렌지":"orange","체리":"cherry","파인애플":"pineapple","코코넛":"coconut"}

fname = list(fruit.keys())
print(fname)

# refname = random.sample(fname,5)
# for i in refname:
#   search= input(f"{i}의 영문을 입력")
#   if fruit[i] == search:
#     print("정답",fruit[i],search)
#   else:
#     print("오답입니다.",fruit[i],search)




# print("영단어 맞추기")
# for i in fruit.keys():
#   search= input(f"{i}의 영문을 입력")
#   if fruit[i] == search:
#     print("정답",fruit[i],search)
#   else:
#     print("오답입니다.",fruit[i],search)





# search= input("바나나의 영문을 입력하세요")
# if fruit['바나나'] == search:
#   print("정답",fruit["바나나"],search)
# else:
#   print("오답입니다.",fruit["바나나"],search)





# 바나나를 입력하면 영어로 banana
# while True:
#   name=input("과일 이름을 입력")
#   if name in fruit:  
#     print("영문으로 ",fruit[name])
#   else :
#     print("과일이 없습니다.")