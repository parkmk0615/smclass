# aArr=[1,2,3,4,5]
# #a_list =[1,4,9,16,25]
# a_list =[i*i for i in aArr] # 리스트 내포
# print(a_list)

# 1-20 중에 3의 배수만 리스트에 추가
a_list=[]
for i in range(1,20):
  if i % 3 == 0:
    a_list.append(i)
print(a_list)

#리스트 내포
#[ 값 for문 조건식 ]
b_list=[i for i in range(1,21) if i%3==0]
print(b_list)

#--------------------------------------------------------

ss="파이썬 수업중 타입 문자열 타입, 정수형 타입, 실수형 타입, 논리형 타입이 있습니다"
sss= ss.replace(" ","")
print(sss)

a_str = "파이썬"
a="-".join(a_str)
print(a)
# idx =0 
# search=input("검색할 단어를 입력하세요 ")
# a_list=[]
# for i in range(5):
#   num=ss.find(search,idx)
#   a_list.append(num)
#   idx = num+1
#print(f"검색개수:{len(a_list)}, 위치 값: {a_list}")

#--------------------------------------------------------


# i_str = input("글자를 입력하세요")
# # 위치 값
# # find - 값이 있으면 위치 값 반환, 없으면 -1 반환
# idx = ss.find(i_str)
# print("위치 값: ",idx)
# # index - 값이 있으면 위치 값 반환, 없으면 에러발생
# idx = ss.index(i_str)
# print("위치 값: ",idx)
# # count - 입력한 글자의 개수출력
# idx = ss.count(i_str)
# print("개수: ",idx)

# # 타입의 위치값을 모두 출력하시오
# for i in range(ss.count(i_str)):
#   idx= ss.find(i_str)
#   print(idx)




# if i_str in ss:
#   print("있습니다.")
# else:
#   print("없습니다")