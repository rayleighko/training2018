## 1장 기본 프로그래밍 구조  

이 문서를 통해 JAVA 프로그래밍의 기초를 학습하며, 간단한 예제를 풀어나갈 것이다.  

### Ubuntu LTS 18.04에서 JAVA 설정하기  

필자는 java 홈페이지에서 `jdk-10.0.1_linux-x64_bin.tar.gz`을 다운로드 해 아래의 과정을 진행하였다.  

```download jdk-10.0.1 for linux 

cd Download/  
tar -xvf jdk-10.0.1_linux-x64_bin.tar.gz  
sudo mkdir /usr/lib/jvm  
sudo mv jdk-10.0.1 /usr/lib/jvm  
sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/jdk-10.0.1/bin/java 1  
sudo update-alternatives --install /usr/bin/javac javac /usr/lib/jvm/jdk-10.0.1/bin/javac 1  
sudo update-alternatives --install /usr/bin/javaws javaws /usr/lib/jvm/jdk-10.0.1/bin/javaws 1  
sudo update-alternatives --install /usr/bin/jshell jshell /usr/lib/jvm/jdk-10.0.1/bin/jshell 1  
```  

위의 과정을 거치면 java를 설치하고, shell에서 java, javac, javaws 명령을 사용하는 것이 가능해진다. 이제 마음놓고 앞으로의 실습을 진행하도록 하자.   

### 학습 목표 설명

> java는 기본적으로 terminal과 편하게 IDE를 사용하여 작성할 수 있다. 필자의 경우에는 앞서 설명한 것과 같이 terminal 환경에서 진행할 것이다.  
> 
> 여기에서 사용될 명령어는 java, javac, javaws, jshell 등이 될 것이고, 사용될 환경은 `Ubuntu LTS 18.04`, `bash shell`으로 진행하게 된다.  

우선 필자의 경우는 이전에 Java를 학습했기 때문에 정말 기본적인 사항에 대해서는 원할한 학습을 위해 생략하고자 한다.  

### JShell  

우리는 앞서 'JShell' 명령을 선언하였다. 다음의 예제를 따라해보자.  

```
$ jshell 
|  Welcome to JShell -- Version 10.0.1
|  For an introduction type: /help intro

jshell> 15
$1 ==> 15

jshell> "Hello, World"
$2 ==> "Hello, World"

jshell> $1*3
$3 ==> 45

jshell> int answer = 90
answer ==> 90

jshell> answer * 3
$5 ==> 270

jshell> new Random() // 여기서 'Shift + Tab'을 누르고, 'v'를 누르면 아래와 같은 모양이 자동 완성된다(동시에 누르면 안된다).

jshell> Random = new Random() // 여기에 아래와 같이 변수 이름을 입력하고 변수를 지정해보자.

jshell> Random generator = new Random()
generator ==> java.util.Random@6d4b1c02

// 이제 generator 변수로 호출할 수 있는 메서드를 확인할 수도 있다. 'tab'을 눌러보자.

jshell> generator.
doubles(         equals(          getClass()
hashCode()       ints(            longs(
nextBoolean()    nextBytes(       nextDouble()
nextFloat()      nextGaussian()   nextInt(
nextLong()       notify()         notifyAll()
setSeed(         toString()       wait(

jshell> generator.nextInt()
$7 ==> -450996732

jshell> Duration // 여기서 'Shift + Tab'을 누르고, 'i'를 누르면 import 대상을 찾아준다. 다음과 같이 말이다.

jshell> Duration
0: Do nothing
1: import: java.time.Duration
2: import: javafx.util.Duration
3: import: javax.xml.datatype.Duration
Choice: // 1을 입력하면 아래와 같이 import 된다.
Imported: java.time.Duration

// 종료는 '/exit'을 입력하거나 'Ctrl + D'를 누르면 된다.
```
  
### "Hello, World" 프로그램 분석하기  

다음의 프로그램을 분석해보자.  

```
package ch01.sec01;

public class HelloWorld {
	public static void main(String[] args) {
		System.out.println("Hello, World!");
	}
}
```
  
우리는 아주 간단한 이 프로그램을 면밀하게 살펴볼 필요가 있다. 왜냐하면 가장 기본적인 문장이지만, 정확하게 이해하지 못하고 있기 때문이다.  

> JAVA는 객체 지향 언어이므로 프로그램에서 대부분은 객체(object)를 조작해서 동작한다. 각 객체는 특정 클래스(class)에 속하며, 그 객체를 각각 클래스의 인스턴스(instance)라고 한다.  
>
> 클래스에는 객체 상태와 할 수 있는 일(method)를 정의한다. JAVA는 모든 코드를 클래스 안에 정의한다. 자세한 내용은 다음 article(2장)을 활용하도록 하자. 이 프로그램은 **HelloWorld** 클래스 하나로 구성되어 있다.  
  
