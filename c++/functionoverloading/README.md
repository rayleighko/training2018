## Function Overloading  

##### 함수 오버로딩에 대해 설명한다.  

[뒤로가기](/c++/README.md)

필자는 C를 처음 접할 당시에는 정말 재미가 없었다. 그런데 어느 순간 재미있기 시작했는데, 그 순간이 바로 **함수**를 배우고 난 이후였다.  

그래서 나름 **function**에 대해서 대해서 애정이 있는데, 일반적인 **C**에서는 다음과 같이 동일한 이름의 함수가 정의되는 것을 허용하지 않는다.  

```
int Func(int num)
{
	num++;
	return num;
}

int Func(int a, int b)
{
	return a+b;
}
```

그런데 개발자들은 허용되지 않는 위의 두 함수를 보고 의문을 품었다. 그들은 **Parameter**나 **Return type**이 서로 다르다면 동일한 이름의 함수를 사용하는 것이 가능하다고 생각하게 되었고, 이를 C++에 적용했다.  

```
int main()
{
	Func(20); //Func(int num) 함수의 호출
    Func(20, 30); //Func(int a, int b) 함수의 호출

	return 0;
}
```

위의 주석에서도 알 수 있듯이 **Function Call** 시 전달되는 인자를 통해서 호출하고자 하는 함수의 구분이 가능하다.   

그렇기 때문에 Parameter의 선언형태가 다르다면, **동일한 이름**의 함수를 정의할 수 있다는 것이 이해될 것이다.  

실제로 C++에서는 이를 허용하며 이를 함수 오버로딩(Function Overloading)이라 부른다. 또한, 다음과 같은 의문이 들 수도 있다.  

> 이런 방법이 예전부터 논의되어 왔을텐데 왜 C++은 **Function Overloading**을 허용하고, C는 허용하지 않는 것일까? 여기에 대한 **답은 함수를 찾는 방법이 서로 다르기 때문**이라고 할 수 있다.  

C++은 호출할 함수를 찾을 때 'Function name'과 'Parameter 선언(Declaration)'의 두 가지 정보를 동시에 활용한다. 반면에 C는 'Function name'만을 이용해서 호출대상을 찾는다.  

때문에 C에서는 함수의 Overloading이 불가능하며, 이를 문법적으로 허용하지 않는다.  

또한, **Function Overloading**이 가능한 것은 **Paramerter Declaration이 다른 경우에만 사용**할 수 있다. return type이 다른 경우도 가능할 것 같지만, 불가능하다.  

> 만약 꼭 이를 가능하게 하고 싶다면 함수를 const로 선언해주도록 하자.  

