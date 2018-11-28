# 언리얼에서의 C++ 심화 - 리플렉션 시스템과 오브젝트/액터 이터레이터



이 자료는 [언리얼 공식 문서](http://api.unrealengine.com/KOR/Programming/Introduction/index.html)를 참고해 만들어졌습니다.



#### 언리얼 리플렉션(프로퍼티) 시스템



> 리플렉션(Reflection)은 프로그램이 실행시간에 자기 자신을 조사하는 기능을 말한다. 이는 엄청 유용한 데다 언리얼 엔진 테크놀로지의 근간을 이루는 것으로, 에디터의 디테일 패널, 시리얼라이제이션, 가비지 콜렉션, 네트워크 리플리케이션, 블루프린트/C++ 커뮤니케이션 등 다수의 시스템에 탑재된 기능이다.

> 그러나 C++은 어떠한 형태의 리플렉션도 지원하지 않아, 언리얼에서는 자체적으로 C++ 클래스, 구조체, 함수, 멤버 변수, 열거형 관련 정보를 수집, 질의, 조작하는 별도의 시스템이 구촉되었다. 전형적으로 이러한 리플렉션은 일명 '프로퍼티 시스템'이라고 부르는데, '리플렉션'은 그래픽 용어이기도 하기 때문이다.



게임플레이 클래스는 특수한 마크업을 활용하므로, 자세히 들어가기 전 언리얼 프로퍼티 시스템의 기초를 약간 살펴보도록 하자. UE4는 별도의 리플렉션을 통해 다양한 동적인 기능을 활용한다. 이러한 기능들은 선택적으로 넣을 수 있는 것들이라, 자신의 유형에 올바른 마크업을 추가해 주지 않으면 언리얼에서는 무시하고 그에 대한 리플렉션 데이터를 생성하지 않는다는 점을 유의하자. 기본 마크업에 대한 개요는 다음과 같다.



* UCLASS() - 언리얼 엔진에게 클래스의 리플렉션 데이터를 생성하라 할 때 쓴다. 이 경우 반드시 UObject 파생 클래스여야 한다.

* USTRUCT() - 언리얼 엔진에게 구조체의 리플렉션 데이터를 생성하라고 명령할 때 쓴다.
* GENERATED_BODY() - UE4에서는 이 부분을 해당 유형에 대해 생성되는 전체 필수 표준(boilerplate) 코드로 대체한다.
* UPROPERTY() - UCLASS 또는 USTRUCT의 멤버 변수를 UPROPERTY로 사용할 수 있도록 해준다. UPROPERTY에는 여러가지 용도가 있다. 변수가 리플리케이트, 시리얼라이즈 되도록 하거나, 블루프린트에서의 접근할 수 있도록 할 수도 있다. UObject로의 레퍼런스가 몇 개나 되는지 가비지 컬렉터가 추적하는 데도 사용된다.
* UFUNCTION() - UCLASS 또는 USTRUCT의 클래스 메소드를 UFUNCTION으로 사용할 수 있도록 해준다. UFUNCTION은 블루프린트에서 클래스 메소드를 호출할 수 있도록, 다른 것보다도 RPC로 사용할 수 있도록 해준다.



일반적인 예제로 UCLASS 선언은 다음과 같이 할 수 있다.

```c++
#include "MyObject.generated.h"

UCLASS(Blueprintable)
class UMyObject : public UObject
{
    GENERATED_BODY()

public:
    MyUObject();

    UPROPERTY(BlueprintReadOnly, EditAnywhere)
    float ExampleProperty;

    UFUNCTION(BlueprintCallable)
    void ExampleFunction();
};
```





가장 먼저 눈에 띄는 것은 "MyObject.generated.h"를 include한 것이다. 언리얼에서는 모든 리플렉션 데이터를 생성하여 이 파일안에 넣는다. 이 파일 include는 유형을 선언하는 헤더 파일에서 마지막 incldue로 넣어줘야 한다.

이 예제의 UCLASS, UPROPERTY, UFUNCTION 마크업에는 부가 지정자를 포함한다. 이를 통해 각 마크업은 특정 작동방식이나 프로퍼티를 지정할 수 있습니다.

- **Blueprintable** - 이 클래스는 블루프린트로 확장시킬 수 있습니다.
- **BlueprintReadOnly** - 이 프로퍼티는 블루프린트에서 읽을 수는 있지만, 쓰기는 불가능합니다.
- **Category** - 이 프로퍼티가 에디터의 디테일 뷰에서 어느 섹션 아래 나타나도록 할지를 정의합니다. 정리용입니다.
- **BlueprintCallable** - 이 함수는 블루프린트에서 호출할 수 있습니다.

이밖에도 지정자는 나열하기 어려울 정도로 많으니 언리얼 문서에서 찾아보도록 하자.



#### 오브젝트/액터 이터레이터

오브젝트 이터레이터(반복처리기)는 특정 UObject 유형과 그 서브클래스의 모든 인스턴스를 대상으로 반복처리할 때 매우 유용하게 사용되는 툴이다.



```c++
// 현재 UObject 인스턴스를 전부 찾는다.
for (TObjectIterator<UObject> It; It; ++It)
{
    UObject* CurrentObject = *It;
    UE_LOG(LogTemp, Log, TEXT("Found UObject named: %s"), *CurrentObject->GetName());
}
```