## Copy Constructor

#####

[뒤로가기](/c++/README.md)
  
이번에는 Copy constructor, 즉 복사 생성자에 대해 이야기하고자 한다. 다소 생소하지만 생성자의 한 형태로 이해하면 어렵지 않을 것이다.  

물론 사전에 참조자와 생성자를 잘 이해했다면 말이다.  

---

우리는 지금까지 아래의 형태로 초기화를 해왔다.  

```
int num = 20;
int &ref = num;
```

하지만 Cpp에서는 다음과 같은 형태로도 초기화가 가능하다.  

```
int num(20);
int &ref(num);
```

위의 두 방식은 결과적으로 동일하다. 그리고 이것을 객체의 생성에도 응용해보자. 우선 아래의 클래스를 명시하도록 하겠다.  

```
class SoSimple
{
private:
	int num1;
    int num2;
public:
	SoSimple(int n1, int n2) : num1(n1), num2(n2)
    {
    	// empty
    }
    void ShowSimpleData()
    {
    	cout << num1 << endl;
        cout << num2 << endl;
    }
};
```

이어서 다음 main 함수의 실행결과를 예상해보자. 단순한 출력결과만이 아니라 객체의 생성관계를 생각하면서 살펴보자.  

```
int main()
{
	SoSimple(15, 20);
    SoSimple sim2 = sim1;
    sim2.ShowSimpleData();

    return 0;
}
```

위의 예제의 2번째 줄을 보면 멤버의 복사가 일어날 것만 같다. 그렇다. 실제로도 멤버의 복사가 일어나며, 아래와 같은 형식으로도 복사할 수 있다.  

```
SoSimple sim2(sim1);
```

그런데 여기서 우리는 의문이 든다. 'Cpp의 모든 객체는 생성자의 호출을 동반하는데, sim2는 어떤 과정을 거쳐서 생성되는 것을까?' 라고 말이다.  

위의 코드를 살펴보자. 이를 생성자의 호출관점에서 분석하면 아래와 같은 의미를 지닌다.  

* SiSimplle형 객체를 생성한다.
* 객체의 이름은 sim2이다.
* sim1을 인자로 받을 수 있는 생성자의 호출하고, 객체를 생성한다.
  

여기에 대한 추가적인 설명은 하지않겠다. 즉, 위의 객체생성문에서 호출하고자 하는 생성자는 아래와 같이 SoSimple 객체를 인자로 받을 수 있는 생성자인 것이다.  

```
SoSimple(SoSimple &copy)
{
	. . . . 
}
```

그런데 앞선 예제의 SoSimple 클래스 내에 이런 생성자는 없었다. 그렇다면 앞선 예제는 잘못된 예제일까? 여기에 대해서는 다음 예제를 보고, default Copy Constructor을 이해하도록 하자.  

```
#include <iostream>
using namespace std;

class SoSimple
{
private:
	int num1;
	int num2;
public:
	SoSimple(int n1, int n2) : num1(n1), num2(n2)
	{
		// empty
	}
	SoSimple(SoSimple &copy) : num1(copy.num1), num2(copy.num2)
	{
		cout << "Called SoSimple(SoSimple &copy)" << endl;
	}
	void ShowSimpleData()
	{
		cout << num1 << endl;
		cout << num2 << endl;
	}
};

int main()
{
	SoSimple sim1(15, 30);
	cout << "생성 및 초기화 직전" << endl;
	SoSimple sim2 = sim1;		// SoSimple sim2(sim1)로 자동 변환된다.
	cout << "생성 및 초기화 직후" << endl;
	sim2.ShowSimpleData();

	return 0;
}
```

위 예제는 특별할 게 없는 예제이다. 조금 특별한 것이 있다면 main 함수의 세 번째 줄에서 자동으로 변환되는 것이니까 말이다.  

무리없이 위 코드를 이해할 수 있다면 'Copy Constructor'에 대해서는 어렵지않게 이해할 것이라고 생각된다.  

왜 별로 다를 것 없는 생성자를 키워드까지 주어가며 부르는 것일까? 그것은 이 생성자가 호출되는 시점이 다른 일반 생성자와 차이가 있기 때문이다.  

그리고 위의 예제가 아닌 아래와 같이 정의를 해야 일반적인 Copy constructor가 된다.  

```
SoSimple(const SoSimple &copy)
	: num1(copy.num1), num2(copy.num2)
{
    cout << "Called SoSimple(const SoSimple &copy)" << endl;
}
```

그 이유는 멤버의 복사에 사용되는 원본을 변경시키는 것을 차단하기 위함이다.  

앞서 우리는 Copy Constructor의 삽입 없이도 멤버의 복사가 진행된 것(첫 번째 예제)을 경험한 적이 있다. 어떻게 그것이 가능한 것일까?  

> "Copy Constructor를 정의하지 않으면, 멤버의 복사를 진행하는 **default Copy Constructor**가 자동으로 삽입된다."
  

이로써 복사 생성자에 대한 기본적인 설명은 끝났다. 그런데 여기까지 배우고서, Copyt Constructor는 자동으로 default가 생성되니 직접 정의할 필요가 없다고 느낄 수도 있다.  

실제로, 많은 경우에서 직접 정의하지 않는다. 그러나 반드시 직접 정의해야 하는 경우도 있으니 참고하도록 하자.  

별도로 변환에 의한 초기화를 막아주는 키워드인 'explicit'에 대해 소개하고자 한다. 아래의 문장은,  

```
SoSimple sim2 = sim1;
```

다음과 같은 형태로 묵시적 변환이 일어나, Copy Constructor가 호출된다고 알고 있을 것이다.  

```
SoSimple sim2(sim1);
```

이는 Copy Constructor가 묵시적으로 호출된 것으로 볼 수 있다.  

따라서 위와 같은 유형의 변환이 마음에 들지 않는다면, 이러한 묵시적 호출을 허용하지 않을 수 있다. 키워드 'explicit'을 사용해서 말이다.  

```
explicit Sosimple(const SoSimple &copy)
	: num1(copy.num1), num2(copy.num2)
{
	// empty
}
```

이제는 묵시적 변환이 발생하지 않아서 아래와 같은 '대입 연산자를 이용한 객체의 생성 및 초기화'는 불가능하다.  

```
SoSimple sim2 = sim1;
```

여기서 '불편하게 굳이' 이렇게 사용하는 것이 좋은가에 대해 의문이 들 수 있다.  

그러나 이러한 묵시적 변환을 허용하는 것이 좋은 것만은 아니다. 묵시적 변환이 많이 발생하는 코드일 수록 코드의 결과를 예측하기 어렵기 때문이다.  

또한, 이러한 묵시적 변환은 Copy Constructor에서만 일어나는 것이 아니다. 전달인자가 하나인 생성자가 있다면, 이 역시 아래와 같이 묵시적 변환이 일어난다.  

```
class AAA
{
private:
	int num;
public:
	AAA(int n) : num(n)
    {
    	. . . . .
    }
};

int main()
{
	AAA obj = 3;	// AAA obj(3); 으로 변환된다
    return 0;
}
```

그리고 이 경우에도 마찬가지로 키워드 explicit가 생성자에 선언되면, 묵시적인 변환은 허용하지 않기 때문에 무조건 아래의 형태로 객체를 생성해야 한다.  

```
AAA obj1(3);
```
