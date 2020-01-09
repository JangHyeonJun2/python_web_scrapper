# mty-web-scraper
# python-web-scrapper
-----------
# 개요 
- 파이썬,beautifulsoup와 라이브러리를 활용하여 특정 사이트에 있는 정보들을 수집하여 DataBase에 주기적으로 저장한다. 그리고 사용자 부동산관련 모든 데이터를 볼 수 있게 나열하며, 가상브라우저를 만들고 ip우회하여 스크래핑을 한다.
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

### 목표 가이드 라인

- User Interface 설정
  - 주기적으로 몇몇 사이트에서 부동산 관련 모든 정보를 스크래핑을 한다.그리고 스크래핑된 데이터에서 selector를 뽑아내어 DB table에 저장한다.현재 지금 몇몇 사이트에서는 스크래핑하는 것을 막아놨기 때문에 Proxy를 사용하여 가상브라우저를 만드는데 이 가상 브라우저를 tor(다크 웹)라는 라이브러리를 사용하여 만든다. 그래서 계속해서 IP주소를 변경해가며 스크래핑을 한다.
- DataBase 설정
  - DataBase CRUD 테스트 하기
  - DataBase Schema 완료하기
  - 여러 사이트에서 데이터를 가져오려면 각 사이트에 셀렉터 및 HTML,CSS의 클래스 이름을 알아야한다. 그래서 한 번 스크랩핑을 할 때 계속해서 selector를 바꿔주거나 함수를 여러개 만들어서 코드를 실행해야 하기 때문에 이러한 부분을 기준을 세워 코딩하기.
    
-------------
### 세부사항

- 주기적인 스크래핑 → Proxy로 가상브라우저 만들고, ip우회 → 데이터에서 selector 조회 → 스크래핑한 데이터 및 selector DB 저장
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




