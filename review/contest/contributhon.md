# contributhon 최종보고서

## Overview

1. Terminal에서 uftrace의 manual이 열리지 않음. 이에 의문을 느껴 [Issue][issue] 작성.  

* 해결  
> [Issue][issue]와 같이  `make install`을 하지 않아 발생한 것을 알아차림. 부끄러움과 함께 `Close`.  

---

2. Terminal에서 uftrace 실습을 위해 `uftrace/tests/` 의 s-alloca.c, s-fork.c, s-malloc-fork.c, s-ucontext.c 에 대한 컴파일 진행.  

* 해결
> 컴파일 과정에서 `warning message(implicit function declaration)` 발생. 이에 대해 [Pull request][pull] 작성.
> Commit message에 대한 수정과 서명을 추가하라는 피드백을 받고, `git rebase`를 이용해 Commit message 수정 후 재전송.
>
> Merge.

---

3. 필자의 경우 `Zsh` 을 사용해 `Bash-completion`만 존재하는 uftrace의 명령어들을 자동완성할 수 없는 문제를 파악. 

* 해결
> `Make install` 명령 시 `Bash-Completion`가 제대로 install되지 않았음에도 `Install` 되었다는 문구를 출력하는 조건적 버그와 `Zsh-completion` 구현에 대한 [Issue][issue2] 작성.
> zsh, shell script에 대한 사전지식이 없고, 사용자 Needs가 크지 않아 진전이 적은 상태(해당 기능은 간단한 기능으로, `Copy and Paste`를 이용해 구현할 수는 있지만 학습에 의의가 없어 이와 같은 방법은 배제함).

[issue]: https://github.com/namhyung/uftrace/issues/192
[pull]: https://github.com/namhyung/uftrace/pull/220
[issue2]: https://github.com/namhyung/uftrace/issues/234

---

## 활동 내역  

### [Issues][issue3]  

[issue3]: https://github.com/namhyung/uftrace/issues

_1. [Linux_terminal] Uftrace manual: https://github.com/namhyung/uftrace/issues/192

_3. 'Bash-completion' is not installed, 'Zsh-completion': https://github.com/namhyung/uftrace/issues/234

### [Pull requests][pull2](test 위주)  
 
[pull2]: https://github.com/namhyung/uftrace/pulls

_2. test: Add explicit function declaration: https://github.com/namhyung/uftrace/pull/220

### [Gitter][gitter]  
[gitter]: https://gitter.im/uftrace/uftrace

`'Zsh-completion'에 대한 간단한 질문`  

![image](https://user-images.githubusercontent.com/24822072/32942870-a701dbb2-cbcd-11e7-9f88-c7c20e371fab.png)


---

`uftrace을 '-pg' 옵션을 이용해 'compile'하는 방법에 대한 답변`  

![image](https://user-images.githubusercontent.com/24822072/32942892-b8af4b10-cbcd-11e7-8fb0-d8bd0bda02c4.png)

### 컨트리뷰톤 과정에서 진행한 Contribution 학습  

**uftrace**  
프로젝트 소개 문서: https://github.com/kosslab-kr/uftrace/issues/11
개발환경 구성하기: https://github.com/kosslab-kr/uftrace/issues/28
커밋 분석 보고서: https://github.com/kosslab-kr/uftrace/issues/29

**개인 블로그**  
[git tutorial article][blog]

[blog]: https://rjs1197.github.io/articles/2017-10/git

