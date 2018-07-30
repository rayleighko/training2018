## Object

[뒤로가기](/javascript/README.md)

###자바스크립트의 기본 데이터 타입은 객체다

객체는 일종의 복합체로, 여러 값들을 묶어 이름으로 저장하고, 값을 가져올 수 있다. 다시 말해 객체는 이름과 값으로 구성된 프로퍼티들의 정렬되지 않은 집합이다. 
프로퍼티의 이름은 문자열이기 때문에, 객체는 문자열을 값에 대응시키는 구조라고 할 수 있다.

자바스크립트 객체는 객체가 가진 고유 프로퍼티를 유지하는 것 외에 **프로토타입**이라는 다른 객체의 프로퍼티를 상속 받는다.

객체의 메서드들은 일반적으로 상속받은 프로퍼티이고, 이를 **프로토타입 상속** 이라고 한다. 프로토타입 상속은 자바스크립트의 핵심적 특징이다.

객체로 가장 많이 하는 작업은 객체를 생성한 후, 프로퍼티를 추가, 질의, 삭제, 테스트, 열거하는 것이다.

프로퍼티는 이름과 값으로 구성된다. 프로퍼티 이름은 빈 문자열을 포함한 어떤 문자열이든 될 수 있다. 같은 이름의 프로퍼티를 두개 가질 수는 없다.

######프로퍼티 속성
>쓰기 속성은 프로퍼티 값의 수정 가능 여부를 결정한다.
>열거 속성은 프로퍼티의 이름을 for/in 루프에서 읽을 수 있는지 여부를 결정한다.
>설정 속성은 프로퍼티의 삭제 가능 여부와 프로퍼티 속성의 변경 가능 여부를 결정한다.

######객체의 세가지 속성
>prototype은 상속받은 프로퍼티들을 가진 객체를 참조한다.
>class는 객체의 자료형을 특정짓는 문자열이다.
>extensible 속성은 객체에 새 프로퍼티를 추가할 수 있는지를 결정한다.

######세 부류의 자바스크립트 객체
>**네이티브 객체** 는 ECMAScript 명세에 정의된 객체 또는 그 객체의 클래스다. Array, Function, Date, 정규 표현식들은 전부 네이티브 객체다.
>**호스트 객체** 는 브라우저와 같이 자바스크립트 인터프리터가 내장된 호스트 환경에 정의된 객체다. HTMLElement 객체는 웹 페이지의 구조가 클라이언트 측 자바스크립트로 표현된 호스트 객체다.
>**사용자 정의 객체** 는 자바스크립트 코드의 실행으로 생성된 객체다.

######두 종류의 프로퍼티
>고유 프로퍼티는 객체에 직접 정의된 프로퍼티다.
>상속받은 프로퍼티는 객체의 프로토타입 객체가 정의한 프로퍼티를 말한다.

##### 객체 생성하기
객체 리터럴을 통해 만들 수도 있고, new 키워드를 사용해 만들수 있다.
ECMAscript5의 Object.create() 함수를 통해 생성할 수도 있다.

#####프로토타입
자바스크립트의 모든 객체는 또 다른 자바스크립트 객체와 연관되어 있다. 이 두 번째 객체는 프로토타입으로 알려져 있고, 이때 객체는 프로토타입으로부터 프로퍼티들을 상속받는다.
객체 리터럴로 생성된 모든 객체는 프로토타입 객체가 같으며, 자바스크립트 코드에서 이 프로토타입 객체는 Object.prototype으로 참조할 수 있다. new 키워드를 사용해 생성자를 호출하면, 생성자 함수의 프로토타입이 생성된 객체의 프로토타입이 된다. 따라서 new Object()로 생성된 객체는 {}로 생성된 객체와 마찬가지로 Object.prototype를 상속받는다. 마찬가지로 new Array()로 생성된 객체는 Array.prototype을 객체의 프로토타입으로 사용한다.

#####Object.create()
ECMAScript5는 객체를 생성하는 Object.create() 메서드를 지원한다. 이 메서드의 첫 번째 인자가 프로토타입 객체다. Object.create()는 새 객체의 프로퍼티 정보를 두 번째 인자로 받을 수 있는데, 이 인자는 생략할 수 있다.
Object.create()정적 함수로, 객체를 통해 호출되는 메서드가 아니다. 함수를 사용하기 위해서는 단순히 프로토타입 객체를 넘기기만 하면 된다.
```
var a1 = Object.create({x:1, y:2});
a1은 x,y프로퍼티를 상속받는다.
```

