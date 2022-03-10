# find_restroom

너무급해!!! 이럴때 화장실을 검색해보세요  
여러분의 구만(ex 서초구, 강남구, ...) 선택하시면 가까운 화장실을 안내해 드립니다.

## 1. 제작기간 & 팀원 소개
* 2022년 3월 7일 ~ 2022년 3월 10일 (총4일)
* 4인 1조 팀 프로젝트  
   - 이성영 : 상세페이지 제작 및 댓글기능구현, DB관리
   - 이현승 : 회원가입, 로그인 기능구현, DB관리, API응답 데이터 처리
   - 이태성 : 서브페이지 제작, API키발급, DB설계 및 관리
   - 홍준기 : 서브페이지 제작, DB관리  

## 2. 사용 기술
  * Back-end
    - python 3
    - Flask (python frame work)
    - MongoDB
  * Front-end
    - bootstrap
    - bulma
    - JQuery
    - AJAX
  * Deploy
    - AWS EC2  
    
## 3. 핵심기능
 * 회원가입 및 로그인
   - JWT를 이용하여 로그인과 회원가입을 구현하였습니다.
   - 회원가입시 아이디를 중복하였는지 확인가능합니다. 
   
 * 서브페이지 기능
   - 각 화장실마다 고유 id를 부여하여 서브페이지 기능을 구현하였습니다.
   - SSR(Server Side Rendering)방식으로 구현하였습니다.  
   
 * 댓글 기능
   - 각 상세페이지마다 댓글의 인덱스와 id를 부여하여 댓글 추가 및 삭제 기능을 구현하였습니다. 
   
 * 구글지도 기능
   - Google cloud platform에서 지도API와 좌표API를 활용하여 상세페이지에 지도 기능을 구현하였습니다.  

## 4. 실행화면
[![누르면 됩니다!](https://img.youtube.com/vi/EKKKtSDHEJg/0.jpg)](https://youtu.be/EKKKtSDHEJg)

## [이슈정리]
* Q1. 화장실 리스트페이지에서 화장실 상세페이지로 이동을 위해서는 각 화장실마다 id를 부여 해야하는데 어떤식으로  
      각 화장실을 규명할 id를 만들어 낼 수 있을까?  
   - A1. 화장실에 대한 DB를 구성할때 ['화장실 이름', '주소', 'id']를 만들어서 넣어주면 각 화장실에대한 id를  
         부여하는것이 될거라고 판단했습니다.  
         따라서 id는 파이썬에서 for문을 이용하여 1부터 N까지 DB에 넣는 순서대로 id를 부여해 주었습니다.  
         그렇게 화장실리스트를 누르면 href = "현재url/화장실id "로 이동하도록하여 각 화장실마다의 id로 상세페이지를 부여해주었습니다.  


* Q2. 화장실에 대한 정보(데이터)를 모아둔 사이트를 크롤링하여 DB에 데이터를 쌓아야했는데, 사이트 혹은 구글지도 등에서 제공하는  
      화장실정보는 사용하기에 너무 불편하게 되어있었던 문제를 어떻게 해결할 것인가?
   - A2. 화장실에대한 정보를 제공해주는 공공데이터포털사이트(API제공 사이트)를 발견하여 여기서  
         화장실이름, 위도, 경도 데이터를 DB에 쌓을 수 있었습니다.  


* Q3. 카카오지도나 구글지도를 크롤링하여서 지도정보를 사용하고 싶은데, 셀레니움이라는 파이썬 라이브러리까지 사용해야 하여 상당히 불편하게 되어있어서 어떻게 하면 지도정도를 가져올 수 있을까?
   - A3. 구글이 제공하는 googlemap API를 사용해보기로 하였습니다. 처음 가입하면 300달러를 지원해주어서  
         이번 단기 프로젝트 하는동안에는 충분하다고 판단되어 구글이 제공하는 map UI와 X,Y좌표를 한국주소로 변환해주는 API를 활용하였습니다.


* Q4.  로그인 페이지에서 ID, PW를 클라이언트 <-> 서버 매칭하여 토큰발행 과정에서 오류 발생.
   - A4. 개발 시 localhost 환경에서는 decode가 이미 되어있어서 필요없는코드였지만,  
         배포 시 리눅스 환경에서는 .decode('utf-8')을 포함시켜서 배포하여 해결하였습니다.  
         ```python
         token = jwt.encode(payload, SECRET_KEY, algorithm='HS256').decode('utf-8')
         ```


