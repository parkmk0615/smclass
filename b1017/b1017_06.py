a=['20', 'tseabrookj', '89', '100', '100', '289', '96.3333333333', '1']
b=['20', '89', '100', '100', '289', '96.3333333333', '1']
t_title =['no','name','kor','eng','math','total','avg','rank']
c=[]


def f_float(value):
  if value.isdigit(): # 정수인지,  실수인지, 문자열인지 구분
    return int(value) # 정수일때 정수 리턴
  else:
    try:
      return float(value) # 실수일때 실수 리턴
    except:
      return value # 문자열일때 문자열 리턴

for idx,value in enumerate(a):
  c.append(f_float(value))
print(c)

# # 숫자로만 구성 - 정수, 실수
# for idx,value in enumerate(b):
#   if value.isdigit():
#     print(f"{idx}번째 {type(int(value))}")
#   else:
#     print(f"{idx}번째 {type(float(value))}")












#  try-except 구문을 사용해서 정수,실수 구분
def tfloat(n):
  try:
    int(n)
    return True
  except:
    return False

# 문자열인지 아닌지 구분
for idx,i in enumerate(a):
  if i.isdigit():
    print(f"{idx} 번째 {i}는 숫자입니다.")
  else:
    print(f"{idx} 번째 {i}는 숫자입니다.")
# for i in b:
#   if tfloat(i):
#     int(i)
#   else: 
#     float(i)
#   c.append(i)
# print(c)


# #b의 리스트를 float으로 변경

# for i in b:
#   c.append(float(i))
# print(c)