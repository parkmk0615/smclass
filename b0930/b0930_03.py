print("{} 평균 : {:.2f}".format("홍길동", (100+100+99)/3))


# f함수프린트  소수 점 처리 : format을 적용 후 변수 전달
name = "홍길동"
avg = "{:.2f}".format(99.666667)
print(f"{name} 평균 : {avg}")

#### f함수 소수점 자리 출력
a=1.12345
print(f"소수 점 둘째 자리 입력 :  {a:.2f}")


print("출력이 됩니다.")

print("""\
1. 29일 뉴스1에 따르면 유노윤호는 2016년 10월 서울 송파구 풍납동 한 건물을 토지 3.3㎡당 3789만원, 총 163억원에 계약했다. 
    1983년 준공된 해당 건물은 지하 1층~지상 5층, 대지면적 430평, 건축면적 189평에 연면적 1186평으로 지어졌다. 
    현재 삼성생명이 입주 중이다.
      """)








# name="홍길동"
# num=100
# num2=100
# num3=99
# print("%s 합계 : %d" %(name, num+num2+num3))
# print("{} 합계 : {}".format(name,num+num2+num3))
# print("%s 평균 : %.2f" %(name, (num+num2+num3)/3))
# print("{} 평균 : {:.2f}".format(name, (num+num2+num3)/3))

# # 숫자 : 12.12345 , 456.78940, 2.252525
# # 소수 점 둘째 자리까지 출력
# #숫자 : 12.12, 456.79, 2.25
# print("{:.2f} {:.2f} {:.2f}".format(12.12345, 456.78940, 2.252525))

# print("\*") # \ 특정한 문자를 출력할때 사용
# print("안녕\n하세요")
# print("안녕\t하세요")
# print("안녕\b하세요")

# print("29일 뉴스1에 따르면 유노윤호는 2016년 10월 서울 송파구 풍납동 한 건물을 토지 3.3㎡당 3789만원, 총 163억원에 계약했다. \n1983년 준공된 해당 건물은 지하 1층~지상 5층, 대지면적 430평, 건축면적 189평에 연면적 1186평으로 지어졌다. \n현재 삼성생명이 입주 중이다.")
# print("""
# 29일 뉴스1에 따르면 유노윤호는 2016년 10월 서울 송파구 풍납동 한 건물을 토지 3.3㎡당 3789만원, 총 163억원에 계약했다. 
#     1983년 준공된 해당 건물은 지하 1층~지상 5층, 대지면적 430평, 건축면적 189평에 연면적 1186평으로 지어졌다. 
#     현재 삼성생명이 입주 중이다.
#       """)