## array

[뒤로가기](/javascript/README.md)


자바스크립트의 배열은 동적이다. 필요에 따라 커질수도 있고, 작아질수도 있다.
자바스크립트 객체의 특별한 형태이고, 배열의 인덱스는 프로퍼티 이름인데, 하필 정수인 것이라고 보면 된다.

배열은 Array.prototype의 프로퍼티들을 상속받는다. Array.prototype에는 배열을 다루는 여러 메서드가 정의도어 있고 대부분 메서드는 제네릭 형태이고, 이말은 배열뿐 아니라 '유사 배열 객체' 에서도 동일하게 동작한다는 의미다.

###배열 만들기
```
var empty = []; -> 원소 없음
var primes = [2, 3, 5, 7, 11]; -> 숫자 원소가 5개인 배열
var misc = [1.1, true, "a", ]; -> 서로다른 종류의 세 원소가 존재, 쉼표로 끝남.
```

상수뿐만 아니라 임의이 표현식과 배열 리터럴또는 다른 배열 리터럴을 포함할 수 있다.
```
var base = 1024;
var table = [base, base+1, base+2];

var a = [[1,{x:1, y:2}],[2, {x:3, y:4}]];
//가운데 원소는 undefined값
var count = [1, ,3];
```

#####배열의 3가지 생성자 생성 방법
1.인자 없이 호출하는 방법
```
var a = new Array();
```
2.배열의 길이를 의미하는 숫자 값을 인자로 주어 호출하는 방법
```
var a = new Array(10);
```
3.두개의 이상 원소, 또는 숫자가 아닌 원소 값 하나를 명시적으로 지정하는 방법
```
var a = new Array(5, 4, 3, 2, 1, "testing, testing");
```
#####배열의 원소 읽기
```
var a = ["world"];
var value = a[0]; -> 0번째 원소값 읽기
a[1] = 3.14; -> 1번째 원소값 읽기
i = 2;
a[i] = 3; -> 2번째 원소값 읽기
a[i + 1] = "hello"; -> 3번째 원소값 읽기
a[a[i]] = a[0]; -> 0번째 원소값과 2번째 원소값 읽거 3번째 원소값에 값을 쓴다.

//a는 동적으로 길이가 저장되기 때문에 a.length 배열의 길이 확인은 4로 표시 된다. 또한 length를 활용하여 길이를 자율적으로 조정할 수 있다.
a = [1,2,3,4,5];
a.length = 3; -> 결과는 [1,2,3];
a.length = 5; -> 결과는 [1,2,3, , ];
```

배열첨자로 음수나, 정수 아닌 수들을 사용할 수 있기는 하다. 그런데 이 경우에는 숫자가 문자열로 변환되고, 변환된 문자열이 배열 객체의 프로퍼티 이름으로 사용된다.

배열의 인덱스가 특별한 종류의 객체 프로퍼티 이름일 뿐이라는 것은, 자바스크립트 배열에서는 "out of bounds" 에러가 발생하기 않는다는 뜻이다. 객체에 존재하지 않는 프로퍼티 이름을 질의하면, 에러가 발생하지 않고 단순히 undefined값이 반환된다.

모든 배열은 객체다. 따라서 배열은 객체의 프로토타입으로부터 원소들을 상속 받을수 있다. ECMAScript 5에서 배열은 심지어 getter와 setter 메서드를 통해 정의된 원소도 가질 수 있따. 그러나 배열 원소를 상속받거나 원소 질의나 생성에 getter/setter를 쓰면 최적화 되지 않은 코드를 쓰게 된다고 생각해야한다.

희소배열은 배열에 속한 원소 위치가 연속족이지 않은 배열을 의미한다.
```
a = new Array(5);
a = [?];
a[1000] = 0;
```

#####배열에 원소를 추가하거나 삭제하기
```
a = []
a[0] = "zero";

a.push("one","two");

b = [1,2,3];
delete b[1];
1 in a -> false 인덱스가 1인 원소값은 지워졌다.
a.length -> delete로는 크기가 줄지 않는다.
```
push와 대조대는 pop메서드는 length를 하나 줄이고, 삭제된 값을 반환한다.

