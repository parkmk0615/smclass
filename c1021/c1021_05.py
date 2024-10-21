import requests

from bs4 import BeautifulSoup

url="https://news.naver.com/main/ranking/popularDay.naver?mid=etc&sid1=111"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res=requests.get(url,headers=headers)
res.raise_for_status()

soup=BeautifulSoup(res.text,"lxml")

print(soup.find("div",{"class":"rankingnews_box_wrap"}))

rankingnews_wrap=soup.find("div",{"class":"rankingnews_box_wrap"}) # find() : 1개 검색
#find_all : 여러개 검색
rankingnews_boxs = rankingnews_wrap.find_all("div",{"class":"rankingnews_boxs"})
print(len(rankingnews_boxs))

print(soup.title)# 제일먼저 찾아지는 것을 출력
print(soup.find("title")) # 특정 위치의 태그과 속성을 가지고찾아줌
print(soup.find("div",{"class":"rankingnews_box_wrap"}))
newlists=soup.find("div",{"class":"rankingnews_box_wrap"}).find_all("div",{"class":"rankingnews_box"})
print("여러개",len(newlists))

for newlist in newlists:
  print(newlist.find("strong",{"class":"rankingnews_name"}))
#print(len(soup.find_all("div",{"class":"rankingnews_box"})))