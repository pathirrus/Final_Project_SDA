from django.urls import path, include
from accounts import *
from accounts import views
from django.contrib import admin

app_name = 'accounts'

urlpatterns = [
    path('register_new_user/', views.register_new_user, name='register_new_user'),
    path('user-account/', views.user_account, name='user_account'),
    path('welcome/', views.welcome, name='welcome'),
    path('logout_user/', views.logout_user, name='logout_user'),

    # path('edit_profile/<int:pk>/', views.edit_profile, name='edit_profile'),
]
