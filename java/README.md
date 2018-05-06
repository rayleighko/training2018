# Round 4. Java

### 들어가며

이번 문서는 '**가장 빨리 만나는 코어 자바 9**'를 리뷰하고, 작성한 글로부터 시작한다. 필자는 Java 9이 발표되기 이전에는 Java의 느린 변화 속도, 오픈소스 프로젝트로 진행되는 프로젝트의 수가 적은 것 등으로 인해 Java라는 언어를 부정적으로 보고 있었다. 또한, 국내 시장 속에서 Java, JVM, Oracle, Spring framework가 지배적이기 때문에, 이에 대한 반항이자 남들과 다르고 싶은 욕구가 만나 자바를 멀리했다.  

그러나 Java se 9가 발표되고 6개월 주기로 새로운 버전을 릴리즈 할 것이라는 발표와 자바 EE의 명칭이 자카르타 EE로 바뀌며 클라우드, 오픈소스 중심의 프로젝트로 발전한다는 소식을 듣고 관심이 생겼고, 본 도서를 통해 새로운 마음으로 자바를 다시 공부해보려 한다.  

### 구성

```
java
├───basic
├───oop
├───interface
├───lambda
├───inheritance
├───reflection
├───exception
├───assertion
├───logging
├───generic
├───collection
├───stream
├───io
├───concurent
├───annotation
├───dateapi
├───globalization
├───compiling
├───scripting
└───platformmodulesystem
```
  

본 도서의 구성은 1장에서는 문법을 포함한 간단한 **자바의 기초적인 내용**을 다루며, 2장에서는 **객체 지향 프로그래밍**(**OOP**)에 필요한 기본 내용을 포함한다. 3장에 이르러서는 '**인터페이스**' 개념과 '**람다 표현식**'을 살펴본다. 여기까지가 자바라는 언어를 기본적으로 다루기 위한 기본 역량이 된다.  

그 다음에 소개할 4장의 '**상속**'과 '**리플렉션**', 5장의 '**예외**', '**단정**', '**로깅**'은 프로젝트에 있어서 꼭 필요한 내용이 되며, 마지막 6장의 '**제네릭 프로그래밍**', 7장의 '**컬렉션**', 8장의 '**스트림**' 9장의 '**입출력 처리**', 10장의 '**병행 프로그래밍**'은 자바로 프로젝트를 하며 '**더 나은 개발자**'가 되기 위해 필요한 내용이 된다.  

추가적으로 이후에 등장하는 11장의 '**애너테이션**', 12장의 '**날짜와 시간 API**', 13장의 '**국제화**', 14장의 '**컴파일링과 스크립팅**', 15장의 '**자바 플랫폼 모듈 시스템**'은 자바를 심화적으로 사용하고자 하는 이들을 위한 내용이다.  

이처럼 이 책의 구성은 기본을 지키면서도 그 구성이 탄탄하고 자바와 관련된 대부분의 독자층을 만족시킬 수 있도록 구성되어 있다. 물론, 책의 내용을 보면 입문자에게는 다소 버거운 느낌을 준다.  

왜냐하면 대부분의 입문 서적에는 꼭 실리는 IDE의 설치 방법이나 진도에 사용되는 Library에 대한 구체적인 설명없이 터미널을 사용하며 책의 진도가 진행되기 때문이다. 더불어 기존에 자바를 공부한 이들이라면 문법적인 요소는 쉽게 접근할 수 있겠지만, 터미널 환경에 익숙하지 않다면 다소 버거울 수 있는 구성이다.  

그럼에도 필자가 **이 책을 추천할 수 있는 이유**는 그러한 어려움이 있어야 성장할 수 있기 때문이다. 책을 통해 배우며 고생하는 과정을 거쳐야 자신이 성장할 수 있기 때문에 이 책은 그러한 성장을 즐기는 이들이라면 충분히 감내할 수 있을 정도의 시련을 준다고 느꼈다. 따라서 책의 구성에서 저자의 의도를 파악하여 학습을 진행하는 것이 바람직할 것이다.  

따라서 이 책을 한마디로 정의하자면 `"지름길 없이 Java SE 9을 익히기 위한 가장 확실한 코스"`라고 할 수 있겠다.  

### 1장 [기본 프로그래밍 구조](/java/basic/README.md)   

### 2장 - [객체 지향 프로그래밍](/java/oop/README.md)  

### 3장 - [인터페이스](/java/interface/README.md), [람다 표현식](/java/lambda/README.md)  

### 4장 - [상속](/java/inheritance/README.md)과[리플렉션](/java/reflection/README.md)  

### 5장 - [예외](/java/exception/README.md), [단정](/java/assertion/README.md), [로깅](/java/logging/RAEDME.md)  

### 6장 - [제네릭 프로그래밍](/java/generic/README.md)  

### 7장 - [컬렉션](/java/collection/README.md)  

### 8장 - [스트림](/java/stream/README.md)  

### 9장 - [입출력 처리](/java/io/README.md)  

### 10장 - [병행 프로그래밍](/java/concurent/README.md)  

### 11장 - [애너테이션](/java/annotation/README.md)   

### 12장 - [날짜와 시간 API](/java/dateapi/README.md)  

### 13장 - [국제화](/java/globalization/README.md)  

### 14장 - [컴파일링](/java/compiling/README.md)과 [스크립팅](/java/scripting/README.md)

### 15장 - [자바 플랫폼 모듈 시스템](java/platformmodulesystem/README.md)  

#### 참고자료  

[가장 빨리 만나는 코어 자바 9](http://www.gilbut.co.kr/book/bookView.aspx?bookcode=BN001975&page=1&sernewbook=Y&orderby=pdate&TF=T)
