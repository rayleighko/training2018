## Round 7-1-3 Form

#### HTML에서의 폼

우리는 웹 사이트를 개발할 때 사용자로부터 입력을 받기 위해 'Form'을 사용한다.  

일반적으로 우리의 상식에 있는 HTML로 표현한 Form의 문장은 다음과 같은 형태일 것이다.  

```
<fomr>
...	more elements
</form>  
```
  
이러한 `form` 문장 속 엘리먼트들의 집합을 통해 웹 사이트 사용자는 텍스트를 입력하거나 항목을 선택할 수도 있다.  

> 이렇게 폼에 입력된 데이터는 웹 DB 서버로 보내진다.  

간단한 폼의 엘리먼트들(텍스트 입력, 체크 박스 등)은 기본 위젯을 사용하지만, 복잡한 엘리먼트들(달력 위젯, 슬라이드 바)은 자바스크립트나 CSS를 사용하기도 한다.  

> 더블어 폼은 `input`엘리먼트 외에도 폼 데이터를 어디로 보낼지 지정해주는 action 속성과 어떤 HTTP 메소드로 보낼지 지정해주는 method 속성을 설정해주어야 한다.  

또한, HTTP 프로토콜 중 폼에서 사용할 수 있는 HTTP 메소드는 GET과 POST 뿐이고, Django에서는 POST 방식만을 사용하고 있다는 점도 유의하자.  

> 우리의 상식 속에서 GET과 POST 방식은 다른 용도로 사용된다. 예를 들어 데이터베이스의 내용을 변경하는 요청은 POST 방식을 사용하고, 시스템의 상태를 바꾸지 않는 요청에는 GET 방식을 사용한다.  
>
> 그리고 GET 방식은 패스워드 폼에서도 사용하지 않도록 권유하는데, 그 이유는 패스워드가 URL이나 브라우저 히스토리, 서버의 로그에 텍스트로 보일 수 있기 때문입니다. 때문에 데이터량이 많거나 이미지와 같은 2진 데이터를 보내는 경우도 앞선 경우와 마찬가지로 GET 방식을 사용하지 않고 POST 방식을 사용한다.  
>
> 추가적으로 Django에서는 보안을 강화하기 위해 CSRF방지 기능을 제공하고 있으며, 검색 폼같은 경우에는 GET 방식이 적절하다. 그 이유는 GET 방식의 데이터가 URL에 포함되므로, URL을 북마크해두고 쉽게 공유하거나 재전송할 수 있기 때문이다.  

#### Django의 폼 기능  

웹 서버에서의 폼 처리는 복잡한 과정이지만, 공통적인 절차를 갖고 있다. 예를 들어 Django의 Admin 사이트를 생각해보면 여러 가지 타입의 많은 데이터들이 폼 화면 출력용으로 준비되어야 하고, HTML로 렌더링되며, 적절한 인터페이스를 사용하여 입력 및 수정되고, 서버로 보내져서 데이터가 유효한지 검증을 거친 후에 적절한 처리를 위해 저장되거나 전달된다. 휴우,,  

Django에서는 이처럼 복잡한 과정의 폼 기능들을 단순화하고 자동화해서 개발자가 직접 코딩하는 것보다 훨씬 안전하게 처리해줍니다. Django는 폼 처리를 위해 다음의 3가지 기능을 제공한다.  

1. 폼 생성에 필요한 데이터를 폼 클래스로 구조화하기  
2. 폼 클래스의 데이터를 렌더링하여 HTML 폼 만들기  
3. 사용자로부터 제출된 폼과 데이터를 수신하고 처리하기  

웹 개발에 있어 '폼'이라는 용어는 HTML의 form tag를 지칭할 수도 있고, form tag를 만들어내는 Django의 Form 클래스일 수도 있고, 서버로 제출된 구조화된 데이터일 수도 있다.  

Django의 Model 클래스가 데이터베이스 테이블의 논리적인 구조 및 동작 기능, 우리에게 보여지는 방식들을 기술하는 거과 마찬가지로, Form 클래스는 폼을 기술하고 폼을 어떻게 작동하고 어떻게 보여지는지를 결정한다.  

> Model 클래스의 필드가 데이터베이스의 필드로 매핑되듯이, Form 클래스의 필드도 HTML 폼의 'input' 엘리먼트에 매핑된다.  
>
> 이 점은 중요하다. 폼 클래스의 필드도 역시 클래스로 취급하고, 폼 데이터를 저장하고 있으며 폼이 제출되면 자신의 데이터에 대한 유효성 검사를 실시한다.  

