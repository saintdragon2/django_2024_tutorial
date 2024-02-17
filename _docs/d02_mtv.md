## MTV (model, template, view)
장고는 MTV 구조다. 원래 일반적으로 웹개발에서 MVC구조라고 부르는 것에 대응하는 개념이다. 

### MVC vs MTV
(Model, View, Controller)
MVC의 개념은 아래 그림과 같다. 

#### MVC
![mvc](imgs/mvc.png)
(이미지출처: https://tibetsandfox.tistory.com/16)

#### MTV
MVC나 MTV나 그게 그거 아닌가 싶다. Model의 역할은 동일하고, Template은 View에 대응되고, Controller는 View에 대응된다. 

![mtv](imgs/mtv_django.png)
(이미지출처: https://tibetsandfox.tistory.com/16)

### 연습. View 만으로 구성하기
여태까지는 Template + View 조합으로 about 페이지와 index 페이지를 만들었다. 

이제 view만으로도 만드는 연습을 해보자. 
```python
# single_pages/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('json_response_practice/', views.json_response_practice, name='json_response_practice'), # <--
    path('http_response_practice/', views.http_response_practice, name='http_response_practice'),  # <--
    path('about/', views.about, name='about'),
    path('', views.index, name='index'),
]

```

```python
# single_pages/views.py
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

...

def http_response_practice(request):
    return HttpResponse('Hello, World! This is a practice of HttpResponse.')

def json_response_practice(request):
    return JsonResponse({
        'message': 'Hello, World! This is a practice of JsonResponse.',
        'numbers': [1, 2, 3, 4, 5]
    })
```

http://127.0.0.1:8000/http_response_practice/

![http response practice](imgs/2024_0217_1513.png)

http://127.0.0.1:8000/json_response_practice/
![json response practice](imgs/2024_0217_1516.png)


