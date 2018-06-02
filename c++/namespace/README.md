## Namespace  

##### 네임스페이스를 통해 간략하게 코드를 짜보자.  

[뒤로가기](/c++/README.md)

직역하면 '이름공간'인 Namespace는 C만을 학습해왔던 이들에게는 다소 생소한 개념이다.  

그래도 어렵지는 않으니 '별도로 이름을 붙여놓은 공간'으로 이해하고 특정 영역에 이름을 붙여주기 위한 **문법적 요소**라고 이해하면 되겠다.  

그럼에도 아직 생소할테니 다음의 탄생 배경을 보며 이해하도록 하자.  

---

Namespace의 등장 이전에 A와 B사가 협업을 한다면 사전에 함수, 변수 이름을 모두 정해서 충돌을 예방해야 했다.  

그러나 이 부분에서 문제가 발생하게 된다. 그것은 새롭게 추가된 함수나 변수의 경우, 자칫 실수를 해버려 충돌이 나게 될 수도 있기 때문에 프로젝트에 치명적인 장애를 끼치게 된다.  

이는 생각만 해도 아찔하지 않은가. 함수 명 하나 때문에 프로젝트 전체를 수정하는 경우가 생길수도 있으니 말이다.  

그래서 이를 해결하고자 C++의 표준에서는 'Namespace'라는 문법을 정의해서 이러한 문제에 대한 근본적인 해결책을 제시한다.  

간단한 예로 한 동에 철수라는 애가 두 명 산다고 생각해보자.  

이 둘을 구분하는 방법은 무수히 많지만 '201호에 사는 철수'와 '202호에 사는 철수'로 구분해보자.  

이때 사용된 201호와 202호가 바로 Namespace의 기본 원리이다.  

'그렇다면 C++에서는 어떤 식으로 철수를 부를까?'  

```
#include <iostram>

void Callcs()
{
	std::cout << "201호에 사는 철수 부르기" << std::endl;
}
void Callcs()
{
	std::cout << "202호에 사는 철수 부르기" << std::endl;
}

int main()
{

	Apt201();
    return 0;
}
```

별다른 설명이 없이도 위의 예제는 이름과 매개변수 형이 동일하기 때문에 문제가 된다고 파악할 수 있다.  

이런 상황에서 아래와 같이 201호의 Namespace를 만들고, 이 안에 함수를 정의하거나 변수를 선언한다면,  

```
namespace Apt201	//201호의 Namespace 이름
{
	// Namespace 내부
}
```

마찬가지로 202호의 Namespace를 다음과 같이 만든다면,  

```
namespace Apt201	//201호의 Namespace 이름
{
	// Namespace 내부
}
```

충돌은 발생하지 않는다. 이제 실제로 Namespcace가 사용되는 것을 예제로 살펴보자.

```
#include <iostram>

namespace Apt201
{
	void Callcs()
	{
		std::cout << "201호에 사는 철수 부르기" << std::endl;
	}
}

namespace Apt202
{
	void Callcs()
	{
		std::cout << "202호에 사는 철수 부르기" << std::endl;
	}
}

int main()
{

	Apt201::Callcs();
    Apt202::Callcs();
    return 0;
}
```

이 구문을 보고 깊이 깨닫게 된 것이 있을 것이다. 바로 연산자 `::` 을 의미하는 'Scope resolution Operator(범위지정 연산자)'을 말이다.  

앞선 게시글에서 언급했듯이 std::cout이라는 문장은 std라는 Namespace에 정의된 cout이라는 함수를 사용하는 것이라고 이해하고 넘어가자.  

그렇다면 다음으로 넘어가서, 우리가 익히 아는 것처럼 프로젝트에서 Function declaration과 definition를 분리하는 것은 일반적인 형태이다.  

이 경우, 'Function Declaration(함수의 선언)'은 헤더파일에 저장하고, 'Function Definition(함수의 정의)'는 소스페일에 저장한다.  

따라서 아래의 예제를 통해 Namespace 기반에서 함수의 선언과 정의를 구분하는 방법을 살펴보자.  

```
#include <iostram>

namespace Apt201
{
	void Callcs();
}

namespace Apt202
{
	void Callcs();
}

int main ()
{
	Apt201::Callcs();
    Apt202::Callcs();
    return 0;
}

void Apt201::Callcs(void)
{
	std::cout << "201호에 사는 철수 부르기" << std::endl;
}

void Apt202::Callcs(void)
{
	std::cout << "202호에 사는 철수 부르기" << std::endl;
}
```

참고로, 동일한 Namespace에 정의된 함수를 호출할 때에는 Namespace를 명시할 필요가 없다. 아래의 예제를 살펴보도록 하자.  

```
#include <iostram>

namespace Apt201
{
	void Callcs();
}

namespace Apt201
{
	void Byecs();
}

namespace Apt202
{
	void Callcs();
}

int main ()
{

	Apt201::Callcs();
    Apt202::Callcs();
    return 0;
}

void Apt201::Callcs()
{

	std::cout << "201호에 사는 철수 부르기" << stdendl;
    Byecs();			//동일한 Namespace의 함수 호출
    Apt202::Callcs();	//다른 Namespace의 함수 호출
}

void Apt201::Byecs()
{
	std::cout << "철수한테 인사하기" << std::endl;
}

void Apt202::Callcs()
{
	std::cout << "202호에 사는 철수 부르기" << std::endl;
}
```

위의 예제를 통해서 Namespace와 관련된 몇 가지 특성을 이해했을 것이다. 그렇다면 Namespace의 마지막 특징인 Overlap(중첩)에 대해 살펴보자.  

Namespace의 Overlap은 하나의 Namespace안에 다른 Namespace가 삽입될 수 있다는 것이다. 아래와 같이 말이다.  

