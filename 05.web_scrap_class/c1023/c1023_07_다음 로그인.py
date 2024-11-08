# 다음 로그인
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
import random


url = "https://www.daum.net"
browser = webdriver.Chrome()
browser.get(url)
#로그인 버튼 클릭
elem=browser.find_element(By.CLASS_NAME,"btn_login")
time.sleep(random.randint(1,3))
elem.click()

# id 입력
elem=browser.find_element(By.ID,"loginId--1")
time.sleep(random.randint(1,3))
elem.send_keys("parkmk0615@naver.com")
# pw 입력
elem=browser.find_element(By.ID,"password--2")
time.sleep(random.randint(1,3))
elem.send_keys("ga135299@")

# 로그인버튼 클릭
elem=browser.find_element(By.CLASS_NAME,"btn_g highlight submit")
elem.click()


input("입력 완료")

