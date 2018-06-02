## Class & Array & 'this' pointer

##### 클래스와 배열, 'this' 포인터를 이용해 간단한 예제를 살펴보자.  

[뒤로가기](/c++/README.md)

C에서 구조체 배열과 구조체 포인터 배열을 선언했던 경험을 살려보자. 이번 시간에 다룰 내용인 객체 배열, 객체 포인터 배열도 이와 유사하다.  

---

우선 객체 배열에 대해 설명하려고 한다. 객체 기반의 배열은 아래와 같은 형태로 선언한다.  

```
SoSimple arr[20];

SoSimple *ptr = new SoSimple[20];	// 동적 할당
```

이러한 형태로 배열을 선언하면 10개의 SoSimple 객체가 배열을 구성하게 된다.  

이렇듯 우리가 알고 있는 구조체 배열의 선언과 차이가 없다.  

그러나 배열을 선언하는 경우에도 생성자는 호출되고, 이러한 생성자는 배열의 선언과정에서는 별도로 명시하지 못한다(이것은 생성자에 인자를 전달하지 못한다고 이해하면 된다).

그리고 배열선언 이후에 각각의 요소를 원하는 값으로 초기화시키려면, 일일이 초기화를 해줘야 한다.  

아래의 예제를 통해서 객체 배열에 대해 자세하게 알아보자.  

```
#include <iostream>
#include <cstring>
using namespace std;

class Person
{
private:
	char* name;
	int age;
public:
	Person(char* myname, int myage)
	{
		int len = (int)strlen(myname) + 1;
		name = new char[len];
		strcpy_s(name, len, myname);
		age = myage;
	}
	Person()
	{
		name = NULL;
		age = 0;
		cout << "called Person()" << endl;
	}
	void SetPersonInfo(char* myname, int myage)
	{
		name = myname;
		age = myage;
	}
	void ShowPersonInfo() const
	{
		cout << "이름: " << name << ", ";
		cout << "나이: " << age << endl;
	}
	~Person()
	{
		delete[]name;
		cout << "called destructor!" << endl;
	}
};

int main()
{
	Person parr[3];
	char namestr[100];
	char* strptr;
	int age;
	int len;

	for (int i = 0; i < 3; i++)
	{
		cout << "이름: ";
		cin >> namestr;
		cout << "나이: ";
		cin >> age;

		len = (int)strlen(namestr) + 1;
		strptr = new char[len];
		strcpy_s(strptr, len, namestr);

		parr[i].SetPersonInfo(strptr, age);
	}

	parr[0].ShowPersonInfo();
	parr[1].ShowPersonInfo();
	parr[2].ShowPersonInfo();

	return 0;
}
```

코드를 간략하게 설명하자면 strlen()과 strcpy_s는 데이터 손실을 줄이고자, 표준을 맞추기 위해 위와 같은 형식으로 호출했고, len의 크기가 namestr + 1인 것은 알다시피 문자열 끝에 포함되는 NULL도 가져오기 위함이다.  

위 예제의 실행결과를 통해 객체 배열 생성과 동시에 void형 생성자가 호출된다는 것과 배열이 소멸하는 것과 동시에 소멸자가 호출되는 것을 확인할 수 있다.  

그럼 이제 객체 포인터 배열도 알아보도록 하자. 객체 포인터 배열은 말 그대로 포인터 변수로 이뤄진 배열이다.  

포인터는 객체의 주소 값을 저장할 수 있다는 것을 알테니 위의 예제의 main()을 객체 포인터 배열 기반으로 아래와 같이 변경해보자.  

```
int main()
{
	Person* parr[3];
	char namestr[100];
	int age;

	for (int i = 0; i < 3; i++)
	{
		cout << "이름: ";
		cin >> namestr;
		cout << "나이: ";
		cin >> age;

		parr[i] = new Person(namestr, age);
	}

	parr[0]->ShowPersonInfo();
	parr[1]->ShowPersonInfo();
	parr[2]->ShowPersonInfo();

	delete parr[0];
	delete parr[1];
	delete parr[2];

	return 0;

}
```

