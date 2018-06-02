## Information Hiding

##### 정보 은닉에 대해 설명한다.  
  
[뒤로가기](/c++/README.md)
  
이번 시간에 다룰 내용은 Information Hiding, 즉 정보은닉에 대해서이다.  

우리는 객체의 생성을 목적으로 클래스를 디자인한다. 그렇다면 좋은 클래스가 되기 위한 조건으로는 어떤 것들이 있을까? 자바를 학습했다면 금세 답이 나올 것이다. 그것은 '정보은닉'과 '캡슐화'라는  것을 말이다.  

위에 언급한 두 가지는 좋은 클래스가 되기 위한 최소한의 조건이기 때문이니 말이다.  

---

얼마전에 사라진 윈도우의 그림판 프로그램을 실행하면 다양한 도형을 그릴 수 있다. 그런데 이와 유사한 성격의 프로그램을 Cpp을 이용해서 구현한다고 가정해보자.  

그럼 다양한 종류의 클래스를 정의해야 할 것이다. 특히 다음과 같이 점의 위좌표를 표현하는 목적의 클래스는 필수적이다.  

```
class Point
{
public:
    int x;	// 0이상 100이하
    int y;	// 0이상 100이하
};
```

이제 위의 클래스를 가지고 정보은닉에 대해 살펴보자.  

일단 위의 클래스에서 멤버변수 x와 y의 범위는 0이상 100이하라고 생각하자. 그렇다면 좌 상단 좌표는 당연히 [0, 0]이고, 우 하단은 [100, 100]일 것이다. 아래 예제는 Point 클래스의 멤버변수가 public으로 선언되었을 때 발생할 수 있는 문제점을 보이고 있다.  

```
#include <iostream>
using namespace std;

class Point
{
public:
	int x;	// 0이상 100이하
	int y;	// 0이상 100이하
};

class Rectangle
{
public:
	Point upLeft;		// 좌 상단
	Point lowRight;		// 우 하단
public:
	void ShowRecInfo()
	{
		cout << "좌 상단: " << '[' << upLeft.x << ", ";
		cout << upLeft.y << ']' << endl;
		cout << "우 하단: " << '[' << lowRight.x << ", ";
		cout << lowRight.y << ']' << endl;
	}
};

int main(void)
{
	Point pos1 = { -2, 4};
	Point pos2 = { 5, 9 };
	Rectangle rec = {pos2, pos1};
	rec.ShowRecInfo();
	return 0;
}
```

우선 31행의 문장이 조금 생소할 수도 있다. Point로 선언된 pos2와 pos1을 Rectangle 클래스 속에 있는 멤버변수인 upLeft와 lowRight에 초기화시키는 작업이다.  

그렇다. 특별히 달라지는 건 없다. 그럼 이제 아래 문장의 실행결과를 알 수 있을 것이다.  

```
Rectangle rec = {pos2, pos1};
```

위의 문장은 객체를 생성하고 초기화하는 문장이다. 즉, 미리 생성해 놓은 두 개의 Point 객체에 저장된 값이 Rectangle 객체의 멤버에 대입되는 것이다.  

이제 위의 예제에서 생소한 것은 없다.  

그럼 어떤 문제점이 있는지 생각해보자. 사실 컴파일이나 런타임에 오류가 있는 것은 아니다. 다만 논리적으로 문제가 되는 것이니 그 부분에 대해 생각해야 한다.  

* 점의 좌표는 0이상 100이하가 되어야 하는데, 그렇지 못한 Point 객체가 있다.
* 직사각형을 의미하는 Rectangle 객체의 좌 상단 좌표 값이 우 하단 좌표 값보다 크다.
  

어떤가 생각한 문제와 같은가? 매우 간단한 문제점이었기에 쉽게 생각했을 것이라 생각하고 문제점들에 대해 생각해보자.  

우선 점의 좌표 값은 0이상 100이하가 되어야 유효하다. 하지만 위의 예제는 이를 지키지 않았다. 이러한 문제는 대부분 프로그래머의 실수를 통해 발생되기 때문에 이에 대한 대책이 필요하다.  

물론 프로그래머도 인간이기에 실수를 할 수 있다. 그렇지만 실수에 대한 대책이 없었기 때문에 문제가 된 것이다.  그래서 우리는 문법적으로는 문제가 없는 위의 예제에서 아래와 같은 마음을 갖고 개발해야한다.  

> "제한된 방법으로의 접근만 허용해서 잘못된 값이 저장되지 않도록 도와야 하고, 실수를 했을 때, 실수가 쉽게 발견되도록 코드를 작성해야한다."
  

