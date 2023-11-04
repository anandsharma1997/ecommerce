from django.contrib import admin
from django.urls import path, include
from ecom_app import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('login/', views.login_user, name='login'),
    path('logout/', views.louout_user, name='logout'),
    path('register/', views.register, name='register')
]
