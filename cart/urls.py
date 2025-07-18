from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.cart_view, name='cart'),
    path('wishlist/', views.wishlist_view, name='wishlist'),
    path('add/', views.add_to_cart, name='add_to_cart'),
]
