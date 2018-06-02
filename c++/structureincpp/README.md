## Structure in C++ 

##### C++의 구조체에 대해 살펴보자.  

[뒤로가기](/c++/README.md)

앞으로 할 이야기는 구조체에 대한 이해를 바탕으로 한다. 만약 구조체에 대한 이해가 부족하다면 따로 학습할 것을 권장한다.  

---

들어가기에 앞서 C언어로 프로그램을 구현한다면, 구조체의 정의는 항상 뒤를 따르기 마련이다. 그렇다면 구조체가 주는 이점이 무엇이기에 이렇듯 중요한 위치를 차지하고 있는 것일까? 이에 대한 답은 다양하지만 다양한 답의 공통분모는 다음의 내용과 같다.  

> "연관 있는 데이터를 하나로 묶으면, 프로그램의 구현 및 관리가 용이하기 때문이다."
  

그리고 이러한 구조체를 한 마디로 정의한다면,  

> "연관 있는 데이터를 묶을 수 있는 문법적 장치"
  

이며, 데이터의 표현을 함에 있어 큰 도움을 준다.  

예를 들어 레이싱 게임의 캐릭터로 등장하는 '자동차'를 표현한다고 가정해보자. 아래와 같은 정보가 자동차에 들어가야한다.  

* 소유주
* 연료량
* 현재 속도
* 취득 점수
* 취득 아이템
  

또한, 게임 사용자가 게임을 종료하면(로그아웃 화면), 위의 정보는 데이터베이스(or file)에 함께 저장되어야 하며, 다시 게임을 시작하면(로그인 화면), 저장된 위의 정보는 모두 함께 복원되어야 한다. 따라서 이들 정보를 이용해서 다음과 같이 구조체를 정의하면 프로그래미이 한결 수월해진다.  

```
struct Car
{
	char gamerID[ID_LEN];	// 소유자 ID
    int fuelGauge;			// 연료량
    int curSpeed;			// 현재 속도
};
```

앞서 추출한 정보들 중 '취득 점수'와 '취득 아이템'을 제외한 나머지를 모두 포함하여 구조체로 정의하였다.  

그렇다면 Cpp에서의 구조체 변수의 선언을 살펴보자. C언어에서 구조체 변수를 선언하는 방법은 아래와 같다.  

```
struct Car basicCar;
struct Car simpleCar;
```

앞에 삽입된 키워드 struct는 이어서 선언되는 자료형이 구조체를 기반으로 정의된 자료형임을 나타낸다. 그리고 키워드 struct를 생략하려면 별도의 typedef 키워드를 이용한 선언이 필요하다.  

하지만 Cpp에서는 기본 자료형 변수의 선언방식이나 구조체를 기반으로 정의된 자료형의 변수 선언 방식에 차이가 없다.  

즉, Cpp에서는 별도의 typedef 선언없이도 다음과 같이 변수를 선언할 수 있다.  

```
Car basicCar;
Car simpleCar;
```

그럼 앞선 설명을 바탕으로 예제를 작성해보자.  

```
#include <iostream>
using namespace std;

#define ID_LEN 20		// ID 최대 길이
#define MAX_SPD 200		// 최대 속도
#define FUEL_STEP 2		// 연료 변화량
#define ACC_STEP 10		// 엑셀 대비 속도 변화량
#define BRK_STEP 10		// 브레이크 대비 속도 변화량

struct Car
{
	char gamerID[ID_LEN];	// 소유자 ID
	int fuelGauge;			// 연료량
	int curSpeed;			// 현재 속도
};

void ShowCarState(const Car &car)
{
	cout << "소유자ID: " << car.gamerID << endl;
	cout << "연료량: " << car.fuelGauge << "%" << endl;
	cout << "현재 속도: " << car.curSpeed << "km/s" << endl << endl;
}

void Accel(Car &car)
{
	if (car.fuelGauge <= 0)
		return;
	else
		car.fuelGauge -= FUEL_STEP;

	if (car.curSpeed + ACC_STEP >= MAX_SPD)
	{
		car.curSpeed = MAX_SPD;
		return;
	}

	car.curSpeed += ACC_STEP;
}

void Break(Car &car)
{
	if (car.curSpeed <= BRK_STEP)
	{
		car.curSpeed = 0;
		return;
	}

	car.curSpeed -= BRK_STEP;
}

int main()
{
	Car run99 = { "run99", 100, 0 };
	Accel(run99);
	Accel(run99);
	ShowCarState(run99);
	Break(run99);
	ShowCarState(run99);

	Car sped77 = { "sped77", 100, 0 };
	Accel(sped77);
	Break(sped77);
	ShowCarState(sped77);
	return 0;
}
```

위의 예제에 구성된 함수들은 구조체 Car에 종속적인 함수라고 말할 수 있다. 그럼에도 불구하고 전역함수의 형태를 띠기 때문에, 이 함수들이 구조체 Car에 종속적임을 나타내지 못하고 있는 상황이다.  

