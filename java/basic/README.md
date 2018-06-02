## 1장 기본 프로그래밍 구조  

##### 자바의 기본을 밑바닥까지 흝어보자. 단, 기초적인 내용은 제외한다.

[뒤로가기](/java/README.md)

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

### 문자열  

문자열의 개념을 '문자의 시퀸스(연속)'이라고 생각하면 이해가 쉽다. 자바에서는 유니코드 문자라면 무엇이든 문자열에 사용할 수 있다(생각보다 많다).  

문자열을 연결하는 방법도 있다.  

```
String location = "Java";
String greeting = "Hello " + location;
```
  
이 코드는 greeting 문자열을 "Hello Java"로 설정한다("Hello "의 스페이스 1개가 포함된다는 걸 유의하자).  

물론 String이 아닌 다른 타입과 결합한다면, 다른 타입을 String으로 바꿔 저장할 수도 있다.  

```
int age = 24;
String output = age + " years";
```
  
`output`은 "24 years"가 된다.  

> 문자열 연결과 덧셈을 섞어서 사용하는 것에 유의하자. 다음의 둘을 비교하여 이해해보자.  

```
"Next year, you will be + age + 1" // 논리적 오류

위 결과는 "Next year, you will be + 251"이 된다.

"Next year, you will be + (age + 1)" // OK
```
  
여러 문자열을 구분자로 구분해서 결합하고자 할 때는 join 메서드를 사용한다.  

```
String names = String.join(", ", "Peter", "Paul". "Jin");
	// names를 ", "로 구분하고, "Peter, Paul, Jin"으로 설정한다.  
```

문자열의 개수는 상관없고, 문자열의 배열을 전달해도 가능하다.  

반복적으로 여러 문자열을 연결해야 한다면 StringBuilder 클래스가 유용하다.  

```
Stringbuilder builder = new StringBuilder();
while (연결할 문자열이 존재한다면)
	builder.append(열결할 다음 문자열);
String result = builder.toString();
```
  
문자열을 연결하는 방법이 있으니 당연히 분리하는 방법도 존재한다. 여기서는 substring 메서드를 사용한다.  

```
String greeting = "Hello, World!";
String location = greeting.substring(7, 12); // location = "World";
```
  
첫 번째 인자는 삽입할 문자열의 시작 위치이고, 두 번째 인자는 삽입하지 않을 문자열의 시작 위치이다. 즉, 느낌표(12)부터 끝까지 삽입하지 않을 문자열인 것이다.  

구분자로 문자열을 연결한 것처럼 split 메서드를 이용해 구분자로 문자열을 분리할 수도 있다.  

```
String names = "Peter, Paul, Jin";
String[] result = names.split(", ");
	// result = ["Peter", "Paul", "Jin"];
```
  
여기서는 추가적으로 어떤 정규 표현식이든 분리자로 사용할 수 있다. 예를 들어 input.split("\\s+")는 input을 공백으로 분리하는 문장이다.  

문자열을 비교하는 메서드도 존재한다. equals 메서드를 사용하면 같은 문자열인지 검사한다.  

```
location.equals("World"); // true를 반환
```
  
> 문자열을 비교할 때는 절대 '==' 연산자를 사용하면 안된다. 이 연산을 진행하게 되면, 메모리에서 동일 객체일 때만 true를 반환하기 때문에 리터럴 문자열("World")의 인스턴스는 오직 한 개씩 존재해 "World" == "World"일 때문 true를 반환한다.  
>
> 예외로 문자열이 null인지 검사할 때는 '==' 연산자를 사용해도 무방하다.  
> null은 빈 문자열("")과 다르다는 점도 유의하자. 빈 문자열은 길이가 0인 문자열인 반면, null은 아예 문자열이 아니다.  
>
> 문자열이 null인 상태에서 메서드를 호출하면 '널 포인트 예외'가 발생한다. 다른 모든 예외처럼 명시적으로 처리하지 않으면 프로그램이 종료된다.  