> main은 메서드(method)이다. 즉, 클래스 안에 선언된 함수이다. 일반적으로 main은 프로그램을 실행할 때 첫 번째로 호출하는 메서드이다. 이 메서드는 객체가 없어도 작동하도록 static으로 선언한다. 또 값을 반환하지 않으므로 void로 선언했다. 매개변수로 선언된 `String[] args`는 이후에 설명하도록 하겠다.  

> JAVA는 많은 기능을 public이나 private으로 선언하는데 지정할 수 있는 형태가 두 개 더 있다. 여기에서는 public으로 선언하였는데, 이는 뜻 그대로 '공개'되어 있어 다른 클래스에서도 접근이 가능하다는 의미이다. 자세한 내용은 이후에 살펴보자.  

> 패키지(Package)는 관련 있는 클래스를 모아 놓은 집합이라고 보면 된다. 클래스를 패키지 안에 넣어 관련 있는 클래스를 함께 관리하고, 같은 이름을 지닌 클래스가 여러 개 있어도 관련된 것끼리 묶었기 때문에 충돌할 염려를 줄일 수 있다.  
>
> 여기서 사용된 `package ch01.sec01`는 장과 절 번호로 소스 코드를 구분하였다. 이 경우 HelloWorld 클래스의 전체 이름은 `ch01.sec01.HelloWorld`이 된다.  

> main 메서드의 body에는 System.out을 사용한 명령이 한 줄 적혀있다. 여기서 System.out은 JAVA 프로그램에서 '표준 출력'을 나타내는 객체다.  

### 기본 타입  

JAVA는 객체 지향 언이이지만 그렇다고 자바의 모든 것이 객체로 구성된 것은 아니다. 몇 가지 값은 기본 타입에 속한다.  

이러한 기본 타입 중 네 가지(byte, short, int, long)는 부호 있는 정수 타입이고, 두 가지(float, double)는 부동소수점 타입이며, 하나는 문자열 인코딩에 사용하는 문자 타입인 char, 나머지 하나는 진릿값을 나타내는 boolean 타입이다.  

#### 정수 타입  

대부분은 'int' 타입이 가장 잘맞다. 물론 지구의 인구를 표현하기 위해서는 'long'을 사용해야 한다. 'byte'나 'short'는 특수한 응용이나 저장 공간이 귀할 때 큰 배열을 만드는 용도로 사용된다.  

> 'long' 타입으로도 충분하지 않을 때는 'BigInteger' 클래스를 사용해야 한다.  

C/C++의 경우에는 컴파일하는 프로세서에 따라 정수 타입이 다르지만, JAVA의 경우에는 머신과 상관없이 동일하다. 이는 JAVA의 매커니즘이 '한 번 작성하고, 어디서나 실행'이기 때문이다.  

정수 리터럴을 이용해 정수의 형태를 지정할 수 있다. 'long' 타입은 접미어 'L'을 리터럴로 사용하여 '4000000000L'과 같이 나타낼 수 있다.  

그러나 'byte'나 'short'는 리터럴이 없어서 '(byte) 127'과 같이 캐스트(cast) 표기법을 사용해야 한다.  

> 이러한 리터럴은 진법의 구분에서도 사용한다. '0xCAFEBABE'는 16진수를, '0b1001'은 2진수를 나타낸다.  
>
> 숫자에 리터럴을 줄 수도 있는데, 이는 사람이 구분하기 위해 사용한다. 가령 '1_000_000'은 1,000,000을 나타내며 컴파일 시 밑줄은 삭제된다.  

#### 부동소수점 타입  

'float' 타입 숫자에는 접미어 'F'를 붙여 '3.14F'와 같이 사용한다. 만약 부동소수점 리터럴에 접미어 'F' 가 붙지않으면, 'double' 타입이 된다(default가 double이지만 접미어 'D'를 붙여 double 타입의 리터럴을 추가할 수 있다).  

> 무한대를 나타내는 **Double.POSITIVE_INFINITY**, 음의 무한대를 나타내는 **Double.NEGATIVE_INFIITY**, 숫자가 아니라는 것(Not a Number)을 나타내는 **Double.NaN** 등 특별한 부동소수점 값이 있다는 것도 알고 넘어가자.  

이러한 부동소수점 수는 금융 계산에는 적합하지 않다. 그 이유는 2진수 체계로 10진수 체계를 제대로 표현하지 못한다는 오류에서 시작되는데, 이는 '반올림 오류'라고 불린다.  

