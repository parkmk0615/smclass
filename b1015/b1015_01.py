# 함수 - 가변 매개변수+키워드 매개변수 동시 사용

def plus(*n,k=10):
  print("k: ",k)
  for i in n:
    print(i)

plus(1,2,3,4,5)





# 함수 3. 키워드 매개변수
def plus(k=10,m=5):
  print("K ",k)
  print("m ",m)

plus()
# plus(1,2) k=1,m=2로 적용되어서출력 된다.





# 함수 - 2.가변 매개변수
def plus(*n1): # def plus(a,*n) 형태로 사용할시 a(기본매개변수)는 앞 쪽에 사용해야 한다.
  for i in n1:
    print(i)
  print(type(n1)) #튜플 타입 출력
plus(1,2,3,4,5)







# 함수 - 1.기본 매개변수
def plus(n1,n2):
  sum=n1+n2
  print("합계: ",sum)

#함수 호출
plus(10,20)







# 함수선언
def calc(st,end):
  # 구구단
  for i in range(st,end+1):
    print(f"[ {i}단 ]")
    for j in range(1,10):
      print(f"{i} X {j} = {i*j}")


#---------------------------------
#2단~9단
st = 2 
end = 9 
calc(2,9)

#3~7단
calc(3,7)

#5~9단
calc(5,9)
