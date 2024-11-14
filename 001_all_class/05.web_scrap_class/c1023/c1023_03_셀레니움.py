
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
browser.get("https://naver.com")

# html위치 찾기 - requests:select
elem=browser.find_element(By.CLASS_NAME,'MyView-module__link_login___HpHMW')
browser.back() # 뒤로가기
browser.forward() # 앞으로가기
browser.refresh() # 새로고침
elem=browser.find_element(By.CLASS_NAME,'pw')
elem=browser.find_element(By.ID,"query")


elem.send_keys("네이버 영화")
elem.send_keys(Keys.ENTER)


elem.click() # 클릭

# 페이지 탭 전환
browser.switch_to.window(browser.window_handles[1])




time.sleep(100)