그래서 다른 영역에서 이 함수를 호출하는 실수를 범할 수 있다.  

그렇다면 이를 해결하기 위해서는 어떤 아이디어가 필요할까? 그것은 구조체 안에 함수를 삽입하는 것이다. 아래와 같은 형태로 말이다.  

```
struct Car
{
	char gamerID[ID_LEN];	// 소유자 ID
	int fuelGauge;			// 연료량
	int curSpeed;			// 현재 속도

	void ShowCarState()
	{
		cout << "소유자ID: " << gamerID << endl;
		cout << "연료량: " << fuelGauge << "%" << endl;
		cout << "현재 속도: " << curSpeed << "km/s" << endl << endl;
	}

	void Accel()
	{
		if (fuelGauge <= 0)
			return;
		else
			fuelGauge -= FUEL_STEP;

		if (curSpeed + ACC_STEP >= MAX_SPD)
		{
			curSpeed = MAX_SPD;
			return;
		}

		curSpeed += ACC_STEP;
	}

	void Break()
	{
		if (curSpeed <= 0)
		{
			curSpeed = 0;
			return;
		}

		curSpeed -= BRK_STEP;
	}
};
```

구조체 안에 삽입된 함수의 정의에 변화가 생겼다. 연산의 대상에 대한 정보가 불필요해 참조자와 그를 받아오는 정보가 사라진 것이다.  

그 이유는 함수가 구조체 내에 삽입되면서 구조체 내에 선언된 변수에 직접접근이 가능하기 때문이다. 또한, 모든 Car 구조체 변수가 하나의 함수를 공유하는 형태로 사용된다.  

다만, 논리적으로 각가의 변수가 자신의 함수를 별도로 지니는 것과 같은 효과 및 결과를 보이기 때문에 Cpp의 구조체 변수는 각각 함수를 가진다고 이해하는 것이 좋다.  

그렇다면 위의 구조체를 이용하여 예제를 바꿔보자.

```
#include <iostream>
using namespace std;

#define ID_LEN 20		// ID 최대 길이
#define MAX_SPD 200		// 최대 속도
#define FUEL_STEP 2		// 연료 변화량
#define ACC_STEP 10		// 엑셀 대비 속도 변화량
#define BRK_STEP 10		// 브레이크 대비 속도 변화량

struct Car
{
	char gamerID[ID_LEN];	// 소유자 ID
	int fuelGauge;			// 연료량
	int curSpeed;			// 현재 속도

	void ShowCarState()
	{
		cout << "소유자ID: " << gamerID << endl;
		cout << "연료량: " << fuelGauge << "%" << endl;
		cout << "현재 속도: " << curSpeed << "km/s" << endl << endl;
	}

	void Accel()
	{
		if (fuelGauge <= 0)
			return;
		else
			fuelGauge -= FUEL_STEP;

		if (curSpeed + ACC_STEP >= MAX_SPD)
		{
			curSpeed = MAX_SPD;
			return;
		}

		curSpeed += ACC_STEP;
	}

	void Break()
	{
		if (curSpeed <= BRK_STEP)
		{
			curSpeed = 0;
			return;
		}

		curSpeed -= BRK_STEP;
	}
};

int main()
{
	Car run99 = { "run99", 100, 0 };
	run99.Accel();
	run99.Accel();
	run99.ShowCarState();
	run99.Break();
	run99.ShowCarState();

	Car sped77 = { "sped77", 100, 0 };
	sped77.Accel();
	sped77.Break();
	sped77.ShowCarState();
	return 0;
}
```

이는 앞서 설명한 예제와 다를 것 없는 예제이다. 이로써 우리는 조금 더 Cpp의 영역에 들어오게 되었다.  

여기서 조금 더 추가해서 구조체 안에 enum 상수를 선언해 매크로 상수들을 하나로 묶어보도록 하자.  

```
Struct Car
{
	enum
    {
    	ID_LEN = 20,
        MAX_SPD = 200,
        FUEL_STEP = 2,
        ACC_STEP = 10,
        BRK_STEP = 10
    };

    char gamerID[ID_LEN];
    int fuelGauge;
    int curSpeed;

    void ShowCarState() { . . . . }
    void Accel() { . . . . }
    void Vreak() { . . . . }
};
```

enum에 대한 설명은 이미 알고 있을테니 자세히 하지 않겠다.  

이렇게 상수도 구조체에 포함시키는 것은 상황에 따라 다르지만 현재는 구조체 Car에게만 의미가 있는 상수들이기 때문에 더 명확하게 코드를 나타낼 수 있다.  

만약 이런 방식이 부담스럽다면 namespace를 활용해 상수가 사용되는 영역을 명시하는 것도 방법이 될 수 있다. 

그리고 이렇게 namespace를 사용하게 되면, 몇몇 구조체들 사이에서만 사용하는 상수들을 선언할 때 특히 도움이 되며, 위에서 보인 방법보다 가독성도 좋아지는 경향이 있다. 아래처럼 말이다.  

