from django.urls import path
from . import views

urlpatterns = [
    path('', views.delivery_list, name='delivery_list'),  # your existing route
    path('dashboard/', views.delivery_dashboard, name='delivery_dashboard'),
    path('mark-delivered/<int:assignment_id>/', views.mark_as_delivered, name='mark_delivered'),
]
