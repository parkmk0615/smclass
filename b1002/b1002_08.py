# 리스트
# in - 데이터가 있는지 확인
# count - 데이터 개수
# find - 데이터가 있는 위치, 없으면 -1 출력 / find(찾을 문자열, 시작위치, 끝위치)
# index - 데이터가 있는 위치, 없으면 에러 

fruit = "사과,배,딸기,포도,복숭아,배,사과,배,딸기"
# 배가 있는지 위치를 모두 출력하시오
search = input("과일 이름을 입력하세요 ")
print("모든 글자")
idx=0
if fruit.count('배')>0:
  for i in range(fruit.count('배')):
    print(f"{search} 글자가 있는 위치 : ",fruit.find(search,idx))
    idx=fruit.find(search,idx)+1
else:
  print("배라는 글자는 없습니다.")




# 문자열 개수확인
# fruit = ['사과','배','딸기','포도','복숭아','배','사과','배','딸기']




# name =input("과일을 입력하세요")
# if name in fruit:
#   print(f"{name}라는 과일이 있습니다.")
#   print("과일 검색 갯수: ", fruit.count(name))
#   print(fruit.find(name))
#   # print(fruit.index(name)) # 과일이 있는 위치의index
# else:
#   print("없습니다.")




# # 리스트의 갯수 확인
# fruit = ['사과','배','딸기','포도','복숭아','배','사과','배','딸기']
# print(fruit.count('배'))
# print(fruit.count('사과'))


#-----------------------------------------------------------------------------



# fruit = ['사과','배','딸기','포도','복숭아']
# # 글을 입력받아 입력한 과일이 있으면, 있습니다 없으면 없습니다 출력
# name = input("과일의 이름을 입력하세요 ")

# if name in fruit:
#   print(f"{name}있습니다.")
# else:
#   print(f"{name}없습니다.")


#-----------------------------------------------------------------------------


#  fruit = "사과,배,딸기,포도"

# if '배' in fruit:
#   print("배가 있습니다.")
# else:
#   print("배가 없습니다.")


#-----------------------------------------------------------------------------

# fruit = ['사과','배','딸기','포도','배']


# if '복숭아' in fruit:
#   print("있습니다.")
# else:
#   print("없습니다.")