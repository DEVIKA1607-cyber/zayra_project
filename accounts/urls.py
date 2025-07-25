from django.urls import path
from . import views

urlpatterns = [
    path('aboutus/', views.aboutus, name='aboutus'),

    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
]
