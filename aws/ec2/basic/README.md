## AWS EC2 Basic  

##### AWS EC2의 기본적인 내용에 대해 살펴보자.  

[뒤로가기](/aws/README.md)  

### EC2

AWS에 로그인하여 접속하면 'Compute' 부분에 EC2가 보인다. EC2를 클릭해 들어가서 우리의 Region을 작업자 혹은 사용자의 지역과 가장 가까운 곳으로 지정하도록 하자. 필자의 경우 Asia public(seoul). 

EC2는 가장 범용적인 서비스이면서도 활용도가 높다. 쉽게 말해 EC2는 사용자에게 독립된 컴퓨터를 제공해준다고 보면 된다.  

#### 속성으로 Instance 생성하기  

하나의 instance는 1개의 컴퓨팅 파워를 나타낸다. 우리가 3개의 인스턴스를 사용한다면, 3대의 컴퓨터를 사용하는 것과 같다고 보면 된다.  

우리는 실습을 위해 무료 버전을 사용하고 있으므로 선택지는 좁다. 탭에서 Instance를 찾아 Lanch해주자. 당연히 모든선택은 free tier로만 지정하자. 그렇지않으면 낭패를 볼 수 있다.   

과정을 계속 진행하다 보면 Tags를 설정하거나 Rules를 설정하는 화면이 등장한다. 우리는 기본적인 내용만 설정하므로 Tags에서는 key를 Name으로 하는 '웹서버'를 하나 설정하고, Rules에서는 SSH와 HTTP를 설정하도록 하자.  

과정을 계속 진행하다 보면 key 파일을 생성해 \*.pem이라는 다운로드 하게 된다. 여기서 발급딘 key는 우리의 instance를 구분하기 위한 key임과 동시에 일련의 비밀번호를 상징한다. 관리에 유의하자.  

이 과정까지 끝났다면 우리는 하나의 컴퓨팅 파워를 얻게 되었다. 이제 이를 조작해 웹서버를 운영하거나 빅데이터를 관리할 수도 있고, 필요한 운영체제를 사용할 수도 있다.  

### 깊게 Instance 생성 다루기

#### Choose AMI(Amazon Machine Image)  

운영체제는 크게 UNIX 기반 운영체제와 Windows 기반 운영체제로 나눌 수 있다. EC2에서는 1년동안 다양한 서버 환경을 무료로 제공한다. 실습에서는 free tier로 충분하므로 추가적인 설명은 진행하지 않겠다.  

#### Choose Instance Type  

Computing Power를 설정할 수 있는 페이지이다. 여기서는 다양한 컴퓨팅 파워를 설정할 수 있는데 free tier에서는 t2.micro만 선택이 가능하다.  

컴퓨팅 파워를 선택할 때는 vCPUs(Amazon에서 측정한 상대적 가상 CPU 성능, 일반적인 CPU의 파워와는 다르므로 직접 사용해 그 차이를 느껴보는 것을 권장함)와 Memory, Network Performance(전송 속도라고 생각하면 된다)를 구분하여 고르도록 하자.  

> 장비는 상대적으로 성능이 측정되어 있기 때문에 free tier를 사용하면서 그 성능을 느껴보고 필요한 성능을 선택하도록 하자.  

