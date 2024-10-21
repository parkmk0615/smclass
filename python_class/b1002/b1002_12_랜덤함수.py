import random

# 랜덤 숫자 생성 - random
# random() :0이상 1미만의 실수 값 추출


print(random.random())
# random - 0~9 랜덤 값 출력 방법
print(random.random()*10)
# random - 1~10 랜덤 값 출력 방법
print(int(random.random()*10)+1)

# randint - 랜덤 int 추출 - 1~3까지 랜덤 값 출력
print(random.randint(1,3)) 

# randrange - 랜덤 범위 추출 - 1~2까지 랜덤 값 출력
print(random.randrange(1,3))

# choice - 리스트를 활용한 랜덤 추출
a=[1,4,5,9]
print(random.choice(a))

# choices - 리스트에서 여러개 랜덤 추출(중복가능)
print(random.choices(a),k=2)

# sample - 리스트에서 여러개 랜덤 추출(중복 불가능)
print(random.sample(a,2))