######특정 프로토 타입을 상속받는 객체 생성하기
```
function inherit(a) {
	if (a == null) throw TypeError();
    if (Object.create)
    	return Object.create(a);
    var t = typeof a;
    
    if (t == "object" && t !== "function") throw TypeError();
    function f() {};
    f.prototype = p;
    return new f();
}
```
inherit 함수를 사용하면 객체가 임의의 라이브러리 함수에 의해 뜻하지 않게 수정되는 것을 막을 수 있다.
```
var a = { x: "나는 변하지 않는다."};
//a가 수정되는것을 막을 수 있다.
library_function(inherit(a));
```

######프로퍼티 접근 및 설정
마침표 연산자와 대괄호 연산자를 사용한다.
```
//book 객체에서 author프로퍼티를 가져온다.
var author = book.author;
var name = author.surname
//book 객체에서 "main title"프로퍼티를 가져온다.
var title = book["main title"]
//book객체에 edition 프로퍼티 만든다.
book.edition = 6;
//main title 프로퍼티 생성
book["main title"] = "ECMAScript";
```

C나 C++, 자바와 같이 타입의 제약이 엄격한 언어에서 객체는 오직 정해진 개수의 프로퍼티를 갖고, 반드시 프로퍼티의 이름을 미리 정의해야 한다.
반면 자바스크립트는 타입의 제약이 느슨하기 때문에, 이와 같은 규칙이 적용되지 않는다. 프로그램은 객체 안에 수많은 프로퍼티들을 만들 수 있다.

[]연산자를 사용해 객체의 프로퍼티에 접근할 때는 프로퍼티의 이름을 문자열로 표현한다. 문자열은 자바스크립트의 자료형이므로 프로그램 실행중에 생성하고 조작할 수 있다.
```
var add = "";
for (i = 0; i < 4; i++) {
	add += customer["address" + i] + '\n';
}
```
customer 객체의 address0 ~ address3 프로퍼티 값을 읽고, 읽은 값을 addr 변수에 차례대로 이어 붙인다.
```
function addstock(portfolio, stockname, shares) {
	portolio[stockname] = shares;
}

function getvalue(portolio) {
	var total = 0.0;
    for (stock in portfolio) {
    	var shares = porfolio[stock];
        var price = getquote(stock);
        total += shares * price;
    }
    return total;
}
```

#####상속
```
var a = {}
a.x = 1;

//b는 객체 a와 Object.prototype을 상속받는 객체고, 고유프로퍼티 y를 갖는다.
var b = inherit(a);
b.y = 2;

//c는 객체 a와b, Objecte.prototype을 상속받는 객체고, 고유프로퍼티 z를 갖는다.
var c = inherit(b);
c.z = 3;
var d = q.toString();

//객체 a와 b에서 상속 받았다.
c.y + c.y
```

자바스크립트의 상속받은 프로퍼티는 변경이 불가능하다.
######프로퍼티 삭제
```
//object.prototype은 속성 변경이 불가능한 프로퍼티이므로 지울 수 없다.
delete Object.prototype;

//지역변수 x를 선언하지만 전역 객체의 프로퍼티 x는 지울 수 없다.
var x = 1;
delete this.x;

//전역함수 f를 선언하지만 전역객체의 함수 f 역시 지울 수 없다.
function f() {};
delete this.f();
```

######프로퍼티 검사하기
```
var o = {x:1}
"x" in o; -> true
"y" in o; -> false
"toString" in o; ->true

var o = {x:1}
o.hasOwnProperty("x"); -> true
o.hasOwnProperty("y"); -> false
o.hasOwnProperty("toString"); -> toString은 상속된 프로퍼티 이기때문에 메서드는 false 반환

//PropertyIsEnumerable는 hasOwnProperty보다 상세한 검사를 한다. 열거할수 있는 프로퍼티 경우만 true를 반환한다.
var o = inherit({t:2});
o.x = 1;
o.propertyIsEnumerable("x"); -> 열거할 수 있는 프로퍼티 x를 가지고 있기때문에 메서드는 true
o.propertyIsEnumerable("y"); -> y는 상속받은 프로퍼티이기 때문에 메서드는 false를 반환한다.
Object.Prototype.propertyIsEnumerable("toString"); -> toString은 내장 프로퍼티이고, 열거할수 없다. false
```

