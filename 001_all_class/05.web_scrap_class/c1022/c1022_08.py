import os
import requests
from bs4 import BeautifulSoup
url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=recent&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=9&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료
# print(res.text)
soup = BeautifulSoup(res.text,"lxml")


#제목,금액, 평점, 평점 참여자 수, 링크 주소, 이미지 주소
# 기준점
data=soup.select_one("#productList")

#금액:90만원 이상,평점:4.5이상,평가수 100명 이상
lists = data.select("li")
# print("제목: ",lists[0].select_one("div.name").text)
# print("금액: ",lists[0].select_one("strong.price-value").text)
# print("금액: ",price)
# print("평점: ",lists[0].select_one("em.rating").text)
# print("평점: ",rating)
# print("평가자 수: ",lists[0].select_one("span.rating-total-count").text)
# print("평가자 수: ",num)
# print("이미지: ","https:/"+lists[0].select_one("dt.image>img")['src'][1:])
# print()

list =[]
for idx,i in enumerate(lists):
  price=int(lists[idx].select_one("strong.price-value").text.replace(",",""))
  rating=float(lists[idx].select_one("em.rating").text)
  num=int(lists[idx].select_one("span.rating-total-count").text[1:-1])
  if price >= 900000 and rating >= 4.5 and num >=100:
    print("링크주소: ","https://www.coupang.com"+lists[0].select_one("a")['href'])
    print("제목: ", i.select_one("div.name").text)
    print("금액 : ",price)
    print("평점: ",rating)
    print("평가자 수",num)
    print("이미지: ","https:/"+lists[0].select_one("dt.image>img")['src'][1:])
    print("-"*50)

  
print(len(a))
