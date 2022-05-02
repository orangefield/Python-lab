# 크롤링 - BeautifulSoup
# 0. python -m pip install beautifulsoup4
# https://wikidocs.net/85739 참고

import requests
from bs4 import BeautifulSoup

# 1. 주소 복사 (데이터 JSON 아님!!)
html = requests.get(
    "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8")

# print(html.text)

soup = BeautifulSoup(html.text, 'html.parser')

# select 하면 무조건 배열
weather_el = soup.select_one(".weather_graphic .temperature_text > strong")
print(weather_el.get_text())
