from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://finance.naver.com/sise/sise_index.nhn?code=KOSPI"
page = urlopen(url)
soup = BeautifulSoup(page, 'lxml')
print(soup.title)

#코스피 정보 가져오기
kospi_info = soup.find("em", id="now_value")
print(kospi_info.text)

#거래량 천주 정보 가져오기
deal_info = soup.find("td", id="quant")
print("거래량: ", deal_info.text)

#장중 최고 정보 가져오기
max_price = soup.find("td", id="high_value")
print("장중 최고: ", max_price.text)

#52주 최고 정보 가져오기
tmp_index = soup.find("table", class_="table_kos_index")
tmp_52week = tmp_index.find_all("tr")[2].find("td")
print(tmp_52week.text)

max_price_52week = soup.find("td", id="high_value")
print("장중 최고: ", max_price.text)

# 시황뉴스 -ul
tmp_news = soup.find("ul", class_="sise_report")
# print(len(tmp_news))
# print(tmp_news)
tmp_li_all = tmp_news.find_all("span", class_="tit")

news = []
str1 = ""
for one in tmp_li_all:
    # print(one.text)
    news.append(one.text)
    str1 = str1 + one.text + ","

# print(news)
# print(str1)
#코스피 정보, 거래량(천주), 장중최고, 52주 최고, 시황뉴스
# no, 코스피 정보, 그래량(천주), 장중최고, 52주 최고, 시황뉴스
# 1, ____,        ___,        ____,    ____,     ____

#시황뉴스 목록을 csv 파일로 만들기
import pandas as pd
dat = pd.DataFrame( {"시황뉴스":news} )
print(dat)
dat.to_csv("news.csv", index=False)
dat.to_excel("news_excel.xlsx", index=False)


