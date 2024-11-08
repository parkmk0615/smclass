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


with open("c1025/aaa1.html","r",encoding="utf-8") as f:
  soup=BeautifulSoup(f,"lxml")

data = soup.select_one("#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx > div")
pro_lists=data.select("div.adProduct_item__1zC9h")
#print("갯수",len(pro_lists))

# csv 파일 저장
f = open("c1025/nshop.csv","a",encoding='utf-8=sig',newline="")
writer=csv.writer(f)

# 광고 상품 리스트 
for i,pro_list in enumerate(pro_lists):
  print(f"{i+1}.")
  try:
    # 1.제목
    title = pro_list.select_one("div.adProduct_title__amInq > a").text.strip()
    print(title)
    
    # 2. 금액 - 정수형 타입 변경
    price = int(pro_list.select_one("div.adProduct_price_area__yA7Ad > strong > span.price > span.price_num__S2p_v > em").text.strip().replace(",",""))
    print(price)

    # 3. 평점 - float 타입 변경
    rating = float(pro_list.select_one("div.adProduct_etc_box__UJJ90 > span:nth-child(1) > a > span.adProduct_rating__PaMzh").text.strip())
    print(rating)

    # 4. 평가수
    a_count=int(pro_list.select_one("div.adProduct_etc_box__UJJ90 > span:nth-child(1) > a > em").text.strip().replace(",",""))
    print(a_count)

    # 5. 찜 수 
    c_count=int(pro_list.select_one("div.adProduct_etc_box__UJJ90 > span:nth-child(2) > span").text.strip().replace(",",""))
    print(c_count)
    print("-"*50)
    writer.writerow([title,price,rating,a_count,c_count])
  except:
    print("에외처리")

# 실제 상품 리스트

pro_lists=data.select("div.product_item__MDtDF")
print("갯수",len(pro_lists))
f = open("c1025/nshop.csv","a",encoding='utf-8=sig',newline="")
writer=csv.writer(f)

for i,pro_list in enumerate(pro_lists):
  print(f"{i+1}.")
  try:
    title = pro_list.select_one("div.product_title__Mmw2K > a").text.strip()
    print(title)

    price = int(pro_list.select_one("span.price_num__S2p_v > em").text.strip().replace(",",""))
    print(price)

    rating = pro_list.select_one("span.product_grade__IzyU3").text.replace("\n","").replace(" ","").strip()[2:]
    print(rating)

    a_count=pro_list.select_one("div.product_etc_box__ElfVA > a > em").text.strip().replace(" ","").replace(",","").replace("\n","").strip()[1:-1]
    if '만' in a_count:
      a_count = float(a_count[:-1])*10000
    else:
      a_count = float(a_count)
    print(a_count)

    c_count=int(pro_list.select_one("div.product_etc_box__ElfVA > span:nth-child(2) > span").text.strip().replace(",",""))
    print(c_count)
    print("-"*50)
    writer.writerow([title,price,rating,a_count,c_count])
  except:
    print("예외처리")

f.close()