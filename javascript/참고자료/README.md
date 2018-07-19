## web_browser_javascript

[뒤로가기](/javascript/README.md)
#include <iostream>

int main()
{
	std::cout << "Hello, Woruld!" << std::endl;  

	return 0;
}
```

#### 1. 헤더파일의 선언 부분  

구문에서 이해가 안가는 부분이 많겠지만 천천히 **전처리**부터 살펴보자. 우선 C와 C++에서 선언한 헤더파일의 내용은 '표준 입출력'에 대한 것이다.  

C에서의 표준 입출력(printf, scanf 등)을 사용하기 위해 'stdio.h'를 선언했다면 C++에서의 표준 입출력(std::cout, std::cin 등)을 사용하기 위해 'iostream'을 선언해야 한다. 그렇다면 여기서 다음과 같은 의문이 들 것이다.  

> "C++에서는 헤더파일 선언 시에 확장자(.h) 입력이 필요없나요?"  


