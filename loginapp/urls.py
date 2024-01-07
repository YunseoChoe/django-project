from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('afterLogin/', views.afterLogin, name='afterLogin'), # login 성공하면 뜨는 화면

    path('logout/', views.logout, name='logout'),
    path('', views.home, name='home'),
] 