######프로퍼티 열거하기
```
var o = {x:1, y:2, z:3};
o.propertyIsEnumerable("toString"); ->false
for(p in o)
	console.log(p); -> x,y,z 출력 , toString 출력 x
    
간단 예시
function(o, p) {
	for (prop in p) {
    	if (o.hasOwnProperty[prop]) continue;
        o[prop] = p[prop];
    }
    return o;
}
```

#####프로퍼티 Getter와 Setter
ECMAScript5 에서 프로퍼티의 값은 getter/setter 메서드로 대체할 수 있다.
getter/setter 메서드로 정의된 프로퍼티는 단순히 값을 갖는 데이터프로퍼티 와는 다른 **접근자 프로퍼티** 라고 한다.

```
var p = {
	//읽기,쓰기 속성을 가진 일반적인 데이터 프로퍼티 x,y
	x:1.0,
    y:1.0,
    //r은 getter/setter를 통한 읽기/쓰기가 가능한 접근자 프로퍼티다.
    //이러한 접근자 메서드 다음과 쉼표를 반드시 추가해야 한다.
    get r() { return Math.sqrt(this.x*this.x + this.y*this.y); }.
    set r(newvalue) {
    	var oldvalue = Math.sqrt(this.x*this.x + this.y*this.y);
        var ratio = newvalue/oldvalue;
        this.x *= ratio;
        this.y *= ratio;
    },
    //theta는 읽기 전용 접근자 프로퍼티고, getter 함수만 갖는다.
    get theta() { retrurn Math.atan2(this.y, this.x); }
};

var q = inherit(p);
q.x = 1; q.y = 1; -> 객체 q에 고유 데이터 프로퍼티들을 만든 후
console.log(q.r); -> 상속 받은 접근자 프로퍼티를 사용한다.
console.log(q.theta);
```

이 객체는 매법 다른 일련번호를 생성한다.
```
var serialnum = {
	//이 데이터 프로퍼티를 다음 일련번호 값을 갖는다.
    //프로퍼티 이름에 붙은 $는 내부 프로퍼티라는 힌트다.
    $n: 0,
    
    get next() {return this.$n++; },
    
    //새 일련번호 값을 설정, 이때 기존의 값보다 반드시 커야 한다.
    set next(n) {
    	if(n >= this.$n) this.$n = n;
        else throw "숫자는 오직 현제 숫자보다 큰 숫자만 가능하다";
    }
};
```

#####프로퍼티 속성
이름과 값 말고도, 프로퍼티에는 프로퍼티로 할 수 있는 작업을 결정하는 세가지 속성 **writable**과 **enumerable**, **configurable**이 있다.
writable 속성은 프로퍼티 값의 변경 가능 여부를 결정한다.
enumerable 속성은 프로퍼티가 열거될 수 있는지 여부를 결정한다.
configurable 속성은 configurable 속성뿐 아니라 writable 속성과 enumerable 속성 값의 변경 가능 여부를 결정한다.
>프로토타입 객체에 메서드를 추가할 수 있고, 추가된 메서드를 내장 메서드처럼 열거할 수 없게 만들수 있다.
>변경하거나 삭제할 수 없는 프로퍼티를 정의하여, 객체를 고정시킬 수 있다.

이 접근법을 따르면, 데이터 프로퍼티의 값 또한 속성이라고 할 수 있다. 그러므로, 프로퍼티는 이름과 네 가지 속성을 갖는다(value, writable, enumerable, configurable)
접근자 프로퍼티는 value 속성이나 writable 속성을 갖지 않는데, writable 속성은 setter 메서드의 존재 여부에 따라 결정되기 때문이다.(get, set, enumerable, configurable)

프로퍼티의 속성 값을 질의하고, 값을 설정하는 ECMAScript 5의 메서드는 접근자 프로퍼티의 네가지 속성을 표현하기 위해 **'프로퍼티 디스크립터'**라는 객체를 사용한다.

