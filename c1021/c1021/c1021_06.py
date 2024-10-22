import requests
from bs4 import BeautifulSoup

url="https://news.naver.com/main/ranking/popularDay.naver?mid=etc&sid1=111"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res=requests.get(url,headers=headers)
res.raise_for_status()

soup=BeautifulSoup(res.text,"lxml")

print(soup.find("div",{"class":"rankingnews_box_wrap"}))

newlist=soup.find("div",{"class":"rankingnews_box_wrap"}).find("div",{"class":"rankingnews_box"})

print(1,"="*20)
print(newlist)
print(1,"="*20)
#next:검색태그 다음 뒤에오는 태그를 찾아줌
#next_sibling :검색 태그의 형제 관계의 다음 태그를 찾아줌
print(newlist.next_sibling.next_sibling)


print("여러개",len(newlist))