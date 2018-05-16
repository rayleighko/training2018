## Copy Constructor Call Timing

이제 우리는 클래스 별로 필요한 Copy Constructor을 정의할 수 있다. 그럼 이러한 Copy Constructor가 호출되는 세 가지 시기에 대해 알아보도록 하자.  

추가적으로, Copy constructor의 호출시기가 중요한 것은 프로그램에서 Copy Constructor의 호출횟수가 성능에 관관여하기 때문이다. 그럼으로 이는 다소 어렵게 느껴지더라도 꼭 학습해야하는 것이다.  

---

일단 지난 시간에 배운 것처럼 아래의 경우에 Copy constructor가 호출된다는 것은 알고 있다.  

```
Person man1("Lee dong woo", 29);
Person man2 = man1;		// 복사 생성자의 호출
```

하지만 이것이 전부가 아니다. 위에도 언급했던 것처럼 아직 2가지 경우가 남아있다. 정리해보면 아래의 경우에 Copy Constructor가 호출된다.  

1. 기존에 생성된 객체를 이용해서 새로운 객체를 초기화하는 경우(위에서 언급한 경우)  
2. Call-by-value 방식의 함수호출 과정에서 객체를 인자로 전달하는 경우  
3. 객체를 반환하되, 참조형으로 반환하지 않는 경우  

이들은 아래와 같은 공통점이 있다.  

> "객체를 새로 생성해야한다. 단, 생성과 동시에 동일한 자료형의 객체로 초기화해야 한다."  

이것이 왜 공통점인가? 라는 의문이 들 수도 있다. 그러나 이에 대해서는 잠시 후에 설명하도록 하겠다. 그럼 위에서 언급한 첫 번째 경우를 제외한 나머지 경우에 대해 살펴보도록 하자.  

우선 메모리 공간이 할당과 동시에 초기화되는 상황을 살펴보자. 가장 대표적으로는 아래와 같은 상황이다.  

```
int num1 = num2;
```

이는 num1이라는 메모리 공간을 할당과 동시에 num2에 저장된 값으로 초기화시키는, 할당과 동시에 초기화가 이루어지는 문장이다. 그리고 아래와 같은 경우도 동시에 초기화가 이루어진다.  

```
int SimpleFunc(int n)
{
	. . . .
}
int main()
{
	int num = 10;
    SimpleFunc(num);	// 호출되는 순간 매개변수 n이 할당과 동시에 초기화된다.
    . . . .
}
```

위 코드에서 함수가 호출되는 순간에 매개변수 n이 할당과 동시에 변수 num에 저장되어 있는 값으로 초기화되는 것을 알 수 있다. 마지막으로 아래의(이해하기가 가장 난해한) 경우에도 메모리 공간이 할당되면서 동시에 초기화가 이루어진다.  

```
int SimpleFunc(int n)
{
	. . . .
    return n;
}

int main()
{
	int num= 10;
    cout << SimpleFunc(num) << endl;
    . . . .
}
```

이 경우가 난해한 이유는 아래와 같은 의문이 생길 수 있기 때문이다.  

> "정수를 반환하는데, 반환되는 값을 새로운 변수에 저장하는 것도 아닌데 메모리 공간이 할당된다고?"
  

이미 한 번 언급했지만, 반환되는 값을 별도의 변수에 저장하는 것과 별개로, 값을 반환하면 반환된 값은 별도의 메모리 공간이 할당되어서 저장이 된다. 이는 아래의 문장을 통해 다시 한 번 설명하겠다.  

```
cout << SimpleFunc(num) << endl;
```

반환되는 값을 메모리 공간의 어딘가에 저장해 놓지 않았다면, cout에 의한 출력이 가능할까?  

값이 출력되기 위해서는 그 값을 참조할 수 있어야 하고, 참조가 가능하려면 메모리 공간의 어딘가에 저장되어야 한다. 이제 아래와 같이 결론을 내릴 수 있다.  

> "함수가 값을 반환하면, 별도의 메모리 공간이 할당되고, 이 공간에 반환 값이 저장된다(반환 값으로 초기화 되는 것이다)."  

그림을 통해 설명하면 좋겠지만, 여건이 좋지 않아 그림은 생략하도록 하겠다. 그럼에도 충분히 이해했을 거라 생각된다.  

이로써 메모리 공간이 할당되면서 동시에 초기화되는 세 가지 상황을 정리하였다.  

