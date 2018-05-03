# Round 7-2 Template  

### Template System  

MTV 모델에서 사용자에게 보여주는 화면, 즉 UI를 담당하고 있는 기능이 템플릿 시스템이다.  

django template code 작성 시 HTML code와 Python code가 섞이지만, 중요한 점은 template에서는 logic을 표현하는 것이 아니라 사용자에게 어떻게 보여줄지에 대한 룩앤필을 표현한다는 것이다.  

그래서 template coding은 programming이라기 보다는 화면을 구현하는 작업이라고 하는 것이 적절한 표현이다.  

결과적으로 template coding을 거쳐 탄생한 file은 HTML, XML, CSV 등의 단순한 text file에 불과하다.  

지금부터 그러한 django template의 문법을 살펴보도록 하자.  

### Template variable  

```
{{ variable }}  
```
  
template code에서의 변수는 위와 같이 사용할 수 있다. 변수명은 일반 프로그래밍의 변수명처럼 문자, 숫자, 언더바를 사용하여 정의한다. 또한 변수의 속성에 접근할 수 있는 도트(.) 표현식도 가능하다.  

더불어 template system은 정의가 되어 있지 않은 변수를 사용하는 경우, 빈 문자열('')로 채워주며, 이 값을 변경하려면 setting.py 파일에 다음과 같은 속성을 지정해주면 된다(default는 빈 문자열이다).    

```
TEMPLATE_STRING_IF_INVALID  
```
  
### Template filter  

filter란 일반적인 용어로 어떤 객체나 처리 결과에 추가적으로 명령을 적용하여 해당 명령에 맞게 최종 결과를 변경하는 것을 말한다. django template 문법에서도 template 변수에 filter를 적용하여 변수의 출력 결과를 변경할 수 있다.  

filter는 아래의 예시처럼 파이프(|) 문자를 사용한다.  

```
{{ name|lower }}  
```
  
이 문장은 name 변수값의 모든 문자를 소문자로 바꿔주는 filter를 지정한 것이다. filter를 chain으로, 그러니까 연쇄적으로 적용할 수도 있다. text 변수값 중에서 특수 문자를 escape해주고 그 결과 string에 html <p> 태그를 붙여준다.  

```
{{ text|escape|linebreaks }}  
```
  
몇 가지 filter는 인자를 가질 수 있다. 다음은 bio 변수값 중에서 앞에 30개의 단어만 보여주고, 줄 바꿈 문자는 모두 없애준다.  

```
{{ bio|truncatewords:30 }}  
```
  
이외에도 다양한 template filter가 있으니 궁금하면 찾아보도록 하자.  

### Template tag  

template tag는 {% tag %} 형식을 가지며, template viriable이나 filter에 비해 좀 더 복잡한 편이다. 어떤 tag는 시작 tag와 끝 tag 둘다 있어야 하는 경우도 있다. text 결과물을 만들기도 하고, template logic을 제어하기도 하며, 외부 파일을 template 내로 로딩하기도 한다.  

그 중 가장 많이 사용하는 tag는 단연 {% for %}와 {% if %}이다. 이번 절에는 이 두 tag와 form tamplate에서 많이 사용되는 {% csrf_token %} 및 {% url %}, {% with %}, {% load %} 등을 살펴볼 것이다.  

#### {% for %}  

{% for %}를 사용하면 list에 담겨 있는 항목들을 순회하면서 출력할 수 있다.  

```
<ul>
{% for athlete in athlete_list %}
	<li>{{ athlete.name }}</li>
{% endfor %}
</ul>
```
  
위 예제는 운동선수 리스트(athlete_list)를 순회하여 모든 운동선수의 이름을 보여주는 문장이다. 또한, django template은 {% for %}를 사용하여 루프를 돌 때 사용할 수 있는 루프 카운트 등의 여러 가지의 변수를 제공하고 있다.  

#### {% if %}  

다음은 {% if %}이다. 변수를 평가하여 True이면 바로 아래의 문장이 표시되는 tag이다.  

