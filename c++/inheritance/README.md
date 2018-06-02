## Inheritance

##### 상속에 대해 살펴보자. class의 핵심이고, 객체지향 프로그래밍의 대표적인 문법이다.  

[뒤로가기](/c++/README.md)

일단 **상속**을 단순히 문법적으로 이해해보자. 그리고 상속을 하는 이유에 대해서는 그 후에 살펴보기로 하자.  

---

상속이라 하면 흔히 재산의 **상속(Inheritance)**을 생각하기 마련이다. 그러나 Inheritance의 대상은 재산뿐만 아니라 한 사람의 좋은 품성이나 특성도 될 수 있다.  

> "나는 아버지로부터 좋은 외모와 큰 키를 물려받았다."   

따라서 나는 '나'만의 고유한 특성 외에 아버지로부터 물려 받은 좋은 목소리와 큰 키라는 또 다른 특성을 함께 지닐 수 있게 된 것이다.  

이것이 바로 상속의 의미이다. 그렇다면 이제 이러한 특성을 **Class**로 옮겨 생각해보자.  

> "Student Class가 Person Class를 상속한다."  

위에서 언급한 것처럼 **Student** Class는 **Person** Class를 상속하게 되면, Student Class는 Person Class가 지니고 있는 모든 멤버를 물려받는다.  

즉, Student Object에는 Student Class 내의 멤버뿐 아니라 Person Class에 선언되어 있는 멤버도 존재하게 된다.  

### How to use Inheritance, Result  

아래의 예제를 통해 실제 **Inheritance**의 **결과(Result)**를 확인해보자.  

```
class Person
{
private:
	int age;
    char name[50]
public:
    Person(int myage, char * myname) : age(myage)
    {
    	strcpy(name, myname);
    }
    void WhatYourName() const
    {
    	cout << "My name is " << name << endl;
    }
    void HowOldAreYou() const
    {
    	cout << "My age is " << age << endl;
    }
};
```

이 Class에 관한 설명이 없어도 충분히 이해할 것이라 생각된다. 그래서 바로 다음 Class를 소개한다.  

```
class Student : public Person
{
private:
	char major[50];	// 전공 과목
public:
	Student(char * myname, char * mymajor)
    	: Person(myage, myname)
        {
        	strcpy(major, my major);
        }
    void WhoAreYou() const
    {
    	WhatYourName();
        HowOldAreYou();
        cout << "My major is " << major << endl << endl;
    }
};
```

**Student** Class에는 **WhatYourName** 함수와 **HowOldAreYou** 함수가 정의되어 있지 않음에도 불구하고, 이 두 함수를 호출할 수 있는 이유가 바로 `Student Class가 Person Class를 '상속'했기 때문이다.`  

즉, 이 두 함수는 Person Class의 멤버함수이기 때문에 호출이 가능하다. 그리고 이것이 바로 상속의 가장 핵심적인 특징이다.  

> 추가적으로 **Inheritance**을 하게 되면, **Inheritance**의 대상이 되는 Class의 Member까지도 Object 내에 포함이 되기 때문에 호출할 수 있는 것이라고 알아두면 좋다.

다음은  **Inheritance**받은 Class의 **Constructor(생성자)**에 대해 살펴보자.  

### Inheritance받은 Class의 Constructor Define  

앞서 정의한 Student Class의 **Constructor**는 다음과 같이 정의되어 있을 것이다.  

```
Student(char * myname, int myage, char * mymajor)
	: Person(myage, myname)
{
    strcpy(major, mymajor);
}
```

일단 위의 코드를 보고, 아래의 질문에 답을 해보도록 하자.  

> Q1: Student Class의 **Constructor**는 Person Class의 Member까지 **Initialize**해야 할 의무가 있을까?  

답을 결정했다면, 설명을 계속하겠다. 이전에도 언급했듯이 Student **Object**가 생성되면, 그 Objcet 안에는 다음의 **Member Variable**이 존재하게 된다.  

* Person`s Member Variable : age, name  
* Student`s Member Variable : major  

따라서 Student Class의 **Constructor**에서는 이들 모두에 대한 **Initialize**에 책임을 져야 한다.  

> A1: Student Class의 **Constructor**는 Person Class의 Member까지 **Initialize**해야 할 의무가 있다.  

이어서 다음 질문에도 답을 해보자.  

> Q2: Student Class의 **Constructor**가 Person Class의 **Member**를 어떻게 **Initialize**하는 것이 좋겠는가?  

Member는 Class가 정의될 때, Member의 **Initialize**를 목적으로 정의된 **Constructor**를 통해서 **Initialize**하는 것이 가장 안정적이다(당시에 **Initialize**의 내용 및 방법이 결정되기 때문이다).  

그것이 비록 **Inheritance**의 관계로 묶여있다 할지라도 말이다. 따라서 위 질문에 대한 답은 다음과 같다.  

> A2: Student Class의 **Constructor**는, Person Class의 **Constrctor**를 **Call**해서 Person Class의 Member를 **Initialize**하는 것이 좋다.  

그럼 지금 진행한 두 개의 **Q&A Result**를 정리하자.  

> "Student Class의 **Constructor**는 자신이 **Inheritance**한 Person Class의 Member를 **Initialize**할 의무를 지닌다.  
>
> 그래서 Student의 **Constructor**는 Person의 **Constructor**를 호출하는 형태로 Person Class의 Member를 **Initialize**하는 것이 좋다."  

다시 한 번 Student의 Constructor를 살펴보도록 하자.  

```
Student(char * myname, int myage, char * mymajor)
	: Person(myage, myname)
{
    strcpy(major, mymajor);
}
```

Constructor의 매개변수(Parameter) 선언을 보면, Student의 Member뿐만 아니라, Person의 Member를 Initialize하기 위한 인자의 전달까지 요구하고 있음을 알 수 있다.  

그리고 이어서, **Initializer**가 나오는데, 이것이 의미하는 바는 **Constructor**의 **Call**이다.  

즉, Person Class의 Constructor를 **Call**하면서 **Argument**로 **myage**와 **myname**에 저장된 값을 전달하는 것이다.  

이렇듯, Student Class와 같은 **Inheritance**받는 Class는 **Initializer**를 이용해서 **Inheritance**하는 Class의 **Constructor Call**을 명시할 수 있다.  
