# 
def calc(a,b,op):
  if op == '+':
    result = a+b
    return result
  
  elif op == '-':
    result = a-b
    return result

  elif op == '*':
    result = a*b
    return result

  elif op == '/':
    result = a/b
    return result

num1 = int(input("숫자 입력"))
num2 = int(input("숫자 입력"))

op = input("+,-,*,/ 하나를 선택")

print("결과값 : ",calc(num1,num2,op))