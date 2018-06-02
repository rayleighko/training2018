## Class & Object 

##### 클래스와 객체를 살펴보자. 자바의 핵심이다.  

[뒤로가기](/c++/README.md)

앞에서 언급했던 것처럼 Cpp에서의 구조체는 클래스의 일종으로 간주된다. 그렇다면 이번 장에서는 클래스란 무엇이고, 객체에 대한 이야기를 할 것이다.  

---

먼저 클래스와 구조체의 차이점에 대해서 살펴보도록 하자. 우선은 키워드가 다르다. 구조체의 키워드는 struct였고, 이를 대신해서 클래스에서는 class 키워드를 사용한다.  

즉 아래의 코드가 클래스의 정의이다.  

```
class Car
{
	char gaimID[CAR_CONST::ID_LEN];
    int fuelGauge;
    int curSpeed;

    void ShowCarState() { . . . . }
    void Accel() { . . . . }
    void Break() { . . . . }
};
```

이는 구조체와 클래스를 구분하는 코드상에서의 유일한 차이점이다.  

물론 다른 차이점은 여럿 존재한다. 대표적으로 이렇게 선언된 클래스는 앞서 선언된 방식으로 변수를 선언하지 못한다.  

```
Car run99 = {"run99", 100, 0};	// 이 방식은 사용할 수 없다
```

그 이유는 클래스 내에서 선언된 함수가 아닌, 다른 영역(main())에서 변수를 초기화하려 했기 때문이다.  

클래스는 기본적으로(별도의 선언이 없으면) 클래스 내에 선언된 변수는 클래스 내에서 선언된 함수에서만 접근이 가능하다. 아래와 같은 형태로 말이다.  

```
Car run99;
```

그런데 이러한 방식은 지금까지의 방식과는 너무 다르다. 그래서 우리는 이렇게 선언해야하면 초기화를 다음과 같이 한다고 생각할 수 있다.  

```
int main()
{
	Car run99;
    strcpy_s(run99.gamerID, "run99");
    run99.fuelGauge = 100;
    run99.surSpeed = 0;
}
```

하지만 맨 처음 문장을 제외하고는 컴파일이 되지 않는다.  

그 이유는 클래스 내에 선언된 변수는 기본적으로 클래스 내에 선언된 함수에서만 접근이 가능하기 때문이라고 앞서 말했다.  

> "그럼 접근이 불가능한데 어떻게 써!"
  

물론 접근이 불가능하기만 하다면, 쓸모가 없을 것이다. 그러나 클래스는 멤버의 접근과 관련해 다음과 같이 이야기한다.  

> "접근과 관련해서 별도의 선언을 하지 않으면, 클래스 내에 선언된 변수 및 함수에 대한 접근은 허용하지 않을 테니, 접근과 관련된 지시를 별도로 내려줘"  

아직도 이해가 안된다면 이것을 조금 달리 이야기하면 정의하는 과정에서 각각의 변수 및 함수의 접근 허용범위를 별도로 선언해야 한다는 것이라고 생각하기 바란다.  

이제부터는 Access Modifier(접근제어자)에 대해 이야기해보자.  

사실 Access Modifier은 접근제어자, 접근제어 지시자, 엑세스 한정자 등등으로 해석되어진다. 그래서 여기서는 Access Modifier로 통일하겠다. Cpp에서의 Access Modifier는 아래와 같이 총 3가지 존재한다.  

* public		어디서든 접근 허용
* protected		상속관계에 놓여있을 때, 유도 클래스에서의 접근허용
* private		클래스 내(클래스 내에 정의된 함수)에서만 접근허용  

이 중에서 protected는 이후에 나올 '상속'에 대해 먼저 학습하고 살펴보도록 하고, 나머지는 아래의 예제를 보고 설명하겠다.  

