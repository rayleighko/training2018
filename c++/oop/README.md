## OOP(Object Oriented Programming)

##### 객체지향 프로그래밍에 대해 공부하고, 이를 활용하는 연습을 하자.  

[뒤로가기](/c++/README.md)

지금까지의 내용은 C언어에서 Cpp로 자연스럽게 이동할 수 있도록, 구조체를 시작으로 클래스를 설명했다.  

그런데 이번에는 객체지향의 관점에서 클래스를 전혀 다른 방법으로, 다시 한 번 설명하고자 한다.  

앞서 언급한 구조체를 확장한 것이 클래스라고 인식하는 것 자체는 문제가 되지 않으나, 그것이 전부라고 인식하는 것은 문제가 있기 때문에 재차 설명한다.  

---

Cpp은 객체지향 언어이다. 따라서 객체지향에 대한 이해가 필요하다.  

이것이 C와 같은 절차지향적 언어보다 모든 면에서 우월하지는 않지만, 절차지향적 특성이 갖지 못하는 많은 장점을 객체지향은 지니고 있다(물론 절차지향도 그 나름의 장점이 있다).  

객체는 영어로 Object이다. 그리고 이것의 사전적 의미 중 Cpp에서 말하는 Object는 다음과 같다.  

> "사물, 또는 대상"  

즉, Object는 우리 주변에 존재하는 물건(연필, 붓 등)이나 대상(철수, 영희 등) 전부를 의미한다.  
그렇다면 객체를 지향한다는 객체지향 프로그래밍이라는 것은 무엇일까? 여기서는 아래와 같은 상황을 예로 들겠다.  

> "나는 과일장수에게 두 개의 사과를 구매했다."  

이 문장에 삽입되어 있는 객체의 종류는 다음과 같다.  

> 나, 과일장수, 사과  

그렇다면 '나'라는 객체는 '과일장수'라는 객체로부터 '과일(사과)' 객체의 구매라는 액션을 취할 수 있어야 한다.  

그런데 객체지향 프로그래밍에서는 '나' 그리고 '과일장수'와 같은 객체를 등장시킬 수 있을 뿐만 아니라, '나'라는 객체가 '과일장수'라는 객체로부터 '과일(사과)' 객체를 구매하는 행위도 그대로 표현할 수 있다.  

> "즉, 객체지향 프로그래밍은 현실에 존재하는 사물과 대상, 그리고 그에 따른 행동을 있는 그대로 실체화 시키는 형태의 프로그래밍이다."  

이제 프로그램상에 과일장수 객체가 존재한다고 가정해 보자. 이 객체는 한 가정의 이버지일 수도, 조기 축구회에 다닐 수도 있다.  

그러나 프로그램상에서 바라보는 과일장수의 관점은 '과일의 판매'에 있다. 따라서 프로그램상의 과일장수는 다음과 같다.  

* 과일장수는 과일을 판다.
* 과일장수는 사과 20개, 오렌지 10개를 보유하고 있다.
* 과일장수의 과일판매 수익은 현재까지 50,000원이다.  

이 중에서 첫 번째는 과일장수의 '행동(behavior)'을 의미한다. 그리고 두 번째와 세 번째는 과일장수의 '상태(state)'를 의미한다.  

이처럼 **객체는 하나 이상의 상태 정보(data)와 하나 이상의 행동(function)으로 구성**되며, 상태 정보는 변수를 통해서 표현되고(변수에 상태 정보를 저장함), 행동은 함수를 통해서 표현될 수 있다.  

그럼 아래와 같이 표현해보자.  

* 보유하고 있는 사과의 수		-> int numOfApples;
* 판매 수익					-> int myMoney;  

```
int SaleApple(int money)	// 인자 = 구매액
{
	int num = meney/1000;	// 개당 1,000원으로 사과를 세어

    numOfApple -= num;		// num만큼의 사과를
    myMoney += money;		// 판매수익을 받고

	return num;				// 반환한다.
}
```

이제 이들을 묶어서 객체로 표현해보자. 물론 그 전에 객체의 생성을 위한 '틀'에 대해 설명하겠다.  

이는 흔히 비유되는 붕어빵의 틀과 같이 생각하면 좋다. 즉, 실제 틀이 있고, 그걸로 객체(붕어빵)를 찍어내는 느낌인 것이다.  

이런 개념처럼 '과일장수' 객체를 생성하기 위해 아래와 같은 틀을 만들어야한다. 또한 변수를 초기화하는데 사용할 함수와 현재 상태를 표현할 함수를 추가하겠다.  

