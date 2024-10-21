import requests
from bs4 import BeautifulSoup

url="https://www.melon.com/index.htm"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res=requests.get(url,headers=headers)
res.raise_for_status()

# soup 변환
soup=BeautifulSoup(res.text,"lxml")

with open("c1021/melon.txt","w",encoding="utf-8")as f:
  f.write(soup.prettify())


cont=soup.find("div",{"id":"cont_wrap"})
sing=cont.find("a",{"class":"mlog link-thumb"})

print("제목 ",sing)
print("가수 ")
print("이미지 ")