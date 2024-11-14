import requests
from bs4 import BeautifulSoup

url ="https://news.naver.com/main/ranking/popularDay.naver?mid=etc&sid1=111"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

with open("c1021/1.html","w",encoding="utf-8") as f:
  f.write(res.text)


#html, css 정보를 가진 소스변경
soup=BeautifulSoup(res.text,"lxml") # str -> html태그, css태그 사용될 수 있는 ~~~``

print(soup.title)             # title 태그
print(soup.title.text)  # title 태그 문자열 출력 - text, get_text()
print("에러 태그 : ",soup.titletitle)            # 없는 태그 입력시 None 출력
#print("에러 태그 : ",soup.titletitle.get_text()) # 에러 발생
print(soup.a)            # a태그 첫번째 것을 가져옴
print(soup.a.next.text)  # next 다음 태그를 가져옴
print(soup.a.attrs)      # 태그의 속성 값 가져옴 : 딕셔너리 형태 
print(soup.a["href"])    # a태그의 href 속성 값을 가져옴

# 특정 정보 출력
#print(soup.find("div",attrs={"id":"header"}))
print(soup.find("div",{"id":"header"}))  # div 태그id = "header" 
print(soup.find("h2",{"class":"rankingnews_tit"}).text)   # h2 태그class ="rankingnews_tit"의  ~~~
print(len(soup.find_all("div")))  #모든 div 태그를 출력
print(soup.find_all("div"))  #모든 div 태그갯수 출력
print(type(soup.find_all("div")))


#soup.prettify() 정보 저장
# with open("c1021/2.html","w",encoding="utf-8") as f:
#   #  soup.prettify(): 소스가 정리되어 저장됨
#   f.write(soup.prettify())

print("완료")





# print(res.text)

