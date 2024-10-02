# 날짜 출력
# from datetime import datetime
# today = datetime.now()
import datetime 
today = datetime.datetime.now()

# if 12시이상이면 오후, 오전이라고 출력
if today.hour>=12:
  print("오후")
else:
  print("오전")

# print("{}년 {}월 {}일 {}시 {}분 {}초".format(today.year,today.month,today.day,today.hour,today.minute,today.second))
# print(today.year,"년",end='')
# print(today.month,"월",end='')
# print(today.day,"일",end='')
# print(today.hour,"시",end='')
# print(today.minute,"분",end='')
# print(today.second,"초",end='')
 
#-----------------------------------------------------------------------------