```
{% if athlete_list %}
	Number of athletes: {{ athlete_list|length }}
{% elif athlete_in_locker_room_list %}
	Athlete should be out of the locker room soon!
{% else %}
	No athletes.
{% endif %}
```
  
기존 programming을 어느정도 이해한다면 위의 문장을 어렵지않게 이해할 수 있을 것이다. 만약 athlete_list의 값이 True, 그러니까 값이 존재한다면 첫 번째 문장이 실행되지만 그게 아닐 경우에는 다음 {% elif ~ %} 문장을 검사하고 진행하게 된다.  

또한, {% if %}는 앞서 배운 filter와 기존의 논리 연산자를 사용할 수 있다. 다음과 같이 말이다.  

```
{% if athlete_list|length > 1 %}  
``` 
  
이 문장은 athlete_list의 길이가 1개 이상, 즉 '한 명 이상의 선수가 존재한다면'의 의미를 지닌다.  

#### {% csrf_token %}  

POST 방식의 <form>을 사용하는 templete code에서는 CSRF 공격을 방지하기 위하여 {% csrf_token %}을 사용해야 한다. form data에는 악의적인 script 문장이 들어 있을 수도 있기 때문이다.  

```
<form action="." method="post">{% csrf_token %}
```
  
위치는 위와 같은 <form> element의 첫 줄 다음에 넣어주면 된다. 이 tag를 사용하면 django는 내부적으로 CSRF token값의 유효성을 검증합니다. 만일 CSRF token값 검증에 실패하면 사용자에게 403 error를 보여준다. 한 가지 주의할 점은 CSRF token값이 유출될 수도 있으므로, 외부 URL로 보내는 <form>에는 사용하지 않도록 하자.  

> ##### CSRF 공격이란?
> CSRF(Cross-Site Request Forgery)는 사이트 간 요청 위조 공격이라고도 표현한다. 웹 사이트의 취약점을 공격하는 방식 중의 하나로, 특정 웹 사이트에서 이미 인증을 받은 사용자를 이용하여 공격을 시도한다. 인증을 받은 사용자가 공격 코드가 삽입된 페이지를 열면 공격 대상이 되는 웹 사이트는 위조된 공격 명령을 믿을 수 있는 사용자로부터 발송된 것으로 판단하게 되어 공격을 받게 되는 방식이다.  
  
#### {% url %}  

이 tag의 주 목적은 소스에 URL을 하드 코딩하는 것을 방지하기 위한 것이다. 만일 이 tag를 사용하지 않는다면 비효율적으로 URL을 코딩해야 할 것이다.  

예를 들어 /polls/라는 URL을 /blog/라고 변경하는 경우에 URLconf뿐만 아니라 모든 html을 찾아서 변경해줘야 하는 문제가 발생한다. 또한, /3/이라는 숫자는 런타임에 따라 결정되어 항상 변하는 값이므로, 변수 처리를 해줘야 하기 때문에 이 또한 불편하다.  

이런 이유 때문에 {% url %}을 이용하여 하드 코딩하는 것을 피하는 것이다. {% url %}을 사용하면 URL이 변경되더라도 URLconf 모듈만을 참조하여 원하는 URL을 추출할 수 있게 된다. tag의 사용 형식은 다음과 같다.  

```
{% url 'namespace:view-name' arg1 arg2 %}
```
  
* namespace: urls.py file의 include() 함수에서 정의한 Namespace 이름  
* view-name: urls.py file의 URL pattern에서 정의한 view 함수 또는 pattern 이름  
* argN: view 함수에서 사용하는 인자로, 생략이 가능하며 여러 개인 경우 빈칸으로 구분  

#### {% with %}  

{% with %}는 특정 값을 변수에 저장해 두는 기능을 한다.  

```
{% with total=business.employee.count %}
	{{ total }} people works at business
{% endwith %}
```
  
위 문장에서 total 변수의 유효 범위는 with 구문 내({% with %} ~ {% endwith %})이다. 이 tag는 database를 조회하는 것처럼 부하가 큰 동작의 결과를 저장해 둠으로써, 다시 동일한 동작이 필요한 경우에는 저장해 둔 결과를 활용하여 부하를 줄이기 위한 tag이다. cache memory와 유사하다.  

