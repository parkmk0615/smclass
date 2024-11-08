import requests
# 파일 저장
# f=open("a.html","w",encoding="utf-8")
# f.write(res.text)
# f.close()


# naver파일 저장.리솜리조트 파일

# res=requests.get("https://www.naver.com")


# url="http://www.naver.com"
# url="http://www.resom.co.kr/resom/main/main.asp"
# url="http://www.daum.net"

# url=[
#   "http://www.naver.com","https://www.resom.co.kr/resom/main/main.asp","http://www.coupang.com"
# ]

# url=["http://www.coupang.com/"]

# headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
# for i in range(len(url)):
#   res=requests.get(url[i],headers=headers)
#   res.raise_for_status()

# # 파일 저장
#   with open(f"c1021/{i}.html","w",encoding="utf-8") as f:
#     f.write(res.text)

# print("프로그램 종료")

url="http://www.coupang.com/"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res=requests.get(url,headers=headers)
res.raise_for_status()

# print(res.text)

with open("c1021/coupang.html","w",encoding="utf-8") as f:
  f.write(res.text)


  