폼도 결국은 템플릿의 일부이다. 따라서 템플릿 코드에 포함되어 아래의 렌더링 절차를 거치게 된다.  

1. 렌더링할 객체를 뷰로 가져오기  
2. 그 객체를 템플릿 시스템으로 넘겨주기  
3. 템플릿 문법을 처리해ㅐ서 HTML 마크업 언어로 변환하기  

추가적으로 폼 객체는 모델 객체를 렌더링하는 것과 달리 빈 객체를 렌더링하는 일이 자주 발생하게 된다는 점에 유의하자.  

> 즉, 폼 객체는 보통 뷰 함수에서 생성하는데, 뷰 함수에서 폼 객체를 생성할 때는 데이터없이 만들 것인지, 아니면 데이터를 채워서 만들 것인지 적절히 구분해서 코딩해야 한다.  

데이터가 없는, 빈 객체를 렌더링할 경우 이를 언바운드 폼이라 하며 사용자에게 보여질 때 폼은 비어있거나 기본(default) 값으로 채워진다. 반면 바운드 폼은 제출된 데이터를 갖고 있어서 유효성 검사를 하는 데 사용된다.  

#### Form 클래스로 폼 생성하기  

본격적으로 실제 Django에서 폼을 어떻게 생성하는지 알아보자. 여기서 주목할 점은 Form도 Model처럼 클래스로 정의해서 간편하게 만들 수 있다는 것이다.  

```
<form action="/your-name/" method="post">
	<label for="your_name">Your name: </label>
	<input id="your_name" type="text" name="your_name" value="{{ current_name }}">
	<input type="submit" value="OK">
</form>
```
  
위 예제는 POST방식을 이용해 브라우저에게 폼 데이터를 받아 특정 URL로 보내달라고 요청하는 문장이다.  

장고는 이와 같은 form 엘리먼트의 기능을 제공하기 위해 아래와 같이 Form 클래스를 정의한다. 모든 Form 클래스는 **django.forms.Form**의 자식 클래스로 생성된다.  

```
from django import forms

class NameForm(forms.Form):
	your_name = forms.CharField(label='Your name', max_length100)
```
  
각각의 폼 필드는 위젯 클래스를 갖고 있고, 이 위젯 클래스는 다음과 같은 HTML 폼 위젯으로 대응된다.  

```
<input type="text">
```
  
대부분의 폼 필드는 디폴트 위젯을 갖고 있다. 위 예제에서 사용된 **CharField** 필드 타입은 **TextInput** 위젯이 디폴트 위젯이며 위에서 보인 HTML 폼 위젯으로 변환된다. 만일 디폴트 위젯을 변경하고 싶다면 아래와 같이 폼 필드를 정의할 때 명시적으로 지정하면 된다.  

```
your_name = forms.CharFeild(label='Your name', max_length=100, widget=forms.Textarea)
```
  
> 참고로 Django 폼 클래스는 모든 필드에 대해 유효성 검사 루틴을 실행시키는 메소드(is_calid())를 갖고 있다. 이 메소드가 호출되어 유효성 검사를 하고, 그 결과 만일 모든 필드가 유효하다면 아래와 같은 2가지 일을 한다.  
>
> 1. True를 반환한다.  
> 2. 폼 데이터를 cleaned_data 속성에 넣는다.  
  
위의 폼 클래스가 렌더링되면 다음과 같은 렌더링 결과가 나온다.  

```
<label for="your_name">Your name: </label>  
<input id="your_name" type="text" name="your_name" maxlength="100">  
```
  
렌더링 결과에 form tag나 submit 버튼은 없는데, 이들은 개발자가 직접 템플릿에 넣어줘야 한다. 그래서 template에서 다음과 같이 작성하면 원하는 결과를 얻을 수 있다.  

```
<form action="/your-name/" method="post">
	{% csrf_toekn %}
	{{ form }}
	<input type="submit" value="Submit" />  
</form>  
```
  
CSRF 공격을 방지하기 위하여 {% csrf_token %} tag를 추가하였고, 폼 클래스는 {{ form }} 변수로 사용했다.  

> {{ form }} 변수는 뷰에서 context 변수에 포함하여 템플릿 시스템으로 넘겨주게 된다.  

#### 뷰에서 폼 클래스 처리  

지금까지 작성한 폼 클래스와 html 템플릿을 사용하여 폼을 보여주고 폼 데이터를 수신하여 처리하는 뷰를 작성해보도록 하자.  