```
class FruitSeller
{
private:
	int APPLE_PRICE;
    int numOfApples;
    int myMoney;
public:
	void InitMembers(int price, int num, int money)
    {
    	APPLE_PRICE = price;
        numOfApples = num;
        myMoney = money;
    }
	int SaleApples(int money)
    {
    	int num = money/APPLE_PRICE;
        numOfApples -= num;
        myMoney += money;

        return num;
    }
    void ShowSalesResult()
    {
    	cout << "남은 사과: " << numOfApples << endl;
        cout << "판매 수익: " << myMoney << endl;
    }
};
```

이제 뭔가 아다리가 맞는 느낌이다. 저번에 언급했던 클래스의 새로운 용도이니 말이다.  

이처럼 FruitSeller라는 이름의 클래스가 과일장수의 틀이 되는 것이다. 이 틀을 보면서 APPLE_PRICE가 대문자로 표현되어 있는 것을 보았을 것이다. 이는 상수로 표현하고 싶기 때문이다.  

그러나 클래스의 멤버변수 선언문에서 초기화하는 것을 허용하지 않는다.  

또한, 함수를 호출해서 상수를 초기화하는 것도 불가능하다.  

그 이유는 상수는 선언과 동시에 초기화디어야 하기 때문이다.  

이에 대한 것은 이후에 '생성자'에서 자세히 설명하도록 할테니 이번에는 아쉽지만 넘어가도록 하자.  

자, 지금까지는 '과일장수'를 표현하는 클래스를 정의했다. 그럼 '나'를 표현하는 클래스도 정의해보자. 이는 과일 구매자를 뜻하고, 아래와 같은 변수와 함수로 채워져야 할 것이다.  

* 소유하고 있는 현금의 액수		-> int mymoney;
* 소유하고 있는 사과의 수			-> int numOfApples;  

```
void BuyApples(FruitSeller &seller, int money)
{
	numOfApples += seller.SaleApples(money);
    myMoney -= money;
}
```

여기에 초기화와 내 상태를 확인하는 함수도 추가해서 아래와 같은 클래스를 만들어보자.  

```
class FruitBuyer
{
	int myMoney;			// private:
    int numOfApples = 0;	// private:
public:
	void InitMembers(int money)
    {
    	myMoney = money;
        numOfApples = 0;
    }
    void BuyApples(FruitSeller &seller, int money)
    {
    	numOfApples += seller.SaleApples(money);
        myMoney -= money;
    }
    void ShowBuyResult()
    {
    	cout << "현재 잔액: " << myMoney << endl;
        cout << "사과 개수: " << numOfApples << endl;
    }
};
```

위의 클래스의 특별한 점은 없다. 그러나 변수의 선언 부분에 private이 없다.  

이는 앞서 설명한 것처럼 class의 default Access Modifier는 private이라는 것을 상기시키면 이해할 수 있을 것이다(구조체였다면 public).  

우리는 지금 막 두 개의 클래스를 정의하였다. 그렇다면 객체를 생성하지 않고, 이 두 클래스 안에 존재하는 변수에 접근하고, 함수를 호출하는 것이 가능할까? 언뜻 가능할 것도 같다.  

그러나 이들은 실체(붕어빵)이 아닌 틀(붕어빵 틀)이다. 따라서 접근도 호출도 불가능하다는 것을 알아두자.  

그럼 이제 우리가 해야할 일은 앞서 정의한 클래스를 실체화시키는 것이다. 즉, 객체화시키는 것이다.  

다음은 Cpp에서 정의하고 있는 두 가지 객체 생성 방법이다.  

```
FruitSeller seller;
FruitBuyer buyer;
```

그리고 이를 동적으로 할당하려면 다음과 같이 생성하면 된다.  

```
FruitSeller* objptr1 = new FruitSeller;
FruitBuyer* objptr2 = new FruitBuyer;
```

이로써 기본적인 클래스의 정의방법과 객체의 생성방법, 그리고 클래스와 객체의 의미를 모두 설명했다.  

추가적으로 Message Passing이라는 객체지향의 함수호출 형태가 있다. 이는 마치 메세지를 전달하는 것처럼 함수를 호출하는 것이다.  

예를 들어 'BuyApples(seller, 2000)'라는 함수를 호출하면 "seller, 사과 2,000원어치 줘"라고 전달하는 것과 같이 말이다. 이는 하나의 독립된 클래스가 아닌 두 개의 클래스가 관계를 형성했다는 의미에서 중요하다.  
