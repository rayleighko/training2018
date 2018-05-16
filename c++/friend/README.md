## Friend

A라는 클래스와 B라는 클래스가 있다고 가정해보자. 이 상황에서 A는 B에게 다음과 같이 말한다.  

> "야, B 클래스! 넌 이제부터 내 친구야!"  

그리고 그 다음부터 A 클래스는 B 클래스에게 자신의 속마음을 다 내보인다. 그런데 아직 B 클래스는 A 클래스를 친구라고 생각하지 않고 있다. 따라서 B 클래스는 A 클래스에게 자신의 속마음을 다 내보이지 않는다.  

시간이 지나서 B클래스도 A 클래스의 선언에 진실함이 묻어 있음을 알고선 아래와 같이 외친다.  

> "그래 A 클래스! 넌 정말 나의 친구구나!"  

그리고는 그 다음부터 B 클래스 역시 A 클래스에게 자신의 속마음을 다 내보인다. 결국 둘은 자신의 private한 부분까지도 내보이는 사이가 되었다.   

---

지금 이야기한 내용에 C++의 friend 선언이 의미하는 것이 모두 담겨있다. 아래와 같이 정리할 수 있다.  

* A 클래스가 B 클래스를 대상으로 friend 선언을 하면, B 클래스는 A 클래스의 private 멤버에 직접 접근이 가능하다.
* 단, A 클래스도 B 클래스의 private 멤버에 직접 접근이 가능하려면, B 클래스가 A 클래스를 대상으로 friend 선언을 해줘야 한다.  

이렇듯 friend 선언은 private 멤버의 접근을 허용하는 선언이다. 아래와 같이 사용된다.  

```
class Boy
{
private:
	int height;
	friend class Girl;	// Girl 클래스를 friend로 선언했다
public:
	Boy(int len) : height(len)
	{
		// empty
	}
    . . . . .
};
```

위의 Boy 클래스는 Girl 클래스를 friend 선언하였다. 따라서 Girl 클래스 내에서는 Boy 클래스의 모든 private 멤버에 직접 접근이 가능하다.  

참고로 friend 선언은 클래스 내에 어디든 위치할 수 있다. private 영역에 존재하든, public 영역에 존재하든 상관없이 말이다. 아래의 경우 위에서 작성한 Boy 클래스의 private 변수를 사용하는 예제이다.  

```
class Girl
{
private:
	char phNum[20];
public:
	Girl(char *num)
	{
		strcpy_s(phNum, 20, num);
	}
	void ShowYourFriendInfo(Boy &frn)
	{
		cout << "His height: " << frn.height << endl;	// pivate에 접근
	}
};
```

위는 ShowYoutFriendInfo 함수 내에서 Boy 클래스의 private 멤버인 height에 직접 접근을 하고 있다.  

Girl 클래스는 Boy 클래스의 friend이므로, Girl 클래스 내에 선언된 모든 멤버함수는 이렇듯 Boy 클래스의 private 멤버에 접근이 가능하다.  

그럼 이번에는 위의 두 클래스를 기반으로 서로를 friend 선언하는 예제를 작성해보자.  

```
#include <iostream>
#include <cstring>
using namespace std;

class Girl;

class Boy
{
private:
	int height;
	friend class Girl;	// Girl 클래스를 friend로 선언했다
public:
	Boy(int len) : height(len)
	{
		// empty
	}
	void ShowYourFriendInfo(Girl &frn);
};

class Girl
{
private:
	char phNum[20];
public:
	Girl(char *num)
	{
		strcpy_s(phNum, 20, num);
	}
	void ShowYourFriendInfo(Boy &frn);
	friend class Boy;
};

void Boy::ShowYourFriendInfo(Girl &frn)
{
	cout << "Her phone Number: " << frn.phNum << endl;
}
void Girl::ShowYourFriendInfo(Boy &frn)
{
	cout << "His height: " << frn.height << endl;
}

int main()
{
	Boy boy(180);
	Girl girl("010-1234-5678");

	boy.ShowYourFriendInfo(girl);
	girl.ShowYourFriendInfo(boy);

	return 0;
}
```

friend 선언의 방법과 그 의미를 충분히 파악했을 것이라 생각된다.  

