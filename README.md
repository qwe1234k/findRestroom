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


