# 기본매개변수로 값 전달 - return 필요, 값 전달 필요
def plus(a):
  a+=10
  print("지역변수a :",a)
  return a

a =10
a = plus(a)
print("전역변수a : ",a)







# 복합매개변수로 값 전달 - 리스트, 딕셔너리는 return 필요없음
def plus(a):
  a[0]=100
  a[1]=200
  print("지역변수a :",a)

a=[10,20]
plus(a)
print("전역변수a : ",a)

