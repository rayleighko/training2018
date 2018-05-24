## Constructor & Destructor

##### 

[뒤로가기](/c++/README.md)

지금까지는 객체를 생성하고, 객체의 멤버변수 초기화를 위해 InitMembers()라는 함수를 정의하고, 호출했다.  

정보은닉을 목적으로 멤버변수들을 private으로 선언했으니 초기화를 위해 함수를 정의하는 것은 당연하다. 그러나 이것은 불편하다. 그래서 이러한 불편을 줄이기 위해 만들어진 '생성자'를 알아보자.

---

생성자의 특징은 아래와 같다.  

* 클래스의 이름과 함수(생성자)의 이름이 같다.
* 반환형이 선언되어 있지 않으며, 실제로 반환하지 않는다.  

아래의 SimpleClass()와 같이 말이다.  

```
class SimpleClass
{
private:
	int num;
public:
	SimpleClass(int n)
    {
    	num = n;
    }
    int GetNum() const;
    {
    	return num;
    }
};
```

이러한 유형의 함수를 생성자라고 하며, 객체 생성 시 딱 1회만 호출되는 특징을 갖는다.  

그럼 생성자를 사용하기 전과 후의 객체 생성 과정을 살펴보자.  

```
// 생성자 이전

SimpleClass sc;							// 1. 전역, 지역 및 매개변수의 형태로 선언하는 방법
SimpleClass *ptr = new SimpleClass;		// 2. 동적 할당의 형태로 선언하는 방법
```
  
```
//생성자 이후

SimpleClass sc(20);							// 1. 생성자에 20을 전달.
SimpleClass *ptr = new SimpleClass(30);		// 2. 생성자에 30을 전달.
```

크게 어렵지 않은 내용이고, 아래와 같은 두 가지 사실만 더 기억하면 생성자는 이해하리라고 생각된다.  

* 생성자도 오버로딩이 가능하다.
* 생성자도 매개변수에 '디폴트 값'을 설정할 수 있다.  

생성자도 함수의 일종이기 때문에 위와 같은 특징을 갖는 것은 당연하다. 아래의 예제를 살펴보자.  

```
#include <iostream>
using namespace std;

class SimpleClass
{
private:
	int num1;
    int num2;
public:
	SimpleClass()
    {
    	num1 = 0;
        num2 = 0;
    }
    SimpleClass(int n)
    {
    	num1 = n;
        num2 = 0;
    }
    SimpleClass(int n1, int n2)
    {
    	num1 = n1;
        num2 = n2;
    }
    /*
    Simpleclass (int n1 = 0, int n2 = 0)
    {
    	num1 = n1;
        num2 = n2;
    }
    */
    void ShowData() const
    {
    	cout << num1 << ' ' << num2 << endl;
    }
};

int main()
{
	SimpleClass sc1;
    sc1.ShowData();

    SimpleClass sc2(100);
    sc2.ShowData();

    SimpleClass sc3(100, 200);
    sc3.ShowData();

	return 0;
}
```

우선 우리는 위 예제로 생성자도 오버로딩이 가능하다는 것을 알았다.  

그리고 현재 주석처리 되어있는 생성자의 주석을 빼고 나머지 생성자에 주석을 처리하면 매개변수의 디폴트 값을 설정할 수 있다는 것을 알 수 있었다(만약 다른 생성자를 주석처리하지 않고 디폴트 값을 사용한 생성자의 주석을 풀면 컴파일 에러가 발생한다).  

추가적으로, 아래와 같은 형식으로 선언하는 것은 불가능하다.  

```
SimpleClass sc();	// 이 형태는 불가능하다

// SimpleClass sc; 의 형태로 사용하거나
// SimpleClass *ptr = new SimpleClass; 혹은
// SimpleClass *ptr = new SimpleClass(); 로 사용해야 한다  
```

조금 헷갈릴 수도 있다. 어떤 것은 비슷한 형태인데 가능하고, 어떤 것은 불가능하기 때문이다.  

이 문장이 불가능한 이유는 아래의 예제를 통해 살펴보자.  