앞선 예제처럼 문자열을 리터럴 문자열과 비교할 때는 리터럴 문자열을 앞쪽에 두는 것이 좋다.  

```
"World".equals(location);
```
  
왜냐하면 이 검사는 location이 null일 때도 제대로 동작하기 때문이다.  

이외에도 대소문자 구별없이 비교(equalsIgnoreCase())하거나 문자열의 사전적(유니코드) 순서를 비교(compareTo())하는 메서드가 존재한다.  

정수를 문자열로 변환할 때는 정적 메서드 Integer.toString을 호출하면 된다.  

```
int n = 24;
String str = Integer.toString(n); // str = "24"
```
  
> 정수를 문자열로 변환하는 더 간단한 방법은 빈 문자열과 정수를 연결하는 것이다. 하지만, 가독성과 효율성을 높이기 위해 이 방법은 선호되지 않는다.  

```
"" + n
```
  
반대로 정수를 담고 있는 문자열을 숫자로 변환할 때는 Integer.parseInt 메서드를 사용한다.  

```
String str = "24";
int n = Integer.parseInt(str); // n = 24
```
  
부동소수점 수는 Double.toString과 Double.parseDouble 메서드로 변환한다.  

```
String str = Double.toString(3.14); // str = "3.14"
double x = Double.parseDouble(str); // x = 3.14
```
  
> 자바에서 String 클래스는 불변이라는 점을 유의해야 한다. 즉, String 클래스의 어떤 메서드도 해당 문자열 자체를 변경할 수 없다.  
>
> 또 일부 메서드는 CharSequence 타입 매개변수를 받는다는 점도 유의해야 한다. CharSequence는 String, StringBuilder, 다른 문자 시퀸스의 공통 슈퍼타입이다. 자세한 설명은 생략하겠다.  

### 코드 포인트와 코드 유닛

자바는 처음 만들 당시부터 유니코드 표준을 수용했다. 유니코드 표준은 성가신 문자 인코딩 문제를 해결할 목적으로 개발되었다. 유니코드 이전에는 서로 호환되지 않는 문자 인코딩이 많았다.  

단편적인 예로 영어는 7비트 아스키, 유럽에서는 악센트를 포함해 8비트 아스키, 러시아에서는 키릴 문자를 할당하는 아스키로 확장하는 등 서로 다르게 인코드 되어 있어 인코딩 된 파일 간의 호환이 문제가 되었다.  

유니코드는 이를 해결하기 위해 만들어졌고, 16비트에서 시작해 현재는 21비트를 요구한다.  

유니코드에서 유효한 유니코드 값을 **코드 포인트**라고 한다. 예를 들어 A 문자의 코드 포인트는 U+0041이다.  

> 우리가 흔히 접한 'UTF-8' 혹은 'UTF-16'은 각각 유니코드 문자 한 개를 8, 16로 나타내는 인코딩 방법이다.  

자바는 유니코드가 16비트에서 21비트로 옮겨 가던 중간 시기에 탄생해 어려움을 겪었다. 그래서 자바 문자열은 유니코드 문자(코드 포인트)의 원래 시퀸스가 아닌 UTF-16으로 인코딩된 16비트 숫자인 **코드 유닛**의 시퀸스다.  

따라서 우리가 작업하는 자바는 코드 유닛의 시퀸스를 사용해 문자열을 표현하기 때문에 코드 포인트를 얻기 위해서는 추가적인 메서드를 사용해야 한다. 이는 여기서 다루지않고 넘어가도록 하겠다.  

### 입력과 출력  

터미널 입력을 읽고 포맷 적용 출력을 만들어 내는 방법을 알아보자.  

`System.out.println()`을 호출하면 '표준 출력 스트림'으로 전달되어 터미널에 내용이 출력된다. 반면에 '표준 입력 스트림'에서 내용을 읽는 것은 쉽지않다.  

