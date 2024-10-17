import os

f= open("b1017/students.txt","r",encoding="utf-8")
while True:
  line = f.readline()
  if not line:
    break
  print(line.strip())

# 파일 존재여부 확인
if os.path.isfile("b1017/students.txt"):
  print("존재합니다")
else:
  print("없습니다")