```
#include <iostream>
using namespace std;

class SimpleClass
{
private:
	int num1;
    int num2;
public:
	SimpleClass(int n1 = 0, int n2 = 0)
    {
    	num1 = n1;
        num2 = n2;
    }
    void ShowData() const
    {
    	cout << num1 << ' ' << num2 << endl;
    }
};

int main()
{
	SimpleClass sc1();		// 함수의 원형을 선언한 것이다
    SimpleClass mysc = sc()1;
    mysc.ShowData();
    return 0;
}

SimpleClass sc1()
{
	SimpleClass sc(20, 30);
    return sc;
}
```

이제 조금 감이 잡힐 것이다. 보통 함수의 원형은 함수 밖에(전역적으로) 선언하지만, 함수 내에서도 지역적으로 선언이 가능하다.  

그리고 위에서 'SimpleClass sc1()'의 경우가 이에 해당한다.  

그래서 이 문장을 객체생성으로 인정하면, 컴파일러는 이 문장을 만났을 때, 객체생성문인지 함수의 원형 선언인지 구분할 수 없다.  

결국 이러한 형태는 사용할 수 없게 하는 것이다.  

그렇다면 이전의 예제에 생성자를 적용해보자.  

```
#include <iostream>
using namespace std;

class FruitSeller
{
private:
	int APPLE_PRICE;
	int numOfApples;
	int myMoney;
public:
	FruitSeller(int price, int num, int money)
	{
		APPLE_PRICE = price;
		numOfApples = num;
		myMoney = money;
	}
	int SaleApples(int money)
	{
		int num = money / APPLE_PRICE;
		numOfApples -= num;
		myMoney += money;

		return num;
	}
	void ShowSalesResult() const
	{
		cout << "남은 사과: " << numOfApples << endl;
		cout << "판매 수익: " << myMoney << endl << endl;
	}
};

class FruitBuyer
{
private:
	int myMoney;
	int numOfApples;
public:
	FruitBuyer(int money)
	{
		myMoney = money;
		numOfApples = 0;
	}
	void BuyApples(FruitSeller &seller, int money)
	{
		numOfApples += seller.SaleApples(money);
		myMoney -= money;
	}
	void ShowBuyResult() const
	{
		cout << "현재 잔액: " << myMoney << endl;
		cout << "사과 개수: " << numOfApples << endl << endl;
	}
};

int main()
{
	FruitSeller seller(1000, 20, 0);
	FruitBuyer buyer(5000);
	buyer.BuyApples(seller, 2000);

	cout << "과일 판매자의 현황" << endl;
	seller.ShowSalesResult();
	cout << "과일 구매자의 현황" << endl;
	buyer.ShowBuyResult();

	return 0;
}
```

참고로, 이전에 정의했던 InitMembers 함수를 지우지 않고, 생성자 내에서 이 함수를 호출하게끔 할 수도 있다.  

그리고 실제로 생성자 내에서 멤버의 초기화를 목적으로 함수를 호출할 때도 있으니 참고하기 바란다.  

그럼 이어서 다른 예제들도 생성자를 적용해보도록 하자.  

* Point.h, Point.cpp			// Point 클래스의 선언 및 정의
* Rectangle.h, Rectangle.cpp	// Rectangle 클래스의 선언 및 정의
* RectangleFaultFind.cpp		// 실행을 위한 main 함수의 정의  

이 예제 말이다.  

먼저 Point 클래스에 생성자를 적용해보자. 아래와 같이 말이다.  

```
// Point.h

class Point
{
private:
	int x;
    int y;
public:
	Point(const int &xpos, const int &ypos);	// 생성자
    int GetX() const;
    int GetY() const;
    bool SetX(int xpos);
    bool SetY(int ypos);
};
```

그리고 아래와 같이 정의하면된다.  

```
Point::Point(const int &xpos, const int &ypos)
{
	x = xpos;
    y = ypos;
}
```

하지만 Rectangle 클래스의 생성자 정의는 저금 더 생각을 해봐야 할 것 같다.  