위 예제의 'class Girl;' 선언이 없어도 컴파일은 된다. 아래의 문장이 Girl이 클래스의 이름이라는 것을 알리기 때문이다.  

```
friend class Girl;
```

즉, 위의 문장은 다음 두 가지를 동시에 선언하는 문장이다.  

* Girl은 클래스의 이름이다.
* Girl 클래스를 friend로 선언한다.  

그러나 'class Girl;'을 굳 선언한 이유는 조금 코드의 명확성이 부족한 것 같아 추가하였다. 참고바란다.  

그렇다면 이러한 friend 선언은 언제 사용해야 하는 것일까? friend 선언은 앞선 글들에서 언급한 객체지향의 대명사인 'Information Hiding'을 무너뜨리는 문법이기 때문이다.  

그럼 아래와 같이 의아해할 수도 있다.  

> "그럼 왜 존재하는 거지? 사용하면 안되는 거 아닐까?"
  
그래서 이에 대한 전문가들의 의견은 분분하다. 이 글에서 "사용하지 마세요!"나 "꼭 사용하세요!"라는 말을 할 수 없는 이유이기도 하다.  

그래서 여기서는 알와 같이 이야기하고 넘어가려고 한다.  

> "friend 선언은 지나치면 아주 위험할 수 있으니, 필요한 상황에서 극히 소극적으로 사용하자."  

가령 얽히고 설킨 클래스의 관계를 풀기 위해 friend 선언을 남용했다가는 더 큰 문제를 야기할 수 있다.  

실력이 없을 때 이를 사용하는 것은 학습에도 악영향을 줄 수 있다. 그러니 가급적 사용하지 않는 방향으로 학습하도록 하자.  

> 물론 friend 선언이 편의를 주기 위해 '정보은닉'을 깨는 단점이 있어 아예 사용하지 않으려 할 수도 있다.  
>
> 그러나 '연산자 오버로딩'에서는 좋은 방법으로 사용되니, 이후를 기다리자.
  

추가적으로 전역함수를 대상으로도, 클래스의 멤버함수를 대상으로도 friend가 가능하다는 사실을 알고 넘어가도록 하자.  

물론 friend로 선언된 함수는 자신이 선언된 클래스의 private 영역에 접근이 가능하다. 아래의 예제를 통해 함수를 대상으로 하는 friend 선언방법을 살펴보자.  

```
#include <iostream>
using namespace std;

class Point;

class PointOP
{
private:
	int opcnt;
public:
	PointOP() : opcnt(0)
	{
		// empty
	}

	Point PointAdd(const Point&, const Point&);
	Point PointSub(const Point&, const Point&);
	~PointOP()
	{
		cout << "Operation Times: " << opcnt << endl;
	}
};

class Point
{
private:
	int x;
	int y;
public:
	Point(const int &xpos, const int &ypos) : x(xpos), y(ypos)
	{
		// empty
	}
	friend Point PointOP::PointAdd(const Point&, const Point&);
	friend Point PointOP::PointSub(const Point&, const Point&);
	friend void ShowPointPos(const Point&);
};

Point PointOP::PointAdd(const Point &pnt1, const Point &pnt2)
{
	opcnt++;
	return Point(pnt1.x + pnt2.x, pnt1.y + pnt2.y);
}

Point PointOP::PointSub(const Point &pnt1, const Point &pnt2)
{
	opcnt++;
	return Point(pnt1.x - pnt2.x, pnt1.y - pnt2.y);
}

int main()
{
	Point pos1(1, 2);
	Point pos2(2, 4);
	PointOP op;

	ShowPointPos(op.PointAdd(pos1, pos2));
	ShowPointPos(op.PointSub(pos2, pos1));

	return 0;
}

void ShowPointPos(const Point &pos)
{
	cout << "x: " << pos.x << ", ";
	cout << "y: " << pos.y << endl;
}
```

위 예제를 통해서 전역함수와 멤버함수에 대한 friend 선언방법을 이해하기 바란다. 참고로 하나만 더 이야기하면, 위 예제에서 보인 다음 friend 선언에는,

```
friend void showPointPos(const Point&);
```

friend 선언 이외에, 다음의 함수원형 선언이 포함되어 있다.  

```
void showPointPos(const Point&);
```

따라서 friend 선언을 위해서 별도의 함수원형을 선언할 필요는 없는 것이다.  
