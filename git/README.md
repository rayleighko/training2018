# Round 1 git

## Round 1-1 git basic

##### Don't think about git, just do git!

우리가 대부분의 전자기기나 게임을 할 때 메뉴얼을 보지않고 사용하며 익숙해지는 것처럼 Git이라는 프로그램 또한, 사용하면서 익히도록 하자.

### Git 이란?

개발 과정의 작업 단위 순간을 기록하여 소스파일, 문서를 관리하는 도구.

History에 대한 관리를 제공해 프로그램이 개발되어 온 역사를 살펴볼 수 있고, 특정 시점으로 이동하여 입력, 수정, 삭제 등의 작업을 수행할 수 있다.

예를 들어, 게임에서 무한으로 세이브 포인트를 기록하는 것과 동일하다.

즉, Git은 History 관리 기능과 타임머신 기능을 가지고 있다.

### Git 실습 준비하기

## 1. git 설치하기

* [Mac & Windows][Mac & Windows]

##### Linux - Ubuntu

> apt-get install git 

[Mac & Windows]: https://git-scm.com/downloads

#### 2. Github [회원가입][join]

제목의 링크를 참고하여 회원가입을 진행하자.

[join]: https://github.com/join

#### 3. Editor

예제를 실행하는 editor는 개인의 취향에 맞게 선택하길 바란다.

> 필자의 경우는 linux환경으로 'VIM'이나 'Emacs'를 사용하는 것을 추천한다. 만약  Windows나 MacOS라면 본인 취향에 맞는 에디터를 선정하기 바란다.

#### 4. 실습 전 알아둬야 할 Git 필수 명령어

Git을 입문하기 위해서는 아래와 같은 3가지 명령어를 꼭 기억하고 있어야 한다.

> **add**: 커밋할 목록에 추가
> **commit**: 커밋(History의 단위) 작성하기
> **push**: 작업 시작부터 현재까지의 커밋을 Github에 밀어넣기

#### 5. Git 실습하기

이제는 직접 사용해보는 일만 남았다. 다양한 문서들을 활용하여 학습을 진행하고, 학습용 PC에서 이를 활용하여 본인의 프로젝트를 진행해보자.

또한, 위에서 언급한 필수 명령어는 예제를 따라가며 차근차근 배워보도록 하고, 우선은 [여기][git-tuto]의 과정을 진행하여 학습하도록 하자.

> 이 문서에서는 실습에 관한 전반적인 사항에 대해 언급하는 것보다 git에 대한 전반적인 이해를 돕는 것을 주 목적으로 할 것이다.

## Round 1-2 올바른 깃허브 사용

우리가 이 문서를 활용하는 이유는 취업, 이직, 개인의 성장 등 다양할 것이다. 그러나 모든 이유를 위해 깃허브를 올바르게 사용하는 방법을 학습하도록 하자.

#### 1일 1커밋

타인의 깃허브를 방문한 적이 있는가? 그렇다면 우리가 가장 먼저 보는 것은 '커밋 히트맵(commit Heatmap)'이다. 이것 하나만으로 상대의 개발 실력을 판가름하기는 힘들지만, 이는 성실의 척도가 될 수 있다. '성실한' 이미지를 주는 그 찰나의 순간, 이미 당신은 "이 친구 열심히 사는 친구구먼!"하는 인상을 줄 수 있다.

물론, 이제 시작이다. 이를 위해 TIL(Today I Learned), 개인 블로그 등을 운영하는 것을 추천한다.

#### 올바른 커밋이란 무엇인가?

올바른 깃허브 사용을 위한 올바른 커밋 작성법에 대해 학습하자. 사실 올바른 커밋이란 집단에 따라 다르다. 그러나 보편화된 형식을 따른다면 정갈한 커밋 메시지를 가질 수 있을 것이다. 또한, 그 메시지를 보는 이들의 마음도 정갈해질 것이다.

기본적으로 `타입(Type): 제목`의 형태로 커밋 메시지를 작성할 수 있다.

* Type의 종류

