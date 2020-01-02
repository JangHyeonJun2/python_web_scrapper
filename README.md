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
-----------
# 2주차

### 목표 가이드 라인

- User Interface 설정
  - User가 검색어창에 예를 들면 **맨하탄 월세** 라고 치면 이 검색어를 어떻게 처리해서 우리가 DB에 저장해놓은 데이터를 일치 시키서 가져올것인가 설정.
- DataBase 설정
  - DataBase CRUD 테스트 하기
  - DataBase Schema 완료하기
  - 여러 사이트에서 데이터를 가져오려면 각 사이트에 셀렉터 및 HTML,CSS의 클래스 이름을 알아야한다. 그래서 한 번 스크랩핑을 할 때 계속해서 셀렉터를 바꿔주거나 함수를 여러개 만들어서 코드를 실행해야 하기 때문에 이러한 부분을 기준을 세워 코딩하기.
    
-------------
### 세부사항

- 사용자가 검색어 검색 → (검색어 넘겨줌) →searchData(검색어)함수에서 매개변수로 넘겨주고 검색어 관련 데이터를 print() 함수로 보여준다. **여기서 검색어가 "맨하탄 월세" 이렇게 하나의 단어가 아니라 여러개의 단어일 수 있기 때문에 스플릿함수를 써야한다.** 

- Function Naming

  - DB 접속함수

    - def connect(dbUrl,dbId,dbPassword): retrun conn;
    - 따로 클래스를 만들어서 함수를 만들어준다. Insert,Update,Delete문이 실행할 때 필요하기 때문에 클래스로 만들어둔다.

  - 스크래핑해서 가져온 데이터 DB에 넣는 함수

    - def addInfo테이블이름(): 
    - 이 함수는 Information테이블과 member테이블에만 적용하면 된다. 이유는 데이터가 쌓이는 테이블이 이 두개의 테이블 밖에 없다. 나머지 테이블의 데이터는 개발자나 관리자가 직접 데이터를 넣는 테이블이다. 그리고 addInfo함수에서 searchInfo셀렉터 함수를 사용할 텐데 각 변수를 선언해서 return값을 받는걸로 하자. **ex) a = searchInfo셀렉터() **
    - 스크래핑 할 때 셀렉터별로 함수를 지정해야한다.

  - 스크래핑 하는 함수

    - Def searchInfo셀렉터 이름():  return 데이터;
    - 셀렉터별로 함수를 만들어야 함.

  - 메인함수

    - 선택할 수 있는(어떤 기능 쓸건지) 함수 만들기

    - 무한루프 돌리면서 스위치문에서 선택함수 넣기

      | ![image-20200103071241641](/Users/janghyeonjun/Library/Application Support/typora-user-images/image-20200103071241641.png) |
      | ------------------------------------------------------------ |
      | Flowchart                                                    |

