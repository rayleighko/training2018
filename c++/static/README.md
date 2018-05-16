## static

static에 대해서는 이미 알고 있을 것이다. '정적'이라는 개념으로 말이다. 이는 C++에서도 그대로 통용된다. 조금 다른 점이 있다면, class의 멤버변수와 멤버함수에 static 선언을 추가할 수 있는 것이다. 따라서 이번에는 이것에 대해 알아보도록 하자.  

---

설명에 앞서 C언어의 static 개념을 정리하고 넘어가자.  

> // 전역변수에 선언된 static
> 선언된 파일 내에서만 참조를 허용하겠다는 의미

> // 함수 내에 선언된 static
> 한 번만 초기화되고, 지역변수와 달리 함수를 빠져나가도 소멸되지 않음  

그렇다면 더욱 이해할 수 있게 간단한 예제를 살펴보자.  

```
#include <iostream>
using namespace std;

void Counter()
{
	static int cnt;
	cnt++;
	cout << "Current cnt: " << cnt << endl;
}

int main()
{
	for (int i = 0; i < 10; i++)
		Counter();

	return 0;
}
```

static 변수는 초기화하지 않으면, 지역변수처럼 '0'으로 초기화된다. 그리고 'static int cnt;'는 딱 1번만 실행된다. 즉, 이 'cnt'는 Counter() 가 호출될 때마다 새롭게 할당되는 지역변수가 아닌 것이다.  

상세한 설명은 생략하고, 이어서 C++의 static 멤버에 대해 살펴보자.  

간단한 예제를 통해 접근하도록 하자. 아래의 예제는 전역변수가 필요한 상황을 연출하기 위한 예제이다.  

```
#include <iostream>
using namespace std;

int simObjCnt = 0;
int cmxObjCnt = 0;

class SoSimple
{
public:
	SoSimple()
	{
		simObjCnt++;
		cout << simObjCnt << "번째 SoSimple 객체" << endl;
	}
};

class SoComplex
{
public:
	SoComplex()
	{
		cmxObjCnt++;
		cout << cmxObjCnt << "번째 SoComplex 객체" << endl;
	}
	SoComplex(SoComplex &copy)
	{
		cmxObjCnt++;
		cout << cmxObjCnt << "번째 SoComplex 객체" << endl;
	}
};

int main()
{
	SoSimple sim1;
	SoSimple sim2;

	SoComplex com1;
	SoComplex com2 = com1;
	SoComplex();

	return 0;
}
```

위 예제를 통해 다음과 같은 사실을 확인할 수 있다.  

* simObjCnt는 SoSimple 클래스를 위한 전역변수이다.
* cmxObjCnt는 SoComplex 클래스를 위한 전역변수이다.  

즉, 모든 SoSimple 객체들이 하나의 simObjCnt 변수를 공유하는 것이다. 마찬가지로 cmxObjCnt는 SoComplex  객체들이 공유하는 변수이다.  

그런데 이 둘은 모두 전역변수이기 때문에 이러한 제한이 지켜지지 않는다(어디서든 접근이 가능하다).  

따라서 문제를 일으킬 소지가 매우 높은 것이다. 그러나 simObjCnt를 SoSimple 클래스의 static 멤버로, cmxObjCnt를 SoComplex 클래스의 static 멤버로 선언하면, 이러한 문제가 생길 수 없다.  

어디선가 들어본 '클래스 변수'라고 부르는 static 멤버 변수에 대해서 알아봤다.  

이는 일반적인 멤버변수와 달리 클래스당 하나씩만 생성된다(그래서 클래스 변수라고 부른다). 아래와 같이 선언할 수 있다.  

```
class Sosimple
{
private:
	static int simObjCnt;	// static 멤버변수이자 클래스 변수
public:
	SoSimple()
    {
    	simObjCnt++;
        cout << simObjCnt << "번째 SoSimple 객체" << endl;
    }
};
int SoSimple::simObjCnt = 0;
```

위의 코드에 선언된 static 변수는 객체가 생성될 때마다 함께 생성되어 객체 별로 유지되는 변수가 아니다.  

객체를 생성하든 하지 않든, 메모리 공간에 딱 하나만 할당되어 모든 객체들이 공유하는 변수이다.  

때문에 각 객체의 멤버함수(생성자)에서는 simObjCnt에 멤버변수에 접근하듯이 접근할 수 있다.  

하지만 그렇다고 해서 객체 내에 simObjCnt가 존재하는 것은 아니다. 이 변수는 객체 외부에 있다.  

그리고 생성 및 소멸의 시점도 전역변수와 동일하다.  

따라서 이를 이용하면 앞서 보인 예제를 다음과 같이 보다 안정적으로 구현할 수 있다.  