아래와 같이 말이다.  

```
//Point.h

#pragma once

class Point
{
private:
	int x;
	int y;
public:
	bool InitMembers(int xpos, int ypos);
    int GetX() const;
    int GetY() const;
    bool SetX(int xpos);
    bool SetY(int ypos);
};
```

이는 멤버변수 x와 y를 private으로 선언해서 임의로 값이 저장되는 것을 막아놓았다. 즉, x와 y라는 정보를 은닉한 상황이다.  

대신에 값의 저장 및 참조를 위한 함수를 추가로 정의하였다. 따라서 이 함수 내에서 멤버변수에 저장되는 값을 제한할 수 있게 되었다.  

그럼 이 함수들은 어떻게 정의되어 있을까?  

```
//Point.cpp

#include <iostream>
using namespace std;

bool Point::InitMembers(int xpos, int ypos)
{
	if(xpos < 0 || ypos < 0)
    {
    	cout << "벗어난 범위의 값 전달" << endl;
        return false;
    }

    x = xpos;
    y = ypos;
    return true;
}

int Point::GetX() const
{
	return x;
}

int Point::GetY() const
{
	return y;
}

bool Point::SetX(int xpos)
{
	if(0 > xpos || xpos > 100)
    {
    	cout << "벗어난 범위의 값 전달" << endl;
        return false;
    }

    x = xpos;

	return true;
}

bool Point::SetY(int ypos)
{
	if(0 > ypos || ypos > 100)
    {
    	cout << "벗어난 범위의 값 전달" << endl;
        return false;
    }

    y = ypos;

    return true;
}
```

멤버변수에 값을 저장하는 함수 InitMembers, SetX, SetY는 0이상 100이하의 값이 전달되지 않으면, 에러 메시지를 출력하면서 값의 저장을 허용하지 않는 형태로 정의되어 있다.  

따라서 잘못된 값이 저장되지 않을뿐더러, 값이 잘못 전달되는 경우 출력된 메시지를 통해서 문제가 있음을 확인할 수 있다.  

그럼 이제 아래와 같이 말할 수 있는 것이다.  

> "멤버변수를 private으로 선언하고, 해당 변수에 접근하는 함수를 별도로 정의해서, 안전한 형태로 멤버변수의 접근을 유도하는 것이 바로 '정보은닉'이다."
  

그리고 위의 코드를 보다보면 생소한 표현이 있다.  

```
int GetX() const;
bool SetX(int xpos);

int GetY() const;
bool SetY(int ypos);
```

이들을 가리켜 '엑세스 함수'라 하며, 이 함수는 멤버변수를 private으로 선언하면서, 클래스 외부에서의 멤버변수 접근을 목적을 정의되는 함수들이다.  

이후에 제시하는 완전한 예제를 통해서도 알 수 있겠지만, 이들 함수는 정의도었으되 호출되지 않는 경우도 많다.  

그렇다면 왜 정의하는 것일까? 그 이유는 클래스의 정의과정에서 지금 당장은 필요하지 않지만, 필요할 수 있다고 판단되는 함수들을 자주 호출되는 함수들과 함께 클래스에 포함시키기 때문이다.  

그 대표적인 예가 위에서 언급한 '엑세스 함수'이다. 그러니 이후에 호출되지 않지만 삽입되는 함수가 있다면, 이러한 맥락으로 이해하도록 하자.  

그럼 이어서 Rectangle 클래스를 살펴보자.  

```
//Rectangle.h

#pragma once

#include "Point.h"

class Rectangle
{
private:
	point upLeft;
    point lowRight;
public:
	bool InitMembers(const Point &ul, const Point &lr);
    void ShowRecInfo() const;
};
```

Rectangle 클래스도 멤버변수를 private으로 선언하고, 멤버의 초기화를 위한 별도의 함수를 추가하였다. 이 함수 내에서는 좌 상단과 우 하단의 좌표가 뒤바뀌는 것을 검사하는 내용을 추가했다. 아래와 같이 말이다.  

```
//Rectangle.cpp

#include <iostream>
#include "Rectangle.h"
using namespace std;

bool Rectangle::InitMembers(const Point &ul, const Point &lr)
{
	if(ul.GetX() > lr.GetX() || ul.GetY() > lr.GetY())
    {
    	cout << "잘못된 위치정보 전달" << endl;
        return false;
    }
    upLeft = ul;
    lowRight = lr;

    return true;
}

void Rectangle::ShowrecInfo() const
{
	cout << "좌 상단: "<< '[' << upleft.GetX() <<", ";
    cout << "upleft.GetY()" << ']' << endl;
	cout << "우 하단: "<< '[' << lowRight.GetX() <<", ";
    cout << "lowRight.GetY()" << ']' << endl;
}
```

