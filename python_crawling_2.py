from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus

plusUrl = quote_plus(input('검색어를 입력하세요 : '))
pageNum = 1
count = 1

url = f'https://search.naver.com/search.naver?date_from=&date_option=0&date_to=&dup_remove=1&nso=&post_blogurl=&post_blogurl_without=&query={plusUrl}&sm=tab_pge&srchby=all&st=sim&where=post&start={pageNum}'

i = input('몇 페이지를 크롤링 할까요? : ')
lastPage = int(i) * 10 - 9
print(lastPage)
while pageNum < lastPage + 1:
    url = f'https://search.naver.com/search.naver?date_from=&date_option=0&date_to=&dup_remove=1&nso=&post_blogurl=&post_blogurl_without=&query={plusUrl}&sm=tab_pge&srchby=all&st=sim&where=post&start={pageNum}'
    html = urlopen(url)
    soup = bs(html, "html.parser")
    
    # 조건에 맞는 파일을 다 출력해라
    title = soup.find_all(class_='sh_blog_title')

    print(f'---{count}페이지 결과입니다 --------')
    for i in title:
        print(i.attrs['title'])
        print(i.attrs['href'])
        print()
    pageNum += 10
    count += 1