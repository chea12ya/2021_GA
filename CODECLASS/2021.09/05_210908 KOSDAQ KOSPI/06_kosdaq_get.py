#코스닥 정보에 대한
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://finance.naver.com/sise/sise_index.nhn?code=KOSDAQ"
page = urlopen(url)
soup = BeautifulSoup(page, 'lxml')
print(soup.title)

kosdaq_dat_list = ['코스닥지수', '거래량']
kosdaq=[]
# KOSDAQ 지수 정보 20210908_14_index.csv

kosdaq_info = soup.find("em", id="now_value")
print(kosdaq_info.text)
kosdaq_info.append(kosdaq_info.text)

deal_info = soup.find('td', id='quant')
print("거래량", deal_info.text)
kosdaq_info.append(deal_info.text)

high_info = soup.find('td', id="high_value")
print("장중최고", high_info.text)

kosdaq_info.append(high_info.text)

# KOSDAQ 지수 정보를  csv 파일로 만들기

news=[]
str1 = ""

import pandas as pd
dat = pd.DataFrame( {"210908 KOSDAQ 지수":news} )
print(dat)
dat.to_csv("210908 KOSDAQ 지수.csv", index=False)

# 시황정보 뉴스 20210908_14_news.csv

tmp_news = soup.find("ul", class_="sise_report")
tmp_li_all = tmp_news.find_all("span", class_="tit")

news = []
str1 = ""
for one in tmp_li_all:
    # print(one.text)
    news.append(one.text)
    str1 = str1 + one.text + ","

print(news)
print(str1)

# 시황정보 리포트 20210908_14_report.csv

tmp_report = soup.find("ul", class_="sise_report")
tmp_li_all = tmp_report.find_all("span", class_="tit")

report = []
str2 = ""
for one in tmp_li_all:
    # print(one.text)
    report.append(one.text)
    str2 = str2 + one.text + ","

print(report)
print(str2)

#인기검색어 20210908_14_pop_word.csv
#가장 많이 본 뉴스 20210908_14_cnt_news.csv


