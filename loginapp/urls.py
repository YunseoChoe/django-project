from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.login, name='login'),
    path('home/', views.home, name='home'), # login 성공하면 뜨는 화면

    path('logout/', views.logout, name='logout'),
] 