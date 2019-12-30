from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import urllib.parse


# 네이버 검색 후 검색 결과
baseUrl = 'https://search.naver.com/search.naver?where=post&sm=tab_jum&query='
plusUrl = input('검색어를 입력하세요 : ')
# 한글 검색 자동 변환
url = baseUrl + urllib.parse.quote_plus(plusUrl)
html = urlopen(url)
bsObject = bs(html, "html.parser")

# 조건에 맞는 파일을 다 출력해라
title = bsObject.find_all(class_='sh_blog_title')


for i in title:
    print(i.attrs['title'])
    print(i.attrs['href'])
    print()