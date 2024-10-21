import requests
from bs4 import BeautifulSoup

url="http://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&xfrom=main^gnb"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res=requests.get(url,headers=headers)
res.raise_for_status()

# soup 변환
soup=BeautifulSoup(res.text,"lxml")


print(soup.find("div",{"id":"bestPrdList"}).find("h3").text)
print(soup.find("div",{"id":"bestPrdList"}).find("div",{"class":"pname"}).p.text)


cate = soup.find("div",{"id":"bestprdList"}).find("ul",{"class":"cfix"})
lists=cate.find_all("li")

print("1-28위 갯수: ",len(lists))

for idx,list in enumerate(lists):
  p_title= list.find("div",{"class":"pname"}).p.text
  p_price= list.find("strong",{"class":"sale_price"}).text
  print(f"{idx+1}. {p_title}, 금액: {p_price} 원")