예를 들어 System.out.println(2.0 - 1.1) 명령은 예상처럼 0.9가 아니라 0.89999999999999999를 출력한다.  

이처럼 부동소수점 수를 2진수 체계로 나타내면 10진수 체계로 1/3을 정확히 나타낼 수 없듯이, 1/10을 2진수 체계인 컴퓨터가 정확하게 나타낼 수 없기 때문에 금융 계산과 같이 정확한 값을 표현할 경우에는 적합하지 않다.  

> 큰 수의 정확한 숫자 계산이 필요할 때는 BigDecimal 클래스를 사용하자.  
>
> 이외에도 'char'과 'boolean'이 존재하며, 각각 문자, 참과 거짓을 나타내기 위한 자료형이다.  
  
### 변수  

> "자바는 타입 결합이 강한 언어다."  

이 말의 의미는 각 변수에는 해당 타입 값만 저장할 수 있다는 말이다.  

C언어와 같이 변수를 선언할 때는 타입과 이름을 지정해야 하며, 초깃값을 지정할 수도 있다.  

```
int total = 0;
```
  
또한, 타입이 같은 변수 여러 개를 한 문장에 선언할 수도 있고, 객체를 선언할 수도 있다.  

```
int total = 0, count; // count는 초기화되지 않은 정수를 의미한다.

Random generator = new Random(); // 첫 번째 Random은 generator라는 변수의 타입이고, 두 번째 Random()은 new 표현식의 일부이며 '생성자'라 부른다.  
```
  
또한, 메서드 안에서 선언했다면 해당 변수를 반드시 초기화한 후 사용해야 한다. 안그러면 오류가 일어난다.  

```
int count;
count++; // 오류 발생
```
  
더불어 메서드 안에서는 모든 위치에서 변수를 선언할 수 있다. 보통 사용하기 직전에 선언하는 것이 바람직하다.  

```
Scanner in = new Scanner(System.in);
System.out.println("How old are you?");
int age = in.nextInt(); // 표준 입력을 받아 age에 저장
```

### 상수  

final 키워드는 한 번 할당하면 변경할 수 없는 값에 사용한다. 다른 언어에서는 'constant'로 불리며, 자바에서는 다음과 같이 사용할 수 있다.  

```
final int DAYS_PER_WEEK = 7;
```
  
이처럼 상수 이름은 대문자로 선언하는 관례가 있다. static을 이용해 method 외부에 선언할 수도 있다.  

```
public class calendar {
	public static final int DAYS_PER_WEEK = 7;
	...
}
```
  
이와 같은 형태는 여러 메서드에서 사용할 수 있는 상수를 정의할 때 사용한다. Calendar 내부에서는 이 상수를 DAYS_PER_WEEK으로 참조한고 다른 클래스에서는 Calendar.DAYS_PER_WEEK으로 상수 이름 앞에 클래스 이름을 붙여 사용할 수 있다.  

> 우리가 아무렇지 않게 사용하던 System 클래스의 out은 상수이고, 다음과 같이 System 클래스에 정의되어 있다.  
>
> public static final PrintStream out
>
> 상수에 대문자를 쓰지 않는 예는 몇 가지 되지 않는데, System.out이 그 중 하나이다.  

final은 변수를 상수화하는 것으로, 초기화 시 상수로 사용할 수 있는 것이다. 다음은 final의 초기화 규칙을 만족하는 예제이다.  

```
final int DAYS_IN_FEBRUARY;
if (leadpYear) {
	DAYS_IN_FEBRUARY = 29;
} else {
	DAYS_IN_FEBRUARY = 30;
}
```
  
이제 이름의 기원을 얼핏 알 것 같다. final(최종)이 의미하는 것이 일단 값을 할당하면 최종 값이 되어 절대로 변경할 수 없는 것이라는 것을 말이다.  

### 산술 연산  

자바는 C++을 기반으로 만들어져 일반적인 연산자는 C++과 유사하다. 그러므로 자세한 설명은 생략하고 특별한 부분만 설명한다.  

> 모든 정수를 0으로 나누면 예외가 일어난다. 그래서 이 예외를 잡아내지 않으면 프로그램을 종료한다. 반면에 부동소수점의 경우에는 0으로 나눠도 예외가 일어나지 않고 결과로 무한대 값이나 NaN이 나온다.

> '%' 연산자는 흔히 정수가 짝수인지 검사할 때 사용한다. 표현식 n % 2는 n이 짝수이면 0이 된다. 또한, 양수면 1, 음수면 -1이 되기 때문에 음수처리에 대해서 신경을 써야 한다.  

