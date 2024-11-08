# 7만원 이하의 항공권 출력
# 김포- 제주 7만원 이하 항공권 갯수 : 15개 , 제주 - 김포: 5만원 이하 항공권 갯수: 30개
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
import random


with open("flight.html","r",encoding='utf-8') as f:
  soup = BeautifulSoup(f,'lxml')


