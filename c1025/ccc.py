from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pyautogui
import time
import requests
from bs4 import BeautifulSoup
import random
import csv
# email 발송관련
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


url = "https://comic.naver.com/index"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup=BeautifulSoup(res.text,"lxml")

data = soup.select_one("#container > div.content_wrap > div.Aside__aside_wrap--iF5ju > div:nth-child(2)")
lists = data.select("#container > div.content_wrap > div.Aside__aside_wrap--iF5ju > div:nth-child(2) > ul > li:nth-child(1)")

for list in lists:
  print(list.select_one("#container > div.content_wrap > div.Aside__aside_wrap--iF5ju > div:nth-child(2) > ul > li:nth-child(1) > div.AsideList__info_area--PVPwn > a > span > span"))

