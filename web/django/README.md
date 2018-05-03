# Round 7-1 Django - Python web framework

본 문서는 [장고걸스 튜토리얼][djangogirls tutorial]을 활용하여 작성한 문서임을 밝힙니다. 또한, 개발 환경의 경우 **Ubuntu linux LTS 16.04**와 **Pycharm 2016.03**, **python 3.5.2**, **pip3 9.0.1**, **django 2.0.3**을 사용하여 진행하였습니다. 마지막으로 참고자료에서는 호스팅을 위해 가상환경에서 진행하였지만, 본 문서에서는 가상환경을 사용하지 않고 [localhost](http://127.0.0.1:8000)에 적용하여 진행했습니다.  

[djangogirls tutorial]: https://tutorial.djangogirls.org/ko/

## Round 7-1-1 Django basic

### 설치  

> ##### Python3 설치  
>
> $ sudo apt-get install python3  
>
> ##### pip3 설치  
>
> $ sudo apt-get install python3-pip  
  
// Ubuntu LTS 16.04에서는 python 2.x와 그에 맞는 pip가 기본적으로 설치되어 있다.  

> ##### Django 설치  
> 
> $ pip3 install django  

### 버전 확인  

> ##### Python  
> 
> $ python3 --version  
> Python 3.5.2  
> 
> ##### pip3  
> 
> $ pip3 --version  
> pip 9.0.1 from .../site-pakages (python 3.5)  
> 
> ##### Django  
>
> $ django-admin --version  
> 2.0.3  

### 프로젝트 시작  

> $ mkdir djangotuto  
> $ ~/djangotuto$ django-admin startproject blog .  

이 명령과 동시에 djangotuto라는 디렉터리에 blog라는 프로젝트가 시작된다. 이때 생성되는 파일은 다음과 같다.  

```
djangotuto
├───manage.py
└───blog
		settings.py
		urls.py
		wsgi.py
		__init__.py
```
  
#### 각 파일에 대한 설명

`manage.py`: 사이트 관리를 도와주는 스크립트 파일. 프로젝트의 application 생성, 웹 서버 실행 등의 기능을 한다.  
`settings.py`: 웹사이트의 설정. 서버 시간, 템플릿 정보, 디비 정보, 정적파일 정도 등이 포함된다.  
`urls.py`: `urlresolver`가 사용하는 패턴 목록을 포함. 즉, url의 경로 설정, 경로 탐색 방법 등이 기록된다.  

### 설정 변경  

웹사이트의 설정을 변경하기 위해 `setting.py`를 수정해보자. 우리는 서버 시간 변경, 정적파일 경로 추가, 디비 정보 확인을 진행할 것입니다.  

#### 서버 시간 변경  

서버의 시간은 **'TIME_ZONE'**에 정의되어 있습니다. 이를 수정해 서버 시간을 변경해봅시다.  

```
TIME_ZONE = 'Asia/Seoul'
```
  
#### 정적파일 경로 추가  

후반부에 다룰 CSS 설정 시 필요한 정적파일의 경로를 수정해야 합니다. 이번 한 번의 수정으로 CSS 설정 시 번거로움이 해결될 거에요.

```
STATIC_URL = '/static/'  
STATIC_ROOT = os.path.join(BASE_DIR, 'static')  
```

#### 디비 정보 확인  

이제 디비 정보를 확인해야 합니다. django가 처음이라면 다음과 같은 형태로 `setting.py`에 정의되어 있을 거에요.

```
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
}

```

기본적으로 django에서는 `sqlite3`를 사용합니다. 우리는 별다른 설정없이 기본 값(default)으로 설정된 `sqlite3`를 사용할 거에요.  

### 디비 설정하기  

우리가 만든 블로그에 데이터베이스를 설정하기 위해서는 다음 코드를 실행해야 합니다.  

> ~/djangotuto$ python3 manage.py migrate  

위의 명령으로 알 수 있듯이 python3에 설치된 django를 이용해 현 디렉터리에 존재하는 manage.py를 실행, migrate 명령을 수행하는 것이다. 여기서 migrate는 '이주', '이동'의 의미로, 웹 서버에 데이터베이스를 '이주'하는 동작이라고 이해하면 됩니다.  

### 적용 사항 확인하기(웹서버 실행)  

> ~/djangogirls$ python3 manage.py runserver  

이 문장 그대로 서버를 실행해서 지금까지의 동작을 확인하도록 합시다. [localhost](http://127.0.0.1:8000/)에서 제대로 동작하는지 확인해보세요! 만약 포트 번호를 조정해야 한다면 http://127.0.0.1:8000/ 에서 '8000'을 수정해 적절한 포트 번호를 사용하세요!  

**It worked!**라는 문장이 나오면 성공한 거에요!  

### Round 7-1-2 [Template](/template/README.md)