#####배열 순회 하기
```
일반적인 방법은 for루프를 사용한다.
var key = Object.keys(o); -> 객체 o에서 속성 이름을 배열로 가져온다.
var value = []
for(var i = 0; i < keys.length; i++) {
	var key = keys[i];
	value[i] = keys[i];
}
```
배열에 원소가 가득 차 있고, 각 원소는 적절한 데이터를 가지고 있다고 가정한다. 만약 배열이 가정과 다를 경우, 배열의 원소를 사용하기 전에 반드시 테스트를 해야 한다. null이나 undefined 또는 빈 원소를 제외하고 싶다면 다음과 같이 작성한다.
```
for (var i =0; i < a.length; i++) {
	if(!a[i]) continue
}

//만약 undefined와 빈 원소들만 건너뛰고 싶다면?
for (var i =0; i < a.length; i++) {
	if(a[i] === undefined) continue;
}

//아무 원소도 없는 인덱스는 건너뛰지만 원소 값이 undefined인 경우
for (var i =0; i < a.length; i++) {
	if(!(i in a)) continue; ->빈원소는 건너 뜀
}

//원하지 않는 프로퍼티를 제외하는 테스트를 포함하지 않는다면, for/in 루프를 사용하지 말아야 한다.
for(var i in a) { -> 상속받은 속성은 건너뛴다.
	if (!a.hasOwnProperty(i)) continue;
}
for(var i in a) { -> i가 음의 정수라면 건너뛴다.
	if (String(Math.floor(Math.abs(Number(i)))) !== i) continue;
}

//배열의 원소가 인덱스 순서대로 하나씩 넘어오도록 하여 배열을 순회하는 형태다. forEach() 메서드가 대표적이다.
var data = [1,2,3,4,5];
var sumOfSquares = 0;
data.forEach(function(x) {
	sumOfSquares += x*x;
})
sumOfSquares -> 제곱한 값의 합은 55가 된다.
```
###배열 메서드
ECMAScript3의 Array.Prototype은 배열을 다루는데 필요한 여러 종류의 함수들을 정의하고 있다.
#####join()
```
var a = [1,2,3];
a.join(" "); -> '1 2 3'
var b = new Array(10);
b.join('-'); -> '---------'아홉 개의 하이픈 문자열 생성
```
String.split() 메서드와는 반대로 작동한다. 이 메서드는 문자열을 조각들로 분리하고, 이 조각들을 원소로 하는 배열을 생성한다.

