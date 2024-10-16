#  파일 읽기 -r
# 위치에 파일이 없으면 에러

# 1. readline() - 1줄씩 읽어오기
# 가장 바깥 폴더의 위치에서 파일을 찾음
# # f= open('c:/aaa/a.txt','r',encoding='UTF-8')

# 2. readlines() - 모든 글을 읽어오기
# f=open('a.txt','r',encoding='utf-8')
# lines=f.readlines()
# for line in lines:
#   print(line.strip())
# f.close()

# 3.read()
# f = open('a.txt','r',encoding='utf-8')
# for line in f:
#   print(line.strip())
# f.close()

#----------------------------------------------------

# 파일 쓰기 - w : 파일 생성 후 글자 입력
# f = open('aa.txt','w',encoding='utf8')
# for i in range(1,11):
#   data=f"안녕하세요.{i} \n"
#   f.write(data)
# f.close()
# print("글쓰기 종료")

# while True:
#   print("[ 메모장 ]")
#   data= input("저장하려는 글자를 입력하세요.")
#   f=open("aa.txt","w",encoding='utf-8')
#   f.write(data)
#   f.close()

#----------------------------------------------------

# 파일 이어쓰기  - a
# while True:
#   print("[ 메모장 ]")
#   data= input("저장하려는 글자를 입력하세요.")
#   f=open("aa.txt","a",encoding='utf-8')
#   f.write(data+"\n")
#   f.close()

#----------------------------------------------------

# 파일 with - close()하지 않아도 됨
# with open("aa.txt","w",encoding="utf-8") as f:
#   f.write("안녕하세요")




# f = open('aa.txt','w',encoding='utf8')
# f.write("안녕하세요.1\n")
# f.write("안녕하세요.2\n")
# f.write("안녕하세요.3")
# f.write("안녕하세요.4")
# f.close()
# print("글쓰기 종료")








# 절대 경로를 사용
# f= open('c:/aaa/a.txt','r',encoding='UTF-8')
# f= open('b.txt','r',encoding='UTF-8')
# while True:
#   line =f.readline()
#   if not line:break
#   print(line.strip()) # .strip() : \n 생략
# f.close()