> n++와 ++n의 차이는 n++는 증가 이전의 값을, ++n은 증가 이후의 값을 나타내고 값을 증가시킨다는 것이다.  

> 자바에는 숫자를 제곱수로 만드는 연산자가 없다(Python에서는 **). 그 대신 Math.pow 메서드를 호출해야 한다. Math.pow(x, y)는 x의 y제곱을 나타내며, 제곱근을 구하기 위해서는 Math.sqrt(x)를 호출해야 한다.  
>
> 이 메서드들은 정적(static) 메서드이므로 객체(인스턴스)로 호출할 수 없다. static 상수와 마찬가지로 메서드가 선언된 클래스 이름을 메서드 앞에 붙여 사용해야 한다.
>
> 즉, Math 객체를 만들어 사용할 수 없고, Math.method와 같이 사용해야 한다.  

> 수학 연산에 있어 간단한 연산은 연산자로 사용해도 무방하지만, 복잡한 연산의 경우 math 메서드를 사용하는 것이 편리하고 효율적이다.  

> 자바에서는 서로 다른 타입의 피연산자를 연산할 때, 다음과 같이 우선순위에 따른 규칙을 검사하여 적용한다.  

```
1. 피연산자 중 하나가 double 타입이면 다른 하나를 double로 변환한다.  
2. 피연산자 중 하나가 float 타입이면 다른 하나를 float으로 변환한다.  
3. 피연산자 중 하나가 long 타입이면 다른 하나를 long으로 변환한다.   
4. 이외에는 두 피연산자를 int로 변환한다.  
```

> 이렇게 허용되는 것을 제외하고 강제로 변환을 수행할 때는 캐스트 연산자(대상 타입의 이름을 괄호 안에 넣은 형태)를 사용해야 한다.  

```
double x = 3.75;  
int n = (int)x;  
```
  
> 이렇게 작성하면 소수는 버리고, `n = 3`으로 설정한다.  

> 반올림을 사용하고 싶을 때는 Math.round 메서드를 사용한다. 이 메서드는 long 타입 값을 반환한다. int로 사용하고 싶다면 다음과 같이 사용하자.  

```
int n = (int) Math.round(x);  
```

> 여기서 x는 3.75이므로 n은 4가 된다. 정수 타입을 바이트 수가 더 적은 정수 타입으로 반환할 때도 캐스트 연산자를 사용해야 한다.  

```
int n = 1;
char next = (char)('J' + n); // 75(J)를 'K(76)'로 변환  
```

> 이렇게 더 작은 정수 타입으로 캐스트하면 하위 바이트들만 보존된다.  

```
int n = (int) 3000000000L; // n을 -1294967296으로 설정  
```

> 논리합의 조건을 검사할 때는 첫 번째 조건이 false이면, 그 다음 조건을 평가하지 않는다. 이런 '단락 평가(short circuit evaluation)'는 두 번째 조건이 오류를 일으킬 가능성이 있을 때 유용하다.  

```
n != 0 && s + (100 - s) / n  < 50  
```

> 논리곱의 조건을 검사할 때는 첫 번째 조건이 true이면, 그 다음 조건을 평가하지 않는다.  

```
n == 0 || s + (100 - s) / n >= 50  
```

> 이처럼 조건의 순서에 따라 프로그램의 가치가 달라질 수 있으니 ㅈ심하도록 하자.  

> 조건(conditional) 연산자는 피연산자가 세 개(조건 한 개와 값 두 개)인 연산자이다. 조건이 true면 첫 번째 값이 결과가 되고, false면 두 번재 값이 결과가 된다.  
>
> 예를 들어 다음은 time < 12면 "am" 문자열을, 그렇지 않으면 "pm" 문자열을 돌려준다.  

```
time < 12 ? "am" : "pm"  
```

> 비트 단위(bitwise)  연산자에는 &, |, ^, ~이 있다. 각 비트 단위 AND, OR, XOR, NOT을 나타내며 다음과 같이 사용된다.  

```
n & 0xF // n의 최하위 비트 네 개를 반환한다.  
n | 0xF // n의 최하위 비트 네 개를 1로 설정한다.  
n ^ 0xF // n의 최하위 비트 네 개를 뒤집는다.  
n ~ 0xF // n의 모든 비트를 뒤집는다.  
```

> 큰 숫자를 나타내고자 할 때는 Math 메서드의 BigInteger와 BigDecimal 클래스를 사용하면 된다. 각각 임의로 정밀도 정수와 부동소수점 수 연산을 구현한다.  


