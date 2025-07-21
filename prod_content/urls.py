from django.urls import path
from . import views

urlpatterns = [
    path('track/', views.track_list, name='track_list'),
]
