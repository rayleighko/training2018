## function

[뒤로가기](/javascript/README.md)

함수는 한 번 정의하면 몇 번이든 실행할 수 있고 호출할 수 있는 자바스크립트 코드 블록이다.
함수 정의에는 매개변수 또는 형식인자라고 불리는 식별자 목록이 포함될 수 있는데, 이 매개변수는 함수 몸체 내에서 지역 변수처럼 취급된다.
대개 함수는 반환 값을 계산하는 과정에서 이 실인자, 즉 전달인자 값을 사용하며, 이 반환 값은 함수 호출 표현식의 결과 값이 된다. 각 호출에는 전달인자 외에도 호출 컨텍스트가 포함되는데, this키워드의 값이 바로 해당 컨텍스트다.

어떤 객체의 프로퍼티로 할달된 함수를 해당 객체의 메서드라 한다.
어떤 함수를 객체를 대상으로, 또는 객체를 통해서 호출하면, 이객체는 해당 함수의 호출 컨텍스트, 즉 호출된 함수의 this 값이 된다. 새로 생성된 객체를 초기화 하는 데 쓰이는 함수는 생성자라고 한다.

자바스크립트에서 함수는 객체이고 프로그램 안에서 조작할 수 있다.
자바스크립트는 함수를 변수에 할당할 수 있고, 다른 함수에 인자로 전달할 수도 있다. 함수는 객체이기 때문에 프로퍼티를 지정할 수 있고 심지어는 함수의 메서드를 호출할 수도 있다.

#####함수 정의하기
함수는 function 키워드에 의해 정의되며, function 키워드는 함수 정의 표현식또는 함수 선언문에서 사용된다. 두 경우 모두, 함수 정의는 function 키워드로 시작하고, 그 뒤에 다음과 같은 구성요소들이 따라온다.

1.함수 이름 식별자: 함수 이름은 함수 선언문에서는 반드시 필요하다. 함수 이름은 곧 변수의 이름이며, 새로 정의된 함수 객체는 그 변수에 할당된다.
2.쉼표로 구분된 0개 이상의 식별자들과, 이 식별자들을 둘러싼 한 쌍의 괄호. 이 식별자들은 함수의 매개변수, 즉 형식인자들의 이름이고, 함수 몸체내에서 지역 변수처럼 취급된다.
3.0개 이상의 자바스크립트 문장을 포함하는 한 쌍의 중괄호. 이 자바스크립트 문장들은 함수가 호출될 때마다 실행되는 함수 본문이다.

#####자바스크립트 함수 정의하기
```
// o의 각 속성에 대해 이름과 값을 출력한다. undefined를 반환한다.
function printprops(o) {
	for (var p in o)
    	console.log(p + ": " + o[p] + "\n");
}
//이 함수 표현식은 전달인자를 제곱하고 그 결과를 반환하는 함수를 정의한다. 정의된 함수를 변수에 할당하는 부분을 주목하자.
var squre = function(x) { return x*x };

//함수 포현식은 이름을 포함할 수 있는데, 이러한 이름은 재귀 호출에 유용하게 사용한다.
var f = function fact(x) { if (x <= 1 ) return 1; else return x*fact(x-1); };

//또한, 함수 표현식은 다른 함수의 전달인자로 사용될 수 있다.
data.sort(function(a,b) { return a-b; });

//때로 함수 표현식은 정의되는 즉시 호출된다.
var tensquared = (function(x) { return x*x; }(10));
```

함수 정의 표현식에서 함수 이름은 옵션이다. 함수 선언문이 실제로 하는 일은 어떤 변수를 정의하고 함수 객체를 그 변수에 할당하는 것이다. 
그 함수 이름이 해당 함수의 지역 변수가 되는 것이다. 
함수 선언문은 그 함수를 둘러싼 스크립트나 함수의 맨 위로 끌어올려 진다. 따라서 해당 함수는 이 함수가 정의된 위치보다 앞서 나오는 코드로부터 호출될 수 있다. 그러나 표현식으로 정의된 함수는 다르다. 함수를 호출하려면 먼저 호출할 함수를 참조할 수 있어야 하는데, 표현식으로 정의된 함수는 변수에 할당되기 전까지는 참조할 수 없다. 변수 선언은 끌어올려지지만 변수할당은 그렇지 않다.

######중첩 함수
```
function hypotenuse(a, b) {
	function square(x) { return x*x }
    return Math.sqrt( square(a) + square(b) );
}
```
중첩 함수의 흥미로운 점은, 그 유효범위 규칙이다. 중첩된 함수는 해당 함수가 속한 함수의 매개변수와 변수에 접근할 수 있다. 앞 코드를 예로 들면 안쪽 함수 square()는 바깥쪽 함수 hypotenuse()에 정의된 매개변수 a와b를 읽고 쓸 수 있다.

함수 선언문은 문장이 아니며 함수 선언문은 전역 코드 혹은 다른 함수안에는 등장할 수 있지만, 반복문 내부, 조건문, try/catch/finally 또는 with문 안에는 들어갈 수 없다.

###함수 호출하기
>일반적인 방법
>메서드형태
>생성자
>call()과 apply() 메서드를 통한 간접 호출

#####1.일반적인 방법
```
printprops({x:1});
var total = distance(0,0,2,1) + distance(2,1,3,5);
var probability = factorial(5)/factorial(13);
```

함수가 호출될 때는 먼저, 각각의 전달인자 표현식(괄호 사이에 있는 것)이 평가되고, 평가 결과 값이 해당 함수의 전달인자가 된다. 이 전달인자 값들은 함수 정의에 등장하는 형식인자 각각에 대응된다. 함수 몸체에서 형식 인자는 실인자의 값으로 평가된다.

일반적인 함수 형태로 호출하도록 작성된 함수는 보통 this 키워드를 사용하지 않는다. 그러나 이 this 키워드를, 엄격 모드가 적용되었는지를 판단하기 위해 사용할 수는 있다.
```
//엄격 모드 여부를 알아내기 위한 함수를 정의하고 호출한다.
var strict = (function() { return !this; }());
```
#####2.메서드 호출
```
o.m = f; 			-> 이름이 m인 메서드를 다음과 같이 정의
o.m(); 				-> 객체 o에 메서드 m()을 정의한 다음 다음과 같이 호출 할 수 있다.
o.m(x, y); 			-> m() 이 두 개의 인자를 받는다면, 다음과 같이 호출할 수도 있다.
```

메서드호출의 전달인자와 반환 값에 관한 규칙은 앞에서 설명한 일반 함수호출의 경우와 완전히 같다. 그러나 메서드 호출은 함수 호출에 비해 한 가지 중요한 부분이 다른데, 그것은 바로 호출 컨텍스트다.
프로퍼티 접근 표현식은 객체와 프로퍼티 이름 으로 구성되어 있다. 메서드 호출 표현식에서는 객체 o 가 호출 컨텍스트가 되므로, 함수 몸체에서 this 키워드를 사용해서 객체 o를 참조할 수 있다.
```
var calculator = { 	->객체 리터럴
	operand1: 1,
	operand2: 1,
	add: function(){
		this.result = this.operand1 + this.operand2;
	}
}
calculator.add(); -> 1+1을 계산하기 위해 메서드를 호출.
calculator.result -> 2
```

대괄호를 사용해도 메서드 호출을 할 수 있다.
```
o["m"](x,y); -> o.m(x,y) 과 같은 방법
a[0](z) -> 이 또한 메서드 호출이다. 
```

메서드 호출은 더 복잡한 프로퍼티 접근 표현식을 포함할 수 있다.
```
customer.curname.toUpperCase(); -> customer.surname의 메서드를 호출한다.
f().m(); -> f()가 반환한 객체에 있는 메서드 m()을 호출한다.
```

메서드와 this 키워드는 자바스크립트 객체 지향 프로그래밍 패러다임의 중심이다. 메서드로 사용되는 함수는 메서드의 호출 대상 객체를 암시적 인자로 전달 받는다. 보통 메서드는 해당 객체에 어떤 작업을 수행하기 때문에, 메서드 호출 문법은 그 함수가 해당 객체에 무언가를 한다는 사실을 나타내는 세련된 방법이다. 다음 두줄을 비교하자.
```
rect.setSize(width, height);
setRectSize(rect, width, height);
```