그런데 이러한 세 가지 상황은 객체를 대상으로 해도 달라지지 않는다. 아래와 같이 말이다.  

```
Sosimple obj2 = obj1;
```
  
```
SoSimple SimpleFuncObj(SoSimple ob)
{
	. . . .
}

int main()
{
	SoSimple obj;
    SimpleFuncObj(obj);
    . . . .
}
```

위의 코드에서 함수가 호출되는 순간, 매개변수로 선언된 'ob'라는 객체가 생성되고, 이는 인자로 전달된 obj객체로 초기화되는 것이다.  

즉, 메모리 공간이 할당되는 것과 동시에 초기화되는 것이다.  

이렇듯 앞서 보인 기본 자료형(int)의 인자전달과 차이가 없다. 할당되는 대상이 변수에서 객체로 바뀌었을 뿐이다. 아래의 경우도 마찬가지다.  

```
SoSimple SimpleFuncObj(SoSimple ob)
{
	. . . .
    return ob;	// 반환하는 것과 동시에 메모리 공간이 할당되면서 초기화된다.
}
```

앞서 객체가 생성 및 초기화되는 세 가지 경우를 살펴보았다. 그렇다면 이 때 초기화는 어떻게 이루어질까?  

일단 상황적으로 판단하면, 초기화는 멤버 대 멤버가 복사되는 형태로 이루어질 것이다. 그래서 앞서 배운 Copy Constructor의 호출이 이루어질 것이다.  

또한, default Copy construtor은 멤버 대 멤버가 복사되도록 정의되니, 적절하게 초기화가 이루어질 것이다.  

그럼 아래의 예제를 실행해보자. 그리고 언제 Copy Constructor가 호출되는지 직접 확인해보고, 조금 더 정확하게 이해하도록 하자.  

```
#include <iostream>
using namespace std;

class SoSimple
{
private:
	int num;
public:
	SoSimple(int n) : num(n)
	{
		// empty
	}
	SoSimple(const SoSimple &copy) : num(copy.num)
	{
		cout << "Called Coopy constructor" << endl;
	}
	void ShowData()
	{
		cout << "num: "<< num << endl;
	}
};

void SimpleFuncObj(SoSimple ob)
{
	ob.ShowData();
}

int main()
{
	SoSimple obj(7);
	cout << "함수 호출 전" << endl;
	SimpleFuncObj(obj);
	cout << "함수 호출 후" << endl;
	return 0;
}
```

우선 실행결과를 살펴보면 아래와 같다.  

|실행결과|
|:----:|
|함수호출 전|
|Called Copy Constructor|
|num:7|
|함수호출 후|
  

이로 인해 멤버변수 num에 저장된 값이 복사되는 것일 확인할 수 있다.  

그렇다면 Copy Constructor의 호출에 직접적으로 관여하는 것이 'obj 객체의 Copy Constructor'인지, 'ob 객체의 Copy Constructor'인지에 대해서 혼란스러울 수 있다. 이 부분은 아래에 자세히 설명하도록 하겠다.  

먼저 초기화의 대상은 obj 객체가 아닌, ob 객체이다. 그리고 ob 객체는 obj 객체로 초기화된다. 따라서 ob 객체의 Copy Constructor가 호출되고, obj 객체가 인자로 전달되어야 하는 것이다.  

이것으로 Copy Constructor가 호출되는 두 번째 경우를 살펴보는 것을 마치겠다. 다음 예제를 통해 Copy Constructor가 호출되는 세 번째 경우를 살펴보자.  

```
#include <iostream>
using namespace std;

class SoSimple
{
private:
	int num;
public:
	SoSimple(int n) : num(n)
	{
		// empty
	}
	SoSimple(const SoSimple &copy) : num(copy.num)
	{
		cout << "Called Coopy constructor" << endl;
	}
	SoSimple &AddNum(int n)
	{
		num += n;
		return *this;	// 객체 자신의 주소 = 주소에 저장된 값
	}
	void ShowData()
	{
		cout << "num: "<< num << endl;
	}
};

SoSimple SimpleFuncObj(SoSimple ob)
{
	cout << "return 이전" << endl;
	return ob;
}

int main()
{
	SoSimple obj(7);
	SimpleFuncObj(obj).AddNum(30).ShowData();
	obj.ShowData();

	return 0;
}
```

마찬가지로 실행결과를 살펴보자.  