*feat*: 새로운 기능을 추가할 경우
*fix*: 버그를 고친 경우
*docs*: 문서 수정한 경우
*style*: 코드 포맷 변경, 세미 콜론 누락, 코드 수정이 없는 경우
*refactor*: 프로덕션 코드 리팩터링
*test*: 테스트 추가, 테스트 리팩터링 (프로덕션 코드 변경 없음)
*chore*: 빌드 테스크 업데이트, 패키지 매니저 설정할 경우 (프로덕션 코드 변경 없음)

> 예를 들어, 'myproject.cpp'라는 파일에 'myfunc()'라는 기능을 추가한다면 다음과 같은 형식이어야 한다.
> feat: Add myfunc()
>
> better than yesterday 'myfunc()'.
>
> Resolves: #1111

**제목**은 일반적으로 마침표(`.`)를 사용하지 않는 것을 원칙으로 한다. 제목의 처음은 동사 원형을 이용해 'Added'나 'Modified'가 아닌 'Add', 'Modify'를 사용한다. (50자 이내)

**본문**의 내용은 커밋의 상세 내용을 작성하며 제목과 본문 사이는 한 칸 띄어 구분한다. (72자 이내)

**꼬리말**은 이슈 트래커 ID를 작성하는 것이 기본이다.

#### 커밋을 잘못하면 어쩌지..?

커밋을 작성하며 한 번쯤 이런 생각을 해본 적이 있지 않은가?

> "아 제목을 안달았네 커밋 다시 해야겠다."

혹은

> "아 커밋 메시지를 잘못 입력했어. 새로운 커밋 메시지를 쓰기엔 아까우니까 그냥 넘어가자"

이라고 말이다. 이런 생각을 해본 적이 있다면 이번 챕터가 도움이 될 것이다.

우선 기본적으로 사용할 명령어는 `git commit --amend`와 `git rebase -i`이다. 이 둘을 사용하면 과거 시점에서 새로운 커밋없이 파일을 수정하거나 커밋 메시지를 수정할 수 있다.

먼저 `git commit --amend`를 살펴보자. 이 명령은 바로 이전의 commit 내용을 수정하는 명령이다. 가령 파일 내 문자의 수정, 커밋 메시지의 수정 등이 그 예이다. 아래의 예를 따라 본인의 커밋 메시지를 수정해보자.

##### 사용 예

```
## 커밋 메시지 수정
> git commit -m "docs: Add REEDME.md"
# 실수를 발견(수정)
> git commit --amend
# 에디터 출력

## 파일 내용 수정
> ls
REEDME.md
> git add REEDME.md
> git commit -e
# 실수를 발견(수정)
> mv REEDME.md README.md
> git add README.md
> git commit --amend
# 에디터 출력
```

이와 같이 `git commit --amend`를 사용하면 새로운 커밋의 추가 없이 과거의 커밋에 **'덮어쓰기'**할 수 있다.

다음은 `git rebase -i`에 대해 살펴보자. 우선은 git rebase에 대한 자세한 설명은 [여기][git rebase]를 참고하자.

간단하게 사용 예를 보고 `git rebase -i`의 사용방법에 익숙해져 보자.

```
## 과거 시점으로 돌아가기
> git rebase -i HEAD~3
# 현재 위치(HEAD)를 기준으로 총 3개의 commit message를 보여줌
# (수정을 원하는 commit message의 tag를 edit으로 수정하고 저장하면 과거의 시점으로 돌아감

## 돌아간 과거 시점에서 커밋 메시지 수정하기
> git commit --amend

## 돌아간 과거 시점에서 파일 수정하기
> ls
REEDDME.md
> mv REEDME.md README.md
> git add README.md
> git commit --amend
```

이처럼 `git commit --amend`와 `git rebase -i`를 이용하여 현재 커밋의 내용을 수정하거나 과거 커밋의 내용을 수정할 수 있다.

[git rebase]: https://git-scm.com/book/ko/v1/Git-%EB%B8%8C%EB%9E%9C%EC%B9%98-Rebase%ED%95%98%EA%B8%B0

### 추가 자료

* [영문 git 문서][git-documentation]
* [한국어 git 문서][kor-git-doc]
* [깃허브로 취업하기][git-get-career]

[git-documentation]: https://git-scm.com/doc/
[kor-git-doc]: https://git-scm.com/book/ko/
[git-get-career]: https://sujinlee.me/professional-github/

