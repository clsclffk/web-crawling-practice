# https://fs.jtbc.co.kr/RSS/economy.xml

import requests
from bs4 import BeautifulSoup

jtbc_economy = requests.get("https://fs.jtbc.co.kr/RSS/economy.xml")
# print(jtbc_economy.text)

economy_new_soup = BeautifulSoup(jtbc_economy.content, "xml")
print(economy_new_soup)

link_list = economy_new_soup.select("item > link")
print(len(link_list), "건")

# print(link_list[0].text)

news = requests.get(link_list[0].text)
news_soup = BeautifulSoup(news.content, 'html.parser')

# title 추출
title_el = news_soup.find("meta", {"name":"twitter:title"})
title = title_el['content']

# description 추출
desc_el = news_soup.find("meta", {"name":"twitter:description"})
description = desc_el['content']
print(description)

news_list = []

# 반복문
for link in link_list:
    news = requests.get(link.text)
    news_soup = BeautifulSoup(news.content, 'html.parser')

    title_el = news_soup.find("meta", {"name":"twitter:title"})
    title = title_el['content']

    desc_el = news_soup.find("meta", {"name":"twitter:description"})
    description = desc_el['content']
    
    news_list.append([title, description])

import pandas as pd
df = pd.DataFrame(news_list, columns=['title', 'description'])
print(df.head(1))
df.to_csv('jtbc_newsc.csv', index=False)