호출한 가상 함수들은 rect에 대해 완전히 같은 작업을 수행한다. 그러나 첫 줄에 사용된 문법이, 해당 작업의 주요 초점이 객체 rect에 맞추져 있음을 좀 더 분명하게 드러낸다.

this는 키워드이며 변수나 프로퍼티 이름이 아님에 유의하라 자바스크립트 문법은 this에 값을 할당하는 것을 허용하지 않는다.

변수와 달리 this 키워드에는 유효범위가 없고 중첩 함수는 호출자의 this 값을 상속하지 않는다. 만약 중첩 함수가 메서드 형태로 호출되면, 그 함수의 this 값을 그 함수의 호출 대상 객체다. 만약 중첩 함수가 함수 형태로 호출되면, 중첩 함수의 this값은 global 객체 또는 undefined 중 하나다. 흔히 보는 실수는, 함수 형태로 호출된 중첩 함수가 바깥쪽 함수의 호출 컨텍스트를 획득하기 위해 this 값을 사용할 수 있다고 가정하는 것이다.
만약 바깥쪽 함수의 this 값에 접근하고 싶다면, 안쪽 함수의 유효범위에 바깥쪽 함수의 this 값을 별도의 변수로 저장해야 한다. 이러한 용도로 보통 self 변수를 사용한다.
```
var o = {
	m: function() {
		var self= = this;
		console.log(this === o); -> true;
		f();
		function f() {
			console.log(this === o); -> false; this는 global 또는 undefined값이다.
			console.log(self === o); -> true;
		}
	}
}
o.m(); -> 객체 o의 메서드 m을 호출한다.
```

######메서드 체이닝
메서드가 객체를 반환하면, 메서드의 반환 값을 후속 호출의 일부로 사용할 수 있다. 이는 단일 표현식만으로 일련의 메서드를 호출할 수 있게끔 한다. 예를 들면 jQuery 라이브러리를 사용할 때, 다음과 같은 코드를 흔히 보게 된다.
```
//모든 header를 찾고, 찾은 헤더의 id에 대한 map 함수 결과를 배열로 얻고 (get()) 정렬(sort())한다.
$(":header").map(function() { return this.id }).get().sort();
```

메서드 체이닝은 객체 이름은 한 번만 사용하고 메서드는 여러 번 호출할 수 있는 방식이다.
```
shape.setX(100).setY(100).setSize(50).setOutline("red").setFill("blue").draw();
```
#####3.생성자 호출
함수나 메서드 호출 앞에 new 키워드가 있다면, 그것은 생성자 호출이다.
```
var o = new Object();
var o = new Object;
```

생성자를 호출하면 생성자의 **prototype 프로퍼티를 상속받은 새로운 빈 객체**가 생성된다.
생성자 함수는 객체를 초기화 하고, 새로 생성된 이 객체는 생성자 함수의 호출 컨텍스트로 사용된다. 따라서 생성자 함수는 새로 생성된 객체를 this 키워드로 참조할 수 있다. 주의할 것은 생성자 호출이 마치 메서드 호출처럼 보일지라도, 메서드가 속한 객체가 아닌 새로 생성된 객체가 호출 컨텍스트로 사용된다는 점이다. 
즉, new o.m()과 같은 표현식에서 o가 호출 컨텍스트로 사용되지 않는다는 뜻이다.

#####4. 간접호출  
이 메서드 중 call()과 apply()는 함수를 간접적으로 호출 한다. 두 메서드 모두 호출할 때 this값을 명시적으로 지정할 수 있는데, 심지어 함수가 실제로 그 객체에 속하지 않더라도 말이다.
call() 메서드는 자신에게 주어진 전달인자를 호출할 함수의 전달인자로 사용하고,
apply() 메서드는 값 배열을 전달인자로 사용한다.

###함수 전달인자와 매개변수
자바스크립트에서 함수를 정의할 떄는 함수 매개변수의 타입, 즉 자료형을 명시하지 않는다. 그리고 함수를 호출할 때도, 전달하는 인자 값의 자료형을 검사하지 않는다. 심지어는 전달인자의 개수도 검사하지 않는다. 함수 호출 시 해당 함수에 정의된 매개변수보다 적거나 더 많은 인자가 전달되었을 때 어떤 일이 일어나는지 알아보자.

#####1.생략 가능한 매개변수
본래 정의된 것보다 적은 수의 전달인자로 함수가 호출되면, 나머지 배개변수는 undefined 값으로 설정된다. 전달인자를 생략할 수 있도록 함수를 구현하면 편리할 때가 있다. 이를 위해서 생략된 매개변수에 기본 값을 합리적으로 할당할 수 있어야 한다.
```
//객체 o의 열거 가능한 속성에 대해 각 속성의 이름을 배열 a에 추가하고, a를 반환한다.
//만약 a가 생략되면 새 배열을 생성하고 반환한다.
function getPropertyNames(o /*, optional a*/) {
	if (a === undefined) a = [];
	for (var property in o) a.push(property);
	return a;
}
//이 함수는 1개 또는 2개의 전달인자로 호출될 수 있다
var a = getPropertyNames(o);
getPropertyNames(p,a); -> p의 속성을 배열 a에 추가한다.
```

생략 가능한 전달이낮를 사용하여 함수를 설계할 때, 생략할 수 있는 인자는 전달인자 목록의 제일 뒤쪽에 두어야 한다.
#####2.가변길이 전달인자 목록: Arguments 객체
함수가 호출될 때 정의된 매개변수보다 더 많은 인자가 전달되면, 매개변수 이름이 붙지 않은 인자 값을 직접적으로 참조할 방법이 없다. Arguments 객체는 이러한 문제에 대한 해결책 이다.
```
function f(x, y, z) {
	//먼저 올바른 개수의 전달인자를 받았는지 확인한다.
	if(arguments.length != 3) {
		throw new Error("function f called with " + argument.length + " arguments, but it expects 3 arguments.");
	}
	//이곳에서 나머지 작업 실행
}
```

전달인자의 개수를 검사하는 것은 보통 불필요하다.
Aguments 객체의 한 가지 중요한 용도는 임의 개수의 전달인자를 받는 함수를 작성하는 것이다.
```
function max(/* .... */) {
	var max = Number.NEGATIVE_INFINITY;
	//전달인자를 숭회하며 가장 큰 값을 찾아 기억한다.
	for (var i = 0;, i < arguments.length; i++)
		if (arguments[i] > max) max = arguments[i];
	return max;
}
var largest = max(1, 10, 100, 2, 3, 1000, 4, 5, 10000, 6); -> 10000
```

임의 개수의 전달인자를 받을 수 있는 함수를 보통 varadic 함수, variable arity함수, varags 함수 등으로 부른다. 이 책에서는 C 프로그래밍 언어 초창기 때무터 내려온 구어체 용어인 varags을 사용한다.
varags 함수라고 할지라도 전달인자 없이 호출되는 경우를 허용할 필요는 없다. 이름이 붙은 고정개수의 전달인자 뒤에 임의 개수의 전달인자를 받은 함수를 작성 할 때에도, arguments[]객체는 아주 유용하다.

arguments는 실제로는 배열이 아니라 Arguments 객체임을 기억하라.

Argument 객체에는 별난 특징이 있는데, 비엄격 모드에서 만약 함수에 매개변수가 정의되어 있으면, Argument 객체의 배열 원소는 각 매개변수의 별칭과도 같다. 즉, Arguments 객체의 배열 원소와 매개변수의 이름은 동일한 값을 가리키는 다른 두 이름이다.
전달인자의 이름을 사용하여 인자 값을 변경하면 arguments[] 배열 원소의 값도 바뀐다. 그 반대로 arguments[] 배열 원소의 인자 값을 변경하면 전달인자 이름으로 얻을 수 있는 값도 바뀐다.
```
function f(x) {
	console.log(x);
	arguments[0] = null; -> 배열 요소를 변경하면 x 또한 변경된다.
	console.los(x); -> 이제 null 출력한다.
}
```