출력 결과를 보고, 의문이 생길 수 있다. 이번 예제에서는 delete를 직접 해주었는데, 소멸자가 호출된 것이 의아하기 때문이다.  

할당된 메모리 공간의 소멸이 2번 일어난 것은 아닐까하는 의문이 생긴다. 그런데 이 부분은 delete를 지워보면 알 수 있다. delete를 지우면 소멸자가 호출되지 않는다.  

객체 배열은 저장의 대상을 객체로 하는 것이고, 객체 포인터 배열은 저장의 대상을 객체의 주소 값으로 하는 것이다.  

이제 배열을 이용해서 객체를 저장할 때 2가지 방법을 고를 수 있게 되었다.  

멤버함수 내에서는 this라는 이름의 포인터를 사용할 수 있다. 이는 객체 자신을 가리키는 용도로 사용된다. 아래의 예제를 보며 this 포인터를 알아보도록 하자.  

```
#include <iostream>
#include <cstring>
using namespace std;

class SoSimple
{
private:
	int num;
public:
	SoSimple(int n) : num(n)
	{
		cout << "num = " << num << ", ";
		cout << "address = " << this << endl;
	}
	void ShowSimpleData() const
	{
		cout << num << endl;
	}
	SoSimple* GetThisPointer()
	{
		return this;	// 반환형 Sosimple*을 이용해 객체의 주소 값(this) 반환
	}
};

int main()
{
	SoSimple sim1(100);
	SoSimple* ptr1 = &sim1;
	cout << ptr1 << ", ";
	ptr1->ShowSimpleData();

	SoSimple sim2(200);
	SoSimple* ptr2 = sim2.GetThisPointer();
	cout << ptr2 << ", ";
	ptr2->ShowSimpleData();

	return 0;
}
```

이제 우리는 소스코드와 실행결과를 통해 this는 객체 자신의 주소 값을 의미한다는 사실을 알았다. 이렇듯 this 포인터는 그 주소 값과 자료형이 정해져 있지 않은 포인터이다.  

예를 들어, 100번지에 할당된 SoSimple 객체 내에서 사용되면, this는 SoSimple형의 포인터이면서 그 값을 100번지를 의미하게 되는 것이다.  

이러한 this 포인터는 다양하게 사용할 수 있다. 아래의 클래스를 보면,  

```
class ThisClass
{
private:
	int num;
public:
	void ThisFunc(int num)
    {
    	this -> num = 207;	// 이 객체의 num에 207을 저장하고,
        num = 105;			// 매개변수의 값을 105로 변경한다.
    }
}
```

위 클래스의 멤버변수와 ThisFunc의 매개변수 이름은 num으로 동일하다. 그래서 ThisFunc 함수 내의 num이 의미하는 것은 매개변수 num이다(2번째 줄).

이처럼 함수 내에서 변수 이름만 참조하는 방법으로는 매개변수 num에 접근하는 것은 불가능하다. 

그러나 this 포인터를 이용하면(1번째 줄) 멤버변수에 접근할 수 있다.  

그 이유는 객체의 포인터를 가지고 지역변수에 접근하는 것이 불가능하기 때문이다.  

이를 활용하면 매개변수와 멤버변수의 이름을 달리하지 않아도 된다. 아래와 같이 말이다.  

```
#include <iostream>
using namespace std;

class TwoNumber
{
private:
	int num1;
	int num2;
public:
	TwoNumber(int num1, int num2)
	{
		this->num1 = num1;
		this->num2 = num2;
	}
	/*
	TwoNumber(int num1, int num2)
		: num1(num1), num2(num2)
	{
		// empty
	}
	*/
	void ShowTwoNumber()
	{
		cout << this->num1 << endl;
		cout << this->num2 << endl;
	}
};

int main()
{
	TwoNumber two(2, 4);
	two.ShowTwoNumber();

	return 0;
}
```