표준 입력 스트림에 대응하는 `System.in` 객체에는 바이트 한 개를 읽어 오는 메서드만 있기 때문이다. 문자열과 숫자를 읽기 위해서는 `System.in`에 연결된 Scanner를 생성해야 한다.  

```
Scanner in = new Scanner(System.in);
```
  
nextLine 메서드는 입력을 한 줄 읽는다.  

```
System.out.println("What is your name?");
String name = in.nextLine();  
```
  
이 예제에서는 입력이 공백을 포함할 수 있으므로 nextLine 메서드를 사용하면 좋다. 공백으로 구분된 단어 한 개를 읽으려면 다음과 같이 호출하면 된다.  

```
String firstname = in.next();
```
  
이와 유사하게 정수를 읽으려면 nextInt 메서드를, 부동소수점 수를 읽으려면 nextDouble 메서드를 사용한다.  

```
System.out.println("How old are you?");
int age = in.nextInt();  
```
  
> 지금까지 설명한 Scanner 클래스는 java.util 패키지에 있다. 따라서 사용을 위해서는 아래와 같은 선언이 필수적이다.  

```
import java.util.Scanner;
```
  
> 비밀번호 등 콘솔에 나타나지 않게 입력을 받고자 할 경우에는 Scanner 말고 Console 클래스를 사용해야 한다.  

```
Console terminal = System.console();  
String username = terminal.readLine("User name: ");
char[] passwd = terminal.readPassword("Password: ");
```
  
> readPassword로 입력을 읽으면 비밀번호가 문자 배열로 반환된다. 문자 배열은 비밀번호를 사용한 후 덮어쓸 수 있으므로 String에 저장하는 것보다는 안전하게 사용할 수 있다.  

> 파일에서 입력을 읽어 오거나 파일에 출력을 쓸 경우에는 shell(bash 등)에서 입출력 재지정 문법을 사용한다.  

```
java mypackage.MainClass < input.txt // 입력  
java mypackage.MainClass > output.txt // 출력 
```
  
이제 출력에 대해 살펴보자. 지금까지는 개행을 포함한 출력을 표현했지만 개행이 없는 출력 포맷도 존재한다.  

```
System.out.print("Your age: ");
int age = in.nextInt();
```
  
이렇게 하면 커서가 프롬프트 다음 줄이 아니라 바로 뒤에 머문다.  

> print나 println 메서드로 소수점이 있는 수를 출력하면 뒤에 붙은 0을 제외한 모든 숫자를 출력하니 참고하자.  

```
System.out.print(1000.0 / 3.0);
	// 333.3333333333333
```
  
이런 출력은 화폐로 표시하고 싶을 때 문제가 된다. 이런 문제를 해결하기 위해 숫자의 개수를 제한할 수도 있다.  

```
System.out.print("%8.2f", 1000.0 / 3.0);
	// 333.33
```
  
이 결과는 앞의 빈칸 2개와 문자 6개(총 8개)로 구성된 소수점 아래 2자리까지 표현한 부동소수점 수이다.  

아래의 코드처럼 printf에 매개변수를 여러 개 지정할 수도 있다.  

```
System.out.printf("Hello, %s. Next Year, you'll be %d.\n", name, age);
```
  
우리가 알고있는 printf의 구조와 동일하다. '%(포맷 지정자)'는 각각에 대응하는 인수로 교체된다.  

> 변환 문자표를 보고 포맷 지정자와 문자를 활용해 어떤 자료형과 대응되는지 확인하자. 여기서는 생략한다.  

이외에도 포맷 적용 출력의 모양을 제어하는 플래그를 지정할 수도 있다.  

```
System.out.printf("%, +2f", 100000.0 / 3.0);  
	// +33,333.33
```
  
> 포맷 적용 출력용 플래그표를 보고 여러 플래그를 살펴보자. 여기서는 생략한다.  

더불어 `String.format` 메서드를 사용하면 포맷 적용 문자를 출력하지 않고 문자열 하나를 만들 수 있다.  

```
String message = String.format("Hello, %s. Next year, you'll be %d.\n", name, age);
```
  