```
#include <iostream>
#include <cstring>
using namespace std;

namespace CAR_CONST
{
	enum
	{
		ID_LEN = 20,
		MAX_SPD = 200,
		FUEL_STEP = 2,
		ACC_STEP = 10,
		BRK_STEP = 10
	};
}

class Car
{
private:
	char gamerID[CAR_CONST::ID_LEN];
	int fuelGauge;
	int curSpeed;
public:
	void InitMember(char *ID, int fuel);
	void ShowCarState();
	void Accel();
	void Break();
};

void Car::InitMember(char *ID, int fuel)
{
	strcpy_s(gamerID, ID);
	fuelGauge = fuel;
	curSpeed = 0;
}

void Car::ShowCarState()
{
	cout << "소유자ID: " << gamerID << endl;
	cout << "연료량: " << fuelGauge << "%" << endl;
	cout << "현재 속도: " << curSpeed << "km/s" << endl << endl;
}

void Car::Accel()
{
	if (fuelGauge <= 0)
		return;
	else
		fuelGauge -= CAR_CONST::FUEL_STEP;

	if ((curSpeed + CAR_CONST::ACC_STEP) >= CAR_CONST::MAX_SPD)
	{
		curSpeed = CAR_CONST::MAX_SPD;
		return;
	}
	curSpeed += CAR_CONST::ACC_STEP;
}

void Car::Break()
{
	if (curSpeed < CAR_CONST::BRK_STEP) 
	{
		curSpeed;
		return;	
	}
	curSpeed -= CAR_CONST::BRK_STEP;
}

int main()
{
	Car run99;
	run99.InitMember("run99", 100);

    run99.Accel();
	run99.Accel();
	run99.Accel();
	run99.ShowCarState();
	run99.Break();
	run99.ShowCarState();

	return 0;
}
```

위 예제와 지난 설명을 통해 우리는 아래와 같은 여러 사실을 알 수 있다.  

* Access Modifier인 A가 선언되면, 그 이후에 등장하는 변수나 함수는 A에 해당하는 범위 내에서 접근이 가능하다.
* 그러나 새로운 Access Modifier인 B가 선언되면, 그 이후에 등장하는 변수나 함수는 B에 해당하는 범위 내에서 접근이 가능하다.
* 함수의 정의를 클래스 밖으로 빼도, 이는 클래스의 일부(선언은 클래스 내부)이기 때문에, 함수 내에서는 private으로 선언된 변수에 접근이 가능하다.
* 키워드 struct를 이용해서 정의한 구조체에 선언된 변수와 함수에 별도의 Acccess Modifier를 선언하지 않으면, 모든 변수와 함수는 public으로 선언된다.
* 키워드 class를 이용해서 정의한 클래스에 선언된 변수와 함수에 별도의 Access Modifier를 선언하지 않으면, 모든 변수와 함수는 private으로 선언된다.
  

그리고 위에서 설명하는 struct와 class의 선언에 따른 차이가 구조체와 클래스의 유일한 차이점이다.  

즉, 구조체도 클래스도 접근제어 지시자의 선언이 가능하고, 그 의미도 동일하다.  

다만 default가 public이냐 private이냐의 차이일 뿐이다.  

> "왜 굳이 클래스 내에 존재하는 변수들을 private으로 선언해서 접근에 불편함을 주는 것일까? 그냥 다 public으로 선언하는 게 좋지 않나?"
  

이와 같은 질문에 대해서는 나중에 배울 'Information Hiding'에 대해 배우면 자연스럽게 이해하게 될테니 지금은 넘어가도록 하자.  

앞으로의 진도를 위해 용어를 한 번 정리하고자 한다.  

이제 구조체 변수나 클래스 변수라는 표현은 어울리지 않는다.  

왜냐하면 구조체와 클래스는 변수의 성격만 지니는 것이 아니기 때문이다.  

그래서 변수라는 표현을 대신해서 앞으로는 객체라고 표현하겠다.  

> *"그렇다면 객체는 무엇일까?"*
  

이 질문에 대해서는 다음 시간에 '객체지향 프로그래밍'에 관한 설명을 할 때 자세하게 하도록 할테니 지금은 넘어가도 괜찮다. 지금은 앞선 예제의 run99가 '변수'가 아닌 '객체'라는 것만 알아두자.  

그렇다면 클래스 내에 선언된 변수나 함수는 무엇이라고 부를까? 클래스를 구성하는 변수를 가리켜 '멤버변수'라고 부르고, 함수를 가리켜 '멤버함수'라고 한다. 즉, 예제의 멤버변수는 다음과 같다.  