객체가 가진 프로퍼티에 대한 프로퍼티 디스크립터 객체는 object.getOwnPropertyDescriptor()을 통해 얻을 수 있다.
```
//{value: 1, writable: trun, enumerable: true, configurable: true}를 반환한다.
Object.getOwnPropertyDescriptor({x:1}, "x");

//다른 곳에서 정의한 randow 객체의 octet 프로퍼티의 속성을 살펴보자.
//{ get: /*func*/, set: undiefined, enumerable: true, configurable: true}를 반환
Object.getOwnPropertyDescriptor(random, "octet");

//상속받은 프로퍼티나 존재하지 않는 프로퍼티의 경우 undefined를 반환한다.
Object.getOwnPropertyDescriptor({}, "x"); -> 프로퍼티가 없어 undefined를 반환한다.
Object.getOwnPropertyDescriptor({}, "toString"); -> 상속받은 프로퍼티이므로 undefined를 반환한다.
```

디스크립터는 고유 프로퍼티에서만 동작하며 상속된 프로퍼티의 속성을 검사하기 위해서는 프로토타입 체인을 명시적으로 직접 순회해야 한다.

프로퍼티의 속성을 설정하거나 임의의 속성으로 새 프로퍼티를 만들기 위해서는 Object.defineProperty를 호출한다.
```
var o = {};

//열거할 수 없는 데이터 프로퍼티 x를 정의하고, 프로퍼티의 값을 1로 설정한다.
Object.defineProperty(o, "x", {
	value: 1,
    writable: true,
    enumerable: false,
    configurable: true});
    
//이 상태 에서도 변경가능, 프로퍼티 값을 변경한다.
Object.defineProperty(o, "x", {writable: false});
o.x = 2; o.x -> 1 단순히 값을 변경하지 못하거나, 엄격보드에서 TypeError 예외 발생

//여전히 configurable 프로퍼티이므로, 다음과 같이 기존값을 변경 가능하다.
Object.defineProperty(o, "x", {value: 2});
o.x -> 2;

//프로퍼티 x를 데이터 프로퍼티에서 접근자 프로퍼티로 바꿧다.
Object.defineProperty(o, "x", {get: function() { return 0; } });
o.x -> 0;
```

######프로퍼티 속성 복사하기
```
//Object.prototype에 열거되지 않은 메서드 extend()를 추가한다.
//이 메서드는 호출시에 인자로 전달된 객체에서 프로퍼티들을 복사함으로써 객체를 확장한다.
//단순 프로퍼티의 값뿐 아니라 모든 프로퍼티 속성을 복사한다.
//인자로 넘긴 객체가 소유한 모든 고유 프로퍼티는 대상 객체에 같은 이름의 프로퍼티가 존재하지 않는 한 대상 객체에 복사된다.

Object.defineProperty(Object.prototype,
	"extend",
	{
    	wriatable: true,
    	enumerable: false,
    	configurable: true,
    	value: function(o) {
    		//Object.prototype.extend 메서드의 값은 함수다.
        	//열거되지 않은 프로퍼티들을 포함한 모든 고유 프로퍼티에 대해
        	var names = Object.getOwnPropertyNames(o);
        	for(var i = 0; i < names.length; i++) { //루프에서 살펴봄
        		//this 객체에 이미 같은 이름의 프로퍼티가 존재하면 건너뛴다.
            	if (names[i] in this) continue;
            	//객체 o의 프로퍼티 디스크립터를 가져온다.
            	var desc = Object.getOwnPropertyDescriptor(o,names[i]);
            	//this 객체에 프로퍼티를 생성할 때 앞에서 가져온 디스크립터 객체를 사용한다.
            	Object.defineProperty(this, names[i], desc);
        	}
    	}
    }
);
```

#####객체 속성
모든 객체는 prototype, class, extensible 속성을 가지고 있다.

######prototype 속성
객체의 prototype속성은 프로퍼티를 상속하는 객체를 지정한다. 
객체 o의 프로토타입 속성 이 아닌 **객체 o의 프로토타입**이라고 할 만큼 매우 중요하다.