그 이유는 두 개의 Point 객체를 멤버로 지니고 있어서 Rectangle 객체가 생성되면, 두 개의 Point 객체가 함게 생성되서 아래와 같은 의문이 생기기 때문이다.  

> "Rectangle 객체를 생성하는 과정에서 Point 클래스의 생성자를 통해 Point 객체를 초기화할 수 없을까?"
  

생성자의 목적은 멤버변수의 초기화이기 때문에 객체 생성과정에서의 생성자 호출은 객체의 초기화를 한결 수월하게 한다.  

따라서 위와 같은 생각을 하게될 수밖에 없다. 이를 위해 Member Initializer을 사용해 원하는 것을 해보도록 하자.  

아래는 생성자가 추가된 Rectangle 클래스의 선언이다.  

```
class Rectangle
{
private:
	Point upLeft;
    Point lowRight;
public:
	Rectangle(const int &x1, const int &y1, const int &x2, const int &y2);
    void ShowRecInfo() const;
};
```

생성자는 직사각형을 이루는 두 점의 정보를 직접 전달할 수 있게 정의하였다. 이제 이 정보를 이용해 Point 객체가 초기화되게 만들어야 한다.  

그 전에, Rectangle 클래스의 생성자 정의를 보자.  

```
Rectangle::Rectangle(const int &x1, const int &y1, const int &x2, const int &y2)
			:upLeft(x1, y1), lowRight(x2, y2)

{
	// empty
}
```
  
위 코드에서 아래의 내용이 'Member Initializer(멤버 이니셜라이저)'이다.

```
:upLeft(x1, y1), lowRight(x2, y2)
```
  
그리고 이것이 의미하는 것은 각각 다음과 같다.  

> "객체 upLeft의 생성과정에서 x1과 y1을 인자로 전달받는 생성자를 호출해라"
> "객체 lowRight의 생성과정에서 x2와 y2을 인자로 전달받는 생성자를 호출하라"  

이렇듯 Member Initailizer는 멤버변수로 선언된 객체의 생성자 호출에 활용된다. 그럼 완성된 예시를 살펴보자.  

```
//Point.h

#pragma once

class Point
{
private:
	int x;
	int y;
public:
	Point(const int &xpos, const int &ypos);
	int GetX() const;
	int GetY() const;
	bool SetX(int xpos);
	bool SetY(int ypos);
};
```
  
```
//Point.cpp

#include <iostream>
#include "Point.h"
using namespace std;

Point::Point(const int &xpos, const int &ypos)
{
	x = xpos;
	y = ypos;
}

int Point::GetX() const { return x; }
int Point::GetY() const { return y; }

bool Point::SetX(int xpos)
{
	if (0 > xpos || xpos > 100)
	{
		cout << "벗어난 범위의 값 전달" << endl;

		return false;
	}

	x = xpos;
	return true;
}

bool Point::SetY(int ypos)
{
	if (0 > ypos || ypos > 100)
	{
		cout << "벗어난 범위의 값 전달" << endl;

		return false;
	}

	y = ypos;

	return true;
}
```
  
```
//Rectangle.h

#pragma once

#include "Point.h"

class Rectangle
{
private:
	Point upLeft;
	Point lowRight;
public:
	Rectangle(const int &x1, const int &y1, const int &x2, const int &y2);
	void ShowRecInfo() const;
};

{% endhighlight %}  

{% highlight Cpp %}
//Rectangle.cpp

#include <iostream>
#include "Rectangle.h"
using namespace std;

Rectangle::Rectangle(const int &x1, const int &y1, const int &x2, const int &y2)
	:upLeft(x1, x2), lowRight(x2, y2)
{
	// empty
}

void Rectangle::ShowRecInfo() const
{
	cout << "좌 상단: " << '[' << upLeft.GetX() << ", ";
	cout << upLeft.GetY() << ']' << endl;
	cout << "우 하단: " << '[' << lowRight.GetX() << ", ";
	cout << lowRight.GetY() << ']' << endl;
}
```
  
