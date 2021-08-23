from django.urls import path, include
from accounts import *
from website import views
from django.contrib import admin


app_name = 'website'

urlpatterns = [
    # path('',views.test, name='test'),
    path('', views.home, name='home'),
    path('welcome/', views.welcome, name='welcome'),
    path('logout_user/', views.logout_user, name='logout_user'),

    path('services/', views.services, name='services'),
    path('reservation/', views.reservation, name='reservation'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    # path('login/', views.login, name='login'),
    path('register_new_user/', views.register_new_user, name='register_new_user'),
    path('user-account/', views.user_account, name='user_account'),

    path('create-service/', views.ServiceCreateView.as_view(), name="create-service"),
    path('update-service/<int:pk>/', views.ServiceUpdateView.as_view(), name="update-service"),
    path('delete-service/<int:pk>/', views.ServiceDeleteView.as_view(), name="delete-service"),
]