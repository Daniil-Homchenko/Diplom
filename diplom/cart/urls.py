from django.urls import path
from . import views


urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('update/<int:id>', views.cart_add_or_remove, name='cart_add_or_remove'),
    path('clear/', views.clear_cart, name='clear_cart')
]