### 제어흐름  

분기(branch)와 루프(loop)를 구현하는 방법을 살펴보자.  

흔히 알고 있는 `if`, `switch`와 `for`, `while`이 여기에 해당하니 여기서는 유의할 점만 설명하고 넘어가도록 한다.  

> switch 문을 사용할 때 break를 빼놓는 경우가 있다. 이 경우는 해당 case에서 문장이 끝나지 않고 다음 case의 문장을 수행한다.  
>
> 이는  컴파일러(javac)의 옵션을 이용해 손쉽게 포착할 수 있다.  

```
javac -Xlint:fakkthrough mypackage/MainClass.java  
```
  
이 문장은 케이스 항목이 break이나 return 문으로 끝나지 않을 때 컴파일러가 경고 메시지를 출력한다.  

만약 정말로 다음 case로 분기하고 싶다면, 이너테이션을 사용하도록 하자.  

> while과 for의 사용처는 루프 반복 횟수를 알고 있냐에 따라 다르다. 만약 루프 반복 횟수를 알고 있다면, for을 사용하도록 하자.  
>
> while로는 정해진 루프 반복 횟수로 루프를 도는 것이 아니라 조건만을 만족시키기 때문이다.  

> continue와 break은 유사하지만 서로 다르다. break는 루프를 즉시 빠져나와 반복문 바로 아래로 분기되는 반면, continue는 반복문의 그 다음 조건을 수행한다(검사 부분으로 분기).  

> 레이블을 이용하여 break을 사용할 수도 있는데, 다음과 같이 활용할 수 있다.  

```
outer:
while (...) {
	...
	while (...) {
		...
		if (...) braek outer;
		...
	}
	...
}
// 레이블을 붙인 break는 이 위치로 건너뛰게 한다.
```
  
레이블은 어떤 이름이든 지정할 수 있다. 물론 빠져나갈 문장의 위에 적지만, 문장의 끝으로 건너뛴다는 점에 유의하자.  

이러한 레이블을 이용해 일반적으로 루프나 switch를 빠져나오는 용도로만 사용하던 break를 블록 문을 포함해서 어떤 문장의 끝으로든 제어를 이동할 수 있게 해준다.  

```
exit: {
	...
	if (...) break exit;
	...
}
// 레이블을 붙인 break는 이 위치로 건너뛰게 한다.
```
  
> 레이블을 붙인 continue도 있고, 이는 레이블을 붙인 루프의 다음 번 반복으로 건너뛰게 한다.  

> break나 continue는 단순히 선택적인 문장이다. 같은 로직을 break나 continue 없이 표현할 수 있기 때문이다.  

변수의 유효범위에 대해 고민해보자. 지역 변수는 메서드의 매개변수를 포함해 메서드 안에서 선언한 변수다.  

이러한 지역 변수의 유효 범위는 변수 선언 지점에서 시작해 해당 선언을 감싼 블록의 끝까지 이어진다.  

```
while (...) {
	System.out.println(...);
	String input = in.next(); // 여기서 input의 유효 범위가 시작된다.
	...
	// 여기서 input의 유효범위가 끝난다.
}
```
  
다시 말해 루프가 반복될 때마다 input의 사본을 새로 만들며, 루프 바깥족에는 input 변수가 존재하지 않는 구조를 지닌다.  

> 매개변수의 유효 범위는 메서드 전체다.  

다음 예제를 보며 조금 더 고민해보자.  

```
int next;
do {
	next = generator.nextInt(10);
	count++;
} while (next != target);
```
  
> next 변수를 루프 바깥쪽에 선언해야 조건에 사용할 수 있다. 루프 안쪽에 선언했다면 next의 유효 범위가 루프 바디의 끝까지만 이어졌을 것이다.  

> for에서는 조금 다르게, 반복의 종료까지 유효범위가 지정된다.  

최종적으로 자바에서는 서로 겹치는 유효 범위에 이름이 같은 지역 변수를 여러 개 지정할 수 없다. 이 점을 유의하도록 하자.  

