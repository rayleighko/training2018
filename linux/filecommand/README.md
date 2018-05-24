## File Command  

##### 

[뒤로가기](/linux/README.md)

#### 파일 내용 연속 출력하기 - cat  

```
// 형식  

cat [옵션] 파일명...
```
  
```
// 옵션  

-n : 행 번호를 붙여서 출력
```
  
```
// 사용 예  

[user1@localhost ~]$ cat /etc/hosts
# Copyright (c) 1993-2009 Microsoft Corp.
#
# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
[user1@localhost ~]$ cat -n /etc/hosts
   1  # Copyright (c) 1993-2009 Microsoft Corp.
   2  #
   3  # This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
```
  
#### 화면 단위로 파일 내용 출력하기 - more  

```
// 형식  

more [옵션] 파일명...
```
  
```
// 옵션  

+행 번호 : 출력을 시작할 행 번호를 지정
```
  
```
// 사용 예  

[user1@localhost ~]$ more etc/hosts
# Copyright (c) 1993-2009 Microsoft Corp.
#
# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
#
# This file contains the mappings of IP addresses to host names. Each
# entry should be kept on an individual line. The IP address should
# be placed in the first column followed by the corresponding host name.
# The IP address and the host name should be separated by at least one
# space.
-- More (51%) --
```
  
이 경우 스페이스 바를 누르면 다음 화면이 출력되고, 엔터를 누르면 다음 행이 출력(스크롤)된다.  

'/문자열'을 입력하면 문자열을 찾아 이동하기도 한다. 종료 시에는 q를 이용하여 종료한다.  

또한, more 명령의 경우에는 다음 문장으로만 이동이 가능하기 때문에 앞, 뒤 모두 가능한 'less' 명령을 주로 사용한다.  

#### 개선된 화면 단위 파일 내용 출력하기 - less  

```
// 형식  

less 파일명...
```
  
```
// 사용 예  

[user1@localhost ~]$ less etc/hosts
# Copyright (c) 1993-2009 Microsoft Corp.
#
# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
#
# This file contains the mappings of IP addresses to host names. Each
# entry should be kept on an individual line. The IP address should
# be placed in the first column followed by the corresponding host name.
# The IP address and the host name should be separated by at least one
# space.
/etc/hosts
```
  
한 줄씩 다음 행으로 스크롤 하기 위해서는 'j'를, 이전 행으로 스크롤 하기 위해서는 'k'를 사용한다.  
 
다음 화면은 스페이스바 혹은 'Ctrl + f'를 사용하고, 이전 화면은 'Ctrl + b'를 이용한다.  

#### 파일 뒷부분 출력하기 - tail  

```
// 형식  

tail [옵션] 파일명...
```
  
```
// 옵션  

+행 번호 : 지정한 행 부터 끝까지 출력
-숫자 : 화면에 출력할 행의 수를 지정(default = 10)
-f : 파일 출력이 종료되지 않고 주기적으로 출력된다.
```
  
```
// 사용 예  

[user1@localhost ~]$ tail /etc/hosts
# lines or following the machine name denoted by a '#' symbol.
#
# For example:
#
#      102.54.94.97     rhino.acme.com          # source server
#       38.25.63.10     x.acme.com              # x client host

# localhost name resolution is handled within DNS itself.
#       127.0.0.1       localhost
#       ::1             localhost
```
  
위와 같이 파일의 마지막 10행이 출력된다. 이외에도 옵션을 통해 지정한 숫자만큼 출력하거나 파일 내용을 주기적으로 반복해서 출력할 수도 있다.  

#### 파일 복사하기 -cp  

```
// 형식  

cp [옵션] 파일명1/디렉터리명1 파일명2/디렉터리명2
```
  
```
// 옵션  

-i : 대화식 복사 방법으로 파일명2가 이미 존재할 경우 덮어쓸 것인지 물어본다.
-r : 디렉터리를 복사할 대 지정한다.
```
  
```
// 사용 예  

[user1@localhost ~]$ cp a.txt
[user1@localhost ~]$ cat a.txt
hello
[user1@localhost ~]$ cp a.txt b.txt
[user1@localhost ~]$ cat b.txt
hello
```
  
명령의 인자에는 파일명 외에도 디렉터리명이 올 수 있다. 두 인자 모두 파일이라면 위의 예시처럼 내용이 복사된다.  

그리고 첫 번째 인자는 파일이고 두 번째 인자는 디렉터리인 경우, 파일을 해당 디렉터리 아래에 복사한다.  

더불어 디렉터리를 복사하기 위해서는 옵션에 -r을 주고 두 인자 모두 디렉터리명으로 설정하면 된다(옵션을 주지 않으면 오류가 생긴다).  

