import urllib.request
import requests
from bs4 import BeautifulSoup
import re
# URL = "https://www.naver.com/"

# 페이지1 부동산 이미지
def GetProductImageList(link):
    if link == 0:
        list_property = []

        go = urllib.request.urlopen(url='https://rent.heykorean.com/web/us/property/list')

        source = go.read()
        go.close()
        soup = BeautifulSoup(source, 'html.parser')
        for all_range in soup.find_all('td', class_='image center'):
            list_property.append(str(all_range))
    #page = requests.get(URL)
    #finance_html = soup.select('div.area_links')
        return list_property
#print(GetProductImageList(0))

# 페이지1 부동산 설명글
def GetProductImformationList(link):
    if link == 0:
        list_property = []

        go = urllib.request.urlopen(url='https://rent.heykorean.com/web/us/property/list')

        source = go.read()
        go.close()
        soup = BeautifulSoup(source, 'html.parser')
        for all_range in soup.find_all('div', class_='title-text'):
            list_property.append(str(all_range))
    #page = requests.get(URL)
    #finance_html = soup.select('div.area_links')
        return list_property
print(GetProductImformationList(0))

# 페이지1 부동산 가격
def GetProductPriceList(link):
    if link == 0:
        list_property = []

        go = urllib.request.urlopen(url='https://rent.heykorean.com/web/us/property/list')

        source = go.read()
        go.close()
        soup = BeautifulSoup(source, 'html.parser')
        for all in soup.find('tbody'):
            for all_range in soup.find_all('td', class_='title'):
                list_property.append(str(all_range))
    #page = requests.get(URL)
    #finance_html = soup.select('div.area_links')
        return list_property
#print(GetProductPriceList(0))