> 하지만 유효 범위가 겹치지 않는다면 변수 이름이 같아도 재사용할 수 있다.  

```
for (int i = 0; i < n; i++) { ... }
for (int i = n / 2; i < n; i++) { ... } // i를 재정의해도 상관없다.
```
  
### 배열과 배열 리스트  

배열(Array)는 우리도 익히 알고 있는 것처럼 변수의 집합니다. Python과 달리 자바는 언어 수준에서 배열 타입을 포함한다. 또한, 문자열 자료형도 제공해 문자열 배열의 선언도 간단하다.  

앞서 간단히 설명한 것처럼 모든 타입에는 대응하는 배열 타입이 존재한다. 다음과 같이 말이다.  

```
int[]	// 정수 타입에 대응하는 배열  
String[]	// 문자열 타입에 대응하는 배열  
char[]		// 문자 타입에 대응하는 배열   
```

변수를 초기화 하는 방법에는 **new 연산자**가 필요하다.  

```
String[] names;
names = new String[100];
```
  
물론 위의 두 문장을 하나의 문장으로 선언해도 무방하다.  

```
String[] names = new String[100];
```
  
이제 names는 100개의 문자열(0 ~ 99)로 구성된 배열을 참조하고 각 인덱스에 접근할 수 있다.  

> 만약 인덱스 외(-1, 100 등 존재하지 않는) 요소에 접근하면 ArrayIndexOutOfBoundsException이 일어나니 참고하자.  

또한, 자바에서는 개발자의 편의를 위해 'array.length'를 통해 배열의 길이를 제공한다.  

```
for (int i = 0; i < names.length; i++)
{
	names[i] = "";
}
```
  
추가적으로 C언어의 문법으로 선언해도 무방하지만 타입 사이에 변수 이름을 넣는 꼴이 되어 상대적을 가독성이 좋지 않다.  

```
int numbers[];		// int[] 자료형 사이에 numbers가 존재한다.  
```
  
배열을 생성할 때 암묵적으로 초기화에 대한 규칙이 있다.  

* 숫자 타입(char 포함)의 배열은 0으로 채운다.  
* boolean의 배열은 false로 채운다.  
* 객체의 배열은 null 참조로 채운다.  

객체의 배열을 생성한 후에는 객체로 채워야 한다. 그렇지 않으면 어떤 배열 요소도 객체를 포함하지 않은 상태이다. 그저 null 참조 100개로 채운 배열일 뿐이다.  

```
BigInteger[] numbers = new BigInteger[100];		// 단순한 null 참조일 뿐이다.
for (int i = 0; i < 100; i++)
	number[i] = BigInteger.valueOf(i);
```

또한, new를 사용하지 않고 선언하는 방법이 있는데, 이 경우는 주로 배열의 값을 알고 있을 경우에 사용된다.  

```
int[] primes = { 2, 3, 5, 7, 11, 13 };  
```
  
이처럼 중괄호로 값을 채울 때는 new 연산자를 사용하지 않으며 배열의 길이도 지정하지 않는다. 마지막 요소 뒤에 쉼표를 넣어도 된다.  

```
String[] authors = {
	"James Goslang",
	"Bill Joy",
	"Guy Steele",
};
```
  
배열에 이름을 붙이지 않을 때도 이와 유사한 초기화 문법을 사용한다.  

```
primes = new int[] = { 17, 19, 23, 29, 31 };
```
  
> 길이가 0인 배열도 'new int[0]'이나 'new int[] {}'로 만들 수 있다. 예를 들어 일치하는 항목의 배열을 반환하는 메서드는 특정 입력과 일치하는 항목이 없을 때 길이가 0인 배열을 반환하는 구조를 지닌다.  
>
> 길이가 0인 배열은 null인 배열과 다르므로 참고하자.  

#### 배열 리스트  

배열은 한 번 생성하면 절대로 길이를 변경할 수 없다. 배열은 상수의 개념이기 때문이다. 그래서 실제 프로그램에서는 불편한 경우가 많다.  

