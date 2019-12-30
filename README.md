# mty-web-scraper
# python-web-scrapper
-----------
# 개요 
- 파이썬,beautifulsoup와 라이브러리를 활용하여 특정 사이트에 있는 정보들을 수집하여 DataBase에 주기적으로 저장한다. 그리고 사용자가 검색하는 검색어를 처리하여 DataBase 저장되어있는 정보를 검색어와 비교하여 사용자에게 정보를 보여준다.

--------
# 1주차
- 개발에 필요한 환경설정 준비하기<br>1. visual studio code 설치하기 <br>
2.beautifulsoup4 설치하기 <br>
3.Rmlib와 같은 여러 라이브러리 찾아보기 <br>
4.MTY 회사에서 지금까지 개발한 소스코드 GitHub에서 받아오기 <br>
5.파이썬 , MySQL, PyMySQL 설치하기<br>

- 어디까지 개발 할 것인지 팀원들과 상의하기
  - 개발할 시간이 많지 않은걸 감안하여 팀원들과 서버를 활용하지 않고 콘솔로 웹 페이지에서 가져온 정보를 보여주고 로컬 DataBase에 테이블을 만들어서 정보를 저장하기로 하였다. 여기까지 완성하고 시간이 남으면 더 개발하기로 하였다.

## beautifulSoup사용법과 예제

##### 업데이트(18.05.16) : request 모듈을 통해서 웹에 있는 html 가져오는 부분 추가

- 웹 스크랩핑 

  - 웹 사이트에서 원하는 데이터를 추출함
  - 추추한 데이터를 원하는 형식으로 가공한다.

- 웹 스크래핑 할 때 3가지 단계

  1. Scraping - 데이터 가져오기
  2. Parsing -  데이터 파씽
  3. Manipulation - 데이터 가공

- 필요한 패키지

  - BeautifulSoup
    - HTML과 XML 형식의 데이터를 보다 쉽게 파씽하고 다루는 모듈
  - urllib
    -  URL를 다루는 모듈
    -  파이썬에 기본적으로 내장되어 있는 모듈이다.
  - requests
    - HTTP/1.1 요청을 보낼 수 있다.
    - 요청 내용에 헤더,폼 데이터 , Multipart 파일과  parameter를 포함해서 보낼 수 있다.

- 주요 함수

  - find() 및 find_all함수

    - 함수 인자로는 찾고자 하는 태그의 이름, 속성 기타 등등이 들어간다.
    - find_all(name,attrs,recursive,string,limit,**kwargs)
    - find_all(): 해당 조건에 맞는 모든 태그들을 가져온다.

    ```python
    html = urlopen('url 주소') 
    soup = BeautifulSoup(html, 'html.parser')
    all_divs = soup.find_all("div")
    print(all_divs)
    ------------------
    # find_all('태그명', {'속성명' : '값' ...})
    ex_id_divs = soup.find('div', {'id' : 'ex_id'})
    print(ex_id_divs)
    ```

    - find(name,attrs,recursive,string,**kwargs)
    - find(): 해당 조건에 맞는 하나의 태그를 가져온다. 중복이면 가장 첫 번째 태그를 가져온다.

    ```python
    html = urlopen('url 주소') 
    soup = BeautifulSoup(fp, 'html.parser')
    ex_id_divs = soup.find('div', {'id' : 'ex_id'})
    print(ex_id_divs)
    -----------------
    #find('태그명', {'속성명' : '값' ...})
    first_div = soup.find("div")
    print(first_div)
    ```

    
