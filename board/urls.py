from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.board_detail, name='board_detail'),
    path('', views.board_list, name='board_list'),
]