######callee와 caller 속성
Aguments 객체는 배열 원소 외에도 callee와 caller 프로퍼티를 정의하고 있다.
엄격모드가 아닐 때 ECMAScript 표준은 callee프로퍼티가 현재 실행되고 있는 함수를 참조한다고 정의하고 있다.
caller 프로퍼티는 호출 스택에 접근 할 수 있도록 해주고, callee프로퍼티는 이름없는 함수를 재귀적으로 호출하는 데 유용하다.
```
var factorial = function(x) {
	if ( x <= 1) return 1;
	return x * arguments.callee(x-1);
};
```

#####3.객체의 프로퍼티를 전달인자로 사용하기
어떤 함수에 세 개 이상의 매개변수가 있다면, 이 함수를 호출하는 프로그래머가 인자의 올바른 순서를 기억하기 어려워진다. 프로그래머가 매번 함수를 사용할 떄마다 문서를 참조해야 하는 문제에서 벗어나려면, 전달인자를 순서에 상관없이 이름/값의 쌍으로 함수에 전달하는 편이 효과적일 수 있다.
이런 방식으로 메서드 호출을 할 수 있게 하려면, 먼저 단일 객체를 전달인자로 받는 함수를 정의하고, 함수의 사용자에게 함수에서 요구하는 이름/값 쌍을 가진 객체를 함수의 인자로 넘기도록 하면 된다.
```
//배열 from에서 배열 to로 length 만큼 요소를 복사한다. from 배열의 from_start 요소로부터 복사를 시작하고 to 배열의 to_start 위치부터 복사한 값을 써넣는다.
여기서 올바른 전달인자 순서를 기억하기란 어렵다.
function arraycopy(from, from_start, to, to_start, length) -> start는 array이고 나머지는 index와 length는 integer이다.
{ 이곳에 코드가 위치한다. };

//이 버전은 조금 덜 효과적이지만 전달인자의 순서를 기억할 필요가 없다. 그리고 from_start와 to_start는 기본 값은 0이다.
function easycopy(args) {
	arraycopy(args.from, args.from_start || 0, args.to_start || 0, args.length);
}
var a = [1,2,3,4], b = [];
easycopy({from: a, to: b, length: 4});
```

#####4.전달 인자 방식
자바스크립트 메서드의 매개변수에는 정의된 형식도 없고, 함수에 전달한 값에 대해서 자료형 검사도 하지 않는다. 함수 인자에 해당 인자를 잘 설명하는 이름을 성택하거나 또한 바로 앞의 arraycopy() 메서드에서 처럼 주석에 인자의 자료형을 명시하면 코드를 문서화하는 데 도움이된다.

만약 문자열 인자를 요구하는 함수를 문자열이 아닌 다른 자료형의 인자로 넘겨 호출하면, 그 인자의 값은 해당 함수가 인자를 문자열로 사용하려 할 때 문자열로 변환될 것이다. 모든 원시 형식은 문자열로 변환될 수 있고, 또 모든 객체에는 toString() 메서드가 있으므로, 이렇게 단순히 문자열로 변환되는 경우에는 어떤 에러도 발생하지 않는다.
하지만, 항상 이런 것은 아니다. 앞에서 다룬 arraycopy() 메서드를 다시고려해 보자. 만약 첫번째 인자가 배열 또는 유사배열 객체가 아닐 때 호출은 실패할 것이다. 한두번만 사용하고 '버릴'함수가 아니라면, 인자 자료형을 검사하는 코드를 추가할 가치가 잇는것이다.
```
//배열(혹은 유사배열) 요소의 전체 합을 반환한다. 모든 요소는 숫자여야 하고 null과 undefined는 무시된다.
function sum(a) {
	if (isArrayLike(a)) {
		var total = 0;
		for(var i = 0; i < a.length; i++) { -> 모든 요소 순회함
			var element = a[i];
			if (element == null) continue;
			if (isFinite(element)) total += element;
			else throw new Error ("sum(): 요소는 반드시 유한수 여야 한다.");
		}
        return total;
	}
	else throw new Error("sum(): 인자는 배열 또는 유사 배열이어야 합니다.");
}
```

이 sum() 메서드는 받아들이는 인자에 대해 꽤 엄격하며, 적절하지 않은 값이전달되면 적절한 정보를 담은 에러를 발생시킨다. 하지만 이 메서드는 실제 배열 외에 유사한 배열 객체 와도 호환되며, null과 undefined 배열 요소는 무시하는 유연성도 갖췄다.

자바스크립트는 매우 유연하며 자료형을 느슨하게 처리하는 언어이기에, 때로는 인자 개수와 자료형에 유연한 함수를 작성하는 것이 바람직 하다.
```
function flexisum(a) {
	var total = 0;
	for(var i = 0; i < argument.length; i++) {
		var element = argument[i], n;
		if (element == null) continue; 				-> null과 undefined 인자를 무시한다.
		if (isArray(element))						  -> 만약 인자가 배열이라면
			n = flexisum.apply(this, element); 		-> 재귀적 방식을 통해 합계를 계산
		else if (typeof element === "function")		 -> 인자가 함수라면.
			n = Number(element()); 					-> 함수를 호출하고 숫자로 변환
		else n = Number(element); 					-> 그도 아니라면 숫자로 변환 시도
		
		if (isNaN(n)) -> 숫자로 변환할 수 없다면, error를 발생시킨다.
			throw Error("flexisum(): can`t convert " + element + " to number");
		total += n;
	}
	return total;
}
```

###값으로서의 함수
함수의 가장 중요한 특성은 **정의될 수 있고 또 호출**될 수 있다는 점이다. 함수의 정의와 호출은 자바스크립트 뿐아니라 다른 프로그래밍 언어의 문법적 특징이지만, 자바스크립트에서는 함수는 **문법일 뿐만 아니라 값이기도** 한데, 이는 함수가 변수에 할당될 수 있고, 객체의 프로퍼티나 배열 원소로 저장될 수 있으며, 다른 함수의 인자로 전달될 수도 있고, 기타 여러 방식으로 사용될 수 있음을 뜻한다.
함수가 자바스크립트 문법일 뿐만 아니라 자바스크립트 데이터도 될 수 있다는 것을 이해하기 위해, 다음 함수 정의를 보자
```
//새 함수 객체를 생성하고 이를 변수 square에 할당한다.
function square(x) { return x*x; }

var s = square; -> 이제 s는 square와 같은 함수를 참조한다.
square(4); -> 16
s(4); -> 16

//변수 외에도 객체 프로퍼티에 할당 될 수도 있는데, 이를 메서드라 한다.
var o = {square: function(x) { return x*x; }}; -> 객체 리터럴
var y = o.square(16); -> y는 256이다.

//함수를 배열 요소에 할당한다면 이름은 아예 필요가 없다.
var a = [function(x) { return x*x }, 20]; -> 배열 리터럴
a[0](a[1]); -> 400
```

######데이터로서 함수를 사용하기
```
function add(x,y) { return x + y };
function subtract(x,y) { return x + y };
function multiply(x,y) { return x * y };
function divide(x,y) { return x / y};

//위 함수중 하나를 인자로 받아 두 개의 피연산자와 같이 호출하는 함수를 정의한다.
function operate(operator, operand1, operand2) {
	return operator(operand1, operand2);
}

//(2+3) + (4*5)와 같은 값을 계산하려면 다음과 같이 함수를 호출한다.
var i = operate(add, operate(add, 2, 3), operate(multiply, 4, 5));
```
```
//예제를 위해 다시 간단한 함수를 구현한다. 이번에는 객체 리터럴 속에 함수 리터럴을 사용하였다.
var operators = {
	add: function(x,y) { return x + y };
	subtract: function(x,y) { return x + y };
	multiply: function(x,y) { return x * y };
	divide: function(x,y) { return x / y};
	pow: Math.pow -> 미리정의된 함수를 사용한다.
};

//이 함수는 연산자 이름을 취하고, 객체 안에서 그 연산자를 찾고 나서 주어진 피연산자와 같이 호출한다.
연산자 함수를 호출하는 구문을 눈여겨 보자.
function operate2(operation, operand1, operand2) {
	if (typeof operators[operation] === "function")
		return operators[operation](operand1, operand2);
	else throw "알 수 없는 연산자";
}