위의 문장에서 특별한 점은 Memeber Initializer와 this 포인터를 함께 사용할 수 없다는 것이다.  

대신에 저장하는 변수는 멤버변수로, 저장되는 값은(소괄호 안의 변수 및 상수는) 매개변수로 인식을 하기 때문에 주석처리한 문장이 생성자를 대신할 수 있다(키워드만 사용하지 못한다).  

이렇게 변수의 이름을 구분짓는 것은 개인의 스타일이나 가독성을 위한 것이니, 코드를 읽을 수 있을 정도로만 참고하고 넘어가는 것도 괜찮다.  

이어서 설명할 Self-reference는 객체 자신을 참조할 수 있는 참조자를 의미한다. 앞서 배운 this 포인터를 이용해서, 객체가 자신의 참조에 사용할 수 있는 참

```
#include <iostream>
using namespace std;

class SelfRef
{
private:
	int num;
public:
	SelfRef(int n) : num(n)
	{
		cout << "객체 생성" << endl;
	}
	SelfRef& Adder(int n)
	{
		num += n;
		return *this;
	}
	SelfRef& ShowTwoNumber()
	{
		cout << num << endl;
		return *this;
	}
};

int main()
{
	SelfRef obj(3);
	SelfRef &ref = obj.Adder(2);

	obj.ShowTwoNumber();
	ref.ShowTwoNumber();

	ref.Adder(1).ShowTwoNumber().Adder(2).ShowTwoNumber();

	return 0;
}
```

함수 Adder에서는 선언된 반환형과 반환의 내용을 함께 살펴보아야 한다. 반환의 내용은 *this로, 이는 이 문장을 실행하는 객체 자신의 포인터가 아닌, 객체 자신을 반환하겠다는 의미이다.  

그런데 반환형이 참조형 SelfRef&로 선언되었다. 따라서 객체 자신을 참조할 수 있는 '참조의 정보(참조 값)'가 반환된다.  

이어서 아래의 문장을 설명하겠다.  

> ref.Adder(1).ShowTwoNumber().Adder(2).ShowTwoNumber();
  

객체 ref의 Adder 함수가 먼저 호출된다. 그런데 Adder 함수는 참조 값을 반환하므로, 반환된 참조 값을 이용해서 다시 ShowTwoNumber 함수를 호출하게 된다.  

그리고 마찬가지로 반환되는 참조 값을 이용해서 다시 Adder 함수를 호출하고, 또 이어서 ShowTwoNumber 함수를 호출한다.  

이는 두 함수 Adder와 ShowTwoNumber가 객체의 참조 값을 반환하기 때문에 구성이 가능한 문장이고, 다양한 방법으로 멤버함수를 호출할 수 있다는 것을 보여주기 위함이다.  

자주 사용하지 않으니 참고하고 넘어가자.  

위에서 설명한 '참조 값'에 대해 자세히 알아보자.  

```
int main()
{
	int num = 7;
    int &ref = num;
    . . . . 
}
```

우리는 이 문장을 보고, 두 번째 대입연산에 의해서 변수 num을 참조자 ref가 참조한다는 것을 알고 있다.  

그렇다면 대입연산의 과정에서 참조자 ref에 무엇이 전달된다고 해야할까? 여기서 확실한 것은 num에 저장된 정수 값은 아니라는 것이다. 그래서 아래와 같이 표현하기도 한다.  

> "변수 num을 참조할 수 있는 참조의 정보가 전달된다."  

혹은 아래와 같이 이야기할 수도 있다.  

> "변수 num을 참조할 수 있는 참조 값이 참조자 ref에 전달되어, ref가 변수 num을 참조하게 된다."  

위에 설명한 것이 '참조 값'이 의미하는 것이다.  

대입연산자의 왼편에 '참조자의 선언'이 오거나, 반환형으로 '참조형'이 선언되면, 그 때 전달되는 정보를 표현하기 위해서 '참조 값'이라는 표현을 사용한 것이라고 이해하길 바란다.  