#### {% load %}  

{% load %}는 사용자 정의 tag 및 filter를 로딩해준다.  

```
{% load somelibrary package.otherlibrary %}
```
  
tag 및 filter는 장고에서 기본적으로 제공하는 것 외에도, 개발자가 필요에 따라 스스로 정의하여 사용할 수 있다. 이런 것을 사용자 정의 tag, 사용자 정의 filter라고 한다. 이를 사용하기 위해서는 사용하기 전에 {% load %}를 이용하여 loading을 해줘야 한다.  

위 문장은 somelibrary.py 파일 및 package/otherlibrary.py file에 정의된 사용자 정의 tag 및 filter를 로딩하는 문장이다.  

그 외에도 주석문과 관련된 tag, HTML escape와 관련된 tag 및 template 상속과 관련된 tag도 존재한다.  

### Template 주석  

template code에서도 주석을 사용할 수 있다. 다음과 같이 2가지 방법이 존재한다.  

```
# 한 줄 주석문  

{# greeting #}hello

# 여러 줄 주석문

{% comment "Optional note" %}
<p>Commented out text here</p>
{% endcomment %}
```
  
위 예제에서 한 줄 주석문의 경우 {# #}를 이용하여 모든 내용을 주석처리 한다. 주석문 내의 template code가 들어있는 경우도 마찬가지이다.  

다음으로 {% comment %}를 이용한 여러 줄 주석문의 경우에는 Title도 설정할 수 있다. 위 예제의 title은 "Optional note"이다. 이때 {% comment %}는 중첩할 수 없다는 점도 명심하고 넘어가자.  

### HTML Escape  

template code를 rendering하여 HTML text를 만들 대, 주의해야 할 사항이 하나 있다. 만일 template varialbe에 HTML의 tag가 들어 있는 경우, 있는 그대로 렌더링하면 원하지 않는 결과가 나올 수 있다. 이를 방지하기 위해 HTML을 escape하는 방법을 사용한다. 다음을 살펴보자.  

```
name = "<b>username"
```
  
위 code에서 지정한 name이라는 변수를 아래의 문장에서 사용한다고 해보자.  

```
Hello, {{ name }}
```
  
그 결과는 다음과 같다.  

```
Hello, <b>username
```
  
이 결과는 브라우저에 표시될 때 \<b> 이후의 문장을 모두 bold로 바꿔버리기 때문에, 우리가 원했던 Hello, \<b>username과는 다른 결과가 나타난다. 참고로 이런 약점을 이용하여 XSS 공격이 이루어진다.  

> ##### XXS 공격이란?
> XSS(Cross-Site Scripting)는 사이트 간 스크립팅 공격이라고도 표현한다. 웹 사이트의 취약점을 공격하는 방식 중의 하나로, 웹 사이트 관리자가 아닌 일반 사용자라도 시도할 수 있는 공격 방법이다. 주로 여러 사용자가 보게 되는 전자 게시판에 악성 스크립트가 담긴 글을 올리는 형태로 이루어진다. 이 취약점은 web application이 사용자로부터 입력받은 값을 제대로 검사하지 않고 사용할 경우 나타난다.  

이처럼 사용자가 입력한 data를 그대로 randering하는 것은 위험할 수 있다. 그래서 django는 위와 같은 결과를 방지하기 위해 자동 이슼케이프 기능을 제공한다. django는 default로 HTML에 사용되는 예약 문자들을 다음과 같이 예약 의미를 제거한 문자로 변경해주는 기능을 제공한다.  

```
< (less than) 문자는 &lt; 로 변경함
> (greater than) 문자는 &gt; 로 변경함
' (single quote) 문자는 &#39; 로 변경함
" (double quote) 문자는 &quot; 로 변경함
& (ampersand) 문자는 &amp; 로 변경함
```
  
그러나 이와 같은 자동 HTML escape 기능을 비활성화시켜야 하는 경우도 종종 있다. 예를 들어 HTML tag를 그대로 출력하고 싶은 경우나, Escape  문자가 들어 있는 이메일 메시지를 템플릿 파일에 출력하는 경우가 이에 해당한다.  

비활성화 시키는 방법은 필요한 경우 따로 찾아보도록 하자.  

### Template 상속  

상속은 template 문법 중에서 가장 복잡하지만, 그만큼 강력한 기능이다. template의 상속을 통해서 template code를 재사용할 수 있고, 사이트의 룩앤필을 일관성 있게 보여줄 수 있다. 부모 template은 template의 뼈대를 만들어주고 {% block %}을 통해 하위로 상속해줄 부분을 지정해주면, 자식 template은 부모 template의 뼈대는 그대로 재사용하고 {% block %} 부분만 채워주면 된다. 다음의 경우를 살펴보자.  

```부모 template
<head>
	<link rel="stylesheet" href="style.css" />
	<title>{% block title %}My Amazing site{% endblock %}</title>
</head>

<body>
	<div id="sidebar">
		<% block sidebar %>
		<ul>
			<li><a href="/">Home</a></li>
			<li><a href="/blog/">Blog</a></li>
		</ul>
		{% endblock %}
	</div>

	<div id="content">
		<% block content %}{% endblock %}
	</div>
</body>
</html>
```
  
자식 template에서는 위에서 언급한 3개의 {% block %} 중에서 2개를 채워 사용했다. 이처럼 모든 {% block %}을 채울 필요는 없다. 만약 자식 template에서 {% block %}의 내용을 채우지 않았다면 부모 template의 내용을 그대로 따라가니 명심하도록 하자.  

```자식 template
{% extend "부모.html" %}

{% block title %}My Amazing blog{% endblock %}

{% block content %}
{% for entry in blog_entries %}
	<h2>{{ entry.title }}</h2>
	<p>{{ entry.body }}</p>
{% endfor %}
{% endblock %}
```
  
자식 template에서는 상속받는 의미로 {% extend %}를 사용한다. 다음은 자식 template file로, 부모 template code로부터 상속을 받고 자식 template code에서 rendering한 결과를 나타낸 것이다.  

``` 자식 template 처리 결과
<head>
	<link rel="stylesheet" href="style.css" />
	<title>My Amazing blog</title>
</head>

<body>
	<div id="sidebar">
		<ul>
			<li><a href="/">Home</a></li>
			<li><a href="/blog/">Blog</a></li>
		</ul>
	</div>

	<div id="content">
		<h2>Entry one</h2>
		<p>This is my first entry.</p>

		<h2>Entry Two</h2>
		<p>This is my second entry.</p>
	</div>
</body>
</html>
```
  
이와 같이 template 상속을 사용하면 template 전체의 모습을 구조화할 수 있어 code의 재사용이나 변경이 용이하고, 무엇보다도 사이트의 UI의 룩앤필을 일관되게 가져갈 수 있다. 사이트 전체적으로 조화로운 룩앤필을 위하여 일반적으로 template 상속을 3단계로 사용하는 것을 권장하고 있다.  

* 1단계: 사이트 전체에 룩앤필을 담고 있는 base.html을 만든다.  
* 2단계: 사이트 하위의 섹션별 스타일을 담고 있는 base_news.html, base_sport.html 등의 template을 만든다. 물론 base.html을 상속받는다.  
* 3단계: 개별 page에 대한 template을 만든다. 3단계 templates는 2단계 template 중에서 적절한 template을 상속받는다.  

마지막으로 template 상속 시 주의해야 할 사항이다.  

* {% extend %}는 사용하는 tag 중에서 가장 먼저 나와야 한다.  
* template의 공통 사항을 가능하면 많이 뽑아서 1단계 부모 template에 {% block %}가 많아질수록 좋은 상속 구조이다.  
* 부모 template에 있는 {% block %}의 내용을 그대로 사용하고 싶다면 자식 template에서 {{ block.super }} 변수를 사용하면 된다. 이 경우는 부모 template의 {% block %} 내용을 자식 template의 내용으로 오버라이딩하지 않는다.  
* 가독성을 높이기 위하여 {% endblock content %}처럼 블록명을 기입해도 된다.  
