from django.urls import path

from . import views

app_name = 'user'
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('admin/', views.admin_login, name='admin'),
    path('top/', views.top_page, name='top'),
    path('logout/', views.logout, name='logout')
]
