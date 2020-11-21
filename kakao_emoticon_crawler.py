# pip install BeautifulSoup4
# pip install selenium
# download chromedriver 참고 : https://beomi.github.io/2017/02/27/HowToMakeWebCrawler-With-Selenium/


from selenium import webdriver
from bs4 import BeautifulSoup
import time

# 본인의 크롬드라이버 경로 설정
chromedriver = 'C:/Users/user/Desktop/장봄/2020-2/bda/chromedriver.exe'

# 긁어올 이모티콘 링크 설정
emo_url = "https://e.kakao.com/t/lovely-chocos-day-ver-6"

driver = webdriver.Chrome(chromedriver)
driver.get(emo_url)
time.sleep(5)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
prodList = soup.find_all("img", {"class":"img_emoticon"})

i = 1

for prod in prodList:
    if 'src' in prod.attrs:
        # print(i, end=", ") 그림이 몇개인지 궁금하면 주석 해제
        print("('", end="")
        print(prod['src'], end="', '")
        print(prod['alt'], end="'")
        print(", ''), ")
    i = i+1
print("(", end="'")
print(prod['alt'], end="', '")
print(emo_url, end="')")