```
#include <iostream>
using namespace std;

class SoSimple
{
private:
	static int simObjCnt;
public:
	SoSimple()
	{
		simObjCnt++;
		cout << simObjCnt << "번째 SoSimple 객체" << endl;
	}
};
int SoSimple::simObjCnt = 0;

class SoComplex
{
private:
	static int cmxObjCnt;
public:
	SoComplex()
	{
		cmxObjCnt++;
		cout << cmxObjCnt << "번째 SoComplex 객체" << endl;
	}
	SoComplex(SoComplex &copy)
	{
		cmxObjCnt++;
		cout << cmxObjCnt << "번째 SoComplex 객체" << endl;
	}
};
int SoComplex::cmxObjCnt = 0;

int main()
{
	SoSimple sim1;
	SoSimple sim2;

	SoComplex com1;
	SoComplex com2 = com1;
	SoComplex();

	return 0;
}
```

위 예제를 통해서 형성되는 객체와 변수의 관계는 앞서 설명한 것처럼 각 객체가 하나의 'static' 변수에 접근하는 모양이다.  

또한, simObjCnt에 접근을 허용하는 객체와 cmxObjCnt에 접근을 허용하는 객체가 구분되기 대문에 각각의 변수에 다른 영역에서 잘못 접근하는 일은 발생하지 않는다.

클래스가 끝나고 삽입된 'int SoSimple ::simObjCnt = 0;'은 static 변수의 초기화 방법이다.  

이렇듯 생성자가 아닌, 클래스 외부에서 초기화를 해야 하는 이유는 만약 SoSimple의 생성자를 아래와 같이 정의한다면, 객체가 생성될 때마다 변수 simObjCnt는 0으로 초기화될 것이다.  

```
SoSimple()
{
	simObjCnt = 0;
	simObjCnt++;
    cout << simObjCnt << "번째 SoSimple 객체" << endl;
}
```

왜냐하면 변수 simObjCnt는 객체가 생성될 때와 동시에 생성되는 변수가 아니라, 이미 메머리 공간에 할당이 이뤄진 변수이기 때문이다.  

그래서 static 멤버변수의 초기화 문법은 위의 코드처럼 생성자 밖에서 별도로 정의되는 것이다.  

이는 SoSimple 클래스의 static 멤버변수 simObjCnt가 메모리 공간에 저장될 때 0으로 초기화하라는 뜻이다.  

이제 static 멤버변수의 초기화를 별도의 방식으로 진행해야 하는 이유를 알았을 것이다.  

그렇다면 또 다른 접근 방법에 대해 알아보자. 사실 static 멤버변수는 어디서든 접근이 가능하다.  

이게 무슨 소리인가 함은 위의 예제와 같이 private으로 선언되면, 해당 클래스의 객체들만 접근이 가능하지만, public으로 선언되면, 클래스의 이름 또는 객체의 이름을 통해서 어디서든 접근이 가능하다는 말이다.  

이와 관련해서 아래의 예제를 보자(이 예제는 static 멤버변수가 객체 내에 존재하지 않는다는 사실도 알 수 있다).  

```
#include <iostream>
using namespace std;

class SoSimple
{
public:
	static int simObjCnt;
public:
	SoSimple()
	{
		simObjCnt++;
	}
};
int SoSimple::simObjCnt = 0;

int main()
{
	cout << SoSimple::simObjCnt << "번째 Sosimple 객체" << endl;

	SoSimple sim1;
	SoSimple sim2;

	cout << SoSimple::simObjCnt << "번째 SoSimple 객체" << endl;
	cout << sim1.simObjCnt << "번째 SoSimple 객체" << endl;
	cout << sim2.simObjCnt << "번째 SoSimple 객체" << endl;

	return 0;
}
```

|실행결과|
|----|
|0번째 SoSimple 객체|
|2번째 SoSimple 객체|
|2번째 SoSimple 객체|
|2번째 SoSimple 객체|
  

실행결과를 통해서도 알 수 있듯이, 다음 세 문장은 동일한 변수에 접근해서 동일한 출력을 보인다.  

```
cout << SoSimple::simObjCnt << "번째 SoSimple 객체" << endl;
cout << sim1.simObjCnt << "번째 SoSimple 객체" << endl;
cout << sim2.simObjCnt << "번째 SoSimple 객체" << endl;
```

그런데, 이 중에서 두 번째, 세 번째 문장은 sim1의 멤버변수와 sim2의 멤버변수에 접근하는 것같은 느낌이 든다(사실은 그것이 아닌 걸 알 것이다).  

따라서 public static 멤버에 접근할 대에는 첫 번째 문장에서 보이듯이 클래스의 이름을 사용해서 접근하는 것이 좋다(오해의 소지가 없기 때문이다).  

static 멤버함수 역시 그 특성이 static 멤버변수와 동일하다. 따라서 위에서 설명한 다음 특성이 그대로 적용된다.  

* 선언된 클래스의 모든 객체가 공유한다.  
* public으로 선언이 되면, 클래스의 이름을 이용해서 호출이 가능하다.  
* 객체의 멤버로 존재하는 것이 아니다.  

여기서 특히 주목할 것은 객체의 멤버로 존재하지 않는다는 사실이다.  

때문에 다음과 같은 코드는 컴파일 에러를 일으키게 된다.  

