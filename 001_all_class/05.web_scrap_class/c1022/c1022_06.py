import requests
from bs4 import BeautifulSoup

url="http://www.melon.com/chart/index.htm"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res=requests.get(url,headers=headers)
res.raise_for_status() # 에러 발생 시 종료
soup = BeautifulSoup(res.text,"lxml")

# 순위, 사진 링크 주소, 제목, 가수명