```
#include <iostram>

namespace Parent
{
	int num = 2;

    namespace SubOne
    {
    	int num = 3;
    }

    namespace SubTwo
    {
    	int num = 4;
    }
}
```

위 예제에 대해서는 어렵지않게 이해했으리라 생각된다.  

총 3개의 num이 존재하는데, 각각 선언된 Namespace가 다르기 때문에 충돌이 발생하지 않았다.  

그렇다면 각각의 변수 num의 접근해보자.  

```
std::cout << Parent::num << std::endl
std::cout << Parent::SubOne::num << std::endl;
std::cout << Parent::SubTwo::num << std::endl;
```  

이는 순서대로 2, 3, 4가 출력된다. 이정도면 Namespace의 문법적 규칙을 거의 파악했을 것이다.  

앞서 이야기한 std::cout, std::cin, std::endl을 사용해 콘솔의 입출력을 진행했다.  

우리는 이것에 대해 자세히는 모르지만 조금은 알 수 있다. `::` 연산자의 의미를 알게되었기 때문이다.  

이는 아래와 같이 이야기할 수도 있다.  

```
std::cout : namespace std에 선언된 cout
std::cin : namespace std에 선언된 cin
std::endl : namespace std에 선언된 endl
```  

따라서 다음과 같이 Namespace의 구성을 머리 속에 그려볼 수 있다. 아직까지 cout, cin, endl의 문법 구성은 모르지만 말이다.  

```
namespace std
{
	cout . . . .
    cin . . . .
    enl . . . .
}
```

때문에 헤더파일 `<iostream>`에 선언되어 있는 'cout', 'cin' 그리고 'endl'은 'namespace std' 안에 선언되어 있다는 결론을 내릴 수 있다.  

이렇듯 C++에서는 충돌을 막기 위해, C++표준에서 제공하는 다양한 요소들은 'namespace std' 안에 선언되어 있다.  

그런데 이쯤되면 이런 생각을 하게 될 것이다. "좋은 건 알겠는데 너무 번거롭지 않나?"라고 말이다.  

C++에서는 그런 사용자들의 needs를 알고 이런 귀찮음을 해소하기 위해 `using`이라는 키워드를 제공한다.  

다음 예제를 살펴보자.  

```
#include <iostream>

namespace Simple
{
	void SimpleFunc()
    {
    	std::cout << "Simple Function!" << endl;
        std::cout << "In Namespace Simple!" << endl;
    }
}

int main()
{

	using Simple::SimpleFunc;
    SimpleFunc();
    return 0;
}
```

위 예제에서 사용된 using이라는 키워드는 'SimpleFunc()를 Namespace Simple에서 찾아라!'라는 일종의 선언이다.  

이때, SimpleFunc의 자리는 function이 될 수도 있고, variable이 될 수도 있다.  

그리고 위 예제에서는 using이 main function 내에 존재하는데, 이러한 경우 local variable decalation과 마찬가지로 선언된 이후부터 효력을 발휘한다.  

또한, 선언된 지역(local)을 벗어나면, declaration의 효력은 잃게된다.  

따라서 프로그램 전체 영역에 효력을 미치게 하려면 global variable과 마찬가지로 function 밖에서 declaration을 해야 한다.  

여기서 생각해볼 것은 하나의 Namespace를 사용하는데 그 안에 속한 함수나 변수가 너무 많을 때는 번거롭게 일일이 선언해야하냐는 것이다.  

이에 대해서는 아래와 같이 사용하면 되겠다.  

```
#include <iostream>
using namespace std;

int main()
{

	int num = 20;
    cout << "Hello World!" << endl;
    cout << "Hello " << "World!" << endl;
    cout << num << ' ' << 'A';
    cout << ' ' << 3.14 << endl;
}
```

이와 같이 사용하면 **편하다는 장점**이 있다. 그러나 잠깐 생각해본다면 이렇게 사용하는 경우에는 충돌이 날 가능성이 높아진다.  

따라서, **무조건 편한 것을 사용하기 보다는 혼용하는 것이 바람직하다.**  

마지막으로 살펴볼 내용은 Namespace의 별칭 지정이다. 이것은 중첩과 관련되어 여러번 중첩이 된 경우에 사용할 수 있다.  

가령 다음과 같이 과도하게 사용되었을 경우에는  

```
namespace AAA
{
	namespace BBB
    {
    	namespace CCC
        {
        	int num1;
            int num2;
        }
    }
}
```

다음과 같은 방법으로 변수 num1과 num2를 호출한다면 매우 불편할 것이다.  

```
AAA::BBB::CCC::num1 = 20;
AAA::BBB::CCC::num2 = 30;
```  

그래서 이러한 경우에는 다음과 같이 별칭을 줄 수 있다.  

```
namespace ABC = AAA::BBB::CCC;
```  

이처럼 별칭을 주고 아래처럼 사용하면 된다.  

```
ABC::num1 = 20;
ABC::num2 = 30;
```  

간단한 팁으로 연산자 `::` 의 또 다른 기능을 살펴보도록 하자.  

local variable의 이름이 global variable과 같을 경우, global variable은 local variable에 의해 가려진다는 특징은 익히 알고있을 것이다.  

그렇다면 이렇게 가려진 상황에서 전역변수에 접근하려면 어떻게 해야할까? 거기에 대한 답은 'Scope resolution Operator'가 해줄 것이다. 아래의 예제를 살펴보자.  

```
#include <iostream>
int var=100;	// global variable

int SimpleFunc()
{

	int val = 20;	// local variable
    var += 3;		// local variable의 값 3 증가
    ::var += 7;	// global variable의 값 7 증가
}
```