//("hello" + ' ' + 'world')같은 값을 계산하려면?
var j = operand2("add", "hello", operand2("add", "world));

//미리 정의된 Math.pow() 함수를 사용한다.
var k = operand2("pow", 10, 2);
```
이처럼 함수 인자 때문에 Array.sort()는 완전히 일반화 되고 한없이 유연해 진다.

#####1. 자신만의 함수 프로퍼티 정의하기
자바스크립트에서 함수를 원시 값이 아니지만 특별한 종류의 객체이고 이는 함수가 프로퍼티를 가질 수 있음을 의미한다. 함수가 여러 번 호출되어 그 값이 유지되어야 하는 정적 변수가 필요할 때는, 전역 변수를 선언해서 네임스페이스를 난잡하게 하기보다 함수의 프로퍼티를 사용하는 것이 편리한 경우가 많다.
호출 될 때마다 유일한 값을 반환하는 예제이다.
```
//함수 객체의 카우넡 프로퍼티를 초기화한다. uniqueIntegr 함수 정의는 끌어올려져 해석되기 때문에 실제 uniqueIntegr 함수 정의문 앞에서 이렇게 먼저 할당을 할 수 있다.
uniqueIntegr.counter = 0;

//이 함수는 호출될 때마다 매번 다른 정수 반환한다. 다음 반환 값을 기억하기 위해 자신의 프로퍼티를 사용한다.
function uniqueIntegr() {
	return uniqueIntegr.counter++; ->  카운터 프로퍼티를 반환하고 증가한다.
}
```

###네임스페이스로서의 함수
자바스크립트는 함수 단위의 유효범위를 갖는다. 함수 내부에서 정의된 변수는 해당 함수 내부에서는 접근할 수 있지만, 그 함수 바깥에는 존재할 수 없다. 함수 밖에서 정의된 변수는 전역 변수이고 자바스크립트 프로그램 전체에서 접근할 수 있다.
자바스크립트 단일 코드 블록 내에서만 유효한 변수를 정의하는 방법을 제공하지 않기에, 간단한 일시 네임스페이스처럼 작동하는 함수를 정의하는 기법은 전역 네임스페이스를 어지럽히지 않고도 변수를 정의할 수 있어서 유용하게 사용되는 방법이다.

예를들어 어떤 자바스크립트 모듈이 있고, 이 모듈을 다수의 다른 자바스크립트에서 사용한다고 가정하자. 대다수 코드수 코드와 마찬가지로, 이코드는 계산의 중간 결과 값을 저장하는 변수를 정의한다고 가정하자. 문제는 이 모듈은 여러 프로그램에서 사용될 것이므로, 모듈 안의 변수가 해당 모듈을 불러오는 프로그램의 변수와 충돌을 일으킬 수 있다는 것이다. 물론, 해결책은 모듈을 불러오는 프로그램 내에 두고 그 함수를 호출하는 것이다. 이런 방식으로 변수들을 전역 변수로 취급하는 대신 그 함수의 지역 변수로 다룰 수 있다.
```
function mymodule() {
//모듈 코드는 여기에 위치하며, 모듈에서 사용하는 어떤 변수건 이 함수의 지역변수다.
//따라서 전역 네임스페이스를 어지럽히지 않는다.
}
mymodule(); -> 함수를 호출해야 하는 것을 잊지 말자.
```

하나의 프로퍼티(함수)를 정의하는 것도 과하다면, **익명 함수**를 정의하고 호출하는 단일 표현식을 이용하는 방법도 있다.
```
(function () { // 이름이 없는 표현식으로 mymodule함수를 재작성
 -> 코드모듈 여기에 위치
}()); -> //함수 리터럴을 끝내고 바로 호출함.
```

앞 코드에서 중괄호 부분을 보자, 함수 앞의 시작 괄호는 반드시 필요한데, 만약 시작 괄호가 없으면 자바스크립트 인터프리터는 function키워드를 함수 선언문으로 해석하기 때문이다. 괄호가 있으면 인터프리터는 이것을 표현식 형태의 함수 선언으로 올바르게 인식한다.

다음 예제는 네임스페이스 기법을 보여준다. 익명 함수의 코드는 인터넷 익스플로러의 잘 알려진 버그가 있는지 검사하고, 만약 버그가 있다면 패치된 함수를 반환한다. 또한, 이 익명 함수의 네임스페이스는 프로퍼티 이름 배열을 내부로 감추는 구실도 하고 있다.
```
//extend 함수를 정의한다. extend 함수는 두 번째 인자와 그 다음에 오는 인자들의 프로퍼티를 첫 번째 인자로 복사한다.
//여기서 IE의 버그에 대응하는데, 만약 o의 프로토타입에 열거할 수 없는 프로퍼티가 있고 o에는 그 프로퍼티와 이름이 같은 프로퍼티가 열거 가능하다면, IE의 여러 버전에서 for/in 루프는 o의 열거 가능한 프로퍼티를 제대로 열거하지 못한다.
//즉, toString()과 같은 프로퍼토타입에서 상속 받은 프로퍼티는 우리가 해당 프로퍼티를 명시적으로 검사하지 않는 한 제대로 처리될 수 없다는 뜻이다.
var extend = (function () {
	//패치전 버그를 검사한다.
	for(var p in {toString:null}) {							->toString을 검사하기위해 인위적으로 만듦
		//여기에 이르면 for/in 루프가 제대로 작동한 것이고, extend()함수의 단순한 버전을 반환하면 된다.
		return function extend(o) {
			for(var i = 1; i < argument.length; i++) {
				var source = arguments[i];
				for (var prop in source) o[prop] = source[prop];
			}
			return o;
		};
	}

	//여기에 이르면, for/in 루프는 텍스트 객체의 toString 프로퍼티를 제대로 열거하지 못했다는 뜻이다.
	//따라서 Object.prototype의 열거할 수 없는 프로퍼티를 명시적으로 테스트하는 extent() 함수를 반환한다.
	return function patched_extend(o) {
		for(var i = 1; i < argument.length; i++) {
			var source = arguments[i];
			//열거 가능한 모든 프로퍼티를 복사한다.
			for(var prop in source) o[prop] = source[prop];
			//그리고 이제 특별한 프로퍼티를 검사한다.
			for(var j = 0; j < prototype.length; j++) {
				prop = protprops[j];
				if (source.hasOwnProperty(prop)) o[prop] = source[prop];
			}
		}
		return o;
	}
	//이것은 검사해야 하는 특별한 프로퍼티의 목록이다.
	var protoprops = ["toString", "valueOf", "construnctor", "hasOwnProperty", "isPrototypeOf", "propertyIsEnumerable", "toLocaleString"];
}())
```

###클로저
이는 함수를 호출하는 시점에서의 변수 유효 범위가 아니라, **함수가 정의된 시점의 변수 유효범위를 사용하여 함수가 실행**된다는 뜻이다. 함수 객체와 함수의 변수가 해석되는 유효범위를 아룰러 컴퓨터 과학 문헌에서는 클로저라고 일컫는다.
기술적으로 모든 자바스크립트 함수는 클로저인데, 함수는 객체이고 함수 자신과 관련된 유효범위 체인을 가지고 있기 때문이다. 함수 대부분은 함수가 정의 되었을 때의 유효범위 체인을 사용하여 호출되고, 클로저가 개입되었는지의 여부는 중요하지 않다. 클로저는 정의된 유효범위와 다른 유효범위 체인에서 사용될 때 더욱 흥미롭다.
가장일반적인 경우는 어떤 함수가 그 함수 내부에서 정의한 중첩함수를 반환하는 것이다. 중첩함수 클로저와 관련한 여러 강력한 프로그래밍 기법들이 있고, 다른 언어에 비해 자바스크립트에서는 이러한 기법이 일반적으로 사용된다.
```
var scope = "global scope";
function checkscope() {
	var scope = "local scope";
    function f() { return scope; }
    return f();
}
checkscope() -> 'local scope'
```

다음코드는?
```
var scope = "global scope";
function checkscope() {
	var scope = "local scope";
    function f() { return scope; }
    return f;
}
checkscope()() -> ?
```

어휘적 유효범위의 기본적인 규칙을 기억하자. 자바스크립트 함수는 함수가 정의되었을 때의 유효범위 체인을 사용하여 실행된다.
중첩 함수 f()가 정의된 유효범위 체인에서 변수 scope는 "local scope"로 바인드되어 있다. f가 어디서 호출되든 상관없이 f가 실행될 때 이 바인딩은 항상 유효하다. 따라서 코드의 제일 마지막 줄은 "global scope"가 아니라 "local scope"를 반환한다.

다음 uniqueInterger() 함수는 다음에 반환할 값을 유지하기 위해 함수 자신의 프로퍼티를 사용했다. 이런 방식의 한 가지 결점은, 버그가 있는 코드나 악성 코드가 카운터를 초기화하거나 정수가 아닌 값으로 프로퍼티를 설정할 수 있고, 그 결과 uniqueInterger() 함수가 유일한 또는 정수 라는 규약을 위반하게 할 수 있다는 것이다. 클로저는 함수의 지역 변수를 포착하고, 이 변수들을 내부 상태로 사용할 수 있다. uniqueInterger() 함수가 클로저를 사용하도록 어떻게 코드를 작성 하였는지 살펴보자.
```
var uniqueInterger = (function() { 				->함수를 정의하고 바로 호출.
	var counter = 0;							->아래 함수의 내부 상태.
    return function() { return counter++; };
})
```
처음 보면, 코드의 첫 줄은 함수를 uniqueInterger 변수에 할당하는 것처럼 보인다. 사실, 그 코드는 함수를 정의하고 호출하는 것이며, 함수의 반환 결과가 uniqueInterger 변수에 할당된다.
함수의 반환값은 또 다른 함수임을 알 수 있다. 중첩 함수는 유효범위에 있는 변수에 접근하고, 바깥쪽 함수에 정의된 counter 변수를 사용할 수 있다. 바깥쪽 함수의 실행이 끝나면, 어떤 코드도 counter 변수를 볼 수 없다. 오직 안쪽 함수만 단독으로 counter 변수에 접근할 수 있을 뿐이다.
counter와 같은 내부 변수는 여러 클로저가 공유할 수 있다. 즉, 같은 함수안에 정의된 중첩 함수들은 같은 유효범위 체인을 공유한다.
```
function counter() {
	var n = 0;
    return {
    	count : function() { return n++; },
        reset : function() { n = 0; }
    };
}
var c = counter(), d = counter();
c.count()										 -> 0
d.count()										 -> 0
c.reset()										 -> reset 메서드와 count 메서드는 상태를 공유한다.
c.count()										 -> 0
d.count()										 -> 1
```

이 두 메서드가 'privat varialble', 즉 내부 변수 n을 공유한다는 것이다. 그다음 이해해야 할 것은 counter()를 호출할 때마다 새로운 유효범위 체인과 새로운 내부 변수가 생성된다는 점이다. 따라서 counter()를 두번 호출하면, 서로 다른 내부 변수를 가진 두 개의 counter 객체를 얻는다.
클로저 기법과 getter/setter 프로퍼티를 결합할 수 있다는 사실은 주목할 가치가 있다. 내부 상태를 다루는 데 일반 객체 프로퍼티 대신 클로저를 사용한다.
```
function counter(n) {
	return {
    	//getter 메서드 프로퍼티를 counter 변수를 반환하고 증가시킨다.
        get count() { return n++; }.
        //setter 프로퍼티는 n 값을 감소시키는 것을 허용하지 않는다.
        set count(m) {
        	if(m >= n) n = m;
            	else throw Error("count는 오직 더 큰 값으로만 설정될 수 있습니다.");
        }
    };
}
var c = counter(1000);
c.count						-> 1000
c.count						-> 1001
c.count = 2000
c.count						-> 2000
c.count = 2000				-> 에러
```

다음은 클로저 기법을 사용하여 내부 상태를 공유하는 기법을 일반화한 것이다. 이 함수는 하나의 내부 변수와 그 변수를 얻고 설정하는 두 중첩 함수를 정의한다. 그리고 두 중첩 함수를 특정 객체의 메서드로 추가한다.
```
//이 함수는 프로퍼티 접근 메서드를 객체 o의 프로퍼티에 특정 이름으로 추가한다. 메서드 이름은 get<name>, set<name>이 된다.
//만약 단정(predicate) 함수가 제공되면, setter 메서드는 전달 인자를 저장하기 전에 인자 유효성을 테스트하기 위해 단정 함수를 사용한다.
//만약 단정 함수가 false를 반환하면 setter 메서드는 예외를 발생시킨다.

//주의할 것은, getter/setter 메서드가 제어하고 있는 프로퍼티 값이 객체 o에 저장되지 않는 것이다.
//대신, 그값은 오직 이 함수의 지역 변수로만 저장된다.
//또한, getter/setter 메서드는 이 함수 내부에 지역적으로 정의되기 떄문에 이 함수의 지역 변수에 접근할 수 있다.
//다시 말해 value 변수는 두 접근 메서드 전용이고, setter 메서드를 통하지 않고서는 설정되거나 수정될 수 없다는 뜻이다.
function addPrivateProperty(o, name, predicate) {
	var value;
    
    //getter 메서드는 단순히 value를 반환한다.
    o["get" + name] = function() { return value; };
    
    o["set" + name] = function(v) {
    	if(predicate && !predicate(v))						->??
        	throw Error("set" + name + ": 유효하지 않은 값 " + v);
        else
        	value = v;
    };
}

var o = {};

addPrivateProperty(o, "name", function(x) { return typeof x == "string"; });

o.setName("Frank");			  ->프로퍼티 값을 설정한다.
console.log(o.getName());		->프로퍼티 값을 얻는다.
o.setName(0);					->엉뚱한 자료형의 값을 설정해본다.
```

###함수 프로퍼티, 메서드, 생성자
자바스크립트 프로그램에서 함수는 일종의 값이다. typeof 연산자를 함수에 사용하면 "function"문자열을 얻을 수 있지만, 함수는 정말 독특한 자바스크립트 객체다.
함수는 객체이기 때문에 프로퍼티와 메서드를 가질 수 있다. 또한, Function()이라는 생성자도 갖고 있다.
#####1.length 프로퍼티
함수 모체내에서 argument.length는 함수에 실제로 전달된 인자의 개수다. 그러나 함수 자체의 length 프로퍼티는 의미가 다르다.

다음 코드는 arguments를 인자로 받는다. 그리고 argument.length(실제로 전달된 인자의 개수)와 argument.callee.length(요구하는 인자의 개수)를 비교하여 해당 함수에 올바른 개수의 인자가 전달되었는지를 판단한다.
```
//이 함수는 argument.callee를 사용하고, 따라서 엄격 모드에서는 작동하지 않는다.
function check(args) {
	var actual = args.length;
    var expected = args.callee.length;
    
    if (actual !== expected)		-> 두값이 다르면 예외 발생.
    throw Error("Expected " + expected + "args; got " + actual);
}

function f(x, y, z) {
	check(arguments);				-> 실제 인자 개수가 요구 개수와 같은지 검사한다.
    return x + y + z;				-> 함수의 나머지를 수행한다.
}
```
#####2.prototype 프로퍼티
모든 함수에는 prototype 프로퍼티가 있는데, 이 프로퍼티는 프로토타입 객체를 참조한다. 모든 함수는 서로 다른 프로토타입 객체를 가지고 있다. 함수가 생성자로 사용될 때, 새로 생성된 객체는 함수의 프로토 타입 객체로부터 프로퍼티들을 상속받는다.

#####3.call()과 apply() 메서드
call()과 apply()는 어떤 함수를 다른 객체의 메서드인 것처럼 간접적으로 호출 할 수 있도록 한다.
이 메서드 들은 첫 번째 인자를 호출되는 함수와 관련이 있는 객체다. 이 함수 f()를 객체 o의 메서드로 호출 하려면 다음과 같이 call() 또는 apply() 를 사용하면 된다.
```
f.call(o);
f.apply(o);
```
위의 코드는 다음 코드와 비슷하다.
```
o.m = f			->f를 o의 임시 메서드로 만든다.
o.m();			 ->아무 인자 없이 호출.
delete o.m;		->임시 메서드를 제거한다.
```

ECMAScript5의 엄격 모드에서 call() 또는 apply()의 **첫 번째 인자는 함수 내에서 this의 값**이 되는데, 그 값이 원시 값이든 null이든 undefined든 상관없다.

call()의 첫 번째 호출 컨텍스트 다음에 있는 모든 인자는 호출되는 함수로 전달된다. 
예를 들어 함수 f()로 두 숫자를 전달하고 이 함수를 객체 o의 메서드로 호출하려면, 다음과 같은 코드를 사용한다.
```
f.call(o, 1, 2);
```
apply() 메서드는 call()메서드와 비슷하지만 함수에 전달할 인자는 배열 형태여야 한다.
```
f.apply(o, [1,2]);
```

함수가 임의 개수의 인자를 받도록 정의되었다면, apply() 메서드는 임의 길이의 배열을 사용하여 해당 함수를 호출할 수 있다. 예를 들어 숫자들로 이루어진 배열에서 가장 큰 숫자를 찾으려면 apply() 메서드를 사용하여 배열의 각 요소를 Math.max()에 전달할 수 있다.
```
var biggest = Math.max.apply(Math, array_of_numbers);
```

apply()는 실제 배열과 마찬가지로 유사 배열 객체와도 잘 작동한다. 특히 argument 배열을 직접 apply()에 넘김으로써, 다른 함수를 호출할 때 현재 함수에 전달된 인자와 같은 인자를 전달할 수 있다.
```
//객체 o의 메서드 m을 원본 메서드 호출 전후에 로그 메세지를 남기는 버전으로 교체한다.
function trace(o, m) {
	var original = o[m];								->원본 메서드를 클로저에 기억한다.
    o[m] = function() {									->이제 새 메서드를 정의한다.
    	console.log(new Date(), "Entering:", m);
        var result = original.apply(this, argument);
        console.log(new Date(), "Exiting:", m);
        return result;
    };
}
```
#####4.bind() 메서드
함수와 객체를 서로 묶는 것이다. 함수 f의 bind() 메서드를 호출하면서 객체 o를 전달하면, bind()메서드는 새로운 함수를 반환한다. 반환된 새 함수를 호출하면, 원래 함수가 f가 o의 메서드로 호출된다. 새로운 함수에 전달한 모든 인자는 원래 함수에도 전달된다.
```
function f(y) { return this.x + y; }		->바인드 되어야 하는 함수
var o = { x:1 };							->바인드될 객체.
var g = f.bind(o);						  ->g(x)를 호출하면 o.f(x)가 호출된다.
g(2);									   ->3
```
다음과 같은 코드를 통해서도 구현 가능하다.
```
function bind(f, o) {
	if (f.bind) return f.bind(o);
    else return function() {
    	return f.apply(o, arguments);
    };
}
```
bind() 메서드는 파셜 애플리케이션을 구현하는데, bind()에 전달하는 인자 중 첫 번째 이후의 모든 인자는 this값과 함께 해당 함수의 인자로 바인딩 된다.
파셜 애플리케이션은 함수 프로그래밍에서 일반적인 기법이고 때로는 커링 이라 부리기도 한다.
다음은 파셜애플리케이션 구현을 위해 bind() 메서드를 사용하는 예제다.
>파샬 애플리케이션 : 여러 개의 인자를 받는 함수가 있을 때 일부의 인자를 고정한 함수를 만드는기법.
>커링(currying) : 파샬 애플리케이션과 같이 인자를 미리 고정할 수 있지만 하나씩만 고정한다는 것이 특징이다.

```
var sum = function(x,y) { return x + y };
//sum과 비슷한 새 함수를 생성하지만, this 값은 null로 바인딩되고 첫 번째 인자는 1로 바인딩 된다..
//새로운 함수는 단지 하나의 인자만 요구한다.
var succ = sum.bind(null, 1);
succ(2)												-> 3: x는 1에 바인딩되고, y 인자로 2를 넘긴다.

function f(y,z) { return this.x + y + z };
var g = f.bind({x:1}, 2);							-> 6: this.x는 1에 바인딩 되고, y는 2에 z는 3에 바인딩된다.
g(3)
```

ECMAScript3 에서도 이렇게 this 값을 바인딩할 수 있고 파샬 애플리케이션을 구현할 수 있다.
다음 과 같은 코드로 표준 bind() 메서드를 시물레이션 할 수 있다. 이 메서드를 Function.prototype.bind로 저장한 것에 주목하자.
이렇게 해서 모든 함수 객체는 Function.prototype.bind를 상속한다.
```
if (!Function.prototype.bind) {
	Function.prototype.bind = function(o /*, args */){
    	var self = this, boundArgs = arguments;
        
        //bind() 메서드의 반환된 값은 함수다
        return function() {
        	//인자 목록을 작성하는데, 첫 번째 이후의 인자부터 나머지 모든 인자를 이 함수에 전달한다.
            var args [], i;
            for(i = 1; i < boundArgs.length; i++) args.push(boundArgs[i]);
            for(i = 0; i < arguments.length; i++) args.push(arguments[i]);
            
            //인자들을 포함하여 o의 메서드로 self를 호출한다.
            return self.apply(o, args);
        };
    };
}
```
이 메서드에 의해 반환되는 함수는 바깥쪽 함수에서 정의된 변수 self와 boundArgs를 사용하는 클로저이며, 바깥쪽 함수가 안쪽 함수를 반환한 후 바깥쪽 한수가 종료되더라도 안쪽 함수를 호출할 수 있게 한다.

앞 예제에서는 할 수 없는 ECMAScript 5의 bind() 메서드 특징이 있다.
1. 실제 bind() 메서드는 함수 객체를 length프로퍼티와 함께 반환하는데, 이 length 프로퍼티는 바인딩 된 함수에 정의되어 있는 인자 개수에서 바인딩된 인자의 수를 뺸 값이다.
2. ECMAScript5의 bind() 메서드는 함수 생성자에 대해 파셜 애플리케이션으로 사용될 수 있다. 반약 bind()에 의해 반환된 함수가 생성자로 사용되면, bind()에 전달했던 this는 무시되고 원본 함수가 생성자로 호출되며, 이때 이미 바인딩된 인자들이 원본 함수 생성자에 전달된다.

bind()메서드가 반환하는 함수에는 prototype 프로퍼티가 없다. (일반 한수에 있는 prototype 프로퍼티는 삭제될 수 없다.)
그리고 바인딩된 함수를 생성자로 사용하여 만든 객체는 원본 함수의 rptotype을 상속받는다.
또한 바인딩 된 생성자 instanceof 연산자를 사용한 결과는 원본 한수에 instanceof 연산자를 사용한 경우와 같다.

#####5.toString() 메서드
모든 자바스크립트 객체와 마찬가지로 함수도 toString() 메서드를 가지고 있다. ECMAScript 명세는 이 메서드가 함수 선언문 다음에 나오는 문자열을 반환하라고 요구한다. 실제로 대부분의 toString메서드 구현체들은 함수의 전체 소수 코드를 반환한다. 

#####6.Function() 생성자
함수 정의문, 함수 리터럴 표현식 두경우 모드 function 키워드를 사용하여 함수를 정의한다. 하지만 함수는 Function() 생성자를 통해서도 정의될 수 있다.
```
var f = new Function("x", "y", "return x*y");

이 함수는 다음과 같이 이미 익숙한 문법으로 정의된 함수르와 완전히 같다.
var f = function(x, y) { return x*y }
```

Function() 생성자는 생성하려는 함수의 이름을 지정하는 어떤 인자도 받지 않는다. 함수 리터럴과 마찬가지로 Function() 생성자는 익명 한수를 생성한다. 그리고 몇가지 중요한 점이 있다.
1. Function() 생성자는 도적으로 자바스크립트 함수를 생성하고 실행 시간에 컴파일되는 것을 가능케 한다.
2. Function() 생성자는 생성자가 호출될 때마다 함수 몸체를 분석하여 새로운 함수 객체를 생성한다. 로프 내부 또는 자주 호출되는 함수 내에서 생성자를 호출한다면 이는 비효율적이다. 이와 반대로, 중첩된 함수나 함수 정의 표현식은 루프 내에 있더라도 매번 재컴파일 되지 않는다.
3. Function() 생성자와 관련하여 매우 중요한 점은 함수 생성자가 생성하는 함수는 어휘적 유효범위를 사용하지 않는다는 것이다. 함수 생성자가 생성한 함수는 언제나 최상위 레밸 함수로 컴파일된다.

```
var scope = "global";
function constructFunction() {
	var scope = "local";
    return new Function("return scope");		-> 지역 유효범위를 포착하지 않는다.
} 
//이 줄은 'global'을 반환하는데 Function() 생성자가 반환한 함수는 지역 유효범위를 사용하지 않기 때문이다.
constructFunction()(); 							-> 'global'
```

Function() 생성자는 전역 유효범위에서 동작하는 eval()과 같다고 생각하면 될 것이다. 코드에서 Function() 생성자를 사용할 필요는 거의 없을 것이다.

#####7. 호출 가능한 객체
이 전에 배열처럼 다룰 수 있는 유사 배열 객체에 대해 알아보았다. 함수도 비슷한 개념이 있으며, 호출 가능 객체는 함수 호출 표현식을 통해 호출할 수 있는 객체다. 모든 함수는 호출 가능한 객체지만, 호출 가능 객체가 모두 함수는 아니다.
오늘날 자바스크립트 구현체에서 함수가 아닌 호출 가능 객체는 두가지 상황에서 볼 수 있다.
1. IE웹 브라우저는 window.alert() 와 Document.getElementById() 같은 클라이언트 측 메서드를 구현하는데, 원시 Function객체가 아니라 호출 가능한 호스트 객체를 사용했다. 이런 메서드들은 IE에서도 다른 브라우저와 똑같이 동작하지만, 실제 Function 객체는 아니다.
2. 호출 가능한 객체의 또 다른 일반적인 형태는 RegExp 객체다. 많은 브라우저에서 RxgExp 객체의 exec() 메서드를 호출하는 대신, RegExp 객체를 직접적으로 호출할 수 있다. 이것은 넷스케이프와 호환성을 확보하기 위해 여러 벤더의 호환 제품이 지원하는 비표준 자바스크립트 기능이다. RegExp를 직접 호출할 수 있다고 해서 이를 직접 호출하는 코드를 작성하지 않도록 하라. 이 기능은 더는 사용되지 않을 것이고 미래에는 제거될 것이라 합니다.

만약 어떤 객체가 진짜 함수 객체(그리고 함수 메서드를 가지고 있는지)인지를 알아보고 싶다면, 다음 class 속성을 테스트 해보면 된다.
```
function isFunction(x) {
	return Object.prototype.toString.call(x) === "[object Function]";
}
```
이 isFunction() 함수가 이전에 나온 isArray() 함수와 매우 비슷하다는 것에 유의하라.

### 함수형 프로그래밍
자바스크립트는 리스프나 헤스켈 같은 함수형 프로그래밍 언어는 아니지만, 자바스크립트가 함수를 객체로 취급할 수 있다는 말은 자바스크립트에서도 함수형 프로그래밍 기법을 사용할 수 있다는 의미다. ECMAScript 5에서 지원하는 map()과 reduce() 같은 배열 메서드는 함수형 프로그래밍 스타일에 적합한 구조를 지니고 있다.
여기서는 자바스크립트로 함수형 프로그래밍을 하는데 필요한 기법을 설명하며, 좋은 프로그래밍 스타일이 어떤 것인지를 주장하는 것은 아니며 단지 자바스크립트 합수가 그 정도로 강력하다는 것만 살펴볼 것이다.

#####1.함수로 배열 처리하기
숫자로 이루어진 배열이 있다고 가정하고, 이 배열에 있는 값들의 평균과 표준편차를 구한다고 하자. 비-함수형 프로그래밍 스타일에서는 다음과 같은 식으로 코드를 작성할 것이다.
```
var data = [1,1,3,5,5];							-> 숫자 배열
//mean은 배열 요소의 합을 배열 요소의 개수로 나눈 값이다.
var total = 0;
for (var i = 0; i < data.length; i++) total += data[i];
var mean = total/data.length;

//표준 편차를 계산하기 위해, 먼저 각 요소의 편차에 대한 제곱을 모두 더한다/
total = 0;
for(var i = 0; i < data.length; i++) {
	var deviation = data[i] - mean;
    total += deviation * deviation;
}
var stddev = Math.sqrt(total/(data.length-1));		-> 표준 편차는 2이다.
```

배열 객체의 map() 메서드와 reduce() 메서드를 사용하면 함수형 스타일로 이와 같은 게산을 간단히 처리할 수 있다.
```
//먼저 간단한 두 함수 정의
var sum = function(x,y) { return x + y; };
var square = function(x,y) { return x * y; };

//평균과 표준편차를 구하고자 Array의 메서드(map, reduce)에 앞에서 정의한 두 함수를 적용한다.
var data = [1,1,3,5,5];
var mean = data.reduce(sum)/data.length;
var deviations = data.map(function(x) {return x-mean;});
var stddev = Math.sqrt(deviations.map(square).reduce(sum)/(data.length-1));
```

위의 map()과 reduce() 같은 메서드는 ECMAScript5 에서 소개된 메서드 인데, 만약 자신이 ECMAScript 3을 사용하고 있기 때문에 사용할수 없다면 별도의 map()과 reduce()를 정의할 수 있는데, 이미 내장 메서드가 있다면 map()과 reduce()는 별도로 구현한 것을 사용하지 않고 내장 메서드를 사용한다.
```
//배열의 a의 각 요소에 대해 함수 f를 호출하고 result 배열을 반환한다.
//만약 Array.prototype.map이 이미 정의되어 있다면 그것을 사용한다.
var map = Array.prototype.map ? 
	function(a, f) { return a.map(f); } : function(a, f) {
    	var results = [];
        for(var i = 0, len = a.length; i < len; i++) {
        	if(i in a) results[i] = f.call(null, a[i], i, a);
        }
        result;
    };

//함수 f와 초기 값 인자를 사용하여 배열 a를 단일 값으로 만든다. (Reduce)
//만약 Array.prototype.reduce가 이미정의되어 있다면 그것을 사용한다.
var reduce = Array.prototype.reduce ?
	function(a, f, initial) {
    	if(argument.length > 2) return a.reduce(f, initial);
        else return a.reduce(f);
    }
    : fucntion (a, f, initial) {
    	var i = 0, len = a.length, accumulator;
        
        //지정된 초기 값이나 a의 첫 번째 값으로 시작한다.
        if(argument.length > 2) accumulator = initial;
        else {												->배열에서 첫 번째 인덱스를 찾는다.
        	if(len == 0) throw TypeError();
            while(i < len) {
            	if(i in a) {
                	accumulator = a[i++];
                    break;
                }
                else i++;
            }
            else i++;
        }
        if (i == len) throw TypeError();
    }
    
    //배열의 나머지 요소들에 대해 f를 호출한다.
    while(i < len) {
    	if(i in a)
        	accumulator = f.call(undefined, accumulator, a[i], i, a);
        i++;
    }
    return accumulator;
};
```

앞에서 정의한 map()과 reduce() 함수를 사용하여 평균과 표준편차를 계산하는 코드는 다음과 같이 작성할 수 있다.
```
var data = [1,1,3,5,5];
var sum = function(x,y) { return x+y };
var squar = function(x) { reutrn x*x };
var mean = reduce(data, sum)/data.length;
var deviations = map(data, function(x) {return x-mean;});
var stddev = Math.sqrt(reduce(map(deviations, square), sum)/(data.length-1));
```

#####2.고차 함수
고차 함수는 하나 이상의 함수를 인자로 받고, 새 함수를 반환하는 함수다.
```
//이 고차 함수는 자신의 인자를 f에 전달하고, f의 반환 값에 대해 논리적 부정을 계산하는 함수를 반환한다.
function not(f) {
	return function() {
    	var result = f.apply(this, arguments);
        return !result;
    }
}

var even = function(x) {
	return x % 2 === 0;
};

var odd = not(even);
[1,1,3,5,5].every(odd) 			->true;
```
not()함수는 고차 함수인데, 이는 not() 함수가 함수를 인자로 받고 새로 생성한 함수를 반환하기 떄문이다. 

다음 mapper() 함수 또한 함수를 인자로 받고, 전달받은 함수를 사용하여 하나의 배열을 다른 배열에 매핑 하는 함수를 반환한다. 이 함수는 앞에서 정의한 map() 함수를 사용하는데, mapper()와 map() 두 함수가 어떻게 다르닞 이해하는 것이 중요하다.
```
function mapper(f) {
	return function(a) { return map(a,f); };
}

var increment = function(x) { return x+1; };
var incrementer = mapper(increment);
incrementer([1,2,3]); 						->[2,3,4]
```
좀 더 일반적인 예제가 있다. 이 예제는 인자로 두 함수 f와 g를 받아서 f(g())를 계산하는 함수를 반환한다.
```
//f(g(...))를 계산하는 새로운 함수를 반환한다.
//반환되는 함수 h는 모든 전달인자를 g로 전달하고, g의 결과 값을 f에 전달한다 
//그리고 f의 결과 값을 반환한다. f와 g모두 같은 this값을 사용하여 호출되는데, 이 this 값은 h가 호출될 때의 this 값과 같은 것이다.

function comporse(f,g) {
	return function() {
    	//f는 하나의 값만 넘기기 때문에 call을 사용하고 g에는 값 배열을 넘겨야 하기 때문에 apply를 사용한다.
        return f.call(this, g.apply(this, arguments));
    };
}

var square = function(x) { return x*x; };
var sum = function(x,y) { return x+y; };
var squareof = compose(squre, sum);
squareof(2,3)				-> 25
```

#####3.함수의 파셜 애플리케이션
이 전의 단락에서본 bind()메서드는 지정된 컨텍스트와 지정된 인자 집합을 사용하여 함수 f를 호출하는 함수를 반환한다. 즉 함수를 어떤 객체에 바인딩하고, 부분적으로 인자를 적용한다는 뜻이다.
```
//유사 배열 객체를 실제 배열로 변환하는 유틸리티 함수. 이후 코드에서 인자 객체를 실제 배열로 변환하는데 사용함.
function array(a, n) { return Array.prototype.slice.call(a, n||0); }
//이 함수에 전달된 인자는 대상 함수의 인자 목록에 대해 왼쪽으로 전달된다.
function partialLeft(f /*, ...*/) {
	var args = arguments() {
    	return function() {
        	var a = array(args, 1);
            a = a.concat(array(arguments));
            return f.apply(this, a);
        };
    }
}

//이 함수에 전달된 인자는 대상 함수의 인자 목록에 대해 오른쪽으로 전달된다.
function partialRight(f /*, ...*/) {
	var args = arguments;
    return function() {
    	var a = array(arguments);
        a = a.concat(array(args,1));
        return f.apply(this, a);
    };
}

//이 함수에 전달된 인자는 템플릿으로 사용된다. 인자 목록에서 정의되지 않은(undefined)값은 내부 함수에 전달된 인자의 값으로 채워진다.
function partial(f /*, ...*/) {
	var args argument;
    return function() {
    	var a = array(args, 1);
        var i=0, j=0;
        //args에 대해 루프를 돌며, undefined 값을 만나면 내부 함수에 전달된 인자 값으로 설정한다.
        for (; i < a.length; i++)
        	if(a[i] === undefined) a[i] = arguments[j++];
        //이제 남은 내부 인자 값들을 추가한다.
        a = a.concat(array(arguments, j))
        return f.apply(this, a);
    };
}

//세 인자를 전달하는 함수
var f = function(x,y,z) { return x * (y - z); };
//이 세 파셜 애플리케이션이 서로 어떻게 다른지 살펴보자
partialLeft(f, 2)(3, 4)									-> -2: 첫 번째 인자로 바인딩 함: 2 * ( 3 - 4 )
partialRight(f, 2)(3, 4)								-> 6: 마지막 인자로 바인딩 함: 3 * ( 4 - 2 )
partial(f, undefined, 2)(3, 4)							-> -6: 가운데 인자로 바인딩 함: 3 * ( 2 - 4 )
```

파셜 애플리케이션은 고차함수와 결합해서 사용할 떄 좀 더 흥미롭다. 다음 예제는 앞에서 다룬 not() 함수를 조합과 파셜 애플리케이션을 사용하여 정의하는 방법을 다루고 있다.
```
var not = partialLeft(compose, function(x) { return !x; });
var even = function(x) { return x % 2 === 0; };
var odd = not(even);
var isNumber = not(isNaN)
```

또한 평균 표준편차를 구하는 방법을 조합과 파셜 애플리케이션을 사용하여 진정한 함수형 프로그래밍 스타일로 구현할 수 있다.
```
var data = [1,1,3,5,5];
var sum = function(x,y) { return x+y; };
var product = function(x,y) { return x*y; };
var neg = partial(product, -1);
var square = partial(Math.pow, undefined, 2);
var sqr = partial(Math.pow, undefined, .5);
var reciprocal = partial(Math.pow, undefined, -1);

//이제 평균과 표준 편차를 계산함. 모든 함수 호출 뿐이며 이떠한 연산자도 사용되지 않았다.
//이 코드는 마지막 리스프 코드처럼 보인다.
var mean = product(reduce(data, sum), reciprocal(data.length));
var stddev = sqrt(
	product(reduce(map(data,compose(square, partial(sum, neg(mean)))), sum), reciprocal(sum(data.length, -1))));
```

#####4.메모이제이션
이전에 계산 결과를 캐시해두는 팩터리얼 함수를 정의 했었다. 함수형 프로그래밍에서는 이러한 캐싱 방식을 메모이제이션 이라고 부른다. 다음 코드는 고차 함수 memize()이며, 이 함수는 인자로 함수를 받아들이고 그 함수에 메모이제이션을 적용한 새로운 함수를 반환한다.
```
//함수 f의 결과를 저장한 버전을 반환한다. 함수 f의 모든 인자가 서로 구분할 수 있는 문자열 표현일 때만 작동한다.
function memoize(f) {
	var cache = {};					-> 결과 값을 캐시하는 클로저 상의 객체.
    return function() {
    	//캐시키로 사용하기 위해, 인자들을 조합하여 하나의 문자열로 만든다.
        var key = arguments.length + Array.prototype.join.call(arguments,",");
        if(key in cache) return cache[key];
        else return cache[key] = f.apply(this, arguments);
    }
}
```

memoize() 함수는 캐시 값을 저장하는 데 사용할 새 객체를 생성하고, memoize()의 지역변수에 이 객체를 할당한다. 따라서 이 객체는 반환되는 함수의 내부(클로저)에만 존재한다. 반환된 함수는 인자들을 문자열로 변환하고, 그 문자열을 캐시 객체의 프로퍼티 이름으로 사용한다. 만약 캐시에 값이 있다면 그 값을 바로 반환한다.만약 캐시된 값이 없으면 지정된 함수를 호출하고 결과 값을 캐시한 다음 해당 함수를 반환한다.
```
//자바스크립트의 함수는 객체이기 떄문에 프로퍼티를 가질수 있다. 
//이점을 이요하여 함수에 프로퍼티를 추가해 값을 캐시하고, 다음 호출 지정에 그 연산을 반복하지 않고 캐시된 프로퍼티 값을 반환하는 것을 메모이제이션 패턴이라고 한다.
var addFunc = function(number) {
	var value = 0;
    for (var i = 1; i <= number; i++) {
    	value += i;
    }
    return value;
}

//1~100 까지 많은 반복문 수행해야 함
var addFunc = function() {
	var cache = {};
    var add = function(number) {
    	if(number > 0) {
        	var saved = cache[number - 1] || addFunc(number - 1);
            console.log(number, saved);
            return saved + number;
        }
        else {
        	return 0;
        }
    };
    return add;
}();
```
cache[number - 1]에 그 값이 존재할 경우 number와 더해준후 반환한다. 또한 즉시 실행 함수 내에서 클로저를 이용했기 떄문에 cache를 함부로 설정 불가한다.