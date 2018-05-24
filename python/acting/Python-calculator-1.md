# Tkinter Module

##### 

[뒤로가기](/python/README.md)

필자는 새해를 맞이해 Python에 대해 간단한 프로젝트부터 복잡한 프로젝트까지 다양한 형식의 프로젝트를 진행하려고 한다. 그리고 이 article에서는 Tkinter Module을 이용해 Python 계산기를 구현한 경험을 공유하고자 한다.

---

우선 필자가 참고한 곳은 [생활코딩-파이썬 계산기 만들기][pycalc]이다. 이곳의 예제를 그대로 사용하니느 않고, Tkinter의 사용법을 참고하여 필자만의 계산기를 만들 것이다.  

이것의 시작은 **'프로그래머의 위기지학'** 즉, '자신이 사용할 프로그램은 자신이 만드는 것이 프로그래머의 덕목'이라는 뉘앙스의 글을 보고 감명받았기 때문이다.  

또한, 프로젝트의 이름은 'chocolate'이고, 모양은 Google-Calcualtor과 유사한 느낌으로 만드려고 한다. 이름이 chocolate인 이유는 계산기의 모양이 chocolate와 비슷하기 때문이니 넘어가도록 하자.  

[pycalc]: https://opentutorials.org/module/2980/17973

필자는 프로젝트를 시작하기 전 'Tkinter'를 import해야 했는데, 필자의 개발환경이 'Ubuntu 16.04'였기 때문에 windows와 mac과는 다른 방법으로 접근해야 했다.  

또한, Pycharm을 사용함에 있어 미숙했기에 한참 해매고서야 아래와 같이 Tkinter을 import해서 기본 base를 잡을 수 있었다.  

```
from Tkinter import *


root = Tk()
root.title("Calculator")
root.geometry("200x200")



root.mainloop()
```

여담으로 'Tkinter'를 'tkinter'라고 적어 package가 import되지 않았는데, 이를 간파하기까지 꽤 오랜 시간이 걸렸다.  

```
sudo apt-get install python-tk
```

와 같이 Ubuntu에서 python-tk library를 사용하기 위한 대부분의 수단을 사용했는데도 import되지 않아서 포기하는 마음으로 `_`를 붙이거나 앞자리를 대문자로 바꾸는 등 다양한 방법을 사용해 문제를 해결할 수 있었다.  

해결하고 난 후에는 어처구니가 없어 한참을 멍하니 있었다.  

찾아보니 Python2에서는 Tkinter를, Python3에서는 tkinter를 import해야 한다고 하더라.  

Tkinter에 대해 간단히 설명하자면, Tcl/Tk에 대한 Python Wrapper로 파이썬에서 사용할 수 있도록 한 Lightweight GUI 모듈이다. Tcl은 'Tool command language'라는 일종의 언어이며, Tk는 크로스 플랫폼에 사용되는 일종의 GUI toolkit이다.  

또한, 기본적으로는 Tk Class Object를 'root'라는 이름으로 생성하고, 이 Object의 mainloop() method를 call하는 형식으로 화면에 출력한다.  

따라서 위의 Code와 같은 예제를 실행하면 크기 200x200의 빈 화면(Dialog)가 출력된다.  
