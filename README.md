# MTY
# python-web-scrapper

[1.개요](#개요)<br>
[2.1주차](#1주차)<br>
[3.2주차](#2주차)<br>
[4.3주차](#3주차)<br>
[5.GitHub Fork 정리](#github-fork-정리)<br>

-----------
# 개요 
- 파이썬,beautifulsoup와 라이브러리 그리고 tor를 활용하여 특정 사이트에 있는 정보들을  DataBase에 주기적으로 저장한다. 그리고 스크래핑할시 ip차단을 피하기 위하여 임의의 ip를 생성하여 접속하는 프로그램이다.
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
- beautifulsoup란?
  - Beautiful Soup은 HTML 및 XML 문서를 구문 분석하기위한 Python 패키지입니다. 웹 스크래핑에 유용한 HTML에서 데이터를 추출하는 데 사용할 수있는 구문 분석 된 페이지에 대한 구문 분석 트리를 만듭니다.
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
    
## Selenium의 정의와 사용법

- selenium이란?
 selenium은 브라우저 자동화,크롤링과 관련된 라이브러리이다. 보통 윈도우 익스플로러 같은 경우 DOM이라는 것을 통해 제어한다. 크롬이나 파이어폭스 같은 경우 웹 드라이버를 따로 지원해줘서 selenium을 통해 제어가 가능하다.
- selenium 설치 및 크롬드라이버 설치
 터미널이나 cmd창에서 pip install selenium을 치면 간단히 설치할 수 있다. 또한 크롬 드라이버는 크롬 버전을 꼭 확인하고 거기에 맞는 드라이버를 설치해야한다.
- ID를 통해 요소 접근하기
[![2020-01-10-2-05-44.png](https://i.postimg.cc/HLNv3nKQ/2020-01-10-2-05-44.png)](https://postimg.cc/QBpqd8jt)
먼저 태그에 접근하기 위해서는 태그 id를 알아야한다. 개발자 도구를 들어간 후 여러가지 항목에 마우스 커서를 올리면 무엇에 관한건지 캡처되어 설명이 나오는 걸 알 수 있다.
- 사용법
1. from selenium import webdriver
2. driver = webdriver.Chrome('C:/chromedriver.exe')
3. driver.get("http://naver.com")
4. elem1=driver.find_element_by_id("query")
5. elem1.send_keys("셀레니움")

3번째 라인 - 크롬 드라이버를 통해 크롬을 연다.<br>
4번째 라인 - 네이버에 접속한다.<br>
5번째 라인 id query라는 이름을 가진 element(요소)에 접근한다.<br>
6번째 라인 - 그 요소에서 “셀레니움”이라는 값을 send(전송) 해준다.<br>

-----------
# 2주차

### 목표

- User Interface 설정
  - 주기적으로 몇몇 사이트에서 부동산 관련 몇몇 정보를 스크래핑을 한다.여기서 스크래핑된 데이터는 selector를 미리 지정하여야 한다. 그리고 데이터는 DB table에 저장한다.현재 지금 몇몇 사이트에서는 스크래핑하는 것을 막아놨기 때문에 Proxy를 사용하여 가상브라우저를 만드는데 이 가상 브라우저를 tor(다크 웹)라는 라이브러리를 사용하여 만든다. 그래서 계속해서 IP주소를 변경해가며 스크래핑을 한다.
- DataBase 설정
  - DataBase CRUD 테스트 하기
  - DataBase Schema 완료하기
  - 여러 사이트에서 데이터를 가져오려면 각 사이트에 셀렉터 및 HTML,CSS의 클래스 이름을 알아야한다. 
    
-------------
### 세부사항

- 주기적인 스크래핑 → Proxy로 가상브라우저 만들고, ip우회 → 지정된 selector를 통하여 데이터 조회 → 스크래핑한 데이터 및 지정된 selector DB 저장
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

    - 프로그램 실행

---------------
# 3주차

#### 스키마 다시작성, Selector바로알기, IP우회해서 사이트 접속하기

- DataBase 스키마 다시작성<br>
요구사항과 프로그램개발 방향이 잘못되어 다시 데이터베이스 설계

- css selector 정의

  - 스타일을 지정할 요소를 선택하는 데 사용되는 패턴입니다.
  - 선택자는 css규치 세트의 일부이다. 그래서 ID,Class,type,attribute 등에 따라 HTML요소를 선택한다. 

  | Selector                                                     | Example                                                      | Example description                                          |
  | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
  | [.*class*](https://www.w3schools.com/cssref/sel_class.asp)   | .intro                                                       | Selects all elements with class="intro"                      |
  | *.class1.class2*                                             | <div class="name1 name2">...</div>                           | Selects all elements with both *name1* and *name2* set within its class attribute |
  | *.class1 .class2*                                            | <div class="name1">  <div class="name2">   ...  </div> </div> | Selects all elements with *name2* that is a descendant of an element with *name1* |
  | [#*id*](https://www.w3schools.com/cssref/sel_id.asp)         | #firstname                                                   | Selects the element with id="firstname"                      |
  | [*](https://www.w3schools.com/cssref/sel_all.asp)            | *                                                            | Selects all elements                                         |
  | *[element](https://www.w3schools.com/cssref/sel_element.asp)* | p                                                            | Selects all <p> elements                                     |
  | *[element.class](https://www.w3schools.com/cssref/sel_element_class.asp)* | p.intro                                                      | Selects all <p> elements with class="intro"                  |

  

- css selector 스크래핑

- css selector가 있어야 사용자가 이 selector를 이용하여 어디 위치인지 바로 알 수 있다.

  - Css selector = 선택자 

  - 선택자란 말 그대로 선택해 주는 요소이다.css 코드에서 특정 요소를 선택하여 스타일을 적용할 때 사용한다. 이 선택자를 이용해 필요한 부분을 선택하여 스크래핑 한다.

  - ```
    #PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li:nth-child(19) > a > span.ah_k
    ```

  - 메모장에 붙여 넣어 보면 이런 선택자가 보인다.여기서 **li:nth-child(19)**에서 숫자 19는 순위를 의미 한다는 것을 알 수 있다. 다른 순위들을 클릭해보면 1등은 **li:nth-child(1)** 같이 규칙적으로 변한다. 만약 이 **li:nth-child(19)** 를 그대로 사용하면 19미만이 출력이 될 것이다. 19등만 선택한 선택자이기 때문이다.그래서 좀 더 포괄적으로 필요한 데이터를 가져오기 위해 **li:nth-child()** 부분을 지워줘야한다.

---------

#### IP우회 코드

- ip를 우회하는 이유

  - 대량으로 크롤링을 시도할 때 이를 방지하기 위해서 웹사이트에서는 로봇으로 인식하여 사이트를

    막아버리는 추세이다.

    따라서 ip를 우회하여 웹페이지가 로봇이 아닌 사람으로 인식 할 수 있도록 먼저 해당 코드를 작성한다.

- 시작하기전에

  1. 컴퓨터에 Tor를 설치

  2. brew services start tor명령어를 사용하여 백그라운드에서 지속적으로 실행

  3. 컴퓨터에 Firefox설치

  4. /usr/local/etc/tor/torrc.sample코드를 torrc로 변경하며 torrc의 코드중 주석되어있는 2개를 주석을 풀어준다.

     ```
     ControlPort 9051
     CookieAuthentication 1
     ```

--------------------

```python
from stem import Signal
from stem.control import Controller
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def switchIP():
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)
```

- switchIp -> ip 전환하는 함수

  ​    Signal.NEWNYM port Tor Control Port(9051)에 신호를 전달하여 Tor에게 라우팅 할 새 회로를

  ​    원한다고 알려준다. 이렇게 하면 새로운 출구 노드가 생겨 다른 IP에서 온 것처럼 보인다.

  - Control Port는 Tor를 제어하는데 사용된다.그리고 밑에서 Socks포트를 이용할텐데 Socks5 실행되는 프록시이다.또한 Tor는 HTTP 프록시가 아니므로 스크립트가 SOCKS5 프록시를 사용하도록 구성되어야한다.

-----------

```python
def my_proxy(PROXY_HOST,PROXY_PORT):
    fp = webdriver.FirefoxProfile()
    # Direct = 0, Manual = 1, PAC = 2, AUTODETECT = 4, SYSTEM = 5
    fp.set_preference("network.proxy.type", 1)
    fp.set_preference("network.proxy.socks",PROXY_HOST)
    fp.set_preference("network.proxy.socks_port",int(PROXY_PORT))
    fp.update_preferences()
    options = Options()
    options.headless = True
    return webdriver.Firefox(options=options, firefox_profile=fp)
```

- my_proxy함수

  headless 모드에서 firefox 브라우저를 이용하여 tor를 프록시로 사용하고 라우팅하도록

  selenium 웹 드라이버를 다운 받아 설정한다.

- 이 코드에서 socks는 socks 서버의 반대쪽에 있는 호스트의 연결 요청을 재지정하여 직접적인 IP 접근 없이 한쪽의 호스트가 다른쪽의 호스트에 완전하게 액세스 할 수 있도록 하는 네트워킹 Proxy Protocol이다. socks 권한 없는 사용자가 인터넷을 통해 내부 호스트에 액세스하는 것은 방지하면서도 socks서버 뒤의 호스트가 인터넷에 완전하게 액세스할 수 있도록 하는 네트워크 방화벽이다.

-------------

```python
for x in range(10):
    proxy = my_proxy("127.0.0.1", 9050)
    proxy.get("https://streeteasy.com/")
    html = proxy.page_source
    soup = BeautifulSoup(html, 'lxml')
    print(soup.find("span", {"id": "ipv4"}))
    print(soup.find("span", {"id": "ipv6"}))
    switchIP()
```

- ​    https://streeteasy.com/로 요청을 보내서 selenium 웹 드라이버를 통해

  ​    요청된 ip를 확인할 수 있다.

  ​    때때로 주소가 ipv4이고 때로는 ipv6이기 때문에 Tor회로의 종료 노드의 ipv4 및 ipv6

  ​    주소를 복사한다. 그런 다음 새로운 Tor 회로를 구축하여 새로운 ip를 요청한다.

##### 실행

[![2020-01-17-5-14-09.png](https://i.postimg.cc/J4jcnPmv/2020-01-17-5-14-09.png)](https://postimg.cc/qzMCDcNx)

**설치되어있는 Tor를 실행시키고, 위에 코드를 실행한다.**



##### 결과

[![2020-01-17-5-13-26.png](https://i.postimg.cc/d3bhmm9f/2020-01-17-5-13-26.png)](https://postimg.cc/q6GBpKSc)

[![2020-01-17-5-13-34.png](https://i.postimg.cc/Kz4j6sqV/2020-01-17-5-13-34.png)](https://postimg.cc/G8wbYz1J)

이렇게 https://streeteasy.com/ 사이트에 접속하는 IP가 다르게 출력이 된다.

------------------
# 4주차

#### 스키마작성 및 임의의 데이터값 넣어보기

**DataBase 스키마**

[![2020-01-17-7-23-22.png](https://i.postimg.cc/VvgXBNhL/2020-01-17-7-23-22.png)](https://postimg.cc/2LqqCCmP)

##### DataBase 설계 고려했던 사항

- Selector는 개발자가 생각하는 것이 아니다.
- 지정된 Selector에서 하위 태그의 Data는 어떻게 처리할 것인가?
- 여러개의 사이트에서 데이터를 가져올 때 데이터가 사이트 URL과 Data를 어떻게 관계를 맺을 것인가?
- Selector에 대응하는 Data 1:1인데 테이블을 어떻게 나눌것인가?
- 지정된 Selector에서 Data 없을 수도 있나?
- Selector테이블과 Data테이블은 나눈다면 관계는 어떻게 할 것 인가?
- Selector테이블과 Data테이블에 Column은 무엇이 들어가겠는가?

--------------

#### IP 우회코드에 스크래핑할 수 있는 함수 넣고 테스트하기

```python
from stem import Signal
from stem.control import Controller
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

# signal TOR for a new connection
def switchIP():
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)

# get a new selenium webdriver with tor as the proxy
def my_proxy(PROXY_HOST,PROXY_PORT):
    fp = webdriver.FirefoxProfile()
    # Direct = 0, Manual = 1, PAC = 2, AUTODETECT = 4, SYSTEM = 5
    fp.set_preference("network.proxy.type", 1)
    fp.set_preference("network.proxy.socks",PROXY_HOST)
    fp.set_preference("network.proxy.socks_port",PROXY_PORT)
    fp.update_preferences()
   # options = Options()
   # options.headless = True
    return webdriver.Firefox(fp)

for x in range(10):
    proxy = my_proxy("127.0.0.1", 9050)
    proxy.get('https://music.naver.com/')
    html = proxy.page_source
    ----------------------------------------------------------------------
    soup = BeautifulSoup(html, 'html.parser')
    body = soup.select('tbody > tr._tracklist_move._track_dsc.list1.on')
    print (type(body), len(body))
    for p in body:
       print(p.text)
    ----------------------------------------------------------------------
    print(soup.find("span", {"id": "ipv4"}))
    print(soup.find("span", {"id": "ipv6"}))
    switchIP()
```

##### 결과

[![2020-01-17-8-07-55.png](https://i.postimg.cc/9M4fgnK5/2020-01-17-8-07-55.png)](https://postimg.cc/bDh8s3q3)



-------------------
# GitHub Fork 정리

### 개요

1. Fork란?
2. Clone,remote 설정
3. Branch 생성
4. 수정 작업 후 add, commit,push
5. Pull Request 생성
6. 코드리뷰,Merge Pull Request
7. Merge 이후 branch 삭제 및 동기화

---------

#### Fork란?

- Fork는 다른 사람의 Github repository에서 내가 어떤 부분을 수정하거나 추가 기능을 넣고 싶을 때 해당 repository를 내 Github repositroy로 그대로 복제하는 기능이다.Fork한 저장소는 원본(다른 사람의 github repositroy)와 연결되어 있다. 여기서 연결되어 있다는 의미는 original repository에 어떤 변화가 생기면(새로운 commit)이는 그래도 forked된 repository로 반영할 수 있다. 그 후 original repository에 변경 사항을 적용하고 싶으면 해당 저장소에 pull request를 해야한다. pull request가 original repository의 관리자로부터 승인 되었으면 내가 만든 코드가 commit,merge되어 original에 반영된다.pull request 하기 전까지는 내 github에 있는 forked repository에만 change가 적용된다.

- 타겟 프로젝트의 저장소를 자신의 저장소로 Fork 한다.

[![2020-01-06-3-12-34.png](https://i.postimg.cc/Ls2yBVVY/2020-01-06-3-12-34.png)](https://postimg.cc/hXZbKT6c)

[![2020-01-06-3-14-07.png](https://i.postimg.cc/QdJL3C47/2020-01-06-3-14-07.png)](https://postimg.cc/v4T27Yd8)

-----------

#### Clone,remote 설정

- fork로 생성한 본인 계정의 저장소에서 **clone or download** 버튼을 누르고 표시되는 url을 복사한다. (중요 - 브라우저 url을 그냥 복사하면 안 된다)

[![2020-01-06-3-19-56.png](https://i.postimg.cc/CKh3L0XQ/2020-01-06-3-19-56.png)](https://postimg.cc/pmSGqw2f)

- 터미널을 켠다(mac기준)

- 자신의 컴퓨터에서 작업을 하기 위해서 Fork한 저장소를 로컬에 clone 한다.

```
git clone https://github.com/JangHyeonJun2/application.git
```

- 로컬 저장소에 원격 저장소를 추가한다. 위 작업과 동일하게 github 저장소에서 **clone or download** 메뉴를 통해서 확인한 url을 사용한다.

  - 원본 프로젝트 저장소 (직접 추가 필요)
  - fork한 로컬 프로젝트 (origin이라는 별명으로 기본으로 추가되어 있다. 따로 추가할 필요 없음)

  ```
  # 원본 프로젝트 저장소를 원격 저장소로 추가
  $ git remote add mty(별명) https://github.com/원본계정/blog.github.io.git
  
  # 원격 저장소 설정 현황 확인방법
  $ git remote -v
  ```

--------

#### branch 생성

- 자신의 로컬 컴퓨터에서 코드를 추가하는 작업은 branch를 만들어서 진행한다.

**개발을 하다 보면 코드를 여러 개로 복사해야 하는 일이 자주 생긴다. 코드를 통째로 복사하고 나서 원래 코드와는 상관없이 독립적으로 개발을 진행할 수 있는데, 이렇게 독립적으로 개발하는 것이 브랜치다. **

```
# develop 이라는 이름의 branch를 생성한다.
$ git checkout -b develop
Switched to a new branch 'develop'

# 이제 2개의 브랜치가 존재한다.
$ git branch
* develop
  master
```

-----

#### 수정 작업 후 add, commit,push

##### pull request 보내기(local 저장소의 수정사항을 remote 컨트리뷰터 저장소로 보내기)

- 먼저 clone한 디렉토리로 이동합니다.

```
janghyeonjun-ui-MacBookPro:~ janghyeonjun$ cd application/
janghyeonjun-ui-MacBookPro:application janghyeonjun$ ls
app.py
```

- develop branch에서 PR을 보내기 위한 수정을 처리하게 되면 PR 보낼 때 문제가 발생하게 됩니다.
  발생할 문제에 대해서는 뒤에 언급 하도록 하겠습니다. develop branch로 PR을 보내므로 develop branch에서 새로운 branch를 생성합니다.

```
janghyeonjun-ui-MacBookPro:application janghyeonjun$ git checkout -b develop-test1
Switched to a new branch 'develop-test1'
```

**develop-test1은 임의로 정한 branch 이름입니다. 개인의 취향에 맞게 작성하시면 됩니다.**

- Application/app.py를 수정하고 commit합니다.

```
janghyeonjun-ui-MacBookPro:application janghyeonjun$ ls
app.py
janghyeonjun-ui-MacBookPro:application janghyeonjun$ vi app.py
janghyeonjun-ui-MacBookPro:application janghyeonjun$ vi app.py
janghyeonjun-ui-MacBookPro:application janghyeonjun$ git add app.py
janghyeonjun-ui-MacBookPro:application janghyeonjun$ git commit -m "Fork연습"
```

- 수정 변경 사항을 내 저장소로 push합니다.

```
janghyeonjun-ui-MacBookPro:application janghyeonjun$ git push origin develop-test1
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 298 bytes | 298.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
remote: 
remote: Create a pull request for 'develop-test1' on GitHub by visiting:
remote:      https://github.com/JangHyeonJun2/application/pull/new/develop-test
remote: 
To https://github.com/JangHyeonJun2/application.git
 * [new branch]      develop-test1 -> develop-test1
```

- 나의 remote 저장소에  develop-test1 branch가 생성되고 commit 내용이 push되었다.

[![2020-01-06-4-06-12.png](https://i.postimg.cc/7ZDcmDHZ/2020-01-06-4-06-12.png)](https://postimg.cc/567n2hQh)

- JangHyeonJun2 저장소의 develop-test1 branch 의 수정된 내용을 koriny저장소의 develp branch로 보내야 합니다. 현재 koriny 저장소의 master branch로 보내도록 되어 있으므로 branch를 develop으로 변경합니다.(하지만 지금 실습에는 koriny에 develop브랜치가 없기 때문에 master로 하였다.)

[![2020-01-07-2-33-06.png](https://i.postimg.cc/nLSPFDvX/2020-01-07-2-33-06.png)](https://postimg.cc/NyT4bLCt)

- 다음 단계에서 Create Pull Request를 클릭하여 PR을 보낸다.

[![2020-01-07-2-34-40.png](https://i.postimg.cc/xTVF1Yb3/2020-01-07-2-34-40.png)](https://postimg.cc/hhM02ksX)

-------

#### 코드리뷰,Merge Pull Request

- PR을 받은 원본 저장소 관리자는 코드 변경내역을 확인하고 Merge여부를 결정한다.

#### Merge 이후 동기화 및 branch 삭제

- 원본 저장소에 Merge가 완료되면 로컬 코드와 원본 저장소의 코드를 동기화 한다.
- 작업하던 로컬의 branch를 삭제한다.

```
# 코드 동기화
$ git pull real-blog(remote 별명)
# 브랜치 삭제
$ git branch -d develop(브랜치 별명)
```

- 나중에 추가로 작업할 일이 있으면 `git pull real-blog(remote 별명)` 명령을 통해 원본 저장소와 동기화를 진행하고 3~7을 반복한다.

-----------
#### 오리지널 저장소의 변경 내역 최신화 하기 - fetch, pull, merge

- 풀리퀘스트를 보내며 프로젝트에 기여하기 시작하면, 프로젝트의 최신화 버전도 가져올 수 있어야 합니다. 그래야 과거의 소스를 가지고 수정하는 불상사가 없을테니까요.mty 저장소를 등록해놓았으니 이 경로를 이용해 프로젝트가 최신 내역인지 확인해보겠습니다.
- 사용할 키워드는 fetch와 merge입니다. 우선 fetch를 이용해 mty 저장소에 변경 내역이 있는지 확인한다.

```
git fech mty
```

- 아무런 변경 내역이 없으면 출력 결과가 없다. 변경 내역이 있으면 결과가 출력된다. 변경 내역이 있으면 변경 내역을 가져올 차례이다.

```
git merge mty/master
```

- mty 저장소의 마스터 브랜치를 우리의 프로젝트에 병합하겠다는 의미입니다. 정상적으로 병합이 완료되면 출력이 나온다.


------------

#### 참고문헌

https://xe1.xpressengine.com/devlog/22791272<br>
https://wayhome25.github.io/git/2017/07/08/git-first-pull-request-story/<br>
https://playinlion.tistory.com/29




