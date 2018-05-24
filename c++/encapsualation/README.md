## Encapsulation(캡슐화) 

##### 

[뒤로가기](/c++/README.md)

흔히 우리는 좋은 클래스를 만들기 위해 두 가지를 이야기한다. 그것은 바로 Information Hiding(정보은닉)과 Incapsulation(캡슐화)이다.  

사실 좋은 클래스보다는 클래스의 가장 기본적이고, 중요한 원칙이라고 할 수 있다.  

캡슐화라고 하면 조금 생소하겠지만 캡슐을 만드는 과정, 즉 여러 알맹이들을 하나의 캡슐에 담는 것(숨기는 것)이라고 생각하면 이해하기 쉽다. 이번에는 그 캡슐화에 대해 다뤄보겠다.

---

사실 많은 이들이 캡슐화와 정보은닉의 차이를 이해하지 못하고 있다. 예를 들어 하나의 기능을 하는 캡슐에 A, B, C의 기능이 있다고 치자. 이는 캡슐화가 되어있는 것이다.  

그러나 만약 이러한 캡슐이 하나의 캡슐이 아닌 A를 위한 캡슐, B를 위한 캡슐, C를 위한 캡슐로 나누어져있다면 이는 캡슐화가 이루어져있지 않은 것이다.  

즉, 하나의 목적을 위해 여러 기능이 모여서 하나의 목적을 달성하는 것이 캡슐화의 본질이다.  

아래의 코드를 보고 자세하게 이해해보자.  

```
#include <iostream>
using namespace std;

class SinivelCap	// 콧물 처치용 캡슐
{
public:
	void Take() const { cout << "콧물 처치" << endl; }
};

class SneezeCap	// 재채기 처치용 캡슐
{
public:
	void Take() const { cout << "재채기 처치" << endl; }
};

class SnuffleCap	// 코막힘 처치용 캡슐
{
public:
	void Take() const { cout << "코막힘 처치" << endl; }
};

class ColdPatient
{
public:
	void TakeSinivelCap(const SinivelCap &cap) const { cap.Take();}
	void TakeSneezeCap(const SneezeCap &cap) const { cap.Take();}
	void TakeSnuffleCap(const SnuffleCap &cap) const { cap.Take();}
};

int main()
{
	SinivelCap scap;
	SneezeCap zcap;
	SnuffleCap ncap;

	ColdPatient sufferer;
	sufferer.TakeSinivelCap(scap);
	sufferer.TakeSneezeCap(zcap);
	sufferer.TakeSnuffleCap(ncap);

	return 0;
}
```

위 예제를 보고 아래와 같은 생각을 할 수도 있다.  

> "상황에 따라 콧물없이 재채기랑 코막힘이 있을 경우에는 이것도 괜찮은 거 아닌가?"  

라고 말이다. 반대로,  

> "코감기는 항상 콧물, 재채기, 코막힘을 동반한다"  

라는 가정을 하게 되면 캡슐화가 무너져버리게 된다.  

그러나 문제는 이것만이 아니다. 절차가 너무 복잡하다는 것도 있다. 3번의 복용과정말이다. 이를 하나의 캡슐로 만들어 놓았다면, 과정이 간소화되는 것이다.  

그리고 아직 더 큰 문제가 남아있다.  

만약 아래와 같이 가정한다면,  

> "약의 복용은 반드시 SinivelCap, SneezeCap, SnuffleCap의 순서로 복용해야한다"  

각 클래스들의 상호관계도 잘 알아야하는 상황이다. 만약 상호관계를 알지 못하면 순서가 틀어질 수 있기 때문이다.  

이처럼 캡슐화가 무너지면 객체의 활용이 매우 어렵고, 복잡해질 수 있다.  

그렇다면 이를 해결하기 위해 어떤 식으로 캡슐화를 해야할까? 아래의 에제를 살펴보자.  

```
#include <iostream>
using namespace std;

class SinivelCap
{
public:
	void Take() const { cout << "콧물 퇴치" << endl; }
};

class SneezeCap
{
public:
	void Take() const { cout << "재채기 퇴치" << endl; }
};

class SnuffleCap
{
public:
	void Take() const { cout << "코막힘 퇴치" << endl; }
};

class MSTCAP
{
private:
	SinivelCap sin;
	SneezeCap sne;
	SnuffleCap snu;
public:
	void Take() const
	{
		sin.Take();
		sne.Take();
		snu.Take();
	}
};

class ColdPatient
{
public:
	void TakeMSTCAP(const MSTCAP &cap) const { cap.Take(); }
};

int main() {
	MSTCAP cap;
	ColdPatient sufferer;
	sufferer.TakeMSTCAP(cap);
	return 0;
}
```

이로써 캡슐화를 어떻게 하는 것이 좋은 예인지에 대해 알아보았다.  

참고로, 캡슐화를 한다고 해서 하나의 클래스로만 모든 것을 구성해야 하는 것은 아니니 알아두도록 하자.  

예를 들어 MSTCAP 클래스가 SinivelCap, SneezeCap, SnuffleCap 객체를 멤버로 둔 것처럼 말이다. 중요한 것은 어떻게 구성하느냐 보다는 어떤 내용으로 구성했는가이다.  

사실 위의 예제는 간단하고, 이미 짜여진 코드를 보는 것이라 캡슐화가 그리 어렵지않게 느껴질 수 있다.  

그러나 캡슐화는 어려운 개념이다. 그 이유는 범위를 정하기 쉽지 않기 때문이다.  

사실 제대로 감기를 퇴치하기 위해서는 위의 예제에 있는 클래스와 함께 기침, 몸살, 고열 등을 위한 클래스도 넣어야한다. 그렇기 때문에 캡슐화는 복잡하고, 어려운 개념일 수밖에 없다.  

덧붙여 경험 많은 객체지향 프로그래머를 구분하는 첫 번째 기준은 캡슐화이다. 캡슐화는 일관되게 적용할 수 있는 단순한 개념이 아니고, 구현하는 프로그램의 성격과 특성에 따라 적용하는 범위가 달라지는 개념이기 때문이다.  

이처럼 캡슐화는 정답이 딱히 없는 것이다. 그래서 상대적으로 정보은닉은 쉽고, 캡슐화는 어렵다고 할 수 있다.  

캡슐화의 첫 번째 우선조건은 '항상'이다. 만약 위의 예제의 가정을 아래와 같이 한다면,  

> "감기는 코감기, 목감기, 몸살감기가 항상 동반한다"  

위의 예제 또한 제대로 캡슐화되지 못한 것이라고 할 수 있다.  

그렇기에 캡슐화를 위해서는 보다 구체적인 정보와 가정이 필요하다. 그래서 클래스를 캡슐화시키는 능력은 경험이 중요한 것이다.  

내용을 보충하면,

> "캡슐화에는 정보은닉이 기본적으로 포함된다."   

그렇다. 캡슐화에는 정보은닉이 기본적으로 포함된다. 그 이유는 이왕 캡슐화하는 거 정보은닉을 포함하는 것이 좋기 때문이다.  

그래서 캡슐화는 기본적으로 캡슐화를 포함한다고 이야기할 수 있다. 그러나 여기서는 둘의 구분을 확실하게 할 수 있는 것으로 만족하자.  
