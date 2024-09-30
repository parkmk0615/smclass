stu_title = ['번호','이름','국어','영어','수학','과학','합계','평균']
stu_datas = [[1,'홍길동',100,100,100,99],[2,'유관순',100,99,98,99],[3,'이순신',80,100,90,99],[4,'김구',80,100,90,99],[5,'김유신',80,100,90,99]]

# append - 합계, 평균을 추가해서 출력하시오

stu_title.append('등수')
print(stu_title)

print("[학생 성적 프로그램]")
print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(stu_title[0],stu_title[1],stu_title[2],stu_title[3],stu_title[4],stu_title[5],stu_title[6],stu_title[7],stu_title[8]))
print("-"*70)

for i in stu_datas:
  i.append(i[2]+i[3]+i[4]+i[5])
  i.append((i[2]+i[3]+i[4]+i[5])/4)
  print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))