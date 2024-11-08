from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
import random

# 1. 네이버 항공권 페이지 열기
url="http://flight.naver.com/"
browser=webdriver.Chrome()
browser.maximize_window()
browser.get(url)

# 2. 출발지 입력 - 김포
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[1]').click()
browser.find_element(By.CLASS_NAME,"autocomplete_input__qbYlb").send_keys("김포")
time.sleep(1)
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/section/ul/li[2]/a/b').click()

# 3. 도착지 입력 - 제주
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[2]/b').click()
browser.find_element(By.CLASS_NAME,"autocomplete_input__qbYlb").send_keys("제주")
time.sleep(1)
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/section/ul/li/a/b').click()

# 4. 가는 날 - 날짜 선택
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[2]/button[1]').click()
time.sleep(1)
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[4]/button').click()

# 5 오는 날 - 날짜 선택
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[2]/button[2]').click()
time.sleep(1)
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[7]/button/b').click()


# 6 인원 선택 = 1명 추가
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[3]/button').click()
time.sleep(1)
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[4]/div/div/div[1]/div[1]/button[2]').click()


# 7 항공권 검색 버튼 클릭
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/button[1]').click()
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/button[1]').click()
time.sleep(1)

#8. 데이터 검색 동안 대기상태

time.sleep(7)
#-----------------------------------------
# 화면 스크롤 내리기
# 현재 스크롤 높이 검색
prev_height = browser.execute_script("return document.body.scrollHeight")
print("최초 높이 :",prev_height)

# 스크롤 내리기
while True:
  browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
  time.sleep(2)

  # 높이 확인
  curr_height = browser.execute_script("return document.body.scrollHeight")
  if prev_height == curr_height:
    break
  prev_height = curr_height
  print("현재 높이: ",curr_height)

  # 데이터 가져와서 처리
  #Beautifulsoup 데이터 처리
  # 웹 스크래핑
soup=BeautifulSoup(browser.page_source,"lxml")
with open('flight1.html','w',encoding='utf-8') as f:
  f.write(soup.prettify())

input('enter키를 입력하면 프로그램이 종료됩니다.')
browser.quit()


time.sleep(100)