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

#제목, 가격, 평점, 평가수, 찜 정보를 1페이지에서 5페이지 까지 출력
#평점4.8 이상, 평가수 1000명 이상, csv 파일로 저장 

browser=webdriver.Chrome()
browser.maximize_window()
for i in range(1,6):
  url = f"http://search.shopping.naver.com/search/all?adQuery=%EB%AC%B4%EC%84%A0%20%EB%A7%88%EC%9A%B0%EC%8A%A4&origQuery=%EB%AC%B4%EC%84%A0%20%EB%A7%88%EC%9A%B0%EC%8A%A4&pagingIndex={i}&pagingSize=40&productSet=total&query=%EB%AC%B4%EC%84%A0%20%EB%A7%88%EC%9A%B0%EC%8A%A4&sort=rel&timestamp=&viewType=list"
  browser.get(url)
  
  time.sleep(1)

  prev_height = browser.execute_script("return document.body.scrollHeight")
  while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)
    curr_height=browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
      break
    prev_height = curr_height
    print("현재 높이: ",curr_height)
  
  
  soup=BeautifulSoup(browser.page_source,"lxml")
  with open(f"c1025/aaa{i}.html","w",encoding="utf-8") as f:
    f.write(soup.prettify())

  with open(f"c1025/aaa{i}.html","r",encoding="utf-8") as f:
    soup = BeautifulSoup(f,"lxml")

  data=soup.select_one("#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx > div")
  pros=data.select("div.adProduct_item__1zC9h")