#####reverse()
```
var a = [1,2,3];
a.reverse().join() -> a는 [3,2,1]이 되고, 문자열 '3,2,1'을 생성한다.
```
#####sort()
Array.sort() 메서드는 배열 안의 원소들을 정렬하여 반환한다. sort() 메서드를 별도의 전달인자 없이 호출하면, 배열 안의 원소들을 알파벳순으로 정렬한다.
```
var a = new Array("banana", "cherry", "apple");
a.sort();
var s = a.join(", ") -> s == 'apple, banana, cherry' undefined는 배열 끝부분으로
```
배열 원소들을 알파벳 순이 아닌 번호순으로 정렬하려면 다음과 같이 코드작성
```
var a = [33, 4, 1111, 222];
a.sort();
a.sort(function(a,b) {
	return a-b;
});												 ->오름차순 정렬 4, 33, 222, 1111으로 큰 순서대로 정렬
a.sort(function(a,b) {return b-a});				 ->내림차순 정렬
```
대소문자를 구분하지 않는 알파뱃 순으로 배열을 정렬할 수 있다. toLowerCase() 메서드를 사용해 소문자로 바꾼 후 비교 작업을 수행한다.
```
a = ['ant', 'Bug', 'cat', 'Dog']
a.sort();
a.sort(function(s,t) {
	var a = s.toLowerCase();
	var b = t.toLowerCase();
	if (a < b) return -1;
	if (a > b) return 1;
})
```
#####concat()
이 메서드의 전달인자들을 추가한 새로운 배열을 반환한다. 만약 이 메서드의 전달인자로 배열을 전달하면, 이 배열안의 원소들을 꺼내어 반환하는 배열에 추가한다.
```
var a = [1,2,3];
a.concat(4,5); -> [1,2,3,4,5];
a.concat([4,5]); -> [1,2,3,4,5,6,7];
a.concat(4, [5,[6,7]]); -> [1,2,3,4,5,[6,7]];
```
#####slice()
이 메서드는 부분 배열을 반환한다. 잘라낸 원소들을 담은 새 배열을 반환한다.
```
var a = [1,2,3,4,5];
a.slice(0,3); -> [1,2,3]
a.slice(3); -> [4,5]
a.slice(1,-1); -> [2,3,4]
a.slice(-3,-1); -> [3]
```
#####splice()
이 메서드는 배열의 원소를 삽입하거나 원소를 제거하려 할 때 범용적으로 사용할 수 있는 메서드다. splice() 메서드는 slice()나 concat() 메서드와 달리 호출 대상 배열을 바로 수정한다.
```
var a = [1,2,3,4,5,6,7,8];
a.splice(4); -> [5,6,7,8] 반환, a는 [1,2,3,4]
a.splice(1,2); -> [2,3] 반환, a는 [1,4]

var a = [1,2,3,4,5]
a.splice(2,0,'a','b'); -> [] 반환, a는 [1,2,'a','b',3,4,5]
a.splice(2,2,[1,2],3); -> ['a','b'] 반환, a는 [1,2,[1,2],3,3,4,5]
```
#####unshift()와 shift()
이 메서드는 push(), pop()과 매우 유사하게 동작하는데, 배열의 끝이 아니라 배열의 맨 앞에서 원소를 추가하고 제거한다는 점이 다르다.
```
var a = [?];
a.unshift(1); ->a:[1] => 1을 반환
a.unshift(22); ->a:[22,1] => 2을 반환
a.shift(); -> 22반환
a.unshift(3,[4,5]); ->a:[3,[4,5],1] => 3을 반환
```
#####toString()과 toLocalString()
배열의 toString() 메서드는 우선 배열의 모든 원소를 문자열로 변환하고 이 문자열들을 쉼표로 분리한 목록을 반환한다. 변환된 문자열을 대괄호 문자나 배열 값의 종류를 분류하는 구분자를 포함하지 않는다.
```
[1,2,3].toString() -> '1,2,3'
["a" ,"b" ,"c"].toString() -> 'a,b,c'
[1, [2,'c']].toString() -> '1,2,c'
```
toLocalString()은 toString()의 지역화 버전이다. 이 메서드는 우선 배열의 각 원소들을 그 원소의 toLocalString() 메서드를 사용해 변환하고, 변환된 문자열들을 지역화 구분자 문자열로 연결하여 반환한다.

###ECMAScript5 배열 메서드
대부분의 메서드들은 첫 번째 전달인자로 함수를 받는데, 이는 배열의 각 원소마다 한 번씩 실행하거나 일부 원소들에 한해 실행된다. 대부분의 경우, 첫 번째 전달인자로 지정한 함수는 세 개의 전달인자를 가지고 호출되는데, 이는 배열 원소의 값과 인덱스, 마지막으로 배열 그 자체이다. 
첫 인자로 함수를 받는 대부분의 ECMAScript 5의 배열 메서드들은 생략 가능한 두 번째 인자를 받는다. 두번째 인자는 첫 번째 전달인자인 함수 안에서 this키워드의 값으로 사용된다.

