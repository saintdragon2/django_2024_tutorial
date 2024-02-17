from django.urls import path
from . import views

urlpatterns = [
    path('json_response_practice/', views.json_response_practice, name='json_response_practice'),
    path('http_response_practice/', views.http_response_practice, name='http_response_practice'),
    path('about/', views.about, name='about'),
    path('', views.index, name='index'),
]
