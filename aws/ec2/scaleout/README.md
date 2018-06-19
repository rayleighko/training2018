## Scale Out  

##### Scale out을 이용해 Scalability를 보장하자.  

Scaleout은 여러 대의 컴퓨터가 협력해 동일한 목표를 달성하는 하나의 분산된 컴퓨팅 시슽템을 구성하는 의미를 가진다.  

즉, 하나의 뿌리를 가진 숲을 구성하는 것이라고 볼 수 있다. 각각의 나무가 존재하고, 이 나무들은 하나의 숲을 구성하여 하나의 뿌리를 지닌 숲을 만드는 목표를 달성하는 것이다.  

이러한 Scale out은 작은 서비스에서는 사실상 불필요하다. 그러나 우리가 이를 학습함으로써 Scale up으로는 해결할 수 없는 상황에서 기민하게 대처할 수 있을 것이기 때문에 간단하게 살펴보고 넘어가자.  

#### Scale out의 흐름  

여기서는 주로 Web Application에서의 scale out을 설명한다. 그렇기 때문에 다른 분야에서 활용하고 싶다면 이를 먼저 학습해보고 다른 분야에서 응용하는데 도움이 될 것이다.  

한 대의 컴퓨터로 시작한 우리의 인프라가 어떻게 Scale out을 해나가는지 살펴보도록 하자. 최종 단계의 우리의 인프라는 다음과 같은 3가지 구성요소로 만들어져있다.  

* Web Server: Apache 등의 Web Server Tools
* Middleware: Python의 Django, flask 등의 Web frameworks  
* Database: MySQL 등의 RDB  

이러한 상황에서 CPU의 자원이 고갈되는 상황(사용률이 90% 이상일 때가 주기적으로 일어나는 상황)일 경우에 우리가 해야할 것은 우선적으로 'Scale Up'이다. 그러나 'Scale Up'으로 감당할 수 있는 경우라면 'Scale Out'은 불필요하다.  

그러나 'Scale Up'으로도 감당이 안되는 경우에 우리는 'Sclae Out'을 사용해 우리 인프라의 Scalability를 보장해야 한다.  

이 경우에는 새로운 컴퓨터를 생성해 앞서 설명한 3가지 구성요소를 분산시키는(Out) 방법을 사용한다. 예를들어 DB에서 많은 자원을 사용하고 있다면 DB를 분산시켜 다른 공간에 DB Server를 두는(Out) 과정을 거쳐야 한다.  

> 이 경우 Middleware의 입장에서는 같은 컴퓨터에 있는 DB로의 경로를 새로운 컴퓨터의 경로(IP 등)로 설정해야 하는 등의 불편함이 생길 수 있다.  

그럼에도 Scalability가 보정되지 않아 문제를 찾아보니 Middleware에 문제가 생긴 것으로 판단했다면, 새로운 컴퓨터를 생성해 Middleware가 구성된 Application Server를 생성해야 한다.  

결국 3개의 컴퓨터가 생겨 우리의 컴퓨터는 다음과 같이 분산되었다.  

* Web Server  
* Application Server
* Database Server  

이제 하나의 데이터를 처리하기 위해서는 Web Server에서 요청을 받아 Application Server에 전달하고, Application Server는 필요한 Data를 Database Server에 요구하고, 다시 전달하는 과정을 거치는 아주 복잡한 형태의 인프라가 형성되었다.  

이러한 인프라는 속도가 느려지는 등 성능이 낮아진다거나 비용이 많이 든다거나 하는 등의 불편함이 존재하지만, 이로써 Scalability를 보장할 수 있게 되었다.  

그런데 서비스가 발전되는 과정에 Data가 쌓이게 되고, Database의 성능이 나빠지게 된다. 이러한 상황에서는 다시 Database Server를 분산시켜 쓰기와 읽기의 기능을 나눠 Database Master와 Database Slave를 구성해야 한다.  

> Database Master의 내용을 Database Slave와 동일하게 구성하고 읽기, 쓰기 등으로 기능별 분산을 진행해 Scalability를 보장할 수 있다.  

만약 그럼에도 Database의 성능이 나쁘거나 이후 서비스가 발전되어 Database의 성능이 나빠진다면 Slave를 추가해 여러 대의 Database로 구성시키는 방법이 있다. 그럼에도 보장이 안된다면 'Sharding'을 이용해 Database Master를 여러 개로 분산해 사용자 별로 사용할 Database Master를 지정하는 방식이 있다.  