이러한 문제를 해결하기 위해 ArrayList 클래스를 사용할 수 있다. ArrayList 객체는 내부에서 배열을 관리한다.  

배열이 너무 작아지거나 배열의 공간이 많이 남으면, 다른 내부 배열을 자동으로 생성해서 원본 배열의 요소를 옮긴다. 이 과정은 배열 리스트를 사용하는 개발자에게는 보이지 않아 신경쓰지 않고 편하게 사용할 수 있다.  

배열과 배열 리스트의 문법은 완전히 다르다. 배열은 특수 문법을 사용한다. 요소에 접근할 때는 '[]' 연산자를 사용하고, 배열 타입에는 'Type[]' 문법, 배열을 생성할 때는 'new Type[n]' 문법을 사용한다. 이와 달리 배열 리스트는 클래스이므로 일반 인스턴스 생성 문법과 메서드 호출 문법을 사용한다.  

> 지금까지 다룬 클래스와 다르개 ArrayList는 제너릭 클래스, 즉 타입 매개변수가 있는 클래스다. 이에 대해서는 재너릭 클래스에 대한 문서를 살펴보기 바란다.  

```
ArrayList<String> friends;
```
  
배열 리스트 변수를 선언하려면 재너릭 클래스 문법을 사용해 '<>' 안에 타입을 지정해야 한다.  

위 배열과 마찬가지로 변수를 선언만 하는 문장이다. 이는 다음과 같이 생성하는 문법을 동반해 사용해야 한다.  

```
friends = new ArrayList<>();
	// 또는 new ArrayList<string>()
```
  
이러한 '<>'와 같은 단축 표기를 다이아몬드 문법이라고 한다. 위의 예제에서는 비어있는데, 이 경우에는 컴파일러가 변수의 타입에서 타입 매개변수를 추론해준다.  

이 호출에는 생성 인수가 없지만, 그럼에도 끝에 '()'을 붙여야 한다. 결관느 크기가 0인 배열 리스트다. add 메서드로 요소의 끝에 추가할 수 있으니 참고하자.  

```
friends.add("Peter");
friends.add("Jin");
```
  
안타깝게도 배열 리스트용 초기값 지정 문법은 없다. 따라서 배열 리스트의 초기값을 지정하기 위해 다음과 같은 형태로 생성하는 것이 최선이다.  

```
ArrayList<String> friends = new ArrayList<>(List.of("Peter", "Paul"));
```
  
여기서 List.of 메서드는 지정한 요소들로 구성된 수정 불가능한 리스트를 반환한다. 여기서는 이렇게 반환받은 리스트로 ArrayList를 생성한다. ArrayList의 어느 위치든 요소를 추가하고 제거할 수 있다.  

```
friends.remove(1);
friend.add(0, "Paul"); // 인덱스 0 앞에 Paul을 추가한다.
```
  
배열 리스트의 요소에 접근하려면 '[]'문법이 아니라 메서드 호출을 사용해야 한다. get 메서드는 요소를 읽어오고, set 메서드는 요소를 다른 값으로 교체한다.  

```
String first = fiends.get(0);
friends.set(1, "Mary");
```

size 메서드는 리스트의 현재 크기를 돌려준다. length와 같다고 보면 된다.  

```
for (int i = 0; i < friends.size(); i++)
{
	System.out.println(friends.get(i));
}
```
  
> 제너릭 클래스에는 불편한 제약이 하나 있다. 바로 기본 타입을 매개변수로 사용할 수 없다는 점인데 예를 들어 아래의 경우를 허용하지 않는 것이다.  

```
ArrayList<int>
```
  
그래서 해결책으로 wrapper class를 제공한다. 즉, 기본 타입에 대응하는 wrapper가 존재하는 것이다.  

```
Byte, Short, Integer, Long, Float, Double, Character, Boolean
```
  
이를 사용해 다음과 같은 형태로 사용할 수 있는 것이다.  

