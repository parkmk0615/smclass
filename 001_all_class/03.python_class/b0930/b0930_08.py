a_list = [1,2,3]
print(a_list)
a_list.append(4)
print(a_list)
a_list.append(10)
print(a_list)
a_list.insert(0,50)
print(a_list)
a_list.insert(3,20)
print(a_list)

# 삭제 - del - index위치에 데이터 삭제, remove - 데이터 값으로 삭제
del a_list[0]
print(a_list)
del a_list[2]
print(a_list)

a_list.remove(4)
print(a_list)
a_list.remove(1)
print(a_list)

#합계 평균 추가 
stu=[1,'홍길동',100,100,100,99]
stu.append(stu[2]+stu[3]+stu[4]+stu[5])
stu.append((stu[2]+stu[3]+stu[4]+stu[5])/4)
print(stu)


