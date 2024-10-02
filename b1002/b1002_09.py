fruit = "사과,배,딸기,포도,복숭아,배,사과,배,딸기"
fruits = fruit.split(",")
print(fruits)
# 리스트인 경우 검색해서 해당되는 index를 출력하시오
# 배에 해당되는 index 번호를 출력하시오
search = input("과일 이름을 입력하시오 ")
for i,data in enumerate(fruits):
  if data == search:
    print("해당되는 index 번호는 : ", i)


# print(fruit.find("딸기",0)) # 5
# print(fruit.find("딸기",fruit.find("딸기",0)+1))
# print(fruit.find("딸기",6)) # 22

# print(fruit.find('배',0)) # 3
# print(fruit.find('배',3+1))
# print(fruit.find('배',fruit.find('배',0)+1)) # 15
# print(fruit.find('배',15+1))
# print(fruit.find('배',fruit.find('배',fruit.find('배',0)+1)+1))

