## Boolean  

bool은 C언어에는 존재하지 않고,(C99 이후에는 존재하지만 Cpp와는 다른 형태로 사용된다. <의미는 같으나 사용 방식이 차이가 있음) Cpp에만 존재하는 자료형이다.  

간략하게 설명했지만 아직도 몇몇 C컴파일러에서는 bool형태를 지원하지 않으니 bool은 Cpp의 자료형이라고 생각하면 된다. bool 자료형에 대한 설명 이전에 '참'과 '거짓'을 의미하는 true와 false를 이해해보자.  

---

C에서와 마찬가지로 '0'은 거짓을 의미하는 숫자이다. 그리고 '0'을 제외한 모든 정수는 '참'을 의미하는 숫자로 정의하고 있다. 따라서 기존의 C에서 참과 거짓을 나타내려면 아래와 같이 사전에 작업을 해줘야한다.  

```
#define TRUE	1
#define FALSE	0
```

이러한 참과 거짓의 표현방법은 Cpp에서도 여전히 사용된다. 그러나 Cpp에서는 사전에 키워드 true와 false를 정의하고 있기 때문에 굳이 상수선언을 이용할 필요가 없다. 다음의 예제처럼 키워드 true와 false를 사용할 수 있다.  

```
#include <iostream>
using namespace std;

int main()
{
	int num = 10;
    int i = 0;

    cout << "true: " << true << endl;
    cout << "false: " << false << endl;

    while(true)
    {
    	cout << i++ << ' ';
        if(i > num)
        {
        	break;
        }
        cout << endl;

        cout << "sizeof 1: " << sizeof(1) << endl;
        cout << "sizeof 0: " << sizeof(0) << endl;
        cout << "sizeof true: " << sizeof(true) << endl;
        cout << "sizeof false: " << sizeof(false) << endl;
        return 0;
    }
}
```

위 예제의 결과를 보면 알테지만 true와 false이 1과 0을 의미하는 것이 아니다. 이 둘은 참과 거짓을 표현하기 위한 1바이트 크기의 데이터일 뿐이다.  

다만, true와 false가 정의되기 이전에는 참을 표현하기 위해 숫자 1을, 거짓을 표혀하기 위해 숫자 0을 사용했기 때문에, 이 둘을 출력하거나 정수의 형태로 형 변환하는 경우에 각각 1과 0으로 변환되도록 정의되어 있을 뿐이다.  

그래서 위의 예제에서도 true와 flase를 출력하는 경우에 각각 1과 0이 출력되었으며, 다음과 같이 정수가 와야할 위치에 true와 ㄹalse가 오는 경우에도 1과 0으로 변환이 된다.  

```
int num1 = true;			// num1에는 1이 저장된다.
int num2 = false;			// num2에는 0이 저장된다.
int num3 = treu+false;	// num3에는 1+0이 저장된다.
```

따라서 true와 false를 굳이 숫자에 연결시켜서 이해하려 들지 않길 바란다. true와 ㄹalse는 그 자체를 '참'과 '거짓'을 나타내는 목적으로 정의된 데이터로 인식하는 것이 바람직하기 때문이다.  

true와 false는 그 자체로 참과 거짓을 의미하는 데이터이기 때문에 이들 데이터의 저장을 위한 자료형이 별도로 정의되어 있는 것이 당연할 것이다. true와 flase를 가리켜 bool형 데이터라고 한다. 그리고 bool은 int, double과 마찬가지로 기본자료형의 하나이기 때문에 다음과 같이 bool형 변수를 선언하는 것이 가능하다.  

> bool isTrue=true;
> bool isFalse=false;
  

또한 bool형은 함수의 반환형으로도 사용할 수 있고, 선언된 bool형 변수에 값을 저장할 수도 있다.  
