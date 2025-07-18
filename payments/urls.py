from django.urls import path
from . import views

urlpatterns = [
    path('payment/', views.payment_list, name='payment_list'),
    path('upi/',views.upi_payment,name='upi_payment'),
    path('success/',views.success,name='success'),
]
