from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('dashboard/', views.vendor_dashboard, name='vendor_dashboard'),
    path('category/<int:category_id>/', views.products_by_category, name='products_by_category'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('categories/', views.category_view, name='categories'),

]