```
//RectangleConstructor.cpp

#include <iostream>
#include "Point.h"
#include "Rectangle.h"
using namespace std;

int main()
{
	Rectangle rec(1, 1, 5, 5);
	rec.ShowRecInfo();
	return 0;
}
```

이제 제법 클래스다운 모습이 되었다. 참고로 Member Initializer를 사용하다 보면, 생성자의 몸체 부분이 비는 경우가 많이 발생한다. 이것은 이상한 것이 아니니 신경이 쓰여도 익숙해지도록 하자.  

그러면 우리는 아래와 같이 3단계로 객체의 생성과정을 정리할 수 있다.  

1. 메모리 공간의 할당		// 선언
2. 이니셜라이저를 이용한 멤버변수(객체)의 초기화	// or 생성자의 몸체부분 실행
3. 생성자의 몸체부분 실행
  

Cpp의 모든 객체는 위의 세 가지 과정을 순서대로 거쳐서 생성이 완성된다(물론 Initializer가 선언되지 않았다면, 메모리 공간의 할당과 생성의 몸체부분의 실행으로 객체생성은 완성된다).  

그렇다면 만약 생성자도, MemberInitializer도 정의되어 있지 않다면 어떻게 될까? 그것은 바로 '디폴트 생성자'를 자동으로 삽입되어 호출하게 된다.  

이에 대해서는 잠시 후에 살펴보도록 하고, Initializer에 대해 조금 더 자세하게 살펴보자.  

Member Initializer는 객체가 아닌 멤버의 초기화에도 사용할 수 있다. 아래와 같이 말이다.  

```
class SoSimple
{
private:
	int num1;
    int num2;
public:
	SoSimple(int n1, int n2) : num1(n1)
    {
    	num2 = n2;
    }
    . . . . .
};
```

이제 우리는 생성자의 몸체에서 초기화하는 방법과 이니셜라이저를 이용하는 초기화 방법 중에서 선택이 가능하다. 그러나 일반적으로 멤버변수의 초기화에 있어서는 이니셜라이저를 선호하는 편이다. 아래와 같은 장점이 있기 때문이다.  

* 초기화의 대상을 명확히 인식할 수 있다.
* 성능향상에 약간 도움이 된다.
* 명확한 표기라고 생각된다. (실제 많은 프로그래머들이 이렇게 생각한다)
  
Initializer를 통해서 초기화되는 멤버는 선언과 **동시에** 초기화가 이뤄지는 형태로 바이너리 코드가 생성된다.  

반면, 생성자의 몸체부분에서 대입연산을 통한 초기화를 진행하면, 선언과 초기화를 각각 **별도의 문장으로** 진행하는 형태로 바이너리 코드가 생성된다.  

그리고 이는 선언과 동시에 초기화해야 하는 const에도 적용이 가능해 Initializer를 이용해 const 멤버변수의 초기화도 가능하다. 아래의 예제를 통해 실습해보자.  

```
#include <iostream>
using namespace std;

class FruitSeller
{
private:
	const int APPLE_PRICE;
    int numOfApples;
    int myMoney;
public:
	FruitSeller(int price, int num, int money)
    	: APPLE_PRICE(price), numOfApples(num), myMoney(money)
    {
      	// empty
    }
    int Saleapples(int money) { . . . . }
    void SowSalesResult() const { . . . . }
};

class FruitBuyer
{
private:
   	int myMoney;
    int numOfApples;
public:
  	FruitBuyer(int money)
      	: myMoney(money), numOfApples(0)
    {
    	// empty
    }
    void BuyApples(FruitSeller &seller, int money) { . . . . }
    void showBuyResult() const { . . . . }
};

int main() { . . . . }
```

중복되는 부분은 생략하고 const 멤버변수가 이니셜라이저를 통해서 초기화가 가능하다는 사실만 확인해보자.  

또한, Initializer는 참조자도 멤버변수로 선언될 수 있다. 아래와 같이 말이다.  

