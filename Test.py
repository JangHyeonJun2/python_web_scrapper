from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://rent.heykorean.com/web/us/property/list')
bsObj = BeautifulSoup(html,"html.parser")
main_news = bsObj.find("table",{"class":"rent-list-table"})

