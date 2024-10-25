from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from bs4 import BeautifulSoup
import random
from selenium.webdriver.chrome.options import Options
import pyautogui
import csv


# 네이버 쇼핑 검색창 입력 enter 키 입력
# 네이버  쇼핑 클릭
# 네이버 쇼핑에서 무선 마우스 검색창 입력 enter 키 입력

url="https://naver.com"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

elem =  browser.find_element(By.ID,"query") 
elem.send_keys("네이버 쇼핑")
time.sleep(1)
elem.send_keys(Keys.ENTER)

time.sleep(1)
elem =  browser.find_element(By.CLASS_NAME,"link_name")
time.sleep(1)
elem.click()

time.sleep(1)
browser.switch_to.window(browser.window_handles[1])
time.sleep(1)

elem=browser.find_element(By.CLASS_NAME,"_searchInput_search_text_3CUDs")
elem.send_keys("무선 마우스")
elem.send_keys(Keys.ENTER)

time.sleep(100)





#제목, 가격, 평점, 평가수, 찜 정보를 1페이지에서 5페이지 까지 출력
#평점4.8 이상, 평가수 1000명 이상, csv 파일로 저장 

# browser=webdriver.Chrome()
# browser.maximize_window()
# for i in range(1,6):
  # url = f"http://search.shopping.naver.com/search/all?adQuery=%EB%AC%B4%EC%84%A0%20%EB%A7%88%EC%9A%B0%EC%8A%A4&origQuery=%EB%AC%B4%EC%84%A0%20%EB%A7%88%EC%9A%B0%EC%8A%A4&pagingIndex={i}&pagingSize=40&productSet=total&query=%EB%AC%B4%EC%84%A0%20%EB%A7%88%EC%9A%B0%EC%8A%A4&sort=rel&timestamp=&viewType=list"
  # browser = webdriver.Chrome()
  # browser.maximize_window()
  # browser.get(url)
  # soup=BeautifulSoup(browser.page_source,"lxml")
  # time.sleep(1)


  # data=soup.select_one("#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx")
  # lists=data.select("adProduct_item__1zC9h")

  # f= open("c1025/navershop.csv","w",encoding="utf-8")
  # writer=csv.writer(f)
    