> 이 경우 만약 두 번째 인자로 준 디렉터리명이 존재한다면, 원본 디렉터리가 목적지 디렉터리 아래에 원본 디렉터리와 같은 이름으로 복사된다(헷갈릴 수 있으니 직접 해보는 것을 추천한다).  

#### 파일 이동하기 - mv  

```
// 형식  

mv [옵션] 파일명1/디렉터리명1 파일명2/디렉터리명2
```
  
```
// 옵션  

-i : 파일명2/디렉터리명2가 존재하면 덮어쓸 것인지 물어본다.
```
  
```
// 사용 예  

[user1@localhost ~]$ ls
temp a.txt b.txt c.txt
[user1@localhost ~]$ mv a.txt temp
[user1@localhost ~]$ ls
temp b.txt c.txt
[user1@localhost ~]$ mv b.txt c.txt
temp c.txt
```
  
위와 같이 파일을 디렉터리로 옮기거나 파일로 옮기는 경우 2가지가 있다.  

첫 번째의 경우는 원본 파일을 지정한 디렉터리로 이동하는 것이고, 두 번째의 경우는 '덮어쓰기'이다.  

#### 파일 삭제하기 - rm  

```
// 형식

rm [옵션] 파일명/디렉터리명 ...
```
  
```
// 옵션  

-i : 지정한 파일을 삭제할 것인지 대화식으로 확인한다.
-r : 지정한 디렉터리를 삭제한다.
```
  
```
// 사용 예  

[user1@localhost ~]$ ls
temp a.txt b.txt c.txt
[user1@localhost ~]$ rm a.txt
[user1@localhost ~]$ ls
temp b.txt c.txt
[user1@localhost ~]$ rm -r temp
b.txt c.txt
```
  
#### 파일 링크 만들기 - ln  

```
// 형식  

ln [옵션] 원본파일명 링크파일명
```
  
```
// 옵션  

-s : 심벌링 링크 파일을 생성한다.
```
  
```
// 사용 예   

[user1@localhost ~]$ ls
temp a.txt b.txt c.txt
[user1@localhost ~]$ mv a.txt temp
[user1@localhost ~]$ ls
temp b.txt c.txt
[user1@localhost ~]$ mv b.txt c.txt
temp c.txt
```
  
파일 링크는 기존에 있는 파일에 새로운 파일명을 붙이는 것이다.  

파일 링크의 종류는 기존파일에 새로운 파일명을 추가하는 하드링크와 원본파일을 가리키는 새로운 파일을 만드는 심볼릭링크가 있다.  

> 두 차이가 애매하지만 심볼릭 링크는 인덱스 번호를 매겨 원본과의 차이를 둔다.

자세한 설명에 앞서 리눅스의 파일 구조를 알아두어야 한다. 리눅스의 파일은 '파일명 + inode + 데이터 블록'으로 구성된다.  

각 요소를 설명하자면 '파일명'은 사용자가 파일에 접근할 때 사용하는 파일의 이름이다.  

'inode'는 파일에 대한 정보를 가지고 있는 특별한 구조체로, 외부적으로는 번호로 표시되고 내부적으로는 파일의 종류 및 크기, 소유자, 파일 변경 시간, 파일명 등 파일 상세 정보와 데이터 블록의 주소가 저장되어 있다.  

> ls -l 명령 수행 시 출력되는 정보는 사실 inode에 저장되어 있는 파일 상세 정보라는 것에 유의하자.  

하드 링크의 확장자는 '.ln'을 사용하고, 심볼릭 링크는 '.sl'을 사용한다.

하드 링크로 만든 링크는 원본과 inode 값이 같고, 심볼릭 링크로 만든 링크는 원본과 다르다. 아래는 심볼릭 링크의 특징이니 참고하기 바란다.

* 파일의 종류가 'l'로 표시된다.  
* 하드 링크의 개수가 하나이다. 즉, 원본 파일에 이름을 추가하는 것이 아니다(심볼릭 링크는 원본파일을 가리키는 새로운 파일이다).  
* 파일 이름 뒤에 원본 파일의 이름이 표시된다.  
* inode 번호가 원본 파일과 다르다. 즉, 원본 파일과 심볼릭 링크 파일은 별개의 파일이다.  

> 심볼릭 링크가 하드 링크에 비해 탁월한 점은 하드 링크는 디렉터리에 생성할 수 없고 다른 파일 시스템에 생성할 수 없지만 심벌릭 링크는 디렉터리에도 지정할 수 있고 파일 시스템이 달라도 생성할 수 있다는 것이다.
  
