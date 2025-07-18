from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.homepage, name='homepage'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    
]