from django.urls import path
from . import views

urlpatterns = [
    path('', views.payment_page, name='payment'),
    path('upi/', views.upi_page, name='upi_page'),
    path('success/', views.success_page, name='success_page'),
]
