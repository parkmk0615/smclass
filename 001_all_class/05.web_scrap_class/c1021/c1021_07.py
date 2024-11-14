import requests
from bs4 import BeautifulSoup

url="https://news.naver.com/main/ranking/popularDay.naver?mid=etc&sid1=111"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res=requests.get(url,headers=headers)
res.raise_for_status()

soup=BeautifulSoup(res.text,"lxml")

print(soup.find("div",{"class":"rankingnews_box_wrap"}))

newlists=soup.find("div",{"class":"rankingnews_box_wrap"}).find_all("div",{"class":"rankingnews_box"})
print("개수: ",len(newlists))

for idx,newlist in enumerate(newlists):
  print(f"{idx+1}.타이틀: ",newlist.find("strong",{"class":"rankingnews_name"}).text)
  ranks=newlist.find("ul",{"class":"rankingnews_list"})
  tlists=ranks.find_all("li")

  for i, t in enumerate(tlists):
    print(i+1,":",t.find("a").text)