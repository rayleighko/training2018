## Call C Standard library in C++

Cpp로 프로그래밍 하다 보면, 자신이 잘 알고 사용해오던 C언어의 표준함수를 사용하고 싶을 때가 있다. 이럴 때는 아래를 참고하도록 하자.  

---

우선 기본적으로 c를 더하고 .h를 빼는 것으로 생각하면 된다. C언어 라이브러리에는 매우 다양한 유형의 함수들이 정의되어 있다.  

그런데 이러한 함수들은 Cpp의 표준 라이브러리에도 포함되어 있다. 따라서 어렵지 않게 사용이 가능하다.  

다음은 C언어의 헤더 파일에 대응하는 Cpp의 헤더정보를 일부만 정리한 것이다.  

* \#include \<stdio.h\> -> \#include \<cstdio\>
* \#include \<stdlib\> -> \#include \<cstdlib\>
* \#include \<math.h\> -> \#include \<cmath\>
* \#include \<string.h\> -> \#include \<cstring\>
  

위의 예를 보면 다음과 같이 알 수 있을 것이다.  

>"헤더 파일의 확장자인 .h를 생략하고앞에 c를 붙이면 C언어에 대응하는 Cpp의 헤더파일 이름이 되는구나!"
  

사실 namespace std 내에 선언되어 있다는 사실만 제외하면, Cpp의 헤더는 C언어의 헤더와 별 차이가 없다. 그리고 C언어의 헤더파일도 좋지만 가급적 Cpp의 헤더를 기반으로 프로그래밍하도록 하자.  

그럼 당므으로 넘어가서 Cpp의 관점에서, 여전히 위와 같은 형태로 함수호출을 허용하는 이유는 '하위 버전과의 호환성'을 제공하기 위함으로 볼 수 있다.  

그리고 Cpp 표준 라이브러리가 제공하는 함수들과 C 표준 라이브러리가 제공하는 함수들이 완전히 일치하는 것도 아니다. 예를 들어 abs함수같은 경우는 아래와 같이 차이가 있다.  

```
//C에서의 선언 형태

int abs(int num);

{% endhighlight %}  

{% highlight Cpp %}
//Cpp에서의 선언 형태

long abs(long num);
float abs(float num);
double abs(double num);
long double abs(long double num);
```

이렇게 말이다. Cpp에서는 함수 오버로딩이 가능하기 때문에 자료형에 따라서 함수의 이름을 달맇서 정의하지 않고, 보다 사용하기편하도록 함수를 오버로딩 해 놓은 것이다.  

이렇듯 Cpp문법을 기반으로 개선된 형태로 라이브러리가 구성되어 있으므로, 가급적 Cpp의 표준헤더를 이용해서 함수를 호출하는 것이 좋다.  
