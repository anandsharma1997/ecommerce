from django.contrib import admin
from django.urls import path, include
from ecom_app import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('login/', views.login_user, name='login'),
    path('logout/', views.louout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('product/<int:pk>/', views.product, name='product'),
    path('categories/<str:gname>/', views.categoryPage, name='categorypage'),
    path('<path:invalid_path>', views.custom_404, name='custom_404'),
]
