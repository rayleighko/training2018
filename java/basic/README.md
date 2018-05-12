## 1장 기본 프로그래밍 구조  

이 문서를 통해 JAVA 프로그래밍의 기초를 학습하며, 간단한 예제를 풀어나갈 것이다.  

### Ubuntu LTS 18.04에서 JAVA 설정하기  

필자는 java 홈페이지에서 `jdk-10.0.1_linux-x64_bin.tar.gz`을 다운로드 해 아래의 과정을 진행하였다.  

```download jdk-10.0.1 for linux 

cd Download/  
tar -xvf jdk-10.0.1_linux-x64_bin.tar.gz  
sudo mkdir /usr/lib/jvm  
sudo mv jdk-10.0.1 /usr/lib/jvm  
sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/jdk-10.0.1/bin/java 1  
sudo update-alternatives --install /usr/bin/javac javac /usr/lib/jvm/jdk-10.0.1/bin/javac 1  
sudo update-alternatives --install /usr/bin/javaws javaws /usr/lib/jvm/jdk-10.0.1/bin/javaws 1  
```  

위의 과정을 거치면 java를 설치하고, shell에서 java, javac, javaws 명령을 사용하는 것이 가능해진다. 이제 마음놓고 앞으로의 실습을 진행하도록 하자.   

### JAVA의 기본적인 문법  

> java는 기본적으로 terminal과 편하게 IDE를 사용하여 작성할 수 있다. 필자의 경우에는 앞서 설명한 것과 같이 terminal 환경에서 진행할 것이다.  
> 
> 여기에서 사용될 명령어는 java, javac, javaws, jshell 등이 될 것이고, 사용될 환경은 `Ubuntu LTS 18.04`, `bash shell`으로 진행하게 된다.  

우선 필자의 경우는 이전에 Java를 학습했기 때문에 정말 기본적인 사항에 대해서는 학습의 동기를 위해 생략하고자 한다. 따라서 본 과정을 필자 마음대로 진행할 것이라 다소 어려움이 있다면 다른 예제를 참고하길 바란다.  


