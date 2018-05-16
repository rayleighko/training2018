## Inline Function  

**Inline Function**은 무엇일까? 쓰여진 그대로 해석해보면 안쪽을 뜻하는 in과 프로그램의 선을 뜻하는 line의 합성이이다. 따라서 이는 **'프로그램 코드 라인 안의 함수'**라고 이해할 수 있을 것이다.  

**Inline Function**을 설명하기 전에 그와 유사한 C언어의 **Macro Function**을 짚고 넘어가자. Macro Function의 **장점**은 일반적인 함수에 비해 **실행속도가 빠르다**는 것이 있다. **단점**으로는 **복잡한 함수를 정의하기에 한계가 있다**는 것이다. 복습 삼아 Macro Function을 하나 정의해보자.  

```
#include <iostram>
#define SQUARE(x) ((x)*(x)) // Macro Function

int main ()
{
	std::cout << SQUARE(5) << std::endl;

	return 0;
}
```

위의 코드는 전처리 과정을 거치면 아래의 코드와 같은 모양이 된다(여기서 중요한 포인트는 function body가 Function call을 대신했다는 점이다).  

```
#include <iostram>

int main (void)
{
	std::cout << ((5)*(5))) << std::endl;

	return 0;
}
```

위 예제와 같이 Function body가 Function call을 완전히 대체했을 때 **"함수가 인라인화 되었다"**라고 표현한다. 그런데 우리는 **macro function**의 장점과 단점을 잘 알고 있으니, 다음과 같은 생각을 하지 않을 수 없다.  

> "Macro Function은 정의하기가 복잡하니, 장점은 살리면서 일반 함수처럼 정의가 가능하면 좋겠는데?"  

그러면 Cpp에서는 어떻게 이러한 기능을 가지는 **Inline Function**를 제공하는지 살표보자.  

```
#include <iostram>

inline int SQUARE(int x)
{
	return x*x;
}

int main (void)
{
	std::cout << SQUARE(5) << std::endl;
	std::cout << SQUARE(12) << std::endl;

	return 0;
}
```

별로 특별한 것은 없어 보인다. 이제 항상 Inline을 사용하면 편할 것 같다. 그렇지만 모든 것에는 일장일단이 있듯이 **Inline Function**도 만능은 아니다. **Macro Function을** 이용한 Function Inline(첫 번째 예제)은 전처리기에 의해서 처리되지만, **키워드 Inline**을 이용한 Function Inline(두 번째 예제)은 **Compiler**에 의해서 처리가 된다.  

따라서 **Compiler**는 **Function Inline**이 오히려 성능에 해가 된다고 판단할 경우, Inline 키워드를 **무시**해버리기도 한다.  

> 또한, 컴파일러는 필요한 경우 일부 함수를 임의로 Inline 처리하기도 한다.  

더불어 Inline Function는 Macro Function의 장점을 완전히 대체하지 못했다. Macro Function의 경우는 type에 의존적이지 않은 함수가 되지만 Inline Function의 경우에는 자료형에 따라 다르게 정의해야 한다.  

물론 **Function Overloading**을 통해서 이 문제를 해결할 수 있으나 한 번만 정의하면 되는 매크로 함수의 장점을 버리는 결과로 이어지게 된다.  

> 이러한 것을 보완하기 위해서 이후에 배울 '템플릿(Template)'이라는 것을 이용하면 **Macro Function**과 마찬가지로 **type**에 의존적이지 않은 함수가 완성된다. 아래와 같이 말이다.  

```
#include <iostram>

template <typename T>
inline T SQUARE(int x)
{
	return x*x;
}

int main (void)
{
	std::cout << SQUARE(5.5) << std::endl;
	std::cout << SQUARE(12) << std::endl;
	return 0;
}
```

실제로 위 코드를 실행해보면, 데이터의 손실이 발생하지 않음을 알 수 있다.  
