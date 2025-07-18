from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('homepage/',views.product_categories,name='product_categories')
]