오류상황에 대한 처리의 방법은 프로그램의 성격 및 내용에 따라 달라질 수 있으니, 함수를 통해서 멤버변수의 접근에 제한을 두었다는 사실에 주목하기 바란다.  

그리고 직사각형의 정보를 출력하는 함수에도 const 함수가 추가되었는데, 이와 관련해서는 아래의 예제인 main 함수를 보고 설명하도록 하겠다.  

```
#include <iostream>
#include "Point.h"
#include "rectangle.h"

int main(void)
{
	Point pos1;
    if(!pos1.InitMembers(-2, 4))

    	cout << "초기화 실패" << endl;	// false가 나와서 true로 바뀐 후 2줄의 메세지 출력
    if(!pos1.InitMembers(2, 4))
    	cout << "초기화 실패" << endl;	// 초기화 성공

	Point pos2;
    if(!pos2.InitMembers(5, 9))
    	cout << "초기화 실패" << endl;	// 초기화 성공

    Rectangle rec;
    if(!rec.InitMembers(pos2, pos1))
    	cout << "직사각형 초기화 실패" << endl;	// false가 나와서 true로 바뀐 후 2줄의 메세지 출력

    if(!rec.InitMembers(pos1, pos2))
    	cout << "직사각형 초기화 실패" << endl;	// 초기화 성공

    rec.ShowRecInfo();
    return 0;
}
```

그럼 아까 설명못한 const 함수에 대해 알아보자.  

```
int GetX() const;
int GetY() const;
void ShowRecInfo() const;
```

이 const들이 의미하는 것은 아래와 같다.  

> "이 함수 내에서는 멤버변수에 저장된 값을 변경하지마!"
  

매개변수도 아니고, 지역변수도 아닌, 멤버변수에 저장된 값을 변경하지 않겠다는 선언인 것이다.  

따라서 우리가 아는 것처럼 const 선언이 추가된 멤버변수 내에서 멤버변수의 값을 변경하는 코드가 삽입되면, 컴파일 에러가 발생한다.  

이러한 const 함수의 사용은 실수로 자신이 의도한 것과는 다르게 멤버변수의 값을 변경했을 때, 컴파일 에러를 통해서 이를 확인할 수 있는 것이다.  

그런데 이러한 const 함수에는 또 다른 특징이 있다. 이는 다음 코드를 통해서 살펴보자.  

```
class SimpleClass
{
private:
	int num;

public:
	void Initnum(int n)
    {
    	num = n;
    }
    int GetNum()
    {
    	return num;
    }
    void ShowNum() const
    {
    	cout << getNum() << endl;	// 컴파일 에러 발생
    }
}
```

위의 클래스 정의에서 ShowNum 함수는 const 함수로 선언되었다. 그리고 실제로 함수 내에서는 멤버변수인 num의 값을 변경하지 않았다.  

그런데도 불구하고 GetNum 함수를 호출하는 문장에서 컴파일 에러가 발생한다. 그 이유는 다음과 같다.  

> "const 함수 내에서는 const가 아닌 함수의 호출이 제한된다."
  

const로 선언되지 않은 함수는 아무리 멤버변수에 저장된 값을 변경하지 않더라도, 변경할 수 있는 가능성을 지닌 함수이다.  

따라서 이러한 변경이 가능한 함수의 호출을 사전에 허용하지 않는 것이다. 이와 유사한 것이 const 참조자이다. 이는 아래 예제를 통해 살펴보자.  

```
class EasyClass
{
private:
    int num;
public:
	void Initnum(int n)
    {
    	num = n;
    }
    int GetNum()
    {
    	return num;
    }
};

class LiveClass
{
private:
    int num;
public:
	void InitNum(const EasyClass &easy)
    {
    	num = easy.GetNum();	// 컴파일 에러 발생
    }
};
```

위의 클래스 정의에서 initNum 함수의 매개변수 easy는 const 참조자이다. 그런데 이를 대상으로 GetNum 함수를 호출하면 컴파일 에러가 발생한다.  

이는 앞서 이야기한 것처럼 GetNum이 const 함수가 아니기 때문이다.  

Cpp에서는 const 참조자를 대상으로 실제 값의 변경여부에 상관없이 값의 변경 능력을 가진 함수의 호출을 허용하지 않는다. 따라서 const 참조자를 이용해서는 const 함수만 호출이 가능한 것이다.  

이는 다소 번거로운 작업이지만 이는 분명 코드의 안정성을 높이는 좋은 방법이 될 수 있다.  