또한, 가격정책도 민감한 부분이다. 각 컴퓨팅 파워는 제공되는 성능에 비례해 가격이 올라간다. 여기서는 free tier의 가격 정책만 소개하고 넘어갈테니 필요하다면 [AWS EC2 가격정책](https://aws.amazon.com/ko/ec2/pricing/)을 참고하자.  

##### 예약 인스턴스  

예약 인스턴스를 구매하면 1, 3년 단위로 계약을 해 상대적으로 저렴한 가격으로 사용할 수 있다.  

##### 스팟 인스턴스  

스팟 인스턴스는 인스턴스의 가격이 주가처럼 가변적이라는 말이다. AWS측에 놀고 있는 컴퓨터가 많으면 가격이 저렴하고, 컴퓨터가 적으면 가격이 비싸지는 경향을 보인다. 이에 대해서는 추후에 살펴보도록 하자.  

##### AWS EC2 Free tier의 가격정책  

Free tier에서는 EC2를 월별 750시간 제공한다. 이 말의 의미는 하나의 Instance를 750시간, 2개의 Instance를 325시간 제공한다는 말이다. 즉, 1개의 인스턴스를 매일 돌린다고 해도 750시간을 채우기는 힘들다(31일이라고 해도 744시간이므로).  

더불어 원하는 범용(SSD) 또는 마그네틱 조합으로 Amazon Elastic Bolck Storage를 30GB 제공하고, I/O 200만 건, 모든 AWS 서비스를 합산해 15GB의 데이터를 전송하게 되면 과금이 발생한다.  

> 위의 어려운 내용을 쉽게 설명하면 우리가 임대한 컴퓨터의 저장장치의 무료 용량은 최대 30GB이고, 이 저장장치에서 데이터를 읽고 쓰는 것이 200만 건 이상 발생하면 과금을 부가하겠다는 의미이다.  

#### Configure Instance  

우리가 만들고자 하는 컴퓨터의 여러 세팅을 진행할 수 있다. Instance의 개수를 지정하거나 Spot Instance로 지정하거나 네트워크과 관련된 설정을 진행할 수 있다.  

또한, 운영체제에서 컴퓨터를 종료(shutdown)했을 때 인스턴스를 종료시킬 것인지 삭제시킬 것인지를 설정할 수도 있고, 실수로 인스턴스를 삭제하는 것을 방지하는 기능, 인스턴스의 상태(CPU의 상태, Memory 점유율 등)을 구체적으로 저장하는 기능이 존재한다.  

#### Add Storage  

컴퓨터의 저장 장치(EBS: Elastic Block Storage)를 장착하는 설정이다. 앞서 언급한 것처럼 무료로 30GB까지 사용할 수 있다.  

또한, 저장장치의 타입을 설정(SSD, Magnetic 등)할 수 있다. 선택에 의해 IOPS가 증가하게 되는데, 가격과 정비례하므로 유의하도록 하자.  

Delete on Termination을 선택하면 컴퓨터가 Termination되면 저장장치도 같이 삭제하는 개념이다(선택하면 내장하드, 안하면 외장하드).   

#### Tag Instance  

어떤 인스턴스를 만들면 해당하는 인스턴스가 어떤 역할을 하는지, 누가 관리자인지 등을 설정할 수 있다(한글 가능). 즉, 인스턴스에 대한 설명을 저장한다.  

#### Configure Security Group  

보안과 관련된 페이지인데, 일종의 방화벽 역할을 하는 기능을 설정할 수 있다. 우리가 생성한 인스턴스에 접속할 수 있는 권한을 설정하는 것이다.  

중복되지 않게 그룹 이름을 설정하고, 이 그룹에 해당하는 정책을 설정할 수 있다. SSH와 HTTP같은 Protocol을 설정한다고 보면 된다.  

이렇게 설정된 정책만을 통해 우리의 인스턴스에 접근할 수 있도록 하는 기능이다.  

SSH는 Secure SHell의 약자로, 리눅스나 맥같은 유닉스 계열의 원격제어 방식을 이야기한다. 후반부에 source(송신측)를 설정하는 것은 허용할 SSH의 Address를 설정하는 것임을 참고하자. 여러 개의 IP를 설정하고 싶다면 새로운 SSH를 생성해서 custom ip를 설정해 진행하도록 하자.   

> 만약 Instance가 Windows라면 SSH가 아닌 RDP를 통해 원격제어를 진행해야 한다.  

만약 인스턴스를 웹 서버로 사용해 이용자들이 웹 브라우저를 통해 인스턴스에 접근하는 것을 허용하려면 HTTP를 설정해야 한다. 여기서의 source를 하나의 IP로 설정하면 그 해당 IP에서만 웹 브라우저를 통해 접근할 수 있는 것이다.  

#### Review  

마지막 단계에서는 우리의 인스턴스를 다시 한 번 점검하고, Password를 설정한다. AWS EC2에서는 자체적인 보안을 통해 자동으로 key pair을 제공한다. key pair의 이름을 설정하고 Download를 진행하도록 하자.  

한 번 저장하고, 인스턴스를 생성하면 이후에 더이상 발급받을 수 없기 때문에 이 점 유의하도록 하자. 더불어 생성한 key pair는 추후에 인스턴스에 접근하기 위해서는 필수적이기 때문에 

> 추가적으로 public key pair와 private key pair가 존재하는데, 여기에 대해서는 따로 찾아보기 바란다.  

### Linux Ubuntu Instance에 웹 서버 설치하기  

우선 인스턴스는 running 상태여야 한다. 상태를 확인한 후 AWS의 콘솔(웹사이트)에서 connect 버튼을 클릭하자.  

그러면 자세한 설명이 나오는데 필자는 Linux 환경이므로 다음과 같이 진행했다(rayleigh_web.pem은 필자의 key pair이고, ec2-13~ 하는 부분은 필자의 인스턴스 식별번호이다).  

> 1. Open an SSH client. (find out how to connect using PuTTY)
>
> 2. Locate your private key file (rayleigh_web.pem). The wizard automatically detects the key you used to launch the instance.
>
> 3. Your key must not be publicly viewable for SSH to work. Use this command if needed:
> chmod 400 rayleigh_web.pem
>
> 4. Connect to your instance using its Public DNS:
> ec2-13-125-237-254.ap-northeast-2.compute.amazonaws.com
>
> Example: ssh -i "rayleigh_web.pem" ubuntu@ec2-13-125-237-254.ap-northeast-2.compute.amazonaws.co  

이 과정을 거치면 우리는 해당 인스턴스의 터미널에 접속하게 된다(인스턴스의 식별번호는 stop 후 start하게 되면 바뀌니 참고하도록 하자).  

이후에는 리눅스 환경으로 진행되므로 리눅스에 익숙하지 않다면 주의하도록 하자.  

```
ubuntu@ip-172-31-31-193:~$ sudo apt-get update  
// 패키지 저장소 최신화

ubuntu@ip-172-31-31-193:~$ sudo apt-get install apache2
// apache2 패키지 설치 - 자동으로 시작된다.  
```
  

아파치 서버가 실행된 것을 확인하고 이를 웹 브라우저에서 확인하고자 한다면 해당 인스턴스의 도메인 주소 혹은 IP 주소를 알아야 한다. AWS 콘솔에서 인스턴스를 눌러 하단의 정보를 확인하자.  

> Public IP가 IP 주소이고, Public DNS가 도메인 주소이다.  

이제 웹 브라우저에서 IP 주소 혹은 도메인 주소로 접속해보면 우리가 설치한 웹 서버가 제대로 구동되는 것을 확인할 수 있다.  

여기서 제공되는 페이지는 우리의 인스턴스에 존재하는 '/var/www/html' 디렉터리 안에 있는 index.html를 보여주는 것이므로 index.html을 수정하면 수정된 정보가 기록된다.  

index.html의 내용을 모두 지우고 'Hello~'를 입력해보자. 어떤 변화가 있는가?  

```
Hello~
```
  
우리는 앞서 Security Group을 설정했기 때문에 HTTP를 통한 접근(웹 브라우저)과 SSH를 통한 접근(유닉스 터미널)에 대한 권한이 주어진 것이다. 만약 이를 설정하지 않았다면 접근에 문제가 생기므로 이에 대해 유의하도록 하자.  

#### Marketplace  

지금까지는 우리만의 인스턴스를 만들었다면, 이제는 다른 사람이 만든 EC2의 인스턴스를 사용하는 방법에 대해 알아볼 것이다.  

AWS에서는 인스턴스에 설치할 이미지를 AMI라는 형태로 제공한다. 앞서 'Lanch Instances'를 눌러 나오던 내용의 빠른 이해를 위해 AMI를 '하나의 운영체제'라고 이야기했다. 사실 정확하게 설명하면 AWS에서 제공하는 운영체제 이미지 형식을 말한다.  

> 우리가 앞서 만든 인스턴스의 경우에도 Lanch Instances를 눌러 나오는 Choose AMI 탭에서 좌측 메뉴의 My AMIs를 눌러 선택할 수 있는 것이다.  

이와 더불어 좌측의 메뉴를 살펴보자. 일반적으로 우리가 다른 사람의 AMI를 가져오기 위해서는 Marketplace를 이용하거나 Community AMIs를 이용해야 한다.  

여기서 우리는 Marketplace를 사용할 것이다. 가령 WordPress가 이미 설치되서 바로 서비스를 할 수 있는 이미지(AMI)를 Marketplace에서 찾아 바로 설치할 수 있다.  

여기서는 해당 AMI의 Rigion과 Instance type(free tier - t2.micro), 보안 설정 등을 선택해 인스턴스를 생성할 수 있다. 굉장히 편리한 기능이라고 할 수 있다.  

> 여기서 주의할 점은 AMI 생산자에 따라 인증 절차도 다르기 때문에 이 점을 주의해야 한다. 이에 대해서는 생산자로부터 메일로 날아오거나 생성 후 마지막에 나오는 페이지를 참고해야 하니 이 점을 유의해야 한다.  
>
> 보통 초기 admin 비밀번호의 경우에는 랜덤하게 생성되므로 Instance의 Instance Settings에서 Get System Log를 통해 비밀번호를 확인해야 한다.  

지금까지 인스턴스를 직접 생성하는 것보다 안정적이고, 생산적인 방법인 marketplace를 사용하는 방법을 살펴보았다. 이에 대해서는 활용하며 좀 더 익혀보자.


#### 참고 자료  

[AWS - free tier](https://aws.amazon.com/ko/free/)  
[생활코딩 - AWS EC2](https://opentutorials.org/course/2717/11274)  

