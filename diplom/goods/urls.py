from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.goods_list, name='goods_list'),
    path('<int:pk>/', views.goods_detail, name='goods_detail'),
    path('search/', views.goods_search, name='goods_search'),
    path('add/', views.add_goods, name='add_goods'),
]