폼을 처리하는 뷰는 2가지가 필요하다. 하나는 폼을 보여주는 뷰이고, 다른 하나는 제출된 폼을 처리하는 뷰이다. 2개의 뷰는 하나의 뷰로 통합하여 처리할 수 있는데, 장고에서는 하나의 뷰로 통합하여 폼을 처리하는 것을 권장한다.  

이렇게 하나의 뷰에서 2가지 기능을 처리하려면, 처음 사용자에게 보여주는 폼과 사용자가 데이터를 입력한 후 제출된 폼을 구분하여 처리할 수 있어야 한다. Django는 이를 HTTP 메소드로 구분하는데, 뷰가 GET 방식으로 요청을 받은 경우에는 사용자에게 처음으로 폼을 보여주도록 처리하고, POST 방식으로 요청을 받은 경우엔느 데이터가 담긴 제출된 품으로 간주하여 처리하게 된다.  

```
from django.shortcuts import render
from django.http import HttpResonseRedirect

def get_name(request):
	# POST 방식이면, 데이터가 담긴 제출된 폼으로 간주한다.
	if request.method == 'POST':
		# request에 담긴 데이터로, 클래스 폼을 생성한다.
		form = NameForm(request.Post)
		# 폼에 담긴 데이터가 유효한지 검사
		if form.is_valid():
			# 유효하다면, 데이터는 cleaned_data로 복사한다.
			new_name = form.cleaned_data['name']
			# 로직에 따라 추가적인 처리를 진행한다.
			...
			# 새로운 URL로 리데이렉션 시킨다.
			return HttpResponseRedirect('/thanks/')

	# POST 방식이 아니면(보통은 GET 요청이 해당),
	# 빈 폼을 사용자에게 보여준다.
	else:
		form = NameForm()
	
	# POST가 아니라면 render() 함수를 호출한다. 또한, 템플릿 시스템으로 전달되는 컨텍스트 변수 'form'에는 직전에 제출된 폼 데이터로 채워진다.
	# render() 함수는 템플릿 코드 name.html에 컨텍스트 변수를 적용하여 사용자에게 보여줄 최종 템플릿 파일을 만들고, 이를 담아서 HttpResponse 객체를 반환한다.
	return render(request, 'name.html', {'form': form})
```
  
#### 폼 클래스를 템플릿으롭 변환    

앞에서 폼 클래스를 렌더링하여 템플릿으로 변환되는 과정을 살펴보았다. 폼 클래스를 템플릿으로 변환하기 위해서는 폼 객체를 생성해서 이를 템플릿 시스템에 넘겨주면 된다. 템플릿 시스템에서는 템플릿 문법 및 폼 객체를 해석해서 HTML 템플릿파일을 만들어 준다.

앞에서도 보았지만, {{ form }} 구문은 HTML의 label tag와 input tag 엘리먼트 쌍으로 렌더링된다. 이 경우 아래와 같은 3가지 옵션이 더 있다.  

* {{ form.as_table }}: tr tag(`<tr>`)로 감싸서 테이블 셀로 렌더링된다.  
* {{ form.as_p }}: p tag(`<p>`)로 감싸도록 렌더링된다.
* {{ form.as_ul }}: li tag(`<li>`)로 감싸도록 렌더링된다.  

여기서도 개발자가 직접 추가해야 하는 부분이 존재한다. 예제를 통해 살펴보자.  

```
from django import forms

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100)
	message = forms.CharField(widget=forms.Textarea)
	sender = forms.EmailField()
	cc_myself = forms.BooleanField(required=False)
```
  
{{ form.as_p }} 옵션으로 변환하는 경우, 그 결과 템플릿 파일은 다음과 같은 내용이 될 것이다.  

```
<p><label for="id_subject">Subject:</label>  
	<input id="id_subject" type="text" name="subject" maxlength="100" /></p>  
<p><label for="id_message">Message:</label>  
	<input type="text" name="message" id="id_message" /></p>  
<p><label for="id_sender">Sender:</label>  
	<input type="email" name="sender" id="id_sender" /></p>  
<p><label for="id_cc_myself">Cc myself:</label>  
	<input type="checkbox" name="cc_myself" id="id_cc_myself /></p>  
```
  
폼 클래스의 각 필드 타입에 따라 input type 태그 타입이 어떻게 변환되었는지 살펴보자.  

label tag에 나타나는 텍스트는 각 필드를 정의할 대 명시적으로 지정할 수 있다. 위 예제에서는 지정하지 않았기 때문에 디폴트 레이블 텍스트를 사용하였다.  

> 디폴트 레이블 텍스트는 필드명에서 첫자를 대문자로 하고 밑줄(_)은 빈칸( )으로 변경하여 만든다.  