|실행결과|
|:----:|
|Called Copy Constructor|
|return 이전|
|Called Copy Constructor|
|num: 37|
|num: 7|
  

그리고 아래의 두 문장의 실행결과를 생각해보자.  

```
int main()
{
	Sosimple obj(7);
    SimpleFuncObj(obj);
    . . . . .
}
```

위의 경우의 첫 번째 줄이 의미하는 것은 객체 obj에 인자 7을 전달하고, 생성한다는 것이다.  

그리고 이어지는 두 번째 줄의 경우 obj를 인자로 SimpleFuncObj 함수를 호출하는 것이다. 함수가 호출되면 객체 obj가 전달하는 것과 동시에 아래의 함수에서 객체 ob가 생성된다.  

```
SoSimple SimpleFuncObj(SoSimple ob)
{
	cout << "return 이전" << endl;
	return ob;
}
```

객체 ob가 생성되고 함수를 실행한 후 객체 ob를 리턴하는 상황이 발생한다. 이 경우에는 '임시객체'에 ob가 전달되고, 임시객체의 Copy Constructor가 생성되는 것이다. 결국 이때 생성된 임시 객체가 최종적으로 반환되는 것이다.  

따라서 함수호출이 완료되고 나면, 지역적으로 선언된 객체 ob는 소멸되고, obj 객체와 임시객체만 남게된다. 그럼 아래의 코드를 보자.  

```
SimpeFuncObj(obj).AddNum(30).ShowData();
```

SimpleFuncObj 함수의 호출결과로 반환된 임시객체를 대상으로, 바로 이어서 AddNum 함수를 호출하는 부분이다.  

이 경우 AddNum 함수의 호출로 인해, 임시객체에 저장된 값이 30증가한다. 그리고 이어서 ShowData 함수호출을 통해 임시객체에 저장된 값을 출력한다.  

그리고 이때 출력된 값은, obj 객체를 대상으로 하는 출력과 다르다는 것을 우리는 실행결과를 통해 알고 있다. 당연한 결과일 수 있지만, 임시객체라는 개념을 새롭게 알 수 있었다.  

이 임시객체는 앞서 설명한 '임시변수'와 유사한 개념이라고 생각하면 된다. 그리고 이러한 임시객체는 우리가 임의로 만들 수도 있다. 아래의 예제를 통해 자세히 살펴보자.  

```
#include <iostream>
using namespace std;

class Temporary
{
private:
	int num;
public:
	Temporary(int n) : num(n)
	{
		cout << "creat obj:" << num << endl;
	}
	~Temporary()
	{
		cout << "destroy obj: " << num << endl;
	}
	void ShowTempInfo()
	{
		cout << "My num is " << num << endl;
	}
};

int main()
{
	Temporary(100);
	cout << "******* after make!" << endl << endl;

	Temporary(200).ShowTempInfo();
	cout << "******* after make!" << endl << endl;

	const Temporary &ref = Temporary(300);
	cout << "******* end of main!" << endl << endl;

	return 0;
}
```

실행해서 결과를 확인했는가? 그 결과를 확인하기에 앞서 아래의 문장에 대해 설명하려고 한다.  

```
Temporary(200).ShowTempInfo
```

클래스 외부에서 객체의 멤버변수를 호출하기 위해 필요한 것은 다음 세 가지 중 하나이다.  

* 객체에 붙여진 이름
* 객체의 참조 값(객체 참조에 사용되는 정보)
* 객체의 주소 값  

그런데 임시객체가 생성된 위치에는 임시객체의 참조 값이 반환되는 것을 알 수 있다. 즉, 위 문장의 경우 먼저 임시객체가 생성되면서 다음의 형태가 만들어지는 것이다.  

```
(임시객체의 참조 값).ShowTempInfo();
```

그래서, 이어서 멤버함수의 호출이 가능한 것이다. 또한 이렇듯 '참조 값'이 반환되기 때문에 다음의 문장 구성도 가능한 것이다.  

```
const Temporarry &ref = Temporary(300);
```

위의 경우는 임시객체 생성시 반환되는 '참조 값'이 참조자 ref에 전달되어, ref가 임시객체를 참조하게 된다.  

그리고 이 예제 전에 설명한 예제의 다음 문장 구성이 가능한 이유도, 실제로는 임시객체가 통째로 반환되어서가 아니라, 임시객체는 메모리에 저장되고, 그 객체의 참조 값이 반환되었기 때문이다.  