* char GamerID[CAR_CONST::ID_LEN];
* int fuelGauge;
* int curSpeed;  

그리고 멤버함수는 다음과 같다.  

* void InitMembers(char* ID, int fuel);
* void ShowCarState();
* void Accel();
* void Break();  

이제 용어에 대한 정리는 끝났다.  

추가적으로 Cpp에서의 파일분할에 대한 이야기를 해보고자 한다.  

어느정도 규모가 있는 프로그램은 하나의 파일에 모든 것을 담지 않는다. 특히 Cpp은 클래스 별로 헤더파일과 소스 파일을 생성해 클래스의 선언과 정의를 분리하는 경우가 많기에 수 많은 파일이 만들어진다.  

이제부터 설명할 내용은 클래스를 대상으로 파일을 나누는 기준이다. 앞으로의 설명에서 아래의 내용을 알면 좋다(물론 이에 대해 다 알지 못해도 내용을 이해하는데 크게 무리는 없으니 설명을 보고 이해되지 않는 부분을 찾기 위한 목록이라고 생각하고 넘어가도록 하자).  

* 헤더파일의 역할
* C언어를 대상으로 헤더파일에 들어가야할 내용에 대한 이해
* 헤더파일의 중복포함을 막기 위해 사용되는 매크로 \#pragma once
* 둘 이상의 파일을 컴파일해서 하나의 실행파일을 만드는 방법
* 링커의 역할  

이제 본격적으로 Cpp의 파일분할에 대해 이야기해보자. 클래스 Car를 대상으로 파일을 나눌 때에는 보통 다음과 같이 파일을 구분한다.  

* Car.h		// 클래스의 선언
* Car.cpp	// 클래스의 정의(멤버함수의 정의)  

여기서 말하는 클래스의 선언은 다음과 같다.  

```
class Car
{
private:
	char gamerID[CAR_CONST::ID_LEN];
    int fuelGauge;
    int curSpeed;
public:
	void InitMembers(char *ID, int fuel);
    void ShowCarState();
    void Accel();
    void Break();
};
```

이는 컴파일러가 Car 클래스와 관련된 문장의 오류를 잡아내는데 필요한 최소한의 정보이다. 클래스를 구성하는 외형적인 틀이라고 생각하면 된다.  

그래서 이를 가리켜 '클래스의 선언(declaration)'이라 한다. 즉, 컴파일러는 위의 정보를 이용해 클래스 Car와 관련된 문장의 옳고 그름을 판단한다.  

반면, '클래스의 정의(definition)'에 해당하는 다음 함수의 정의는 다른 문장의 컴파일에 필요한 정보를 가지고 있지 않다.  

그래서 함수의 정의는 컴파일이 된 이후에, 링커에 의해 하나의 실행파일로 묶이기만 하면 되는 것이다.  

```
void InitMembers(char* ID, int fuel) { . . . . }
void ShowCarState() { . . . . }
void Accel() { . . . . }
void Break() { . . . . }
```

그럼 이제 우리는 다음과 같이 이해할 수 있을 것이다.  

>"Car클래스와 관련된 문장의 컴파일 정보로 사용되는 '클래스의 선언'은 헤더 파일에 저장해서, 필요한 위치에 쉽게 포함될 수 있도록 해야하고,'클래스의 정의'는 소스 파일에 저장해서, 컴파일이 되도록 하면 되는 구나!"
  

그럼 지금까지 설명한 내용을 기반으로 앞서 보인 예제를 총 3개의 파일로 나눠보자.  

```
//Car.h

#pragma once

namespace CAR_CONST
{
	enum
    {
    	ID_LEN = 20,
        MAX_SPD = 200,
        FUEL_STEP = 2,
        ACC_STEP = 10,
        BRK_STEP = 10
    };
}

class Car
{
	private:
    	char gamerID[CAR_CONST::ID_LEN];
        int fuelGauge;
        int curSpeed;
    public:
    	void InitMembers(char *ID, int fuel);
        void ShowCarState();
        void Accel();
        void Break();
};
```
  
