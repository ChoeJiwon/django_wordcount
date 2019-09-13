# django_wordcount
장고 실습 1주차


**gitignore 작성 tip**
1. gitignore.io 접속
2. 자신의 프로젝트 관련 프레임워크 추가(여기서는 django)
3. 내용 복사(굳이 전체 복사 안해도 됨)


# django 시작
  1. 폴더 하나 생성
  2.
  ```
    $ python -m venv myvenv
    $ source myvenv/Scripts/activate
    $ pip install django
    $ django-admin startproject project_name
    $ cd project_name
    $ python manage.py startapp app_name
  ```
  
  *project를 생성하면 프로젝트 폴더 안에 똑같은 이름의 폴더가 또 있는데 이때 큰 프로젝트 폴더의 이름을 바꿔주면 덜 헷갈린다.*
  
  3. project 폴더 안의 settings.py 수정
```{.python}
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #여기까지 동일
    'app_name.apps.App_nameConfig'
    ]
```
  4. 서버 실행
  `$ python manage.py runserver`

# django를 이용하여 python과 html 연결
*가장 먼저 project 내부의 project 폴더 안에 있는 urls.py에 코드 추가*
```{.python}
import app_name.views     #앱의 views.py 추가

urlpatterns = [
  path('admin/', admin.site.urls),
  path('주소', app_name.views.home, name="home"),   #주소가 공백일 경우 홈 페이지 #app_name의 views.py 안의 home 함수 #그 이름은 home
]
```
* template Tag : {% url 'url view name'%}
* template variable : {{variable}}
* template for loop : {% for a in b %} ... {%endfor%}


## python dictionary
* key 값과 value 값을 저장하는 파이썬의 자료형


## python 문법 (in Django)
1. 'home.html'에 있는 textarea에서 text 가져오는 법
   * views.py안에 정의된 함수에서
   * text = request.GET['textarea의 이름']

2. 긴 텍스트를 나누는 법
   * 리스트 객체를 만들고 (words)
   * words = text.split()
  **이때 words에 split된 텍스트가 리스트의 요소로 들어간다**
  
3. 길이를 구하는 법
   * 한 객체에 대해(words)
   * length = len(words)
  
4. 페이지 넘어가기
   * return render(request, '넘어가고 싶은 페이지(html)', (여기는 안적어도 됨)
   * 세번째 인자는 넘겨줘야할 값이 있을 때 사용
   * 예시 : {'full' : text, 'full_len' : length, 'dictionary' : word_dictionary.items()}
   * 이렇게 넘겨받은 값은 html에서 템플릿변수를 이용하여 사용 가능
  
5. Dictionary 쌍(key, value) 얻기
   * items() 문법 사용
   * 예시 - 'dictionary' : word_dictionary.items()
   * 이렇게 하면 dict_items([('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')]) 이런식으로 값이 들어감.
 
