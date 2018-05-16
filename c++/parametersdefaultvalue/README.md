## Parameter's Default value  

앞서 **Function Overloading**에 관해 설명했다. 그런데 Cpp에서의 함수에는 **'Default'**라는 우리도 흔히 접해 본 값을 설정할 수 있다. 혹시 몰라 설명하자면 여기서의 default는 **'기본적으로 설정되어 있는 값'**을 의미한다(일단은 이 정도만 이해해도 괜찮다).  

---

Cpp에서는 **Function Parameter**를 아래와 같이 선언하는 것이 가능하다.  

```
int FuncOne(int num=7)
{
	return num + 1;
}

int funcTwo(int num1=5, int num2=7)
{
	return num1+num2;
}
```

여기서 **funcOne의 Parameter Declaration**은 다음과 같은 의미를 지닌다.  

> "Function Call 시 Parameter를 전달하지 않으면 7이 전달된 것으로 간주한다."  

따라서 Function call 시 `FuncOne();`과`FuncOne(7);`, 두 함수 호출문은 동일한 의미를 지닌다.  

또한, FuncTwo의 Parameter 선언은 다음과 같은 의미를 지닌다.  

> "Function call 시 Parameter를 전달하지 않으면 num1에 5가, num2에 7이 전달된 것으로 간주하겠다."  

따라서 `funcTwo();`와 `funcTwo(5, 7);`, 두 함수 호출문은 같다.  

그럼 실제 예제를 통해 자세히 알아보자.  

```
#include <iostram>

int Adder(int num1=1, int num2=2)
{
	return num1 + num2;
}

int main (void) 
{
	std::cout << Adder() << std::endl;
	std::cout << Adder(5) << std::endl;
	std::cout << Adder(3,5) << std::endl;

	return 0;
}
```

위 예제를 통해 아래와 같은 사실을 추가로 확인할 수 있다.  

> "Parameter에 Default value가 설정되어 있으면, **Declaration된 Parameter의 수**보다 **적은 수**의 Parameter전달이 가능하다(예를 들어, **Parameter**이 3개 정의되어 있으면 2개의 **Default value**를 설정할 수 있다).  
>
> 그리고 전달되는 Parameter는 **왼쪽부터** 채워져 나가고, 부족분은 **Default value**로 채워진다."  

```
이와 더불어 **Default value**은 **Function Declaration** 부분에만 표현하면 된다는 것도 알 수 있다(물론, 별도의 **Declaration**이 필요한 경우이다).
```
  
```
또한, 부분적으로 **Default value**를 설정하고 싶을 때(예를 들어 3개의 Parameter 중에 2개의 Parameter에만 값(Value)을 전달하고 싶을 때)는 **오른쪽**에서부터 채워야한다는 것을 유의해야한다. 그 이유는 아래에 설명할 **'Default value의 유의미성'**을 위해서이다.  
```

> **Default value의 유의미성**: 가령, `int Func(int num1=12, int num2, int num3){ ... }`라는 함수에 20, 30이라는 Parameter를 전달한다고 가정해보자.  
>
> 이때 Default value가 의미를 지니기 위해선 num2와 num3에 **Parameter**를 전달해야 하는데 **Parameter**는 앞에서부터 채워지기 때문에 불가능해 결과적으로 **num1에 20이, num2에 30이 전달**된다. 그래서 무의미한 Default value를 방지하고자 오른쪽에서부터 Default value를 채워야한다는 것이다.  
