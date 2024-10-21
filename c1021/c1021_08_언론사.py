import requests
from bs4 import BeautifulSoup

url="https://news.naver.com/main/ranking/popularDay.naver?mid=etc&sid1=111"
headers={"User-Agent":" "}
res=requests.get(url,headers=headers)
res.raise_for_status()

# html 전체를 가져옴
soup=BeautifulSoup(res.text,"lxml")
cont = soup.find("div",{"class":"rankingnews_box_wrap _popularRanking"})
ranklists = cont.find_all("div",{"class":"rankingnews_box"})
print("갯수:",len(ranklists))


# 파일 1줄씩 저장하시오
# 파일 저장
# f=open("a.html","w",encoding="utf-8")
# f.write(res.text)
# f.close()
with open("c1021/news.txt","w",encoding="utf-8")as f:
  print("갯수확인 : ", len(ranklists))
  f.write(f"갯수확인: {len(ranklists)}\n")

  for idx,ranklist in enumerate(ranklists):
    # 언론사 이름 출력
    print(f"[ {idx+1}. 언론사: {ranklist.find("strong",{"class":"rankingnews_name"}).text} ]")
    f.write(f"[ {idx+1}. 언론사: {ranklist.find("strong",{"class":"rankingnews_name"}).text} ]\n")
    news = ranklist.find("ul",{"class":"rankingnews_list"})
    newslists = news.find_all("li")
  # print("랭킹 박스 안 뉴스 갯수 : ",len(newslists))

    for i,newslists in enumerate(newslists):
      print(f"{i+1}: {newslists.find("a").text}")
      f.write(f"{i+1}: {newslists.find("a").text}\n")

print("완료")