prototype 속성은 객체가 만들어지는 시점에 설정된다. 객체 리터럴을 통해 만든 객체는 Object.prototype을 객체의 프로토타입으로 설정한다. new를 사용해 만든 객체는 생성자 함수의 prototype 프로퍼티 값이 prototype 속성의 값이 되고, object.create() 메서드로 만든 객체는 메서드의 첫 번째 인자가 프로토타입 속성의 값이 된다.

new 표현식으로 생성된 객체는, 일반적으로 객체를 만드는 데 사용되는 생성자 함수를 참조하는 **constructor 프로퍼티** 를 상속 받는다.
객체 리터럴이나 object.create()로 생성된 객체는 Object()의 생성자를 constructor 프로퍼티로 갖는다. 따라서 constructor.prototype은 객체리터럴에 대해서는 정확한 프로토타입을 참조하지만 Object.create()로 생성된 객체의 경우 그렇지 않다.
```
//객체 A가 객체 B의 프로토타입(또는 프로토타입 체인의 일부)인지 알아보기 위해서는 isPrototypeOf() 메서드를 사용한다.
var p = {x:1};
var o = Object.create(p);
p.isPrototypeOf(o); -> true 객체o 는 객체 p를 상속받는다.
Object.prototype.isPrototypeOf(p); ->true: 객체p는 Object.prototype을 상속받는다.
```

######class 속성
객체의 class속성은 객체의 타입에 대한 정보를 담고 있는 문자열이다.ECMAScript3과 ECMAScript5 모두 어떠한 방법으로도 이 속성을 변경할 수 없고, 그 값을 질의하는 것도 아주 간접적으로만 가능하다.
Object.prototype으로부터 상속되는 기본 toString() 메서드는 객체의 타입을 아래 형태의 문자열로 반환한다.

원하는 toString() 메서드를 호출하기 위해서는 Function.call() 메서드를 참사용해 간접적으로 호출해야한다.
```
function classof(o) {
	if (o === null) return "Null";
    if (o === undefined) return "Undefined";
    return Object.prototype.toString.call(o).slice(8,-1);
}
```

Array나 Date같은 내장 생성자를 통해 생성된 객체는 생성자의 이름만 딴 class 속성을 가지고 있다.
호스트 객체도, 객체의 구현에 따라 다르지만 일반적으로 의미 있는 class 속성을 갖는다.
객체 리터럴이나 Object.create()를 사용해 생성된 객체의 class 속성값은 "Object"다.
```
classof(null) -> Null
classof(1) -> Number
classof("") -> String
classof({}) -> Object
classof([]) -> Array
classof(/./) -> Regexp
classof(new Date()) -> date
classof(window) -> window (클라이언트 측 호스트 객체)
function f() {};
classof(new f()) ->  Object
```

######extensible 속성
extensible속성은 객체에 새 프로퍼티를 추가할 수 있는지 여부를 결정한다.
확장할 수 있는 객체인지 알아보려면 Object.isExtensible() 함수에 해당 객체를 인자로 넘긴다.
객체를 확장할 수 없도록 하려면, Object.preventExtensions() 함수를 사용해 객체를 확장할 수 없도록 설정하면, 설정하기 전 상태로 돌아올수 없다.
프로토타입에 새 프로퍼티를 추가하면, 추가된 프로퍼티는 해당 객체에 상속된다.

ECMAScript 5에서는 이들 속성을 좀 더 쉽게 다루기 위해 몇가지 함수를 정의하고 있다.

object.seal()은 Object.preventExtensions()와 동작이 유사하지만, 객체를 확장할 수 없게 만들 뿐만 아니라 객체가 가진 모든 고유 프로퍼티를 설정 불가능하게 만든다. 다시말해, 객체에 새로운 프로퍼티를 추가할 수 없고, 기존 프로퍼티의 설정을 바꾸거나 지울 수도 없다는 뜻이다. 하지만 writable 속성이 true인 기존 프로퍼티의 값은 변경할 수 있다.
Object.isSealed() 메서드를 사용해 객체가 봉인되어 있는지 검사할 수 있다.

object.freeze() 메서드는 객체를 좀 더 단단히 감근다. 객체를 확장할 수 없게 만들고 프로퍼티 설정을 바꿀 수 없게 바꾼다.
object.isFrozen() 메서드를 사용하면 확인살수 있다. 