이제 Database에서의 Scalability를 보장할 수 있다. 그런데 만약 Middleware 부분에서 보유한 자우너보다 많은 자원을 요구한다면 Middleware를 분산시켜 여러 컴퓨터로 구성해 Web Server는 번갈아가며 여러 Middleware를 균등하게 사용하는  방법이 있으니 참고하도록 하자.  

이제까지 Middleware와 Database의 Scalability를 보장하는 방법에 대해 살펴봤다. 마지막으로 Web Server에서의 분산을 살펴보도록 하자.  

Web Server의 경우에는 하나의 IP를 가지고 있으므로, 여러 개의 Web Server로 인프라를 구성한다면 사용자는 하나의 도메인이나 IP로 서비스에 접속할 수 없는 상황이 발생한다.  

기본적으로 이와 같은 상황을 해결하기 위해서는  '사용자의 입장'에서 'Web Server에 접속하는 방법'에 대해 알 필요가 있다. 여기서는 사용자가 도메인을 이용해 DNS를 거쳐 Web Server의 IP로 접속하게 되는 과정을 거치게 된다.  

따라서 DNS를 이용해 사용자 별로 각기 다른, 이미 분산된 Web Server에 접속하게 할 수 있다는 것이다.  

물론, 이런 방법 외에도 앞으로 살펴볼 'Load Balancer'를 이용하는 방법이 존재한다. 'Load Balancer'는 하나의 장치로, 부하(Load)를 조절(Balancing)하는 역할을 한다.  

'Load Balancer'를 이용하면 사용자는 'Load Balancer'의 IP에 접속하게 되고 'Load Balancer'는 각각의 Web Server로 경로를 지정해 사용자의 요청을 분산시킬 수 있는 것이다.

> 만약 사용자가 도메인을 이용한다면 DNS는 더이상 Web Server의 주소가 아닌 Load balancer의 주소를 가리키게 된다.  

그리고 Load Balancer를 사용하면 성능에 따라 사용자의 부하를 분산시킨다거나 종료된 Web Server를 탐지해 다른 Web Server로 요청을 분산시키는 작업을 진행한다.  

#### ELB(Elastic Load Balancer)  

AWS EC2에서는 ELB(Elastic Load Balancer)를 사용해 이를 구성한다. 그리고 사용자의 입장에서 신경쓰지 않아도 괜찮기 때문에 편리하게 사용할 수 있다.  

AWS EC2의 메뉴에서 Load balancing에 존재하는 Load balance에서 간단하게 생성할 수 있다.  

> 생성 시 Load balancer의 Port와 Instance Port를 설정하는데, 사용자가 Load balancer로 접속할 때 80번 포트로 접속하고, Instance로 접속할 때는 8080번 포트로 접속하는 경우가 존재할 수도 있기 때문에 이 점을 유의해야 한다.
>
> Security Group에 대한 설정은 Instance에서와 동일하게 진행하면 된다.  
> 
> 또한, Health Check를 통해 어떠한 컴퓨터의 시스템이 정지되었는지를 판단할 수 있다. 정상적으로 실행되었는지를 판단할 때는 Ping Port를 통해 Ping Path에 정상적으로 접근했을 때로 한다.  

ELB를 사용하기 위해서는 Web Server가 하나 이상 존재해야 한다. 여러 개의 Web Server를 구성하기 위해서는 현재의 Instance를 이미지로 만들어 새로운 Instance를 만드는 방법을 사용하자.  

이제 복사한 Instance와 동일한 Instance가 생성되었다. Load balancer의 정보가 있는 Load Balancers로 이동해 하단의 정보에서 Instnaces에서 장착할 Intances를 설정할 수 있다.  

> 여기서 주의할 점은 각각의 Instance가 Health check의 조건을 만족해야 제대로 작동한다.
>
> 만들어진 ELB에 접속하기 위해서는 만들어진 ELB의 DNS Name으로 접속해야 한다. 이는 ELB 정보에서 확인할 수 있다.  

또한, 우리는 인스턴스의 상황을 계속 모니터링하고 있을 수 없기 때문에 Auto Scaling을 사용해 자동적으로 Scalability를 보장할 수 있는 방법이 존재한다.  

#### 참고자료  
[생활코딩 - Scale out](https://opentutorials.org/course/2717/11332)