#####forEach()
이 메서드는 배열을 순회하는 메서드로, 첫 번째 인자로 넘긴 함수를 각각의 원소를 대상으로 호출한다.
```
var data = [1,2,3,4,5];
var sum = 0;
data.forEach(function(value) { sum += value; });
data.forEach(function(v, i, a) { a[i] = v + 1; });
data ->[2,3,4,5,6]
```
함수의 try 블록 안에서 forEach()를 호출 하는 foreach() 함수를 정의하고 있다. foreach()에 전달된 함수 f가 내부에서 foreach.break 예외를 임의로 발생시키면, 루프는 중간에 종료된다.
```
function foreach(a,f,t) {
	try { a.forEach(f,t);
		catch(e) {
			if(e === foreach.break) return;
			else throw e;
		}
	}
}
foreach.break = new Error("StopInteration");
```
#####map()
이 메서드는 배열의 각 원소를 메서드의 첫 번째 전달인자로 지정한 함수에 전달하고, 해당 함수의 반환 값을 배열에 담아 반환한다.
```
a = [1, 2, 3];
b = a.map(function(x) { return x*x; }); -> b는 [1, 4, 9];
```
#####filter()
이 메서드는 배열의 일부분을 반환한다.
```
a = [5, 4, 3, 2, 1];
smallvalues = a.filter(function(x) { return x < 3 }); -> [2, 1]
everyother = a.filter(function(x,i) { return i%2==0 }) -> [5, 3, 1]
```
희소배열의 빈 원소를 제거하고 싶다면 다음과 같이 사용하자
```
var dense = sparse.filter(function() { return true; });
```
undefined와 null 값을 갖는 원소도 함께 제거하고 싶다면 다음과 같이 사용하자.
```
a = a.filter(function(x) { return x !== undefined && x != null; })
```
#####every()와 some()
이 메서드는 배열 조건자 함수 이다.
every() 메서드의 경우 전달인자로 넘긴 함수가 배열의 모든 원소에 대하여 true를 반환하는 경우, every() 메서드는 true를 반환한다.
```
a = [1,2,3,4,5];
a.every(function(x) { return x < 10; }) -> true
a.every(function(x) { return x % 2 === 0; }) -> false
```
some() 메서드는 전달인자로 넘긴 함수가 배열의 일부 원소에 대해 true를 반환하는 경우에 some() 메서드는 true를 반환한다.
```
a = [1,2,3,4,5];
a.some(function(x) { return x%2 === 0; }) -> true
a.som( isNaN ) -> false
```
#####reduce()와 reduceRight()
이 메서드는 인자로 주어진 함수를 사용하여 배열의 원소들을 하나의 값으로 결합한다.
```
var a = [1,2,3,4,5];
//배열 a의 원소들의 합
var sum = a.reduce(function(x,y) { return x+y }, 0);
//배열 a의 원소들의 곱
var product = a.reduce(function(x,y) { return x*y }, 1);
//배열 a의 원소 중 가장 큰 값을 찾는 것
var max = a.reduce(function(x,y) { return (x>y)?x:y; });
```
첫 번째 인자는 배열 원소의 감소 작업을 하는 함수다. 이 감소 함수는 어떻게든 원소 중 두 값을 하나로 결합하면서 크기를 줄이고, 마지막으로 남은 값을 반환한다.
```
//redueceRight()는 reduce()와 동작은 같지만, 배열의 끝부터 시작해 반대 방향으로 처리한다.
var a = [2, 3, 4]
//2^(3^4) 를 계산한다. 거듭제곱 계산은 오른쪽에서 왼쪽으로 진행된다.
var big = a.reduceRight(function(accumulator,value) { // accumulator : 4, value : 3
	return Math.pow(value,accumulator);
});
```
#####indexOf()와 lastIndexOf() 
이메서드는 배열의 원소 중에서 특정한 값을 찾는다.
indexOf()는 배열의 처음부터 검색하고, lastIndexOf()는 배열의 끝에서 부터 검색한다.
```
a = [0, 1, 2, 1, 0];
a.index(1) -> 반환값은 1이고, a[1]은 1이다.
a.lastIndexOf(1) -> 반환값은 3이고, a[3]은 1이다.
a.indexOf(3) -> 반환값은 -1이고, 값이 3인 원소는 없다.

//배열 a에서 x인 값을 포함한 원소의 인덱스를 배열로 반환한다.
function findall(a,x) {
	var results = [?], len = a.length, pos = 0;
	while(pos < len) {
		pos = a.indexOf(x, pos);
        if (pos === -1) break;
        results.push(pop);
        pos = pos + 1;
	}
	return results;
}
```
###배열 타입
Array.isArray()라는 함수를 통해 특정 객체가 배열인지 여부를 판단할 수 있다.
```
Array.isArray([?]) -> true;
Array.isArray({?}) -> false;
ypeof 연산자가 배열 뿐만 아니라 함수를 제외한 모든 객체에 대해 "object"를 반환하기 떄문이다.
[] instanceof Array -> true;
({}) instanceof Array -> false;
```
instanceof를 사용하면 웹 브라우저에서 문제가 생길 수 있는데, 종종 하나 이상의 창 또는 프레임이 열려 있는 경우에 해당된다. 각 창 또는 프레임은 고유한 자바스크립트 실행 환경과 전역 객체를 가지고 있다. 또한, 각각의 전역 객체는 별도의 생성자 함수들을 가지고 있다. 따라서 하나의 프레임에 속한 객체는 다른 프레임에 속한 생성자의 인스턴스가 될 수 없다.