```
#include <iostream>
using namespace std;

namespace CAR_SONST
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

struct Car
{
	char gamerID[CAR_SONST::ID_LEN];	// 소유자 ID
	int fuelGauge;			// 연료량
	int curSpeed;			// 현재 속도

	void ShowCarState()
	{
		cout << "소유자ID: " << gamerID << endl;
		cout << "연료량: " << fuelGauge << "%" << endl;
		cout << "현재 속도: " << curSpeed << "km/s" << endl << endl;
	}

	void Accel()
	{
		if (fuelGauge <= 0)
			return;
		else
			fuelGauge -= CAR_SONST::FUEL_STEP;

		if (curSpeed + CAR_SONST::ACC_STEP >= CAR_SONST::MAX_SPD)
		{
			curSpeed = CAR_SONST::MAX_SPD;
			return;
		}

		curSpeed += CAR_SONST::ACC_STEP;
	}

	void Break()
	{
		if (curSpeed <= CAR_SONST::BRK_STEP)
		{
			curSpeed = 0;
			return;
		}

		curSpeed -= CAR_SONST::BRK_STEP;
	}
};

int main()
{
	Car run99 = { "run99", 100, 0 };
	run99.Accel();
	run99.Accel();
	run99.ShowCarState();
	run99.Break();
	run99.ShowCarState();

	Car sped77 = { "sped77", 100, 0 };
	sped77.Accel();
	sped77.Break();
	sped77.ShowCarState();
	return 0;
}
```

그런데 문제점이 생겼다. 구조체가 너무 커져버렸다는 것이다. 그래서 꼭 필요한 정보를 제외하고 함수들은 구조체 밖으로 빼려고 한다.  

꼭 필요한 정보는 아래와 같다.  

* 선언되어 있는 변수정보
* 정의되어 있는 함수정보
  

대부분 프로그램을 분석할 때 함수의 기능만 파악하지, 함수의 세부구현까지 신경을 쓰지는 않는다. 따라서 구조체를 보는 순간, 정의되어 있는 함수의 종류와 기능이 한눈에 들어오게끔 코드를 작성하는 것이 좋다.  

이제 함수를 밖으로 빼보자. 이때는 함수의 원혀언언을 구조체 안에 두고, 함수의 정의를 구조체 밖으로 빼내야한다. 다만, 빼낸 다음에 해당 함수가 어디에 정의되어 있는지에 대한 정보만 추가해주면 된다.  

아래의 예제를 통해 함수를 구조체 밖에로 빼보자.  

```
#include <iostream>
using namespace std;

namespace CAR_SONST
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

struct Car
{
	char gamerID[CAR_SONST::ID_LEN];	// 소유자 ID
	int fuelGauge;			// 연료량
	int curSpeed;			// 현재 속도

	void ShowCarState();	//상태 정보 출력
	void Accel();			//엑셀, 속도 증가 (ACC_STEP)
	void Break();			//브레이크 속도 감소 (BRK_STEP)
};

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
		fuelGauge -= CAR_SONST::FUEL_STEP;

	if (curSpeed + CAR_SONST::ACC_STEP >= CAR_SONST::MAX_SPD)
	{
		curSpeed = CAR_SONST::MAX_SPD;
		return;
	}

	curSpeed += CAR_SONST::ACC_STEP;
}

void Car::Break()
{
	if (curSpeed <= CAR_SONST::BRK_STEP)
	{
		curSpeed = 0;
		return;
	}

	curSpeed -= CAR_SONST::BRK_STEP;
}

int main()
{
	Car run99 = { "run99", 100, 0 };
	run99.Accel();
	run99.Accel();
	run99.ShowCarState();
	run99.Break();
	run99.ShowCarState();

	Car sped77 = { "sped77", 100, 0 };
	sped77.Accel();
	sped77.Break();
	sped77.ShowCarState();
	return 0;
}
```

앞에서 언급하지는 않았지만 사실 구조체 안에 함수가 정의되어 있으면, 인라인으로 처리하라는 의미를 갖게 된다.  

반면, 위의 예제와 같이 함수를 구조체 밖으로 빼면, 이러한 의미가 사라진다.  

따라서 인라인의 의미를 그대로 유지하려면 다음과 같이 키워드 inline을 사용해서 인라인 처리를 명시적으로 지시해야 한다.  

```
inline void Car::ShowCarState() { . . . . }
inline void Car::Accel() { . . . . }
inline void Car::break() { . . . . }
```

이로써 Cpp에서의 구조체에 대한 설명이 마무리되었다. 그런데 Cpp에서의 구조체는 다음에 설명하는 클래스의 일종으로 간주된다.  

그래서 구조체 안에 함수를 정의할 수 있었던 것이다. 그래서 위의 구조체를 '클레스'라고 표현해도 틀리지 않는다.
