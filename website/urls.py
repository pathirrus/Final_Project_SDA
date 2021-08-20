from django.urls import path

from website import views

app_name = 'website'

urlpatterns = [
    # path('',views.test, name='test'),
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('reservation/', views.reservation, name='reservation'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about,name='about'),
    path('gallery/', views.gallery, name='gallery'),
    # path('login/', views.login, name='login'),
    path('register_new_user/', views.register_new_user, name='register_new_user'),

]