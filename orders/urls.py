from django.urls import path
from . import views

urlpatterns = [
    path('yourorder/', views.order_list, name='order_list'),
    path('orderdetail/', views.order_detail, name='order_detail'),
    path('track/<int:order_id>/', views.track_order, name='track'),
    
    path('place-order/', views.place_order, name='place_order'),
    path('success/<int:order_id>/', views.order_success, name='order_success')


]
