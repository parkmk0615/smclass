from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from bs4 import BeautifulSoup
import random



url="https://www.yanolja.com/"
browser=webdriver.Chrome()
browser.maximize_window()
browser.get(url)

# 1. 검색창 클릭 
elem= browser.find_element(By.XPATH,'//*[@id="__next"]/div/div/header/section/a[2]/div')
time.sleep(1)
elem.click()

# 날짜 선택
time.sleep(1)
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div/div[1]/form/div/div[2]/div[1]/button')
elem.click()

# 11~12
time.sleep(1)
elem = browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td[2]')
elem.click()
time.sleep(1)
elem = browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td[3]')
elem.click()

# 선택 완료 버튼
time.sleep(1)
elem = browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[4]/button')
elem.click()

#인원수 선택 버튼
time.sleep(1)
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div/div[1]/form/div/div[2]/div[2]/button')
elem.click()

# 인원수 선택 완료 버튼
time.sleep(1)
elem = browser.find_element(By.XPATH,'/html/body/div[5]/div/div/section/div/div[2]/div/button')
elem.click()

time.sleep(1)
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div/div[1]/form/div/div[1]/div/input')
elem.send_keys("강릉호텔")
elem.send_keys(Keys.ENTER)

# 강릉 호텔 목록창 접속
# elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div/div[2]/ul[1]/li[2]/a')
# time.sleep(1)
# elem.click()

# 자동로딩 대기
# 화면의 호텔검색 내용이 뜰때까지 대기, 최대 30초 대기
WebDriverWait(browser,30).until(lambda x:x.find_element(By.XPATH,'//*[@id="__next"]/div/main/section/div[2]'))

# 화면 스크롤 내리기
# execute_script() : 자바 스크립트 실행 함수
prev_height = browser.execute_script("return document.body.scrollHeight")


while True:
  browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
  time.sleep(1)
  # 로딩 되면서 늘어난 페이지 길이를 다시 가져옴
  curr_height = browser.execute_script("return document.body.scrollHeight")
  # 페이지를 스크롤해서 길이가 더 길어졌는지 확인
  if prev_height == curr_height:
    break
  # 길이가 더 길어졌으면, 이전 길이에 현재 길이를 입력시킴
  prev_height = curr_height
  print("현재 높이 :",curr_height)


print("스크롤 완료")

# 파일 생성
soup = BeautifulSoup(browser.page_source,"lxml")
# html저장하기
with open('c1024/yanolja.html','w',encoding='utf-8') as f:
  f.write(soup.prettify())

# 파일 불러와서 soup으로파싱
with open("c1024/yanolja.html","r",encoding="utf-8") as f:
  soup = BeautifulSoup(f,"lxml")



# 평점이 4.8이상, 금액이 17만원 이하 검색 후 출력
#1. 
# 호텔명:
# 평점 : 
# 금액 : 
# --------
data = soup.select_one("div.PlaceListBody_listContainer__2qFG1")
lists= data.select("a.common_clearfix__M6urU")
print("갯수: ",len(lists))
search_list = []
for idx, i in enumerate(lists):
  try:
    name=i.select_one("div.PlaceListTitle_container__qe7XH>strong").text.strip()
    rating=float(i.select_one("span.PlaceListScore_rating__3Glxf").text.strip())
    price=int(i.select_one("span.PlacePriceInfoV2_discountPrice__1PuwK").text.strip().replace(",",""))
    if rating >=4.8 and price <=170000:
      print(f"[ {idx+1} ]")
      print("호텔명: ",name)
      print("평점: ",rating)
      print("금액: ",price)
      search_list.append([idx+1,name,rating,price])
  except Exception as e:
    print(f"{idx+1}번째 예외처리: ",e)


time.sleep(100)

#input("엔터키를 누르면 완료 됩니다.")


#---------------------------------------------


search_list.sort(key=lambda x:x[2])
print(search_list[0])