```
ArrayList<Integer> numbers = new ArrayList<>();
numbers.add(42);
int first = number.get(0); //first = 0
```
  
추가적으로 이 과정에서는 오토박싱과 언박싱이라는 과정이 존재한다. 오토박싱은 'add(42)'에서 42라는 정수를 ArrayList의 객체로 취급해주는 것이고, 언박싱은 ArrayList의 객체로 취급된 0번째의 42를 정수로 되돌려주는 작업을 말한다.  

#### 향상된 For Loop  

배열의 모든 요소를 방문하는 일은 아주 잦다. 예를 들어 다음 코드는 숫자 배열에 들어 있는 모든 요소의 합계를 계산한다.  

```
int sum = 0;
for (int i = 0; i < numbers.length; i++)
{
	sum += numbers[i];
}
```
  
이런 루프를 자주 사용하기 때문에 향상된 For Loop라는 단축 기법이 만들어졌다.  

```
int sum = 0;
for (int n : numbers)
{
	sum += n
}
```
  
향상된 For Loop은 배열읭 인덱스가 아닌 각 요소를 할당받는다. 따라서 n 변수에는 numbers[0], numbers[1], ... 등이 할당된다. ArrayList에서도 향상된 For Loop을 사용할 수 있다.  

```
for (String name : friends)
{
	System.out.println(name);
}
```
  
#### 복사  

배열 변수를 또 다른 배열 변수로 복사할 수 있지만, 일반적인 방법으로는 같은 배열을 참조하는 두 배열이 생길 뿐이다.  

```
int[] number = primes;
numbers[5] = 42;	// 이 경우 primes[5]도 42가 저장된 배열을 가리킨다.
```
  
이런 공유를 원하지 않는다면 배열의 사본을 만들어야 한다. 이 경우에는 정적 메서드 Arrays.copyOf를 사용한다.  

```
int[] copiedPrimes = Array.copyOf(primes, primes,length)
```
  
이 메서드는 새 배열을 원하는 길이로 생성하고 원본 배열의 요소를 복사한다. 배열 리스트 참조도 동일한 방식으로 작동한다.  

```
ArrayList<String> people = friends;
people.set(0, "Mary")	// 이 경우 friends의 0번째도 "Mary"가 된다.
```
  
배열 리스트의 사본을 만들기 위해선 새 배열 리스트를 생성해야 한다.  

```
String[] names - ...;
ArrayLsit<String> friends = new ArrayList<>(List.of(names));
```
  
배열 리스트를 배열에 복사할 수도 있다. 여기서 자세하게 설명하진 않겠지만 하위 호환성을 고려해 반드시 올바른 타음으로 된 배열을 전달해야 한다.  

```
String[] names = friends.toArray(new String[0]);
```
  
> 기본 타입 배열과 그에 대응하는 래퍼 클래스의 배열 리스트를 상호 변환하기는 쉽지 않다. 예를 들어 정수형(int) 배열과 정수(Integer) 배열 리스트를 상호 변환하려면 명시적인 루프나 IntStream을 사용해야 한다.  

#### 명령줄 인수  

이미 살펴본 것처럼 모든 자바 프로그램의 main 메서드는 문자열의 배열을 매개변수로 받는다.  

```
public static void main(String[] args)
```
  
프로그램을 실행하면 매개변수가 명령줄(command line)에서 지정한 인수들로 설정된다. 예를 들어 다음의 프로그램을 살펴보자.  

```
public class Greeting
{
	public static void main(String[] args)
	{
		for (int i = 0; i < args.length; i++)
		{
			String arg = args[i];
			if (arg.equals("-h")) arg = "Hello";
			else if (arg.equals("-g")) arg = "Goodbye";
			System.out.println(arg);	
		}
	}
}
```
  
이 프로그램을 다음과 같이 실행하면 args[0]은 "-g", args[1]은 "cruel", args[2]는 "world"가 된다.  

```
java Greeting -g cruel world
```
  
