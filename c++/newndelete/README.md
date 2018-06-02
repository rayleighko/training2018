## new & delete  

##### Malloc과 Free를 대신하는 New와 Delete.  

[뒤로가기](/c++/README.md)

우리는 '힙'영역의 특성과 힙의 메모리 할당 및 소멸에 필요한 함수가 malloc과 free라는 것을 이해하고 있을 것이다. 이를 바탕으로 이번에는 Cpp의 동적할당에 대해 살펴보자.  

---

혹시 잊어버렸을 수 있으니 아래의 예제를 통해 간단히 malloc과 free의 사용 형식을 살펴보자.  

```
#include <iostream>
#include <string.h>
#include <stdlib.h>
using namespace std;

char* MakeStrAdr(int len)
{
	char *str = (char*)malloc(sizeof(char)*len);
    return str;
}

int main()
{

	char *str = MakeStrAdr(20);
    // strcpy(str, "I am so Happy~!");의 형태는 VS13 이전의 형식
	strcpy_s(str, 16, "I am so Happy~!");
    cout << str << endl;

    free(str);

    return 0;
}
```

이제 어느정도 기억이 돌아온 것 같다. 그렇다면 이러한 방법이 갖는 두 가지 불편사항도 생각났을 것이다.  

> * 할당할 대상의 정보를 무조건 바이트 크기단위로 전달해야한다.
> (char\* str = (char\*)malloc(**sizeof(char)\*len**);)
  

> * 반환형이 void형 포인터이기 때문에 적절한 형 변환을 거쳐야 한다.
> (char\* str = **(char\*)malloc**(sizeof(char)\*len);)
  

이러한 불편사항을 설명하는 이유는 Cpp에서 제공하는 키워드인 'new & delete'를 사용하면 사라진다는 것을 알리기 위함이다.  

new는 malloc 대신, delete는 free 대신 사용하는 키워드이다. 먼저 new의 사용방법은 다음과 같다.  

> * int형 변수의 할당	-> int\* ptr = new int;
> * double형 변수의 할당 -> double\* ptr2 = new double;
> * 길이가 3인 int형 배열의 할당 -> int\* arr1 = new int[3];
> * 길이가 7인 double형 배열의 할당 -> double\* arr2 = new double[7];   

위 문장은 쉽게 이해할 수 있을 것이다. 특히 할당할 대상의 정부를 직접 명시하고 있음을 주목해야한다.  

그렇다면 delete의 사용방법을 보자.

> * 앞서 할당한 int형 변수의 소멸 -> delete ptr1;
> * 앞서 할당한 double형 변수의 소멸 -> delete ptr2;
> * 앞서 할당한 int형 배열의 소멸 -> delete []arr1;
> * 앞서 할당한 double형 배열의 소멸 -> delete []arr2;
  

이는 new연산 시 반환된 주소 값을 대상으로 delete연산을 진행하되, 할당된 영역이 배열의 구조라면 []를 추가로 명시하라는 의미이다.  

그럼 아래 예제를 통해 new & delete를 사용해보자.  

```
#include <iostream>
#include <string.h>
using namespace std;

char* MakeStrAdr(int len)
{
	// char* str = (char*)malloc(sizeof(char)*len);
    char* str = new cahr[len];

    return str;
}

int main()
{
	char* str = MakeStrAdr(20);
    // strcpy(str, "I am so Happy~!");의 형태는 VS13 이전의 형식
	strcpy_s(str, 16, "I am so Happy~!");
    cout << str << endl;

    // free(str);
    delete []str;

    return 0;
}
```

특히, Cpp에서는 malloc과 free 함수의 호출이 문제가 될 수도 있다.  

클래스와 객체에 대한 설명이 진행되지 않았기 때문에 자세히 언급하지는 않지만, 여기서는 클래스를 C의 구조체쯤으로 생각하길 바란다.  

```
#include <iostream>
#include <stdlib.h>
using namespace std;

class Simple
{
public:
	Simple()
    {
    	cout << "I'm simple constructor!" << endl;
    }
};

int main()
{
	cout << "case1: ";
    Simple* sp1 = new Simple;

    cout << "case2: ";
    Simple* sp2 = (Simple*)malloc(sizeof(Simple)*1);

	cout << endl << "end of main" << endl;

    delete sp1;
    free(sp2);

    return 0;
}
```
  
|실행 결과|
|----|
|case1: I'm simple constructor!|
|case2: |
|end of main|
  

지금은 예제를 이해하지 않고 단순하게 살펴보기만 하자. sp1과 sp2는 서로 다른 방식으로 동적할당을 했다.  

실제로 실행결과를 보면 new로 할당한 sp1은 잘 작동하지만 malloc으로 할당한 sp2는 출력되지 않는다.  

그럼 우리는 이런 생각을 할 수 있다.  

> "new와 mallo함수의 동작방식에는 차이가 있다."
  

지금은 여기까지만 기억하고 넘어가자. 이후 클래스, 객체, 생성자에 대해 알고 나면, 위 예제를 정확하게 이해할 수 있고, 동작방식의 차이를 깨닫게 될 수 있기 때문이다.  

이제 힙에 할당한 변수를 호출하는 방법에 대해 살펴보도록 하자. C에서는 포인터만을 이용해서 접근이 가능했다면 Cpp에는 참조자라는 개념이 있으니 이를 이용할 수 있다.  

앞서 언급한 것처럼 참조자는 상수가 아닌 변수를 대상으로만 선언할 수 있다는 것을 알았다.  

그리고 new로 할당한 메모리 또한 변수로 취급할 것이라는 생각을 할 수 있을 것이다(변수의 자격을 갖추기 위해서는 메모리 공간이 할당되고, 그 공간을 의미하는 이름이 존재해야 하지만, Cpp에서는 new 연산자를 이용해서 할당된 메모리 공간도 변수로 간주한다).  

따라서 다음과 같은 문장의 구성이 가능하다.  

```
int* ptr = new int;
int& ref = *ptr;	// 힙 영역에 할당된 변수에 대한 참조자 선언
ref = 20;

cout << *ptr << endl;	// 출력 결과는 20이다.
```

흔하게 사용하는 문장은 아니지만, 참조자의 선언을 통해서, 포인터 연산 없이 힙 영역에 접근할 수 있다는 사실을 알 수 있다.  
