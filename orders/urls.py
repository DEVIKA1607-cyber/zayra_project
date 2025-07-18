from django.urls import path
from . import views

urlpatterns = [
    path('yourorder/', views.order_list, name='order_list'),
    path('orderdetail/', views.order_detail, name='order_detail'),
]