```
#include <iostream>
using namespace std;

class AAA
{
public:
	AAA()
    {
    	cout << "empty object" << endl;
    }
    void ShowYourName()
    {
    	cout << "I'm class AAA" << endl;
    }
};

class BBB
{
private:
	AAA &ref;
    const int &num;
public:
	BBB(AAA &r, const int &n)
    	: ref(r), num(n)
    {
        // emptyss
    }
    void ShowYourName()
    {
    	ref.ShowYourName();
        cout << "and" << endl;
        cout << "I ref num" << num << endl;
    }
};

int main()
{
	AAA obj1;
    BBB obj2;
    obj2.ShowYourName();
    return 0;
}
```

이처럼 참조자를 멤버변수로 선언하는 경우가 흔한 것은 아니니 의미를 이해할 수 있을 정도만 알고 넘어가도록 하자.  

메모리 공간의 할당 이후에 생성자의 호출까지 완료되어야 '객체'라 할 수 있다. 즉, 객체가 되기 위해서는 반드시 하나의 생성자가 호출되어야 한다.  

그런데 지금까지는 생성자를 선언하지 않았다. 그렇다면 우리는 잘못된 방식으로 프로그램을 구현했던 것일까?  

> "아니다! 생성자를 정의하지 않는 클래스에는 컴파일러에 의해 디폴트 생성자가 자동으로 삽입된다!"
  

그렇다. 또한 디폴트 생성자는 인자를 받지 않으며, 내부적으로 아무런 일도 하지 않는 생성자이다.  

그래서 아래의 두 클래스는 완전히 동일하다.  

```
class AAA
{
private:
	int num;
public:
	int GetNum() { return num; }
};
```
  
```
class AAA
{
private:
	int num;
public:
	AAA(){}
    int GetNum() { return num; }
};
```

이제 모든 객체는 한 번의 생성자 호출을 동반한다는 것을 이해했을 것이다.  

그리고 이는 new 연산자를 이용한 객체의 생성에도 해당하는 이야기이다. 즉, 위의 클래스를 다음의 형태로 생성해도 객체의 생성과정에서 생성자가 호출된다.  

```
AAA *ptr = new AAA;
```

그러나 다음과 같이 new 연산자가 아닌, C언어의 malloc 함수를 사용하면 생성자는 호출되지 않는다.  

```
AAA *ptr = (AAA*)malloc(sizeof(AAA));
```

malloc 함수호출 시, 실제로는 AAA 클래스의 크기 정보만 바이트 단위로 전달되기 때문에 생성자가 호출될 수 없는 것이다.  

따라서 객체를 동적으로 할당하려면 반드시 new 연산자를 이용해야 한다.  

앞서 보인 매개변수가 void형으로 선언되는 디폴트 생성자는 생성자가 하나도 정의되어 있지 않을 때에만 삽입된다.  

그래서 다음과 같은 클래스는 디폴트 생성자가 삽입되지 않는다.  

```
class SoSimple
{
private:
	int num;
public:
	SoSimple(int n) : num(n) { }
};
```

이렇게 되면 아래와 같은 형태로는 객체 생성이 불가능하다. 아래와 같이 매개변수를 받는 생성자가 정의되지도, 자동으로 삽입되지도 않았기 때문이다.  

```
SoSimple simObj2;					// X
SoSimple *simPtr2 = new SoSimple;	// X
```

만약 위의 형태로 객체를 생성하고 싶다면 아래와 같은 형태로 생성자를 추가해야 한다.  

```
SoSimple() : num(0) { }		// 매개변수가 없을 때는 num에 0을 삽입
```

이제 어느정도 생성자에 대한 문법적인 설명이 정리가 되었다. 이제는 심화적으로 생성자를 다뤄보도록 하자.  

그 첫 번째는 private 생성자이다. 앞서 보인 생성자들은 모드 public으로 선언되었다.  

객체의 생성이 클래스의 외부에서 진행되기 때문에 생성자는 public으로 선언되어야 한다.  

그럼 아래와 같은 질문이 생길 수 있다.  

> "클래스 내부에서 객체를 생성한다면, 생성자가 private으로 선언되어도 되는 걸까? 그게 높은 보안성을 유지할 수 있을 것 같은데?"  