#####유사 배열 객체
자바스크립트 배열에는 다른 객체에 없는 몇 가지 특징이 있다.
>***length 프로퍼티는 배열에 새 원소가 추가될 때마다 자동으로 갱신된다.***
>***length 값을 임의로 설정함으로써 배열의 크기를 줄일 수 있다.***
>***배열은 Array.prototype에 정의된 유용한 메서드들을 상속한다.****
>***배열의 class 속성 값은 "Array"로 설정된다.***

이것은 일반 객체와 다른, 자바스크립트 배열만의 고유한 특성이다. 이것은 배열의 핵심적인 특성은 아니며, length 프로퍼티와 양의 정수 이름의 프로퍼티가 있는 객체는 일종의 배열로 취급할 수 있는 것이다.

다음 코드는 일반적인 객체를 배열과 유사한 객체로 만들기 위해 속성들을 추가한다. 이렇게 만들어진 유사 배열의 원소를 순회하는 예제
```
var a = {};
//배열과 유사한 객체로 만들기 위해 속성들을 추가한다.
var i = 0;
while(i < 10) {
	a[i] = i *i;
	i++;
}
a.length = i;

//이 객체가 마치 실제 배열인 것처럼 반복문을 수행한다.
var total = 0;
for(var j = 0; j < a.length; j++)
	total += a[j];
```
아래 함수는 배열과 유사한지 판별하는 함수다.
o가 배열과 유사한 객체인지 판별한다. 문자열과 함수는 length 프로퍼티를 갖고 있지만, 이를 typeof를 통해서 걸러낼 수 있다.
클라이언트 측 자바스크립트에서는 DOM의 text node가 length 프로퍼티를 갖고 있고, 이를 o.nodeType != 3 으로 걸러낼 수 있다.
```
function isArrayLike(o) {
	if (o &&
		typeof o === "object" &&
		isFinite(o.length) &&
		o.length >= 0 &&
		o.length == Math.floor(o.length) &&
		o.length < 4294967296)
		return true;
	else
		return false;
}
```
문자열은 배열로 다루기보다 문자열 그 자체로 다루는 편이 최선이다.
자바스크립트 배열 메서드는 배열뿐 아니라 유사 배열 객체에도 적용이 가능 하도록 범용 메서드로 구현되었다.
유사 배열은 Array.prototype을 상속받지 않기 때문에, 배열 메서드를 해당 객체의 메서드로 호출할 수는 없다. 대신 Function.call 메서드를 통해서 간접적으로 호출 할 수 있다.
```
var a = {"0":"a", "1":"b", "2":"c", length:3};
Array.prototype.join.call(a, "+") -> 'a+b+c'
Array.prototype.slice.call(a, 0) -> ["a","b","c"] 진짜 배열이 복사되어 반환됨
Array.prototype.map.call(a, function(x) {
	return x.toUpperCase(); -> ['A','B','C'];
})
```
#####문자열을 배열처럼 사용하기 
각 문자는 chatAt()메서드로 접근할 수도 있지만 대괄호 []를 사용해 접근할 수도 있다.
```
var s = test;
s.charAt(0) -> 't'
s[1] -> 'e'
```
문자열을 인덱스로 접근함으로써 얻을 수 있는 가장 큰 장점은 charAt()메서드 호출을 단순하게 []로 대체할 수 있다는 것이다.
코드를 대체함으로써 코드가 전보다 간결해지고, 가독성이 높아진다. 문자열에 번용 배열 메서드들을 바로 사용할 수 있다는 점이다.
```
s = "JavaScript"
Array.prototype.join.call(s, " "); -> "J a v a S c r i p t'
Array.prototype.filter.call(s, function(x) {
	retrun x.match(/[^aeiou]/);
}).join("") -> 'JvScrpt'만 반환
```