```
//Car.cpp

#include <iostream>
#include <cstring>
#include "Car.h"
using namespace std;

void Car::InitMembers(char *ID, int fuel)
{
	strcpy_s(gamerID, ID);
    fuelGauge = fuel;
    curSpeed = 0;
}

void Car::ShowCarState()
{
	cout << "소유자ID: " << gamerID << endl;
	cout << "연료량: " << fuelGauge << "%" << endl;
	cout << "현재 속도: " << curSpeed << "km/s" << endl << endl;
}

void Car::Accel()
{
	if (fuelGauge <= 0)
		return;
	else
		fuelGauge -= CAR_CONST::FUEL_STEP;

	if ((curSpeed + CAR_CONST::ACC_STEP) >= CAR_CONST::MAX_SPD)
	{
		curSpeed = CAR_CONST::MAX_SPD;
		return;
	}
	curSpeed += CAR_CONST::ACC_STEP;
}

void Car::Break()
{
	if (curSpeed < CAR_CONST::BRK_STEP)
	{
		curSpeed;
		return;
	}
	curSpeed -= CAR_CONST::BRK_STEP;
}
```
  
```
//RacingMain.cpp

#include "Car.h"

int main()
{
	Car run99;
    run99.InitMembers("run99", 100);

	run99.Accel();
    run99.Accel();
    run99.Accel();
    run99.ShowCarState();
    run99.Break();
    run99.ShowCarState();

    return 0;
}
```

이렇게 파일을 분할하니 클래스 Car을 구성하는 멤버의 파악도 한결 수월해졌다.  

누군가는 파일의 분할이 익숙지 않아서 오히려 부담스럽게 느껴질 수도 있다. 그러나 조금만 익숙해지면, 하나의 파일에 모든 것을 집어넣는 것이 더 이상하게 느껴질 것이다.  

이후에 등장하는 예제들의 경우 성격에 따라 파일의 분할유무가 달라지니 익숙해지면 좋겠다.  

추가적으로 클래스의 인라인 함수에 대해 설명하겠다.  

예를 들어 앞선 예제에서 Car.cpp에 정의된 함수를 인라인화 한 다음에, 그대로 Car.cpp에 두면 컴파일 에러가 발생한다.  

그 이유는 다음과 같다.  

> "컴파일 과정에서 함수의 호출 문이 있는 곳에 함수의 몸체 부분이 삽입되어야 하기 때문이다."
  

예를 들어 아래와 같은 main 함수를 컴파일한다고 가정해보자.  

```
int main()
{
	Car run99;
    run99.InitMembers("run99", 100);

    run99.Accel();
    run99.Break();
	. . . .
}
```

이때 Break 함수가 인라인 함수가 아니라면, Break 함수가 Car 클래스의 멤버함수인지만 확인을 하고 컴파일은 완료된다.  

그러나 Break 함수가 인라인 함수라면, Break 함수의 호출문장은 컴파일러에 의해서 Break 함수의 몸체로 대체되어야 한다.  

때문에 인라인 함수는 클래스의 선언과 동일한 파일에 저장되어서 컴파일러가 동시에 참조할 수 있게 해야 한다. 아래와 같이 말이다.  

```
//CarInline.h

#pragma once

#include <iostream>
using namespace std;

namespace CAR_CONST { . . . . }

class Car
{
	private:
    	char gamerID[CAR_CONST::ID_LEN];
        int fuelGauge;
        int curSpeed;
    public:
    	void InitMembers(char *ID, int fuel);
        void ShowCarState();
        void Accel();
        void Break();
};

inline void Car::Break() { . . . . }	// cpp 파일에서의 정의는 지운다
```

앞서 보인 예제에서 함수를 인라인 선언한 것이 변경의 전부이다.  

그리고 컴파일러는 파일 단위로 컴파일을 진행하기 때문에 A.cpp와 B.cpp를 동시에 컴파일해서 하나의 실행파일을 만든다 해도, A.cpp의 컴파일 과정에서 B.cpp를 참조하지 않으며, 반대도 마찬가지다.  

그래서 위의 예제에서 보이듯이 클래스의 선언과 인라인 함수의 정의를 함께 묶어둔 것이다.  