그렇다. 그래서 클래스 내부에서만 객체의 생성을 허용하려는 목적으로 생성자를 private으로 선언하기도 한다.  

그럼 생성자의 public과 private 선언에 따른 차이점을 확인해보자.  

```
#include <iostream>
using namespace std;

class AAA
{
private:
	int num;
public:
	AAA() : num(0) { }
	AAA& CreateInitObj(int n) const
	{
		AAA *ptr = new AAA(n);
		return *ptr;
	}
	void ShowNum() const { cout << num << endl; }
private:
	AAA(int n) : num(n) { }
};

int main()
{
	AAA base;
	base.ShowNum();

	AAA &obj1 = base.CreateInitObj(3);
	obj1.ShowNum();

	AAA &obj2 = base.CreateInitObj(12);
	obj2.ShowNum();

	delete &obj1;
	delete &obj2;
	return 0;
}
```

위 예제에서는 힙 영역에 생성된 객체를 참조의 형태로 반환하고 있다. 이는 앞서 설명한 아래의 문장을 다시 확인시켜 주는 것이다.  

> "힙에 할당된 메모리 공간은 변수로 간주하여, 참조자를 통함 참조가 가능하다."
  

그리고 위 예제에서는 단순히 private으로 선언된 생성자를 통해서도 객체의 생성이 가능하다는 것을 볼 수 있다.  

하지만 private 생성자도 때로는 유용하게 사용된다. 특히 객체의 생성방법을 제한하고자 하는 경우에는 매우 유용하게 사용된다.  

이제 생성자에 대한 이야기는 마치고, '소멸자'에 대해 알아보자. 객체를 생성하는 데 반드시 필요한 것이 생성자의 호출이라면, 객체의 소멸에는 소멸자가 반드시 호출되어야 한다.  

소멸자는 아래와 같은 특징을 지닌다.  

* 클래스의 이름 앞애 '~'가 붙은 형태의 이름을 갖는다.
* 반환형이 선언되어 있지 않으며, 실제로도 반환하지 않는다.	// 생성자도 마찬가지
* 매개변수는 void형으로 선언되어야 하기 때문에 오버로딩도, 디폴트 값의 설정도 불가능하다.
  

예를 들어 AAA라는 클래스가 정의되어 있다면, 소멸자는 다음과 같은 형태를 지닌다.  

```
~AAA() { . . . . }
```

이러한 소멸자는 객체 소멸 과정에서 자동으로 호출된다. 그리고 프로그래머가 직접 소멸자를 정의하지 않으면, 디폴트 생성자와 같이 디폴트 소멸자가 자동으로 삽입된다.  

이러한 소멸자는 대게 생성자에서 할당한 리소스의 소멸에 사용된다. 만약 생성자 내에서 new 연산자를 이용해서 할당해 놓은 메모리 공간이 있다면, 소멸자에서는 delete 연산자를 이용해서 이 메모리 공간을 소멸시키는 것이다.  

아래의 간단한 예제를 보고 소멸자를 통해서 객체소멸과정에서 처리해야 할 일들을 자동으로 처리할 수 있다는 것을 살펴보도록 하자.  

```
#include <iostream>
#include <cstring>
using namespace std;

class Person
{
private:
	char *name;
	int age;
public:
	Person(char *myname, int myage)
	{
		int len = strlen(myname) + 1;
		name = new char[len];
		strcpy_s(name, len, myname);
		age = myage;
	}
	void ShowPersonInfo() const
	{
		cout << "이름: " << name << endl;
		cout << "나이: " << age << endl;
	}
	~Person()
	{
		delete[]name;
		cout << "called destructor!" << endl;
	}
};

int main(void)
{
	Person man1("Lee dong woo", 29);
	Person man2("Jang dong gun", 41);
	man1.ShowPersonInfo();
	man2.ShowPersonInfo();
	return 0;
}
```

소멸자는 실제로 이런 식으로 사용되니 부가적인 설명은 생략하도록 하겠다.  
