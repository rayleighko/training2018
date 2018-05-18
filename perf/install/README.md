## install Perf

여러 리눅스 커널 중 System의 Performance를 측정하는 Tool인 'Perf'에 대해 살펴보자.  

또한, 이 글이 유용한 대상은 시스템 프로그래밍, 보안, tracing에 관심이 있는 학생 혹은 초보 개발자일 것이다.  

나의 얕은 지식으로는 거기까지가 간접적으로나마 도움을 줄 수 있는 범위라고 생각되기 때문이다. :D  

사전에 준비해야 할 것은 'git', 'cmake', 'C 컴파일러(gcc)' 정도가 될 것이니 이에 대해서는 따로 내려받기를 바란다.  

추가적으로 contribution이 주가 될 것이기 때문에 git과 컴퓨터 시스템에 대한 전반적인 이해를 동반한다면 필자의  성장과 함께할 수 있을 것이다.  

그러니 게시글 외에 git과 컴퓨터 시스템에 대해 따로 공부하도록 하자(필자의 경우도 별도로 공부할 것이다).  

다소 모호할 수 있는 '전반적인 이해'는 '어느정도 숙달된'을 의미한다. git을 예로 들면 rebase -i를 이용하여 과거 커밋을 수정할 수 있는 단계라고 이해하면 된다.  

컴퓨터 시스템의 경우에는 컴퓨터의 내부 구조와 함께 OS 혹은 kernel이 작용하는 과정에 대해 이해하고 있는 것을 의미할 것이다.   

---

우선 리눅스 커널에 존재하는 perf를 빌드하는 방법을 소개하고자 한다. 우선 [여기][this]를 눌러 들어가면 리눅스의 git repository를 확인해보자.  

조금 읽다보면 우리에게 친숙한 리누스 토발즈가 보일 것이다. 또, 의외로 활발하게 기여된다는 것을 느낄 수 있을 것이다. 그렇다면 이곳을 clone해서 로컬 저장소를 만들어보자.  

[this]: https://git.kernel.org/pub/scm/linux/kernel/git/tip/tip.git

링크로 들어가는 것이 번거롭다면 아래의 주소를 clone하기 바란다.  

> https://git.kernel.org/pub/scm/linux/kernel/git/tip/tip.git
  

필자는 다음과 같이 진행했다.  

> mkdir dev; cd dev; git clone https://git.kernel.org/pub/scm/linux/kernel/git/tip/tip.git
  

진행이 끝났다면 이제 레포지토리에 들어가보자(필자는 oh-my-zsh을 사용하고 있다).  

> ➜  tip git:(master) ✗ ls
> arch     CREDITS        firmware  ipc      lib          net      security  virt
> block    crypto         fs        Kbuild   MAINTAINERS  README   sound
> certs    Documentation  include   Kconfig  Makefile     samples  tools
> COPYING  drivers        init      kernel   mm           scripts  usr
  

이것은 필자의 tip 레포지토리의 파일 목록이다. 여기서 tools/perf에 들어가 빌드해보자.  

> ➜  tip git:(master) cd tools/perf/
> ➜  perf git:(master) make 
> BUILD:   Doing 'make -j4' parallel build
> HOSTCC   fixdep.o
> HOSTLD   fixdep-in.o
> LINK     fixdep
> ...


왜 github에 있는 linux 프로젝트를 clone하지 않는 것일까? 그것이 편할텐데 말이다. 그것은 github에 있는 linux 레포지토리는 이 곳의 레포지토리를 clone한 것 뿐이다. 즉, 최신의 버전도 아니거니와 제대로 빌드될 지도 의문이다.  

이것으로 'perf'를 내려받고, 빌드해 보았다. 앞으로의 과정은 'perf'라는 Tool을 사용해보고, 기여할 내용이 무엇이 있는지를 고민할 것이니 참고하기 바란다.   

추가적으로 수퍼바이저 권한이 필요한 작업은  

> ➜  tip git:(master) sudo make install prefix=/usr
  

을 이용해 /usr에 install하도록 하자.  