두 메서드는 주어진 객체의 고유 프로퍼티에만 영향을 미치고, 객체가 가진 프로포타입 객체에는 영향을 미치지 않는다. 객체를 철저히 잠그고 싶다면, 객체의 프로토타입 체인까지 잠궈야 한다.
```
//object.freeze()로 프로토타입을 고정시키고, 열거할 수 없는 프로퍼티 y를 가진 객체를 object.seal()로 봉인한다.
var o = object.seal(
	object.create(object.freeze({x:1}), {y: {value: 2, writable: true}}));
```

#####객체 직렬화하기
객체 직렬화는 객체의 상태를 문자열로 변환하는 과정을 말한다. 이때 생성된 문자열은 나중에 객체 복원에 사용할 수 있다. ECMAScript 5는 자바스크립트 객체를 직렬화하는 JSON.stringify() 메서드와 직렬화한 문자열을 객체로 복원하는 JSON.parse() 메서드를 지원한다. 이 두 함수는 JSON 데이터 교환 형식을 사용한다.
```
o = {x:1, y:{z:[false,null,""]}};
s = JSON.stringify(o); -> '{'x':1, 'y':{'z':[false,null,'']}}' 문자열
p = JSON>parse(s); -> 객체 o 를 복사한 객체
```

JSON문법은 자바스크립트 문법의 부분 집합이기 떄문에, 자바스크립트의 모든 값을 표현할 수 없다. 객체와 배열, 문자열, 유한한수, true, false, null은 모두 직렬화할 수 있고, 반대로 복원할 수도 있다.
NaN, Infinity, null로 직렬화 한다. Date객체는 ISO 날짜 형식을 따르는 문자열로 직렬화 한다. JSON.parse함수는 문자열을 Date객체로 복원하지 않는다. function, RegExp, Error 객체와 undefined값은 직렬화하거나 복원할 수 없다. JSON.stringfy() 메서드는 객체가 가진 열거 가능한 고유 프로퍼티만 직렬화한다. **만약 어떤 프로퍼티 값을 직렬화할 수 없다면, 해당 프로퍼티 값은 직렬화 결과에 포함되지 않는다.**
JSON.stringify()와 JSON.parse()함수는 두 번째 선택 인자를 갖는다. 이 인자를 사용해 직렬화 또는 복원할 프로퍼티 목록을 지정할 수 있다.

#####객체 메서드
모든 자바스크립트 객체(명시적으로는 프로토타입이 없이 생성된 객체는 제외)Object.prototype의 프로퍼티를 상속받는다.
상속된 프로퍼티들은 대부분 메서드이고, 어느 객체에서도 사용할 수 있기 때문에 주요 메서드라고 할 수 있고, 자바스크립트 프로그래머라면 반드시 관심을 가져야 한다.
hasOwnProperty()와 propertyIsEnumerable(), isPrototypeOf() 메서드는 살펴봤고, Object.prototype에 정의된 유용한 전역 객체 메서드들을 본다.
1. toString 메서드
toString 메서드는 어떠한 인자도 받지 않고, 호출 대상 객체의 값을 어떠한 방식으로든 문자열로 만들어 반환한다.
```
[1,2,3].toString -> "1,2,3"
```
2. toLocaleString() 메서드
객체의 지역화된 문자열 표현을 반환하는것이다. 이 메서드는 toString과 동일하게 작동하지만 각 배열 원소의 toLocaleString메서드를 호출한다는 점이 다르다.
3. toJSON() 메서드
object.prototype에는 toJSON() 메서드가 정의되어 있지 않다. 하지만 JSON.stringfy() 메서드는, 직렬화 할 객체에 toJSON() 메서드가 있는지 찾고, 만약 직렬화 하려는 객체에 toJSON() 메서드가 있으면, toJSON() 메서드가 호출되고 그 결과값이 원래 객체 대신 직렬화 된다. (ex -> Date.toJSON)
4. valueOf() 메서드
toString과 매우 유사하며 객체가 원시 타입 값을 필요로 하는 문맥 안에서 사용될 때, 자바스크립트는 valueOf() 메서드를 자동으로 호출한다.