```
class SoSimple
{
private:
	int num1;
    static int num2;
public:
	SoSimple(int n) : num1(n)
    {
    	// empty
    }
    static void Adder(int n)
    {
    	num1 += n;	// 이 경우 컴파일 에러가 발생한다.
        num2 += n;
    }
}
```

static 멤버함수인 Adder에서 멤버변수인 num1에 접근하는 것이 잘못된 것이라는 것은 논리적으로도 이해가 가능한 부분이다. 아래와 같이 말이다.  

> "객체의 멤버가 아닌데, 어떻게 멤버변수에 접근하나!"  
> "객체 생성 이전에도 호출이 가능하다. 그런데 어덯게 멤버변수에 접근이 가능한가!"  
> "그래. 멤버변수에 접근을 한다고 치자, 그렇다면 어던 객체의 멤버변수에 접근을 해야하나?"  

이렇듯, 논리적으로 판단해도 static 멤버함수 내에서는, static으로 선언되지 않은 멤버변수의 접근도, 멤버함수의 호출도 불가능함을 알 수 있다.  

이를 정리하면 아래와 같이 말할 수 있다.  

> "static 멤버함수 내에서는 static 멤버함수와 static 멤버함수만 호출이 가능하다!"  

그리고 이러한 특성을 지니는 static 멤버변수와 static 멤버함수를 잘 활용하면, 대부분의 경우에 있어서 전역변수와 전역함수를 대체할 수 있다.  

앞선 챕터에서 보였듯이, 클래스 내에 선언된 const 멤버변수(상수)의 초기화는 이니셜라이저를 통해야만 가능하다.  

그렇다면 const static은 어떻까? const static으로 선언된 멤버변수(상수)는 아래와 같이 선언과 동시에 초기화할 수 있다.  

```
#include <iostream>
using namespace std;

class ConutryArea
{
public:
	const static int RUSSIA = 1707540;
	const static int CANADA = 998467;
	const static int CHINA = 957290;
	const static int SOUTH_KOREA = 9922;
};

int main()
{
	cout << "러시아 면적" << ConutryArea::RUSSIA << "km^2" << endl;
	cout << "캐나다 면적" << ConutryArea::CANADA << "km^2" << endl;
	cout << "중국 면적" << ConutryArea::CHINA << "km^2" << endl;
	cout << "한국 면적" << ConutryArea::SOUTH_KOREA << "km^2" << endl;

	return 0;

}
```

const static 멤버변수는, 클래스가 정의될 때 지정된 값이 유지되는 상수라는 것은 익히 알고 있을 것이다.  

그렇기 때문에, 위 예제에서 보이는 바와 같이 초기화가 가능하도록 문법으로 정의하고 있다.  

추가적으로 위의 코드를 보면 굳이 객체를 생성하지 않고, 멤버변수를 불러냈다. 이런 형식으로도 사용이 가능하니 참고하도록 하자.  

앞서 우리는 const와 explicit 키워드에 대해 살펴본 적이 있다. 이 둘은 나름의 의미가 있고, 매우 유용하게 사용되는 키워드들이다.  

그런데 이번에 설명할 mustable이라는 키워드는 사용의 빈도수가 거의 없고, 사용을 자제해야하는 키워드이다. 의미는 아래와 같다.  

> "const 함수 내에서의 값의 변경을 예외적으로 허용한다."  

아직은 이해가 되지 않을 수 있다. 그러므로 아래의 예제를 보고, 위 문장이 의미하는 바가 무엇인지 생각해보자.  

```
#include <iostream>
using namespace std;

class SoSimple
{
private:
	int num1;
	mutable int num2;
public:
	SoSimple(int n1, int n2)
		: num1(n1), num2(n2)
	{
		// empty
	}
	void ShowSimpleData() const
	{
		cout << num1 << ", " << num2 << endl;
	}
	void CopyToNum2() const
	{
		num2 = num1;
	}
};

int main()
{
	SoSimple sm(1, 2);

	sm.ShowSimpleData();
	sm.CopyToNum2();
	sm.ShowSimpleData();

	return 0;
}
```

위 예제의 CopyToNum2 함수와 mutable로 선언된 변수 num2에 대해서 긍정적으로 생각할 수 있다.  

> "흠, num2가 mutable로 선언되고, CopyToNum2 함수가 const로 선언되었으니, 이 함수 내에서 실수로 num1의 값이 변경되는 일은 발생하지 않겠구나! 좋은데?"
  

즉, 아래와 같은 대입연산이 거꾸로 진행되는 것을 방지한다는 것에 대해 긍정적일 수 있다.  

```
num1 = num2;	// 대입의 대상이 바뀌는 경우
```

만약 이와 같은 생각을 바탕으로 프로그래밍 코드를 짠다면, C++의 거의 모든 함수는 const로 선언을 해야 하고, 대다수의 멤버변수는 mutable로 선언을 해야할 것이다.  

조금 과장되었지만 mutable의 과도한 사용은 C++에서의 const라는 의미를 없애버릴 수 있는 것이다.  
