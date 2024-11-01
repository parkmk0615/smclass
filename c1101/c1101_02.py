import datetime
# 현재년도
print(datetime.datetime.now().year)
nowyear=datetime.datetime.now().year
#in_year = input("생일입력 : 20020312")
in_year = "20020312"
print(nowyear-int(in_year[0:4]))
#print(f"현재 나이 : {}")