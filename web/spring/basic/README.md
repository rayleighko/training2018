## Spring Basic 

##### Spring을 사용하기 위한 개발 환경을 구성해보자.  

[뒤로가기](/web/spring/README.md)

### Development Environment  

필자의 기본적인 개발 환경은 'Ubuntu 18.04 LTS', 'JDK(Java SE 10.0.1)', 'Eclipse oxygen 3.A - JAVA EE(2018년 6월 이후에는 photon 예정)', 'Tomcat 9.0.8', 'Maven 3.5.9', 'MariaDB 10.1'이다.  

모든 설치자료는 각 회사의 홈페이지에서 다운로드 할 수 있으니 그 부분은 생략하도록 하겠다.  

- [Eclipse](eclipse.org)  
- [JDK](oracle.com)  
- [Tomcat](tomcat.apache.org)  
- [Maven](http://apache.tt.co.kr/maven/)  

### STS(Spring Tool Suite)  

스프링 프레임워크를 사용하다 보면 라이브러리 관리를 비롯하여 개발자가 신경써야 할 부분이 상당히 많다.  

특히 대부분 프레임워크가 그렇듯이 XML 설정 파일을 정확하게 작성하고 관리하는 것이 중요한데, 모든 관리 작업을 전용도구 없이 처리하는 것은 너무 힘든 일일 것이다.

스프링에서는 이런 불편함을 해결하기 위해 STS를 제공한다. STS는 Eclipse Market place에서 설치가 가능하고, 필자가 이 글을 작성할 때를 기준으로 3.9.4 버전까지 사용할 수 있다.  

설치가 완료하고 이클립스를 재실행하면 Preferences에서 Spring 메뉴가 추가된 것을 확인할 수 있을 것이다.  

### Database

데이터베이스의 경우에는 MaraiDB를 이용할 것이며, [여기][여기]를 참고하여 진행할 것이다.  

```
sudo apt update  
sudo apt install mariadb-server mariadb-client  
```
  
설치가 완료되면 관리자 권한으로 mysql을 실행할 수 있다(MariaDB는 MySQL의 불확실한 라이선스 상태에 반발하여 만들어진 GPL v2 라이선스 MySQL이다).  

[여기]: https://websiteforstudents.com/installing-mariadb-database-server-on-ubuntu-18-04-lts-beta-server/

#### 참고도서 

[스프링 퀵 스타드 - 채규태]()
