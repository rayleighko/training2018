## Deep Copy & Shallow Copy

#####

[뒤로가기](/c++/README.md)

이번에 다룰 내용은 Deep Copy(깊은 복사)와 Shallow Copy(얕은 복사)에 대해서이다. 이전에 다룬 Default Copy Constructor은 Shallow Copy에 해당한다.  

이러한 Shallow Copy는 문제점이 있다. 그 문제점은 멤버변수가 힙의 메모리 공간을 참조하는 경우에 발생한다.  

아래의 예제는 컴파일은 제대로 되지만, 실행하면 문제가 발생한다. 어떠한 문제가 발생하는지 확인하고, 원인을 유추해보도록 하자(디버그 모드를 이용하도록 하자).

---

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
	Person(char *name, int age)
	{
		int len = (int)strlen(name) + 1;
		this->name = new char[len];
		strcpy_s(this->name, len, name);
		this->age = age;
	}
	void ShowPersonInfo() const
	{
		cout << "이름: " << name << endl;
		cout << "나이: " << age << endl;
	}
	~Person()
	{
		delete[]name;
		cout << "called destructor" << endl;
	}
};

int main()
{
	Person man1("kim hyung sik", 12);
	Person man2 = man1;
	man1.ShowPersonInfo();
	man2.ShowPersonInfo();

	return 0;
}
```

먼저 실행결과를 살펴보자.  

|실행결과|
|------|
|이름: kim hyung sik|
|나이: 12|
|이름: kim hyung sik|
|나이: 12|
|called destructor|
  

여기서 이상한 점이 있다. 분명 생성한 객체는 2개인데 1번의 소멸만이 이루어진 것이다.  

왜 이런 결과를 보이는 것인지 생각해보자(컴파일러의 종류나 환경에 따라서 2번의 소멸이 이루어질 수도 있다. 여기서는 왜 저런 상황이 발생했는지에 대해 생각해보자).  

문제점을 찾았는가? 필자는 man2과 man1이 같은 객체를 가리킬 것이라고 생각했다. 그래서 하나가 소멸되면, 나머지 하나는 이정표를 잃어버려 죽게될 것이라고 생각했다.  

답을 보니 이러한 생각은 어느정도 비슷하게 접근한 것이었다.  

정확한 답은 default Copy Constructor의 경우에는 멤버의 단순 복사를 진행하기 때문에 복사의 결과로 하나의 문자열을 두 개의 객체가 동시에 참조하는 모양이다.  

이로 인해 객체의 소멸과정에서 문제가 발생하는 것이다.  

조금 풀어 말하면 Shallow Copy의 경우에는 2개의 객체를 생성했을 때, 객체들이 가리키는 값이 서로 별개의 데이터를 복사하는 것이 아니라, 하나의 데이터를 두 개의 객체가 가리킨다고 생각하면 된다.  

그래서 하나의 객체를 지워서 두 객체가 가리키던 하나의 데이터 또한 지우는 것이다. 따라서 이미 지워진 문자열을 대상으로 delete 연산을 하기 때문에 문제가 되는 것이다.  

이러한 문제의 해결 방법은 여러 가지가 있다. 그런데 여기서는 각 객체가 서로 다른 데이터를 가리키도록(참조하도록) Copy Constructor을 정의해 문제를 해결하려고 한다.  

이는 객체 별로 각각 문자열을 참조하기 때문에, 위에서 언급한 객체 소멸 과정에서의 문제는 발생하지 않는다.  

참고로 이러한 형태의 복사를 가리켜 'Deep Copy(깊은 복사)'라고 한다. 멤버뿐만 아니라, 포인터로 참조하는 대상까지 깊게 복사한다고 생각하면 되겠다.  

Deep Copy를 이용한 Copy Constructor은 단순히 Copy Constructor을 정의하면 끝난다. 아래와 같이 말이다.  

```
Person(Person &copy) : age(copy.age)
{
	name = new char[strlen(copy.name) + 1];
	strcpy_s(name, strlen(copy.name) + 1, copy.name);
}
```

이렇게 정의된 생성자가 하는 일은 다음 두 가지다.  

* 멤버변수 age의 멤버끼리 복사를 진행한다.
* 메모리 공간 할당 후 문자열을 복사하고, 할당된 메모리의 주소 값을 멤버 name에 저장한다.  

이렇듯 그다지 어렵지 않은 내용이다. 이번 시간에 배운 Shallow Copy와 Deep Copy는 default냐, 직접 정의하냐의 차이이고, Shallow Copy의 문제점은 얕게 복사하기 때문에 서로 같은 데이터를 가리키고, 이에 따라 소멸 시 다른(복사된) 객체의 소멸은 불가능하다는 것이다.
