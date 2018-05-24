## Struct of Directory(File System) 

##### 

[뒤로가기](/linux/README.md)

이번에는 리눅스의 기본 디렉터리 구조에 대해 살펴보고자 한다.  

이 내용은 [이곳][this]의 내용을 번역한 것이고, 약간의 필자 주장이 들어간다는 것을 참고하길 바란다.  

[this]: http://www.thegeekstuff.com/2010/09/Linux-file-system-structure/

---

![linux-structure](https://raw.githubusercontent.com/rjs1197/rjs1197.github.io/master/img/linux/filesystem-structure.png)  

리눅스 혹은 유닉스는 기본적으로 위와 같은 구조를 지니고 있다.  

가령 '/home/rjs1197'은 필자의 홈 디렉터리이며, 루트 디렉터리 아래 'home'디렉터리, 그 아래 'rjs1197'이라는 디렉터리이다. 앞선 게시글에서 이야기한 것처럼 이는 '~' 기호를 사용하여 표시할 수 있다.  

```
Have you wondered why certain programs are located under /bin, or /sbin, or /usr/bin, or /usr/sbin?
```
  
리눅스를 사용하면서 "왜 어떤 프로그램들은 /bin, /sbin에 위치하고, 어떤 프로그램들은 /usr/bin 혹은 /usr/sbin에 위치하는 것일까?"라는 궁금증을 가진 적이 있지 않은가?
  
```
For example, less command is located under /usr/bin directory. Why not /bin, or /sbin, or /usr/sbin? What is the different between all these directories?
```
  
예를 들어, 적은 수의 명령이 '/usr/bin' 디렉터리 아래 위치한다고 하자. 위치는 왜 '/bin'이나 '/sbin', 'usr/sbin'이 아닐까? 모든 디렉터리 사이에는 무엇이 다른 것일까?
  
```
In this article, let us review the Linux filesystem structures and understand the meaning of individual high-level directories.
```
  
이 글에서, 우리는 리눅스 파일 구조를 리뷰하고, 개별적인 상위 레벨 디렉터리들을 이해할 것이다. 그로 인해 우리는 위에서 한 의문에 답을 찾을 수 있을 것이다.  

그럼 본격적으로 각 디렉터리에 대해 설명하겠다.  

---

* / – Root  

```
Every single file and directory starts from the root directory.  

Only root user has write privilege under this directory.  

Please note that /root is root user’s home directory, which is not same as /.
```
  
모든 싱글 파일과 디렉터리의 시작은 루트 디렉터리이다.  

오직 최상위 유저(root user)만이 이 디렉터리 아래의 쓰기 권한을 가지고 있다.  

/root는 최상위 유저(root user)의 홈 디렉터리를 말하는 것이니 '/'와 같지 않다는 점을 유의하기 바란다.  

* /bin – User Binaries  

```
Contains binary executables.  

Common linux commands you need to use in single-user modes are located under this directory.  

Commands used by all the users of the system are located here.  

For example: ps, ls, ping, grep, cp.  
```

2진(bunary) 실행 파일들이 들어있다.  

당신이 단일 사용자 모드(single-user modes)에서 사용하는 일반적인 리눅스 명령어들이 이 디렉터리 아래에 들어있다.  

시스템의 모든 사용자가 사용하는 명령어들은 이곳에 위치한다.  

예: ps, ls, ping, grep, cp.   

실제로 '/bin'의 파일 목록을 보면 위의 예에서 언급한 명령들이 파일의 형태로 존재한다.  

* /sbin – System Binaries  

```
Just like /bin, /sbin also contains binary executables.  
But, the linux commands located under this directory are used typically by system amdministrator, for system maintenance purpose.  

For example: iptables, reboot, fdisk, ifconfig, swapon  
```
  
'/bin'과 같이 '/sbin' 또한 2진(binary) 실행 파일들이 들어있다.  

하지만, 이 디렉터리 아래에 있는 명령어들은 일반적으로 시스템 관리자가 시스템 유지 보수 목적으로 사용한다.  

예: iptables, reboot, fdisk, ifconfig, swapon  

* /etc – Configuration Files  

```
Contains configuration files required by all programs.  

This also contains startup and shutdown shell scripts used to start/stop individual programs.  

For example: /etc/resolv.conf, /etc/logrotate.conf  
```
  
모든 프로그램에서 요구되는 환경 설정 파일들이 들어있다.  

또한 개개인의 프로그램을 시작/중지하는 데 사용되는 시작/종료 쉘 스크립트들도 포함하고 있다.  

예: /etc/resolv.conf, /etc/logrotate.conf  
 
* /dev – Device Files  

```
Contains device files.  

These include terminal devices, usb, or any device attached to the system.  

For example: /dev/tty1, /dev/usbmon0  
```
  
장치 파일들이 들어있다.  

터미널 장치, USB, 시스템에 탑재된 모든 장치가 여기에 포함된다.  

예:  /dev/tty1, /dev/usbmon0  

* /proc – Process Information  

```
Contains information about system process.  

This is a pseudo filesystem contains information about running process. For example: /proc/{pid} directory contains information about the process with that particular pid.  

This is a virtual filesystem with text information about system resources. For example: /proc/uptime  
```
  
시스템 프로세스에 대한 정보가 들어있다.  

여기에는 실행중인 프로세스에 대한 정보가 들어있다. 실제로는 존재하지 않는 가상 파일시스템이다.  

앞서 이야기한 것처럼 이것은 시스템 리소스들에 대한 문자 정보가 포함된 가상 파일시스템이다.  

예: /proc/uptime
 
* /var – Variable Files

```
var stands for variable files.  

Content of the files that are expected to grow can be found under this directory.  

This includes — system log files (/var/log); packages and database files (/var/lib); emails (/var/mail); print queues (/var/spool); lock files (/var/lock); temp files needed across reboots (/var/tmp);  
```
  
변수 파일을 의미한다(variable files의 약자).  

값이 변화(증가)할 것으로 예상되는 파일들의 내용을 찾을 수 있다.  

다음의 내용을 포함한다. - 시스템 로그 파일들(/var/log); 패키지들과 데이터베이스 파일들(/var/lib); 이메일들(/var/mail); 출력 큐(/var/spool); 파일 잠금(/var/lock); 재부팅 시 필요한 임시 파일들(/var/tmp);  

* /tmp – Temporary Files  

```
Directory that contains temporary files created by system and users.  

Files under this directory are deleted when system is rebooted.  
```
  
시스템과 유저에 의해 생성된 임시 파일들이 들어있다.  

이 디렉터리의 하위 파일들은 시스템이 재부팅될 때 삭제된다.  

* /usr – User Programs  

```
Contains binaries, libraries, documentation, and source-code for second level programs.  

/usr/bin contains binary files for user programs. If you can’t find a user binary under /bin, look under /usr/bin. For example: at, awk, cc, less, scp  

/usr/sbin contains binary files for system administrators. If you can’t find a system binary under /sbin, look under /usr/sbin. For example: atd, cron, sshd, useradd, userdel  

/usr/lib contains libraries for /usr/bin and /usr/sbin  

/usr/local contains users programs that you install from source. For example, when you install apache from source, it goes under /usr/local/apache2  
```
  
이차적인(second level) 프로그램들을 위한 소스코드, 문서, 라이브러리, 이진(binarues) 파일이 들어있다.  

/usr/bin에는 사용자 프로그램들을 위한 이진 파일들이 들어있다. 만약 /bin에서 사용자 이진 파일을 찾을 수 없다면, /usr/bin을 봐라.  

예: at, awk, cc, less, scp  

/usr/sbin에는 시스템 관리자들을 위한 이진 파일들이 들어있다. 만약 /sbin에서 찾을 수 없는 시스템 이진 파일이라면, /usr/sbin을 살펴봐라.  

예: atd, cron, sshd, useradd, userdel  

/usr/lib에는 /usr/bin과 /usr/sbin을 위한 라이브러리들이 들어있다.  

/usr/local에는 소스를 통해 받은 사용자 프로그램들이 들어있다.  

예를 들어, 소스를 통해 아파치를 인스톨한다면, 그것은 /usr/local/apache2로 갈 것이다.  

* /home – Home Directories  

```
Home directories for all users to store their personal files.  

For example: /home/john, /home/nikita  
```
  
모든 유저들의 개인적인 파일들을 적재하기 위한 홈 디렉터리이다.  

예: /home/john, /home/nikita  `
  
* /boot – Boot Loader Files  

```
Contains boot loader related files.  

Kernel initrd, vmlinux, grub files are located under /boot  

For example: initrd.img-2.6.32-24-generic, vmlinuz-2.6.32-24-generic  
```
  
부트 로더와 관련된 파일들이 들어있다.  

Kernel initrd, vmlinux, grup 등의 파일이 /boot 아래에 위치한다.  

예: initrd.img-2.6.32.24.generic, vmlinuxz-2.6.32-24-generic
  

* /lib – System Libraries  

```
Contains library files that supports the binaries located under /bin and /sbin  

Library filenames are either ld* or lib*.so.*  

For example: ld-2.11.1.so, libncurses.so.5.7  
```
  
/bin과 /sbin 아래에 있는 이진 파일들을 지원하는 라이브러리 파일이 들어있다.  

라이브러리의 파일 이름은 ld* 혹은 lib*.so.*이다.  

* /opt – Optional add-on Applications  

```
opt stands for optional.  

Contains add-on applications from individual vendors.  

add-on applications should be installed under either /opt/ or /opt/ sub-directory.  
```
  
opt는 선택 사항을 의미한다(optional).  
개별 벤더(공급처)의 부가기능 응용 프로그램들이 들어있다.  
부가기능 응용 프로그램은 /opt/ 혹은 /opt/ 하위 디렉터리 어느 한 쪽에 설치되어야 한다.  

* /mnt – Mount Directory  

```
Temporary mount directory where sysadmins can mount filesystems.  
```
  
시스템 관리자들이 파일 시스템을 마운트 할 수 있는 임시 마운트 디렉터리를 말한다.  

* /media – Removable Media Devices  

```
Temporary mount directory for removable devices.  

For examples, /media/cdrom for CD-ROM; /media/floppy for floppy drives; /media/cdrecorder for CD writer  
```
  
이동식 장치를 위한 임시 마운트 디렉터리이다.  

예를 들어, CD-ROM을 위한 /media/cdrom; floppy drives를 위한 /media/floppy, CD writer을 위한 /media/derecorder  

* /srv – Service Data  

```
srv stands for service.  

Contains server specific services related data.  

For example, /srv/cvs contains CVS related data.  
```
  
srv는 서비스를 의미한다.  

서버 특유의 서비스 관련 데이터가 들어있다.  

예를 들어, /srv/cvs 에는 CVS와 관련된 데이터가 들어있다.
  
