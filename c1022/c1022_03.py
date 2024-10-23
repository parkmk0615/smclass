import requests
from bs4 import BeautifulSoup

url="http://finance.naver.com/"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res=requests.get(url,headers=headers)
res.raise_for_status() # 에러 발생 시 종료
soup = BeautifulSoup(res.text,"lxml")

# 기준점
data = soup.select_one("#container > div.aside > div > div.aside_area.aside_popular")
# 인기종목
print(data.select_one("span").text)
# 1~5위 종목
pops=data.select("tbody>tr") # tbody에 속한 자식 tr을 모두 가져와라

for i in pops:
  print("회사명 : ", i.select_one("a").text)
  print("현재가: ",i.select_one("td").text)
  #합계구하기
  sum += int(i.select_one("td").text.replace(",",""))



  # next_sbling: 형제관계, find_next_sibling : 형제관계중 검색
  #print("변동: ",i.select_one("td").next_sibling.next_sibling)

  sps= i.select_one("td").find_next_sibling("td").select("span")
  tit=["변동","변동액"]
  for idx,sp in enumerate(sps):
    print(tit[idx],":",sp.text.strip())
  print("-"*30) 
  # print("변동: ",i.select_one("td").find_next_sibling("td").select_one("span").text)
  # print("변동: ",i.select_one("td").find_next_sibling("td").select_one("span").next.next.next.strip())
  
print("합계",sum)