"java"와 "Greeting"은 main 메서드에 전달되지 않는다는 점에 유의하자.  

> 추가적으로 출력은 Goodbye cruel world가 될 것이다.  

#### 다차원 배열  

자바에는 진정한 다차원 배열이 없다. 자바에서는 배열의 배열로 다차원 배열을 구현한다. 예를 들어 다음 코드는 정수로 구성된 2차원 배열을 선언하고 구현한다.  

```
int[][] square = {
	{ 16, 3, 2, 13 },
	{ 5, 10, 11, 8 },
	{ 9, 6, 7, 12 },
	{ 4, 15, 14, 1 }
};
```
  
기술적으로는 int[]로 구성된 1차원 배열일 뿐이다. 하지만 논리적으로는 별반 다를 게 없으니 일반적인 언어에서의 다차원 배열과 유사하다고 생각하면 될 것이다.  
### 기능적 분해  

main 메서드가 너무 길어질 때는 프로그램을 여러 클래스로 분해하는 것이 바람직하다. 하지만 간단한 프로그램이라면 코드를 동일한 클래스 안에서 여러 메서드로 나누어도 된다.  

여기서는 자세히 다루지 않으니 이런 메서드들은 main 메서드와 마찬가지로 반드시 static 제어자로 선언해야 한다는 점만 알고 넘어가도록 하자.  

#### 정적 메서드 선언 및 호출  

메서드는 선언할 때는 다음과 같은 요소들이 필요하다.  

```
public static double average(double x, double y)
{
	double sum x + y;
	return sum / 2;
}
```
  
반환값의 타입, 메서드 이름, 매개변수의 타입과 이름을 메서드 선언부(header)에 작성한다. 그런 다음 메서드 구현부(body)에 구현할 내용을 채워넣어야 한다.  

main 메서드와 같은 클래스 안에 average 메서드를 추가하자. 이 메서드를 main 앞에 두는지, 뒤에 두는지는 중요하지 않다.  

```
public static void main(String[] args)
{
	double a = ...;
	double b = ...;
	double result = average(a, b);
	...
}
```
  
#### 가변 인수  

호출하는 쪽에서 인수를 원하는 개수만큼 넘길 수 있게 하는 메서드도 있다. 이미 이런 메서드로 printf를 살펴보았으니 이해하기 쉬울 것이다.  

```
System.out.printf("%d", n);
System.out.printf("%d %s", n, "widgets");
```
  
첫 번째 호출은 인수가 두 개고 두 번째 호출은 인수가 세 개이지만, 두 호출 모두 같은 메서드를 호출한다.  

이렇게 작동하는 average 메서드를 정의해서 average(3, 4.5, -5, 0)처럼 인수를 원하는 개수만큼 전달하면서 average를 호출할 수 있게 하자. 다음과 같이 타입 뒤에 ...을 붙여서 '가변 인수' 매개변수를 선언하는 것이다.  

```
public static double average(double... values)
```
  
이렇게 선언한 매개변수는 double 타입 배열이 된다. 메서드를 호출할 때 배열이 생성되고, 호출하는 쪽에서 전달하는 인수들로 채워진다. 따라서 메서드 구현부에서는 배열처럼 사용하면 된다.  

```
public static double average(double... values)
{
	double sum = 0;
	for (double v : values) sum += v;
	return values.length == 0 ? 0 : sum / values.length;
}
```
  
인수들이 이미 배열 안에 있으면 풀어 쓸 필요가 없다. 인수 목록 대신 배열을 전달하면 된다.  

```
double[] scores = { 3, 4.5, -5, 0 };
double avg  = average(scores);
```
  
가변 매개변수는 반드시 메서드의 마지막 매개변수여야 한다. 다른 매개변수를 가변 매개변수 앞에 둘 수 있는데, 예를 들어 다음 메서드는 인수가 적어도 하나는 있다.  

```
public static double max(double first, double... rest)
{
	double result = first;
	for (double v : rest) result = Math.max(v, result);
	return result;
}
```
  