```
SimpeFuncObj(obj).AddNum(30);
```

즉, 반환을 위해서 임시객체가 생성은 되지만, 이 객체는 메모리 공간에 존재하고, 이 객체의 참조 값이 반환되어서 AddNum 함수의 호출이 진행된 것이다.  

이제 위 예제의 실행괄겨를 통해서 내릴 수 있는 결론에 대해 이야기해보자. 아래와 같은 결론이 나오지 않는가?  

* 임시객체는 다음 행으로 넘어가면 바로 소멸되어 버린다.
* 참조자에 참조되는 임시객체는 바로 소멸되지 않는다.
  

3+5의 연산에 사용되는 상수 3과 5처럼 임시객체에는 이름이 없기 때문에 다음 행으로 넘어가면 접근이 불가능해진다(당연한 것이다).  

따라서 접근이 불가능하게 된 임시객체는 소멸자가 바로 소멸시켜버린다.  

반면 'const Temporary &ref = Temporary(300);'에서는 임시객체를 생성하고 참조자로 이를 참조한다. 즉, 다음 행에서도 접근이 가능한 것이다(소멸자가 소멸시키지 않는 것이다).  

그럼 이제, 반환할 때 만들어지는 임시객체의 소멸시기를 확인하기 위한 예제에 대해 살펴보자.  

이 예제의 출력 결과는 다소 복잡하지만, 객체의 생성과 소멸을 확인하기에는 최적의 예제라고 생각된다.  

```
#include <iostream>
using namespace std;

class SoSimple
{
private:
	int num;
public:
	SoSimple(int n) : num(n)
	{
		cout << "New Object: " << this << endl;
	}
	SoSimple(const SoSimple &copy) : num(copy.num)
	{
		cout << "New Copy obj: " << this << endl;
	}
	~SoSimple()
	{
		cout << "Destroy obj: " << this << endl;
	}
};

SoSimple SimpleFuncObj(SoSimple ob)
{
	cout << "Parm ADR: " << &ob << endl;
	return ob;
}

int main()
{
	SoSimple obj(7);
	SimpleFuncObj(obj);

	cout << endl;
	SoSimple tempRef = SimpleFuncObj(obj);
	cout << "Return Obj " << &tempRef << endl;

	return 0;
}
```

결과에 대한 설명에 앞서 아래의 문장을 살펴보자.  

```
SoSimple tempRef = SimpleFuncObj(obj);
```

자세히 보지 않으면, tempRef라는 새로운 객체를 생성해서, 반환되는 객체를 가지고 대입연산을 진행하는 것처럼 보인다.  

그러나 아래에 설명할 출력결과에서는 추가로 객체를 생성하지 않고, 반환되는 임시객체에 tempRef라는 이름을 할당하고 있음을 보여준다(객체ㅔ의 생성 수를 하나 줄여서 효율성을 높이기 위함이다).  

아래의 설명을 끝으로, 자세한 설명은 생략하도록 하겠다. 그 이유는 직접 학습하는 것을 목표로 하고 있기 때문이다. 위 예제는 출력결과를 분석하는 데 의미가 있기 때문이다.  

|실행결과|
|----|
|New Object:	100		. . . . . obj 생성|
|New Copy Obj: 200	. . . . . 함수호출로 인한 매개변수 ob의 생성|
|parm ADR: 200		. . . . . 함수의 몸체를 실행하고, 이를 통해|
|New Copy Obj: 300	. . . . . 반환으로 인한 임시객체 생성|
|Destroy obj: 200	. . . . . 매개변수 ob의 소멸|
|Destroy obj: 300	. . . . . 반환으로 생성된 임시객체의 소멸|
||
||
|New Copy Obj: 200	. . . . . 함수호출로 인한 (새로운)매개변수 ob의 생성|
|parm ADR: 200		. . . . . 함수의 몸체를 실행하고, 이를 통해|
|New Copy Obj: 400	. . . . . 반환으로 인한 임시객체 생성|
|Destroy obj: 200	. . . . . 매개변수 ob의 소멸|
|Return Obj: 400	. . . . . 임시객체의 주소 값과 동일하다.|
|Destroy obj: 400	. . . . . tempRef가 참조하는 임시객체가 소멸|
|Destroy obj: 100	. . . . . obj 소멸|
