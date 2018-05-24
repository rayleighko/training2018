## Advanced 'const'

##### 

[뒤로가기](/c++/README.md)

여기서 이야기할 'const' 키워드는 C에서의 const가 아니다. 바로 C++에서의 const에 대해 이야기할 것이다. 이미 앞서 이야기했지만, 앞선 내용에 보충한다는 느낌으로 생각하면 될 것이다.  

---

먼저 const 객체와 const 객체의 특성들에 대한 이야기를 시작할까 한다. 아래와 같이 변수를 상수화한 적이 있을 것이다.  

```
const int num = 10;
```

이와 같이 아래처럼 객체도 상수화할 수 있다.  

```
const SoSimple sim(20);
```

그리고 이렇게 const 선언이 붙은 객체는 해당 객체를 대상으로는 const로 선언된 멤버함수만 호출이 가능하다. 이는 객체의 const 선언이 아래와 같은 의미를 지니기 때문이다.  

> "이 객체의 데이터를 변경하지 마라!"
  

그렇기에 const 멤버함수의 호출만 허용할 수밖에 없는 것이다. 물론 const로 선언되지 않은 함수 중에도 데이터를 변경하지 않는 함수가 있을 수 있다.  

하지만 변경시킬 가능성이 있는 함수는 아예 호출을 허용하지 않는 것이다. 아래의 예제를 통해 const 객체의 특성을 다시 한 번 확인해보자.  

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
	SoSimple &AddNum(int n)
	{
		num += n;
		return *this;
	}
	void ShowData() const
	{
		cout << "num: " << num << endl;
	}
};

int main()
{
	const SoSimple sim(20);
	// sim.AddNum(30);
	sim.ShowData();

	return 0;
}
```

아마 위 함수를 작성하면서 느꼈을 것이다. 주석처리 한 'sim.AddNum(30);'의 경우에는 const 함수가 아니기 때문에 호출이 불가능하다(필자는 ShowData를 작성하다가도 const를 쓰지 않아 이를 찾는데 시간을 쓰기도 했다).  

이처럼 멤버변수에 저장된 값을 수정하지 않는 함수는 가급적 const로 선언해서, const 객체에서도 호출이 가능하도록 할 필요가 있다.  

추가적으로, const와 함수 오버로딩의 관계를 설명하겠다. 함수의 오버로딩이 성립하려면 매개변수의 수나 자료형이 달라야 한다. 하지만 아래와 같이 const의 존재 유무도 함수 오버로딩의 조건에 해당된다.  

```
void SimpleFunc() { . . . . }
void SimpleFunc() const { . . . . }
```

이러한 const 대상의 함수 오버로딩이 어떻게 활용되는지는 지금 설명하지 않겠다. 일단 사실만 기억하고 넘어가자. 아래의 예제를 보고, "아 이렇게 사용되는 구나"라고 생각하고 넘어가길 바란다.  

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
	SoSimple &AddNum(int n)
	{
		num += n;
		return *this;
	}
	void SimpleFunc()
	{
		cout << "SimpleFunc: " << num << endl;
	}
	void SimpleFunc() const
	{
		cout << "const SimpleFunc: " << num << endl;
	}
};

void YourFunc(const SoSimple &obj)
{
	obj.SimpleFunc();
}

int main()
{
	SoSimple obj1(3);
	const SoSimple obj2(10);

	obj1.SimpleFunc();
	obj2.SimpleFunc();

	YourFunc(obj1);
	YourFunc(obj2);

	return 0;
}
```
  
|실행결과|
|----|
|SimpleFunc: 3|
|const SimpleFunc: 10|
|const SimpleFunc: 3|
|const SimpleFunc: 10|  

이는 오버로딩 된 const 함수가 호출되는 시기를 보기위한 예제이다. 참고하기 바란다.  
