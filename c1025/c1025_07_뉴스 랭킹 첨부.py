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
smtpName = "smtp.naver.com"
smtpPort = 587


url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup=BeautifulSoup(res.text,"lxml")


data=soup.select_one("#wrap > div.rankingnews._popularWelBase._persist > div.rankingnews_box_wrap._popularRanking > div > div:nth-child(1) > a > strong")
lists=soup.select_one("#wrap > div.rankingnews._popularWelBase._persist > div.rankingnews_box_wrap._popularRanking > div > div:nth-child(1)").select('li')

f = open("c1025/news.txt","w",encoding="utf-8") 
print(data.text)
f.write(f"[ {data.text} ] \n")
for list in lists:
  a=list.select_one("a").text
  print(list.select_one("a").text)
  f.write(f"{a}\n")
  

sendmail="parkmk0615@naver.com"
pw="@@@@@@@@"
recvmail="parkmk0615@naver.com"
title ="뉴스"
content="뉴스 랭킹 제목 첨부"

#설정
msg=MIMEMultipart()
msg['subject']=title
msg['from']=sendmail
msg['to']=recvmail
msg.attach(MIMEText(content))

#파일 첨부
with open("c1025/news.txt","rb") as f:
  attachment=MIMEApplication(f.read())#파일첨부
  attachment.add_header('content-Disposition','attachment',filename='news.txt')
  msg.attach(attachment)

  s=smtplib.SMTP(smtpName,smtpPort)
  s.starttls()
  s.login(sendmail,pw)
  s.sendmail(sendmail,recvmail,msg.as_string())
  print("msg: ")
  print(msg.as_string())
  s.quit()
  print("발송 되었습니다.")

f.close()