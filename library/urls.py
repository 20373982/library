"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from backend import views

urlpatterns = [
    # 用户登录系统
    path('test/', views.test),
    path('loginC/', views.user_login, name='user_login'),
    path('loginA/', views.admin_login, name='admin_login'),
    path('logout/', views.logout, name='logout'),
    path('registerC/', views.user_register, name='user_register'),
    path('registerA/', views.admin_register, name='admin_register'),
    path('home/', views.home, name='home'),
    path('homeA/', views.homeA, name='admin_home'),
    path('forum/', views.forum, name='forum'),
    path('commentA/', views.add_comment, name='add_comment'),
    path('commentD/', views.delet_comment, name='delet_comment'),
    path('review/', views.review, name='review'),
    path('reviewA/', views.add_reveiw, name='add_review'),
    path('reviewD/', views.delet_review, name='delet_review'),
    path('borrow/', views.borrow_book, name='borrow_book'),
    path('mybook/', views.mybook, name='mybook'),
    path('returnbook/', views.return_book, name='return_book'),
    path('bookadd/', views.add_book, name='add_book'),
]
