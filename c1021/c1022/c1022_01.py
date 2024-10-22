import requests
from bs4 import BeautifulSoup

url="http://news.naver.com/main/ranking/popularDay.naver"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res=requests.get(url,headers=headers)
res.raise_for_status() # 에러 발생 시 종료

# print(res.text)

soup = BeautifulSoup(res.text,"lxml")
# print(soup.prettify()) # html,css 파싱(정렬) 됨




# 태그를 활용한 검색
#find, find_all <=> select_one, select  
#print(soup.find("h2",{"class":"rankingnews_tit"}))
#print(soup.select_one("h2.rankingnews_tit"))
#print(soup.select_one("div#header"))
a = soup.select_one("div.rankingnews_box_wrap")
# b = a.select_one("div.rankingnews_box")
# print("언론사: ",b.select_one("strong.rankingnews_name").text)
# c= b.select("ul.rankingnews_list>li")
b = a.select("div.rankingnews_box")

for idx,news_list in enumerate(b):
  print(f"{[idx+1]}.언론사명: ",news_list.select_one('strong.rankingnews_name').text)
  c=news_list.select("ul.rankingnews_list>li")
  for idx,news in enumerate(c):
    print(f"{idx+1}:",news.select_one("div.list_content>a").text)


