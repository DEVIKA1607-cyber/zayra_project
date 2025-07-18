from django.urls import path
from . import views

urlpatterns = [
    path('payment/', views.payment_view, name='payment'),
    path('upi/', views.upi_view, name='upi_page'),
    path('success/', views.order_success_view, name='order_success'),
]
