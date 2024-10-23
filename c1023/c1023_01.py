import requests
import csv
from bs4 import BeautifulSoup

url = "http://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료

soup = BeautifulSoup(res.text,"lxml")


data=soup.select_one("#contentarea > div.box_type_l > table")
stocks=data.select("tr")

print(len(stocks))

# 1.상단 타이틀
f=open('c1023/stock.csv','w',encoding='utf-8-sig',newline="")
writer=csv.writer(f)
st_list = [sto.text.strip().replace("\t","") for sto in stocks[2].select("td")]
writer.writerow(st_list)
# 30개 주식 정보를 csv 파일로 저장
for stock in stocks:
  sts=stock.select("td")
  if len(sts) <= 1:
    continue
  sto_list = [ st.text.strip().replace("\t","").replace("\n","")  for st in sts ]
  print(sto_list)





# 2.
#print(socks[1].select("td")) # 항목: 1개
print(sto_list)






  

# with open("c1023/stock.csv","w",encoding="utf-8-sig") as f:
#   writer =csv.writer(f)
#   writer.writerow(sto_list)



# list 생성 방법1
# st_list=[]
# sts=stocks[0].select("th")
# for st in sts:
#   print(st.text)
#   st_list.append(st.text)
# print(st_list)

#list 생성 방법2
# sts=stocks[0].select_one("th")
# st_list=[ st.text for st in sts ]
# print(st_list)
